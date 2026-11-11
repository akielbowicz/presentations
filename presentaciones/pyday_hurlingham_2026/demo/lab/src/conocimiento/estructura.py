"""Extractor por estructura: la hipótesis alternativa.

Hipótesis: si además del texto usamos la estructura del documento
(encabezados vs. cuerpo, preguntas vs. enunciados), mejoramos la
precisión sin perder recall ni evidencia.
"""

from .atomizador import MIN_UNIDAD, unidades_de
from .modelo import Afirmacion, Episodio, Evidencia, linea_de

_SECCIONES_NO_CUERPO = frozenset({"título", "encabezado"})


def es_conocimiento(unidad: str) -> bool:
    """Los títulos y las preguntas no son conocimiento; los enunciados sí."""
    if unidad.startswith(("¿", "¡")):
        return False
    return len(unidad) >= MIN_UNIDAD


def proponer_afirmaciones_estructura(episodio: Episodio) -> list[Afirmacion]:
    if episodio.seccion in _SECCIONES_NO_CUERPO:
        return []
    return [
        Afirmacion(
            id="",
            texto=u,
            evidencia=Evidencia(
                seccion=episodio.seccion,
                linea=linea_de(u, episodio),
                cita=u,
            ),
        )
        for u in unidades_de(episodio.texto)
        if es_conocimiento(u)
    ]


class ExtractorEstructura:
    def version(self) -> str:
        return f"estructura-{_VERSION}"

    def proponer(self, episodio: Episodio) -> list[Afirmacion]:
        return proponer_afirmaciones_estructura(episodio)


EXTRACTOR_ESTRUCTURA = ExtractorEstructura()

_VERSION = "0.1.0"
