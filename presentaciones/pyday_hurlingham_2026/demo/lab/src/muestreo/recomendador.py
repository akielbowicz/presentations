"""Recomendador de sample rate: cuánta data hace falta de verdad.

Métricas, en orden de aparición en el demo:
1. piso_ruido: σ del sensor, estimado de las diferencias entre muestras
   contiguas (el ruido blanco se ve en la alta frecuencia).
2. redundancia: fracción de muestras que no aportan nada nuevo
   (la señal cambió menos que el ruido entre una y la siguiente).
3. f_optima: la tasa más baja que reconstruye la señal con error RMS
   ≤ 10% (interpolación lineal sobre las muestras decimadas, comparada
   cruda). Para una dinámica de frecuencia característica f_dyn la
   curva da f_opt ≈ (4 a 8)·f_dyn. Y si la señal entera está en el
   piso de ruido, no hace falta medir rápido: 1 Hz.

La regla que emerge: Nyquist (2·f_dyn) basta para que la señal EXISTA,
pero se necesita ≈4-8·f_dyn para que su forma no MIENTA, con
f_dyn = a_max / (2π·v_max)  →  solo velocidad y aceleración.
"""

from __future__ import annotations

import statistics

from .integrador import media_movil  # para visuales del visor

VENTANA_SUAVIZADO_S = 0.3  # solo para visuales del visor; f_optima compara crudo


def piso_ruido(a: list[float]) -> float:
    """σ estimado: stdev de las diferencias contiguas / √2 (ruido blanco)."""
    if len(a) < 2:
        return 0.0
    diffs = [a[i + 1] - a[i] for i in range(len(a) - 1)]
    return statistics.stdev(diffs) / (2 ** 0.5)


def redundancia(a: list[float], sigma: float) -> float:
    """Fracción de muestras cuya diferencia con la anterior está en el ruido."""
    if len(a) < 2:
        return 0.0
    umbral = 2.0 * sigma
    quietas = sum(1 for i in range(len(a) - 1) if abs(a[i + 1] - a[i]) < umbral)
    return quietas / (len(a) - 1)


def interp_lineal(t_full, t_dec, a_dec, n):
    """Reconstruye la señal completa desde las muestras decimadas."""
    salida = []
    j = 0
    for ti in t_full:
        while j < len(t_dec) - 2 and t_dec[j + 1] < ti:
            j += 1
        t0, t1 = t_dec[j], t_dec[j + 1]
        a0, a1 = a_dec[j], a_dec[j + 1]
        if t1 == t0:
            salida.append(a0)
        else:
            frac = (ti - t0) / (t1 - t0)
            salida.append(a0 + (a1 - a0) * frac)
    return salida[:n]


def f_optima(
    t: list[float],
    a: list[float],
    tasas: tuple[float, ...],
    sigma: float,
    tol_pct: float = 10.0,
) -> float:
    """La tasa más baja que reconstruye la señal con error RMS ≤ tol%.

    La reconstrucción es interpolación lineal sobre las muestras
    decimadas, comparada contra la señal completa sin suavizar: el
    ruido entre muestras es justo la data redundante que no queremos
    reconstruir. Si la señal entera está dentro del piso de ruido: 1 Hz.
    """
    if len(t) < 4:
        return 1.0
    tasa_original = (len(t) - 1) / (t[-1] - t[0]) if t[-1] > t[0] else 1.0
    rms_ref = rms(a)
    if rms_ref < 2.0 * sigma:
        return 1.0  # no pasa nada: la dinámica es indistinguible del ruido
    tolerancia = tol_pct / 100.0 * rms_ref
    for f in sorted(tasas):
        paso = max(1, int(round(tasa_original / f)))
        t_dec = t[::paso]
        a_rec = interp_lineal(t, t_dec, a[::paso], len(t))
        if rms([r - o for r, o in zip(a_rec, a)]) <= tolerancia:
            return float(f)
    return float(sorted(tasas)[-1])


def rms(valores: list[float]) -> float:
    return (sum(x * x for x in valores) / len(valores)) ** 0.5
