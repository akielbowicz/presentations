"""Grabador adaptativo: decide la tasa de guardado MIENTRAS llega el stream.

El análisis offline (cli.analizar) puede mirar la ventana completa; este
grabador está condenado a mirar para atrás — solo pasado, muestra a
muestra. Es la idea del cierre del track 11 hecha código: decirle a
sensor-log qué sample rate usar en cada momento de una grabación real.

Algoritmo (todo causal):
1. Ventana deslizante de `ventana_s` segundos con las lecturas crudas.
2. Cada `decision_cada_s`, el objetivo es LA MISMA f_optima del contrato
   (la tasa más baja que reconstruye la ventana con error ≤10% RMS),
   corrida sobre la ventana deslizante con el σ de piso histórico. Sin
   regla k intermedia: la métrica medida manda — con datos reales la
   banda 4–8× sintética subestima (los k de la captura llegan a 19.6).
3. Histéresis asimétrica: SUBIR es inmediato (perderse un sacudón cuesta
   caro), BAJA solo tras `bajadas_para_bajar` decisiones consecutivas con
   el mismo objetivo (el ruido acecha).
4. El pacing es en UNIDADES DE MUESTRA (enteros), no en segundos flotantes:
   paso = round(tasa_medida / f), la misma interpretación de la grilla que
   hace f_optima. 40 Hz sobre un stream de 59.999 es "cada muestra"; un
   pacing de 1/40 en tiempo continuo dejaría pasar 1 de cada 2 = 30 Hz
   por pura aritmética de punto flotante: aliasing.
5. El sensor MUESTREA a plena tasa en un buffer RAM pase lo que pase: lo
   que se persiste es la decisión. Cuando la tasa SUBE, la ventana se
   re-decima a la nueva tasa desde el buffer — el pre-buffer de la
   cámara del auto, misma idea. Esas muestras ya llegaron; no eran futuro.

La red de seguridad: los tests del oráculo sintético — quieto a 1 Hz,
temblor arriba de 40 Hz, reconstrucción ≤10% RMS, sin hueco en el onset,
y decisiones estrictamente causales.
"""

from __future__ import annotations

from collections import deque

from .recomendador import f_optima, interp_lineal, piso_ruido, rms


class GrabadorAdaptativo:
    def __init__(
        self,
        f_captura: float,
        tasas: tuple[float, ...],
        ventana_s: float = 2.0,
        decision_cada_s: float = 0.5,
        bajadas_para_bajar: int = 2,
    ):
        self.tasas = sorted(tasas)
        self.f_captura = f_captura
        self.ventana: deque = deque(maxlen=max(4, int(ventana_s * f_captura)))
        self.decision_cada = max(1, int(decision_cada_s * f_captura))
        self.bajadas_para_bajar = bajadas_para_bajar
        self.tasa = float(self.tasas[-1])  # arranca conservador: guardar todo
        self._paso = 1  # unidades de muestra
        self.sigma: float | None = None
        self.t_guardadas: list[float] = []
        self.a_guardadas: list[float] = []
        self._idx_guardadas: list[int] = []
        self.decisiones: list[tuple[float, float]] = []
        self._idx = -1
        self._tick = 0
        self._bajas = 0
        self._candidata: float | None = None

    def ofrecer(self, t: float, a: float) -> bool:
        """Alimenta una lectura. Devuelve True si la guardó."""
        self._idx += 1
        self.ventana.append((t, a, self._idx))
        self._tick += 1
        if (
            self._tick % self.decision_cada == 0
            and len(self.ventana) == self.ventana.maxlen
        ):
            self._decidir(t)
        if not self._idx_guardadas or self._idx - self._idx_guardadas[-1] >= self._paso:
            self.t_guardadas.append(t)
            self.a_guardadas.append(a)
            self._idx_guardadas.append(self._idx)
            return True
        return False

    def error_reconstruccion_pct(self, t: list[float], a: list[float]) -> float:
        """RMS de la reconstrucción (interp. lineal sobre lo guardado) vs cruda."""
        a_rec = interp_lineal(t, self.t_guardadas, self.a_guardadas, len(a))
        return 100.0 * rms([r - o for r, o in zip(a_rec, a)]) / max(rms(a), 1e-9)

    def _tasa_ventana(self) -> float:
        """Tasa real deducida de la ventana, con la MISMA fórmula que
        f_optima: (n-1)/(t_fin - t_inicio). En streams reales es 59.9.x,
        no 60.0 justo — y eso cambia el redondeo del paso."""
        if len(self.ventana) >= 4:
            tw = [ti for ti, _, _ in self.ventana]
            span = tw[-1] - tw[0]
            if span > 0:
                return (len(tw) - 1) / span
        return self.f_captura

    def _decidir(self, t: float) -> None:
        t_w = [ti for ti, _, _ in self.ventana]
        a_w = [a for _, a, _ in self.ventana]
        sigma_w = piso_ruido(a_w)
        # el piso de ruido es el mínimo histórico: la ventana más quieta lo revela
        self.sigma = sigma_w if self.sigma is None else min(self.sigma, sigma_w)
        nueva = float(f_optima(t_w, a_w, self.tasas, self.sigma))

        if nueva > self.tasa:  # subir es inmediato
            self._aplicar(t, nueva)
        elif nueva < self.tasa:  # bajar, con calma
            if nueva == self._candidata:
                self._bajas += 1
                if self._bajas >= self.bajadas_para_bajar:
                    self._aplicar(t, nueva)
            else:
                self._candidata, self._bajas = nueva, 1
        else:
            self._candidata, self._bajas = None, 0

    def _aplicar(self, t: float, nueva: float) -> None:
        vieja = self.tasa
        self.tasa = nueva
        self._candidata, self._bajas = None, 0
        self.decisiones.append((round(t, 2), nueva))
        self._paso = max(1, int(round(self._tasa_ventana() / nueva)))
        if nueva > vieja and self.ventana:
            self._redecimar()

    def _redecimar(self) -> None:
        """Subida: la ventana del buffer RAM se re-decima a la nueva tasa.

        No alcanza con rellenar después de la última guardada: el hueco
        puede estar ENTRE dos guardadas viejas (a 1 Hz el turno llega
        antes que la decisión). Se descartan las muestras del rango de la
        ventana —siguen en RAM, no salieron del buffer— y se re-deciman
        desde la última guardada anterior a la ventana, en unidades de
        muestra (enteros, sin deriva de punto flotante).
        """
        inicio = self.ventana[0][2]
        ancora = None
        for ii in reversed(self._idx_guardadas):
            if ii < inicio:
                ancora = ii
                break
        while self._idx_guardadas and self._idx_guardadas[-1] >= inicio:
            self.t_guardadas.pop()
            self.a_guardadas.pop()
            self._idx_guardadas.pop()
        ultimo = ancora if ancora is not None else inicio - self._paso
        for tb, ab, ib in self.ventana:
            if ib - ultimo >= self._paso:
                self.t_guardadas.append(tb)
                self.a_guardadas.append(ab)
                self._idx_guardadas.append(ib)
                ultimo = ib
