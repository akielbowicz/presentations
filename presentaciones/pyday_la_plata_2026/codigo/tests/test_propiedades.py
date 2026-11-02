"""Purpose: Mostrar una propiedad física con ejemplos generados por Hypothesis.
Responsibilities: Comprobar la simetría entre ángulos complementarios.
Rationale: Una propiedad amplía los casos sin agregar más resultados manuales.
"""

import pytest
from hypothesis import given, strategies as st

from tiro_parabolico import simular


@given(angulo=st.floats(min_value=1, max_value=89))
def test_angulos_complementarios_tienen_el_mismo_alcance(angulo):
    uno = simular(velocidad=10, angulo=angulo, gravedad=10)
    otro = simular(velocidad=10, angulo=90 - angulo, gravedad=10)
    assert uno["alcance"] == pytest.approx(otro["alcance"])
