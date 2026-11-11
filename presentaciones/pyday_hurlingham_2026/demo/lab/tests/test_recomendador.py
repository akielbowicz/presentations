"""Tests del recomendador de sample rate.

La regla que el demo descubre: para seguir una señal cuya dinámica
cambia con frecuencia característica f_dyn hace falta muestrear a
~5·f_dyn; más rápido es data que es ruido (redundante), más lento
deforma la medición.

Para una oscilación a_max·sin(2πf·t): v_max = a_max/(2πf) →
f_dyn = a_max/(2π·v_max) = f. La regla usa SOLO velocidad y aceleración.
"""

import math

from muestreo.recomendador import f_optima, piso_ruido, redundancia
from muestreo.senales import REGIMENES, generar

F = 60.0


def test_piso_ruido_estima_sigma_del_sensor():
    serie, _ = generar(seed=7)
    quieto = serie.a[0:600]  # primeros 10 s
    sigma = piso_ruido(quieto)
    assert 0.03 < sigma < 0.05  # el generador usa σ = 0.04


def test_redundancia_quieto_es_casi_toda_ruido():
    serie, _ = generar(seed=7)
    quieto = serie.a[0:600]
    sigma = piso_ruido(quieto)
    assert redundancia(quieto, sigma) > 0.80  # casi cada muestra repite la anterior


def test_redundancia_temblor_es_informacion_real():
    serie, verdad = generar(seed=7)
    seg = _segmento(serie, verdad, "temblor")
    sigma = piso_ruido(serie.a[0:600])
    assert redundancia(serie.a[seg[0] : seg[1]], sigma) < 0.50


def test_tasa_optima_por_regimen():
    serie, verdad = generar(seed=7)
    tasas = (60, 50, 40, 30, 25, 20, 15, 12, 10, 8, 6, 5, 4, 3, 2, 1)
    for nombre, rango in (
        ("quieto", (1, 2)),
        ("caminando", (15, 25)),
        ("temblor", (40, 60)),
    ):
        desde, hasta = _segmento(serie, verdad, nombre)
        f_opt = f_optima(
            serie.t[desde:hasta], serie.a[desde:hasta], tasas=tasas, sigma=piso_ruido(serie.a[0:600])
        )
        assert rango[0] <= f_opt <= rango[1], f"{nombre}: f_opt={f_opt}"


def test_la_regla_k_es_estable_entre_regimenes():
    """El descubrimiento codificado: f_opt ≈ k·f_dyn con k≈8 (5% RMS, interpolación
    lineal) en todos los regímenes — una sola regla, dos dinámicas distintas."""
    serie, verdad = generar(seed=7)
    tasas = (60, 50, 40, 30, 25, 20, 15, 12, 10, 8, 6, 5, 4, 3, 2, 1)
    sigma = piso_ruido(serie.a[0:600])
    for nombre in ("caminando", "temblor"):
        desde, hasta = _segmento(serie, verdad, nombre)
        f_opt = f_optima(serie.t[desde:hasta], serie.a[desde:hasta], tasas=tasas, sigma=sigma)
        v_max, a_max = verdad[nombre]["v_max"], verdad[nombre]["a_max"]
        f_dyn = a_max / (2 * math.pi * v_max)
        k = f_opt / f_dyn
        assert 3.5 < k < 11.0, f"{nombre}: k={k:.1f} (f_dyn={f_dyn:.1f} Hz, f_opt={f_opt})"


def _segmento(serie, verdad: dict, nombre: str) -> tuple[int, int]:
    for reg, desde, hasta, _ in REGIMENES:
        if reg == nombre:
            return (int(desde * serie.f_medida), int(hasta * serie.f_medida))
    raise ValueError(nombre)
