"""Evaluación contra corpus dorado (espeja bajan evals).

Mide precisión y recall de las afirmaciones producidas contra ejemplos
adjudicados a mano. La coincidencia colapsa espacios y compara texto
exacto: simple de explicar en una charla, honesto sobre sus límites.
"""


def _normalizar(texto: str) -> str:
    return " ".join(texto.split())


def puntuar(producidas: list[dict], dorado: list[dict]) -> tuple[int, int, int]:
    """Devuelve (coincidencias_distintas, producidas_precisas, esperadas)."""
    dorado_norm = {_normalizar(d["texto"]) for d in dorado}
    producidas_norm = [_normalizar(p["texto"]) for p in producidas]
    precisas = sum(1 for t in producidas_norm if t in dorado_norm)
    coincidencias = len(dorado_norm & set(producidas_norm))
    return coincidencias, precisas, len(dorado_norm)


def evaluar(producidas: list[dict], dorado: list[dict]) -> tuple[float, float]:
    """Devuelve (precisión, recall); 0.0 si no hay nada que comparar."""
    if not producidas or not dorado:
        return (0.0, 0.0)
    coincidencias, precisas, esperadas = puntuar(producidas, dorado)
    return (precisas / len(producidas), coincidencias / esperadas)
