"""El modelo: episodios, afirmaciones y la costura (seam) de extractores.

Espeja los conceptos de bajan: el pipeline valida, cachea y registra;
los extractores solamente proponen candidatos.
"""

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class Evidencia:
    """Dónde y con qué texto verbatim se respalda una afirmación."""

    seccion: str
    linea: int  # 1-based, dentro del documento original
    cita: str  # verbatim


@dataclass(frozen=True)
class Episodio:
    """Un fragmento normalizado del documento, con su origen."""

    id: str
    seccion: str  # "título", "encabezado" o el nombre de la sección
    linea: int  # línea donde empieza el episodio
    texto: str


@dataclass(frozen=True)
class Afirmacion:
    """Un candidato a conocimiento, respaldado por evidencia verbatim."""

    id: str
    texto: str
    evidencia: Evidencia

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "texto": self.texto,
            "seccion": self.evidencia.seccion,
            "linea": self.evidencia.linea,
            "cita": self.evidencia.cita,
        }


class Extractor(Protocol):
    """El contrato de la costura: proponer candidatos para UN episodio.

    Espeja `bajan::extract::Extractor`: la versión es identidad de caché;
    el pipeline (no el extractor) valida, registra y proyecta lineage.
    """

    def version(self) -> str: ...

    def proponer(self, episodio: Episodio) -> list[Afirmacion]: ...


def linea_de(unidad: str, episodio: Episodio) -> int:
    """Localiza la unidad dentro del episodio y devuelve la línea del documento."""
    offset = episodio.texto.find(unidad)
    if offset < 0:
        return episodio.linea
    return episodio.linea + episodio.texto.count("\n", 0, offset)
