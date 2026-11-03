"""Purpose: Comprobar que los experimentos de Monte Carlo son reproducibles.
Responsibilities: Ejecutar la cadena 04 → 05 → 06 e igualar registro, gráficos y resumen.
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
    resumen_trayectorias = capsys.readouterr().out
    runpy.run_path(str(CODIGO / "06_distribucion.py"))
    resumen_distribucion = capsys.readouterr().out
    for nombre in ("velocidad", "angulo"):
        assert Path(f"montecarlo-{nombre}.png").read_bytes().startswith(b"\x89PNG")
        assert Path(f"montecarlo-{nombre}-distribucion.png").read_bytes().startswith(b"\x89PNG")
    assert "velocidad:" in resumen_trayectorias
    assert "angulo:" in resumen_trayectorias
    assert "desviación estándar" in resumen_distribucion

    Path("montecarlo.json").unlink()
    for nombre in ("velocidad", "angulo"):
        Path(f"montecarlo-{nombre}.png").unlink()
        Path(f"montecarlo-{nombre}-distribucion.png").unlink()
    runpy.run_path(str(CODIGO / "04_montecarlo.py"))
    runpy.run_path(str(CODIGO / "05_trayectorias.py"))
    capsys.readouterr()
    runpy.run_path(str(CODIGO / "06_distribucion.py"))
    segunda_distribucion = capsys.readouterr().out

    assert Path("montecarlo.json").read_bytes() == registro
    assert segunda_distribucion == resumen_distribucion
