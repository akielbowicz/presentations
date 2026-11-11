"""Tests del parser de CSV exportado por sensor-log (JAMS).

Formato real (app.js de jams/sensor-log):
  \\uFEFF (BOM)
  # SensorLog Export - Accelerometer
  # Session: <ISO> | Frequency: 60Hz | Samples: 3600
  timestamp_ms,x,y,z
  1234567890,0.123456,-1.000000,9.810000
"""

from pathlib import Path

import pytest

from muestreo.csv_sensorlog import leer_sensorlog

FIXTURE = Path(__file__).parent / "datos" / "acelerometro-mini.csv"


def test_lee_bom_y_comentarios():
    series = leer_sensorlog(FIXTURE)
    assert len(series.t) == 4


def test_columnas_timestamp_x_y_z():
    series = leer_sensorlog(FIXTURE)
    assert series.t[0] == 0.0
    assert series.t[1] == pytest.approx(0.016)  # ms → segundos, relativos a la primera muestra
    assert series.ax[0] == 0.123456
    assert series.ay[0] == -1.0
    assert series.az[0] == 9.81


def test_frecuencia_reportada():
    series = leer_sensorlog(FIXTURE)
    assert series.f_captura == 60.0  # del comentario "# ... Frequency: 60Hz |"


def test_frecuencia_medida_aproximada():
    series = leer_sensorlog(FIXTURE)
    assert series.f_medida == 62.5  # 4 muestras en 48 ms → 1000/16
