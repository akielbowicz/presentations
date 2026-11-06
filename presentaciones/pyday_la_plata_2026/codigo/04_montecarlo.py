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
    parametros = {
        "velocidad": random.gauss(10.0, 0.5),
        "angulo": 45.0,
    }

    experimentos["velocidad"].append({
        "entrada": parametros,
        "salida" : simular(**parametros),
    })

for _ in range(1000):
    parametros = {
        "velocidad": 10.0,
        "angulo": random.gauss(45.0, 2.0),
    }

    experimentos["angulo"].append({
        "entrada": parametros,
        "salida" : simular(**parametros),
    })

Path("montecarlo.json").write_text(json.dumps(experimentos), encoding="utf-8")
