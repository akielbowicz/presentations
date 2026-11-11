"""Evaluación contra corpus dorado (espeja bajan evals: precisión y recall)."""

from conocimiento.evaluar import evaluar, puntuar

DORADO = [
    {"texto": "La inscripción es obligatoria para todos los talleres."},
    {"texto": "Cada taller tiene un cupo máximo de 25 personas."},
]

PRODUCIDAS = [
    {"texto": "La inscripción es obligatoria para todos los talleres."},
    {"texto": "La inscripción es obligatoria para todos los talleres."},  # duplicada
    {"texto": "Cada taller tiene un cupo máximo de 25 personas."},
    {"texto": "Inscripción"},  # espuria (encabezado)
    {"texto": "¿Los talleres son gratuitos?"},  # espuria (pregunta)
]


def test_coincidencia_colapsa_espacios() -> None:
    producida = {"texto": "La inscripción   es obligatoria\npara todos los talleres."}
    assert puntuar([producida], DORADO) == (1, 1, 2)


def test_precision_recall_y_clases() -> None:
    coincidencias, precisas, esperadas = puntuar(PRODUCIDAS, DORADO)
    assert esperadas == 2
    assert precisas == 3, "ambas doradas + la copia duplicada cuentan como precisas"
    assert coincidencias == 2, "las dos doradas fueron encontradas"
    precisión, recall = evaluar(PRODUCIDAS, DORADO)
    assert precisión == 3 / 5
    assert recall == 2 / 2


def test_nada_producido_no_divide_por_cero() -> None:
    assert evaluar([], DORADO) == (0.0, 0.0)
    assert evaluar(PRODUCIDAS, []) == (0.0, 0.0)
