"""Tests del integrador aceleración → velocidad.

Las dos derivas que la demo muestra:
1. La gravedad que olvidás quitar: integrar 9.81 m/s² deriva LINEALMENTE
   (60 s → el teléfono "vuela" a 588 m/s).
2. El ruido blanco integrado deriva como caminata aleatoria; filtrar
   antes de integrar la recorta.
"""

import random

from muestreo.integrador import integrar, media_movil, quita_tendencia

F = 60.0  # Hz
G = 9.81


def _constante(a: float, dur_s: float) -> tuple[list[float], list[float]]:
    n = int(F * dur_s) + 1
    t = [i / F for i in range(n)]
    return t, [a] * n


def test_integracion_constante_exacta():
    t, a = _constante(1.0, 2.0)
    v = integrar(t, a)
    assert v[0] == 0.0
    assert abs(v[-1] - 2.0) < 0.01  # v = a·t = 2 m/s


def test_gravedad_sin_quitar_deriva_absurdamente():
    t, a = _constante(G, 60.0)  # el teléfono quieto sobre la mesa
    v = integrar(t, a)
    assert abs(v[-1] - G * 60.0) < 0.1  # "vuela" a 588.6 m/s


def test_quita_tendencia_saca_la_gravedad():
    n = 240
    t = [i / F for i in range(n)]
    osc = [0.5 * (i % 2) for i in range(n)]  # media 0.25
    a = [G + x for x in osc]
    sin_gravedad = quita_tendencia(a, ventana=120)
    assert abs(sum(sin_gravedad) / len(sin_gravedad) - 0.25) < 0.05


def test_ruido_filtrado_deriva_menos():
    rng = random.Random(42)
    n = 600  # 10 s
    t = [i / F for i in range(n)]
    a = [rng.gauss(0.0, 0.5) for _ in range(n)]  # a verdadera = 0

    v_cruda = integrar(t, a)
    v_filtrada = integrar(t, quita_tendencia(a, ventana=30))

    deriva_cruda = max(abs(x) for x in v_cruda)
    deriva_filtrada = max(abs(x) for x in v_filtrada)
    assert deriva_cruda / deriva_filtrada > 2.0, "el filtro debe recortar la deriva"
