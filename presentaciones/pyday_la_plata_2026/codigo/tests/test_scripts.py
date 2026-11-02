"""Purpose: Comprobar que los ejemplos generan el gráfico y el registro JSON.
Responsibilities: Ejecutar los tres scripts en una carpeta temporal.
Rationale: Probar los archivos resultantes no requiere subprocesses ni una CLI.
"""

import json
from pathlib import Path
import runpy

import pytest

CODIGO = Path(__file__).resolve().parents[1]


def test_ejemplos(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    runpy.run_path(str(CODIGO / "01_tiro_parabolico.py"))
    runpy.run_path(str(CODIGO / "02_inputs.py"))
    runpy.run_path(str(CODIGO / "03_simular.py"))

    assert Path("trayectoria.png").stat().st_size > 0
    entrada = json.loads(Path("entrada.json").read_text())
    registro = json.loads(Path("resultado.json").read_text())
    assert registro["entrada"] == entrada
    assert registro["salida"]["alcance"] == pytest.approx(10)
