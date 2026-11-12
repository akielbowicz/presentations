"""Tests del CLI y del contrato JSON entre el lab (Lado A) y el visor (Lado B).

El contrato es la costura: el visor no sabe nada de Python; solo consume
este JSON. Si cambia, un test avisa.
"""

import json
from pathlib import Path

from muestreo.cli import analizar, sintetizar, grabar


def test_sintetizar_genera_csv_formato_sensorlog(tmp_path):
    csv = tmp_path / "sintetico.csv"
    sintetizar(csv, seed=7)
    texto = csv.read_text(encoding="utf-8-sig")
    assert texto.startswith("# SensorLog Export")
    assert "timestamp_ms,x,y,z" in texto
    assert (tmp_path / "sintetico.verdad.json").exists()


def test_analizar_produce_contrato_completo(tmp_path):
    csv = tmp_path / "sintetico.csv"
    sintetizar(csv, seed=7)
    salida = tmp_path / "recomendacion.json"
    contrato = analizar(csv, salida)

    assert set(contrato) == {"meta", "segmentos", "senial"}
    meta = contrato["meta"]
    assert meta["f_captura"] == 60.0
    assert 45 <= meta["duracion_s"] <= 55
    assert meta["n_muestras"] == 3000

    segmentos = contrato["segmentos"]
    assert len(segmentos) == 10  # ventanas de 5 s en 50 s
    primero = segmentos[0]
    assert set(primero) == {
        "nombre", "desde_s", "hasta_s", "f_opt", "k",
        "a_max", "v_max", "f_dyn", "redundancia_pct",
        "muestras_60hz", "muestras_f_opt",
    }
    # el primer tramo es "quieto": no hace falta medir rápido
    assert primero["f_opt"] <= 2
    assert primero["nombre"] == "quieto"

    # el ahorro total existe y es real
    total_60 = sum(s["muestras_60hz"] for s in segmentos)
    total_opt = sum(s["muestras_f_opt"] for s in segmentos)
    assert total_opt < total_60 / 2, "la recomendación debe ahorrar más de la mitad"

    senial = contrato["senial"]
    assert len(senial["t"]) == len(senial["a"]) <= 1500  # decimada para el visor
    assert salida.exists()


def test_grabar_decide_sobre_el_stream_y_ahorra(tmp_path):
    csv = tmp_path / "sintetico.csv"
    sintetizar(csv, seed=7)
    r = grabar(csv)
    assert r["totales"] == 3000
    assert r["guardadas"] < r["totales"] / 2
    assert r["error_reconstruccion_pct"] <= 10.0
    assert r["decisiones"], "debe haber al menos un cambio de tasa"
    # quieto → 1 Hz en algún momento; temblor → banda alta al final
    tasas_vistas = {f for _, f in r["decisiones"]}
    assert 1.0 in tasas_vistas
    assert max(f for _, f in r["decisiones"]) >= 40.0


def test_grabar_produce_contrato_de_grabacion(tmp_path):
    """El contrato del visor (Lado B) para el acto del grabador.

    Si cambia la forma, el visor se rompe: este test es la costura.
    """
    csv = tmp_path / "sintetico.csv"
    sintetizar(csv, seed=7)
    salida = tmp_path / "grabacion.json"
    grabar(csv, salida)
    contrato = json.loads(salida.read_text())

    assert set(contrato) == {"meta", "resumen", "decisiones", "guardadas", "senial"}
    meta = contrato["meta"]
    assert set(meta) == {
        "fuente", "f_captura", "f_medida", "duracion_s", "n_muestras",
        "ventana_muestras", "decision_cada_muestras", "bajadas_para_bajar",
    }
    assert meta["ventana_muestras"] == 120  # 2 s a 60 Hz
    assert meta["decision_cada_muestras"] == 30  # cada 0.5 s

    # decisiones: pares (t, tasa) ordenados en el tiempo
    dec = contrato["decisiones"]
    assert all(len(d) == 2 for d in dec)
    assert [d[0] for d in dec] == sorted(d[0] for d in dec)

    # guardadas alineadas y subconjunto del total
    guard = contrato["guardadas"]
    assert len(guard["t"]) == len(guard["a"]) == contrato["resumen"]["guardadas"]
    assert contrato["resumen"]["guardadas"] < meta["n_muestras"]

    # la señal decimada para el canvas, como el contrato offline
    assert len(contrato["senial"]["t"]) == len(contrato["senial"]["a"]) <= 1500
