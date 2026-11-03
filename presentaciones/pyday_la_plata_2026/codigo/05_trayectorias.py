"""Purpose: Visualizar el experimento de Monte Carlo registrado.
Responsibilities: Graficar todas las trayectorias guardadas y resumir la distribución.
Rationale: El resumen se calcula desde lo guardado, no desde un recálculo.
"""

import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

lanzamientos = json.loads(Path("montecarlo.json").read_text(encoding="utf-8"))

for lanzamiento in lanzamientos:
    plt.plot(lanzamiento["x"], lanzamiento["y"], alpha=0.1)

alcances = sorted(lanzamiento["alcance"] for lanzamiento in lanzamientos)
plt.title(f"Monte Carlo: {len(lanzamientos)} lanzamientos")
plt.xlabel("Distancia [m]")
plt.ylabel("Altura [m]")
plt.savefig("montecarlo.png")
print(f"alcance medio: {sum(alcances) / len(alcances):.2f} m")
print(f"percentiles 5 y 95: {alcances[49]:.2f} y {alcances[949]:.2f} m")
