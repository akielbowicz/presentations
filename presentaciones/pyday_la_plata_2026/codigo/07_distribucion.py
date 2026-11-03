"""Purpose: Analizar la distribución de alcances del experimento registrado.
Responsibilities: Graficar el histograma de alcances con la media y la desviación estándar.
Rationale: Un paso extra sobre los datos guardados, sin recalcular simulaciones.
"""

import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
from statistics import mean, stdev

# paso extra sobre los datos guardados: distribución del alcance final
experimentos = json.loads(Path("montecarlo.json").read_text(encoding="utf-8"))

for nombre, lanzamientos in experimentos.items():
    alcances = [lanzamiento["salida"]["alcance"] for lanzamiento in lanzamientos]
    plt.hist(alcances, bins=50)
    plt.axvline(mean(alcances), color="black")
    plt.title(f"Monte Carlo variando {nombre}")
    plt.xlabel("Distancia final [m]")
    plt.savefig(f"montecarlo-{nombre}-distribucion.png")
    plt.close()
    print(f"{nombre}: media {mean(alcances):.2f} m, "
          f"desviación estándar {stdev(alcances):.2f} m")
