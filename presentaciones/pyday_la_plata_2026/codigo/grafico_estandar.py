"""Purpose: Estandarizar el formato de los gráficos de los análisis.
Responsibilities: Crear la figura con el título y las etiquetas estándar de la charla.
Rationale: Los datos y el ploting quedan separados: cada análisis grafica lo suyo con un formato único.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


# el formato único, reusado por 05, 06 y 07
def nueva_figura(titulo, xlabel="Distancia [m]", ylabel="Altura [m]"):
    plt.figure()
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
