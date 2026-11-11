"""Extractor atómico (determinista): segmenta oraciones en unidades.

Espeja `bajan::extract::atomic_claim_units`: límites de oración, fusión
de fragmentos cortos hacia adelante, fusión del fragmento final corto
hacia atrás y división de unidades largas en conectores '; '.
Defecto conocido: extrae encabezados y preguntas como si fueran
conocimiento.
"""

import re

from .modelo import Afirmacion, Episodio, Evidencia, linea_de

MIN_UNIDAD = 20  # chars; unidades menores se fusionan (bajan-5zy)
MAX_UNIDAD = 300  # chars; unidades mayores se dividen en '; '

_ORACION = re.compile(r"[^.!?…]+[.!?…]+[\"'»)\]]*")


def unidades_de(texto: str) -> list[str]:
    """Segmenta en oraciones; misma entrada → mismas unidades."""
    unidades: list[str] = []
    for m in _ORACION.finditer(texto):
        unidad = m.group(0).strip()
        if unidad:
            unidades.append(unidad)
    if not unidades and texto.strip():
        # Sin puntuación final (p. ej. encabezados): el texto entero es una unidad.
        unidades = [texto.strip()]

    # 1. Fusionar hacia adelante mientras la unidad quede bajo el mínimo.
    fusionadas: list[str] = []
    for unidad in unidades:
        if fusionadas and len(fusionadas[-1]) < MIN_UNIDAD:
            fusionadas[-1] = f"{fusionadas[-1]} {unidad}"
        else:
            fusionadas.append(unidad)

    # 2. El fragmento final corto se fusiona hacia atrás.
    if len(fusionadas) > 1 and len(fusionadas[-1]) < MIN_UNIDAD:
        ultima = fusionadas.pop()
        fusionadas[-1] = f"{fusionadas[-1]} {ultima}"

    # 3. Unidades largas se dividen en '; ' (mejor esfuerzo, nunca a mitad
    #    de palabra): una unidad grande honesta vale más que una mangled.
    finales: list[str] = []
    for unidad in fusionadas:
        if len(unidad) > MAX_UNIDAD and "; " in unidad:
            partes = unidad.split("; ")
            finales.append(partes[0] + ";")
            finales.extend(p for p in partes[1:] if p)
        else:
            finales.append(unidad)
    return finales


def proponer_afirmaciones_atomicas(episodio: Episodio) -> list[Afirmacion]:
    unidades = unidades_de(episodio.texto)
    return [
        Afirmacion(
            id="",
            texto=u,
            evidencia=Evidencia(
                seccion=episodio.seccion, linea=linea_de(u, episodio), cita=u
            ),
        )
        for u in unidades
    ]


class ExtractorAtomico:
    def version(self) -> str:
        return f"atomico-{_VERSION}"

    def proponer(self, episodio: Episodio) -> list[Afirmacion]:
        return proponer_afirmaciones_atomicas(episodio)


EXTRACTOR_ATOMICO = ExtractorAtomico()

_VERSION = "0.1.0"
