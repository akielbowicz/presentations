"""Purpose: Simular un experimento de Monte Carlo y registrar sus resultados.
Responsibilities: Perturbar velocidad y angulo, guardar cada lanzamiento en JSON.
Rationale: El módulo puro permite nuevos experimentos sin modificar la física.
"""

import json
import random
from pathlib import Path
from tiro_parabolico import simular

random.seed(42)  # experimento reproducible
lanzamientos = [
    simular(velocidad=random.gauss(10, 0.5), angulo=random.gauss(45, 2))
    for _ in range(1000)
]
Path("montecarlo.json").write_text(json.dumps(lanzamientos), encoding="utf-8")
