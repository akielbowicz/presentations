"""Purpose: Comprobar que los experimentos de Monte Carlo son reproducibles.
Responsibilities: Ejecutar la cadena 04 → 05 e igualar registro, gráficos y resumen.
Rationale: Con semilla fija, guardar y graficar produce siempre el mismo resultado.
"""

import runpy
from pathlib import Path

CODIGO = Path(__file__).resolve().parents[1]


def test_montecarlo_reproducible(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    runpy.run_path(str(CODIGO / "04_montecarlo.py"))
    registro = Path("montecarlo.json").read_bytes()
    runpy.run_path(str(CODIGO / "05_trayectorias.py"))
    primera = capsys.readouterr().out
    assert Path("montecarlo-velocidad.png").read_bytes().startswith(b"\x89PNG")
    assert Path("montecarlo-angulo.png").read_bytes().startswith(b"\x89PNG")
    assert "velocidad:" in primera
    assert "angulo:" in primera

    Path("montecarlo.json").unlink()
    Path("montecarlo-velocidad.png").unlink()
    Path("montecarlo-angulo.png").unlink()
    runpy.run_path(str(CODIGO / "04_montecarlo.py"))
    runpy.run_path(str(CODIGO / "05_trayectorias.py"))
    segunda = capsys.readouterr().out

    assert Path("montecarlo.json").read_bytes() == registro
    assert segunda == primera
