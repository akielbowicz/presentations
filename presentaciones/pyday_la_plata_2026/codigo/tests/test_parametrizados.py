"""Purpose: Mostrar cómo probar varios ángulos sin copiar el mismo test.
Responsibilities: Comparar la distancia final con resultados conocidos.
Rationale: Una tabla hace visible qué cambia entre los casos.
"""

import pytest

from tiro_parabolico import simular


@pytest.mark.parametrize("angulo, alcance", [
    (0, 0),
    (30, 5 * 3**0.5),
    (45, 10),
    (60, 5 * 3**0.5),
    (90, 0),
])
def test_alcances_conocidos(angulo, alcance):
    salida = simular(velocidad=10, angulo=angulo)
    assert salida["x"][-1] == pytest.approx(alcance, abs=1e-12)
