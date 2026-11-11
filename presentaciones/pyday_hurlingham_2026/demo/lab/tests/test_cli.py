"""Tests del CLI y del contrato JSON entre el lab (Lado A) y el visor (Lado B).

El contrato es la costura: el visor no sabe nada de Python; solo consume
este JSON. Si cambia, un test avisa.
"""

import json
from pathlib import Path

from muestreo.cli import analizar, sintetizar


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
