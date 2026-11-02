"""Purpose: Mostrar el cálculo y el gráfico juntos, antes de modularizar.
Responsibilities: Calcular un lanzamiento fijo y guardar trayectoria.png.
Rationale: El primer ejemplo es un script directo, sin clases ni CLI.
"""

from math import cos, radians, sin

import matplotlib.pyplot as plt

velocidad = 10  # m/s
angulo = radians(45)
gravedad = 10  # m/s², para facilitar el cálculo a mano

vx = velocidad * cos(angulo)
vy = velocidad * sin(angulo)
duracion = 2 * vy / gravedad
t = [duracion * i / 100 for i in range(101)]
x = [vx * instante for instante in t]
y = [vy * instante - gravedad * instante**2 / 2 for instante in t]

plt.plot(x, y)
plt.xlabel("Distancia [m]")
plt.ylabel("Altura [m]")
plt.grid()
plt.savefig("trayectoria.png")
plt.close()
