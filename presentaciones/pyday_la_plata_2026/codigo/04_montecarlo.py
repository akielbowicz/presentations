"""Purpose: Simular experimentos de Monte Carlo y registrar sus resultados.
Responsibilities: Perturbar un input por vez y guardar entradas y salidas en JSON.
Rationale: Variar de a un parámetro separa el efecto de velocidad del de angulo.
"""

import json
import random
from pathlib import Path
from tiro_parabolico import simular

random.seed(42)  # experimento reproducible
experimentos = {"velocidad": [], "angulo": []}
for _ in range(1000):
    velocidad = random.gauss(10.0, 0.5)
    angulo = random.gauss(45.0, 2.0)
    experimentos["velocidad"].append({
        "entrada": {"velocidad": velocidad, "angulo": 45},
        "salida": simular(velocidad=velocidad, angulo=45),
    })
    experimentos["angulo"].append({
        "entrada": {"velocidad": 10, "angulo": angulo},
        "salida": simular(velocidad=10, angulo=angulo),
    })
Path("montecarlo.json").write_text(json.dumps(experimentos), encoding="utf-8")
