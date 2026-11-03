"""Purpose: Comprobar un lanzamiento que se puede calcular a mano.
Responsibilities: Verificar alcance, duración y altura máxima.
Rationale: Un caso conocido permite probar la física sin infraestructura adicional.
"""

import pytest

from tiro_parabolico import simular


def test_lanzamiento_a_45_grados():
    salida = simular(velocidad=10, angulo=45, gravedad=10)

    # Calculado a mano: alcance = v²·sen(2θ)/g, duración = 2v·sen(θ)/g, h = v²·sen²(θ)/(2g)
    assert salida["alcance"] == pytest.approx(10)
    assert salida["duracion"] == pytest.approx(2**0.5)
    assert salida["altura_maxima"] == pytest.approx(2.5)
    assert salida["y"][0] == pytest.approx(0)
    assert salida["y"][-1] == pytest.approx(0, abs=1e-12)
