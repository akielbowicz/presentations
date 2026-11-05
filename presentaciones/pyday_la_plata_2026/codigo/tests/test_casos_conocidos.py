"""Purpose: Comprobar un lanzamiento que se puede calcular a mano.
Responsibilities: Verificar la distancia final, la altura máxima y el aterrizaje.
Rationale: Un caso conocido permite probar la física sin infraestructura adicional.
"""

import pytest

from tiro_parabolico import simular


def test_lanzamiento_a_45_grados():
    salida = simular(velocidad=10, angulo=45)

    # Calculado a mano: alcance = v²·sen(2θ)/g = 10 m, altura = v²·sen²(θ)/(2g) = 2.5 m
    assert salida["x"][-1] == pytest.approx(10)
    assert max(salida["y"]) == pytest.approx(2.5)
    assert salida["y"][0] == pytest.approx(0)
    assert salida["y"][-1] == pytest.approx(0, abs=1e-12)
