"""Integración aceleración → velocidad y el filtro que evita la deriva.

Integrar ruido produce deriva (caminata aleatoria): cada muestra de ruido
se acumula en la velocidad. Un promedio móvil antes de integrar corta esa
deriva. Es la razón por la que MÁS data no es MEJOR velocidad.
"""

from __future__ import annotations


def integrar(t: list[float], a: list[float]) -> list[float]:
    """Velocidad por trapecio acumulado, v(0) = 0."""
    v = [0.0]
    for i in range(1, len(t)):
        dt = t[i] - t[i - 1]
        v.append(v[-1] + (a[i] + a[i - 1]) / 2.0 * dt)
    return v


def media_movil(valores: list[float], ventana: int) -> list[float]:
    """Promedio móvil centrado; en los bordes usa la ventana disponible."""
    if ventana < 2:
        return list(valores)
    mitad = ventana // 2
    salida: list[float] = []
    for i in range(len(valores)):
        lo = max(0, i - mitad)
        hi = min(len(valores), i + mitad + 1)
        salida.append(sum(valores[lo:hi]) / (hi - lo))
    return salida
