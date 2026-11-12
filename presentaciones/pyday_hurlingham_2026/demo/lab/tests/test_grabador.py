"""Tests del grabador adaptativo: decisiones sobre el stream, muestra a muestra.

El offline (analizar) puede mirar la ventana completa; el grabador está
condenado a mirar para atrás. El oráculo es la verdad sintética: quieto →
1 Hz, caminando (f_dyn=2) → ~12 Hz, temblor (f_dyn=10) → sube a la banda
alta. Y lo que guarda tiene que reconstruir la señal sin mentir (≤10% RMS),
con mucho menos que los 60 Hz crudos.

La asimetría es parte del contrato: subir es INMEDIATO (perderse un
sacudón cuesta caro), bajar espera (el ruido acecha).
"""

from muestreo.grabador import GrabadorAdaptativo
from muestreo.recomendador import interp_lineal, rms
from muestreo.senales import generar

TASAS = (60, 50, 40, 30, 25, 20, 15, 12, 10, 8, 6, 5, 4, 3, 2, 1)
F = 60.0


def _correr(serie, hasta_s=None):
    g = GrabadorAdaptativo(f_captura=F, tasas=TASAS)
    for t, a in zip(serie.t, serie.a):
        if hasta_s is not None and t > hasta_s:
            break
        g.ofrecer(t, a)
    return g


def test_en_quieto_baja_a_una_lectura_por_segundo():
    serie, _ = generar(seed=7)
    g = _correr(serie, hasta_s=8.0)  # primeros 8 s: solo ruido
    assert g.tasa <= 2.0


def test_en_caminando_se_estabiliza_en_la_banda():
    serie, _ = generar(seed=7)
    g = _correr(serie, hasta_s=25.0)
    # f_dyn = 2 Hz, k = 6 → objetivo 12 Hz; la red cuantiza a la grilla
    assert 8.0 <= g.tasa <= 20.0


def test_en_temblor_sube_a_la_banda_alta():
    serie, _ = generar(seed=7)
    g = _correr(serie, hasta_s=45.0)  # 5 s dentro del temblor
    assert g.tasa >= 40.0


def test_sube_inmediato_ante_el_cambio_de_regimen():
    serie, _ = generar(seed=7)
    g = _correr(serie, hasta_s=41.0)  # 1 s dentro del temblor
    assert g.tasa >= 40.0


def test_sin_hueco_largo_en_el_amanecer_del_temblor():
    # el sensor muestrea a 60 Hz en RAM pase lo que pase; la subida
    # backfillea el hueco desde el buffer — no puede quedar un agujero
    # de 1 s cruzando el onset del movimiento
    serie, _ = generar(seed=7)
    g = _correr(serie, hasta_s=45.0)
    tg = g.t_guardadas
    gaps = [b - a for a, b in zip(tg, tg[1:]) if 39.5 < a < 41.0]
    assert max(gaps) <= 0.05  # cubierto al menos a 20 Hz en el arranque


def test_reconstruccion_desde_lo_guardado_no_miente():
    serie, _ = generar(seed=7)
    g = _correr(serie)
    a_rec = interp_lineal(serie.t, g.t_guardadas, g.a_guardadas, len(serie.a))
    error = rms([r - o for r, o in zip(a_rec, serie.a)])
    assert error <= 0.10 * rms(serie.a)


def test_guarda_mucho_menos_que_los_60hz():
    serie, _ = generar(seed=7)
    g = _correr(serie)
    # 20 de los 50 s son quieto: la cuenta justa tiene que quedar holgada
    assert len(g.a_guardadas) < 0.5 * serie.n_muestras


def test_las_decisiones_son_causales():
    # las decisiones no usan futuro; el backfill re-lee pasado que sigue
    # en el buffer RAM — es una decision de persistencia, no adivinacion
    serie, _ = generar(seed=7)
    g_corto = _correr(serie, hasta_s=30.0)
    g_largo = _correr(serie)
    assert g_corto.decisiones == [d for d in g_largo.decisiones if d[0] <= 30.0]
