"""Tests del integrador aceleración → velocidad.

El punto físico que la demo muestra: integrar ruido deriva
(camina aleatoria); filtrar antes de integrar corta la deriva.
"""

import random

from muestreo.integrador import integrar, media_movil

F = 60.0  # Hz


def _constante(a: float, dur_s: float) -> tuple[list[float], list[float]]:
    n = int(F * dur_s) + 1
    t = [i / F for i in range(n)]
    return t, [a] * n


def test_integracion_constante_exacta():
    t, a = _constante(1.0, 2.0)
    v = integrar(t, a)
    assert v[0] == 0.0
    assert abs(v[-1] - 2.0) < 0.01  # v = a·t = 2 m/s


def test_filtro_quita_offset_gravitatorio():
    n = 120
    t = [i / F for i in range(n)]
    osc = [0.5 * (i % 2) for i in range(n)]  # señal que alternante, media 0.25
    a = [9.81 + x for x in osc]  # gravedad + señal
    filtrada = media_movil(a, ventana=21)
    assert abs(sum(filtrada) / len(filtrada) - 0.25) < 0.05  # la gravedad desapareció


def test_ruido_integrado_deriva_y_filtro_la_corta():
    rng = random.Random(42)
    n = 600  # 10 s
    t = [i / F for i in range(n)]
    a = [rng.gauss(0.0, 0.5) for _ in range(n)]  # a verdadera = 0, puro ruido

    v_cruda = integrar(t, a)
    v_filtrada = integrar(t, media_movil(a, ventana=30))

    assert abs(v_cruda[-1]) > 1.0, "el ruido sin filtrar debe derivar visiblemente"
    assert abs(v_filtrada[-1]) < 0.3, "el filtro debe cortar la deriva"
