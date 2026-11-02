"""Purpose: Calcular un tiro parabólico para los ejemplos de la charla.
Responsibilities: Recibir parámetros y devolver resultados en un diccionario.
Rationale: Una función basta para separar la física de los archivos y el gráfico.
"""

from math import cos, radians, sin


def simular(velocidad, angulo, gravedad=10):
    """Sin rozamiento, desde el suelo. v > 0, g > 0 y ángulo entre 0 y 90°.

    Velocidad en m/s, ángulo en grados y gravedad en m/s².
    """
    vx = velocidad * cos(radians(angulo))
    vy = velocidad * sin(radians(angulo))
    duracion = 2 * vy / gravedad
    t = [duracion * i / 100 for i in range(101)]
    x = [vx * instante for instante in t]
    y = [vy * instante - gravedad * instante**2 / 2 for instante in t]
    return {
        "t": t,
        "x": x,
        "y": y,
        "duracion": duracion,
        "alcance": vx * duracion,
        "altura_maxima": vy**2 / (2 * gravedad),
    }
