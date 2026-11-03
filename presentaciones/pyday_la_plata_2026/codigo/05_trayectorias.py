"""Purpose: Visualizar las trayectorias de los experimentos registrados.
Responsibilities: Graficar las trayectorias guardadas y resumir sus alcances.
Rationale: El resumen se calcula desde lo guardado, no desde un recálculo.
"""

import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

experimentos = json.loads(Path("montecarlo.json").read_text(encoding="utf-8"))

for nombre, lanzamientos in experimentos.items():
    for lanzamiento in lanzamientos:
        plt.plot(lanzamiento["salida"]["x"], lanzamiento["salida"]["y"], alpha=0.1)
    plt.title(f"Monte Carlo variando {nombre}")
    plt.savefig(f"montecarlo-{nombre}.png")
    plt.close()
    alcances = sorted(lanzamiento["salida"]["alcance"] for lanzamiento in lanzamientos)
    media = sum(alcances) / len(alcances)
    print(f"{nombre}: alcance medio {media:.2f} m, "
          f"percentiles 5 y 95: {alcances[49]:.2f} y {alcances[949]:.2f} m")
