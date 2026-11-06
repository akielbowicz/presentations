"""Purpose: Comprobar que los experimentos de Monte Carlo son reproducibles.
Responsibilities: Ejecutar la cadena 04 → 05 → 06 → 07 e igualar todo lo generado.
Rationale: Con semilla fija, guardar y graficar produce siempre el mismo resultado.
"""

import json
import runpy
from pathlib import Path

CODIGO = Path(__file__).resolve().parents[1]


def test_montecarlo_reproducible(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    runpy.run_path(str(CODIGO / "04_montecarlo.py"))
    registro = Path("montecarlo.json").read_text(encoding="utf-8")
    experimentos = json.loads(registro)
    assert experimentos["velocidad"][0]["entrada"]["angulo"] == 45
    assert experimentos["angulo"][0]["entrada"]["velocidad"] == 10

    runpy.run_path(str(CODIGO / "05_trayectorias.py"))
    resumen_trayectorias = capsys.readouterr().out
    runpy.run_path(str(CODIGO / "06_dispersion.py"))
    resumen_dispersion = capsys.readouterr().out
    runpy.run_path(str(CODIGO / "07_distribucion.py"))
    resumen_distribucion = capsys.readouterr().out

    for nombre in ("velocidad", "angulo"):
        for sufijo in ("", "-dispersion", "-distribucion"):
            assert Path(f"montecarlo-{nombre}{sufijo}.png").read_bytes().startswith(b"\x89PNG")
    assert "velocidad:" in resumen_trayectorias
    assert "angulo:" in resumen_trayectorias
    assert "correlación" in resumen_dispersion
    assert "desviación estándar" in resumen_distribucion

    Path("montecarlo.json").unlink()
    for nombre in ("velocidad", "angulo"):
        for sufijo in ("", "-dispersion", "-distribucion"):
            Path(f"montecarlo-{nombre}{sufijo}.png").unlink()
    runpy.run_path(str(CODIGO / "04_montecarlo.py"))
    runpy.run_path(str(CODIGO / "05_trayectorias.py"))
    segunda_trayectorias = capsys.readouterr().out
    runpy.run_path(str(CODIGO / "06_dispersion.py"))
    segunda_dispersion = capsys.readouterr().out
    runpy.run_path(str(CODIGO / "07_distribucion.py"))
    segunda_distribucion = capsys.readouterr().out

    assert Path("montecarlo.json").read_text(encoding="utf-8") == registro
    assert segunda_trayectorias == resumen_trayectorias
    assert segunda_dispersion == resumen_dispersion
    assert segunda_distribucion == resumen_distribucion
