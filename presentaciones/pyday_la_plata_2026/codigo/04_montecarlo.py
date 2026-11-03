"""Purpose: Simular experimentos de Monte Carlo y registrar sus resultados.
Responsibilities: Perturbar un input por vez y guardar cada lanzamiento en JSON.
Rationale: Variar de a un parámetro separa el efecto de velocidad del de angulo.
"""

import json
import random
from pathlib import Path
from tiro_parabolico import simular

random.seed(42)  # experimento reproducible
experimentos = {
    "velocidad": [
        simular(velocidad=random.gauss(10, 0.5), angulo=45)
        for _ in range(1000)
    ],
    "angulo": [
        simular(velocidad=10, angulo=random.gauss(45, 2))
        for _ in range(1000)
    ],
}
Path("montecarlo.json").write_text(json.dumps(experimentos), encoding="utf-8")
