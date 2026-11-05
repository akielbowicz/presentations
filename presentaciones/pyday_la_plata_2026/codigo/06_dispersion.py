"""Purpose: Relacionar el parámetro perturbado con la distancia final registrada.
Responsibilities: Graficar el scatter entrada vs alcance para cada experimento.
Rationale: El registro guarda los inputs, así que el efecto es rastreable al parámetro.
"""

import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from grafico_estandar import nueva_figura
from pathlib import Path
from statistics import correlation

experimentos = json.loads(Path("montecarlo.json").read_text(encoding="utf-8"))

for nombre, lanzamientos in experimentos.items():
    nueva_figura(f"Monte Carlo variando {nombre}", xlabel=nombre,
                 ylabel="Distancia final [m]")
    plt.scatter(
        [lanzamiento["entrada"][nombre] for lanzamiento in lanzamientos],
        [lanzamiento["salida"]["x"][-1] for lanzamiento in lanzamientos],
        alpha=0.1,
    )
    plt.savefig(f"montecarlo-{nombre}-dispersion.png")
    plt.close()
    correlacion = correlation(
        [lanzamiento["entrada"][nombre] for lanzamiento in lanzamientos],
        [lanzamiento["salida"]["x"][-1] for lanzamiento in lanzamientos],
    )
    print(f"{nombre}: correlación {correlacion:+.2f}")
