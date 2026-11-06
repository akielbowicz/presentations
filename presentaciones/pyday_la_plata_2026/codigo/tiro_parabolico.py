"""Purpose: Calcular un tiro parabólico para los ejemplos de la charla.
Responsibilities: Recibir velocidad y angulo, devolver la trayectoria x e y.
Rationale: La gravedad es constante del módulo: la salida es solo la trayectoria.
"""

from math import cos, radians, sin

GRAVEDAD = 10.0  # m/s², para facilitar el cálculo a mano


def simular(velocidad, angulo):
    """Sin rozamiento, desde el suelo. v > 0 y ángulo entre 0 y 90°.

    Velocidad en m/s. Devuelve las posiciones x e y en metros.
    """
    angulo_rad = radians(angulo)
    vx = velocidad * cos(angulo_rad)
    vy = velocidad * sin(angulo_rad)
    duracion = 2.0 * vy / GRAVEDAD
    t = [duracion * i / 100.0 for i in range(101)]
    x = [vx * instante for instante in t]
    y = [vy * instante - GRAVEDAD * instante**2 / 2.0 for instante in t]
    resultado = {"x": x, "y": y}
    return resultado
