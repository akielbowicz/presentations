"""Especificaciones y su correspondencia con los tests.

Espeja los specs de bajan (`specs/*.md` con frontmatter id/kind/statement
y propiedades [[ancla]]) y la idea de espectacular: cada propiedad tiene
un test que la verifica y cada ancla declarada existe en alguna spec.
Sin fantasmas (anclas mal escritas), sin olvidadas (propiedades sin test).
"""

import re
from dataclasses import dataclass, field
from pathlib import Path

_FRONTMATTER_ID = re.compile(r"^id:\s*(.+)$", re.MULTILINE)
_FRONTMATTER_STATEMENT = re.compile(r'^statement:\s*"(.+)"', re.MULTILINE)
_ANCLA = re.compile(r"\[\[([\w.\-]+)\]\]")
_DECORADOR = re.compile(r"""@especifica\(\s*["']([\w.\-]+)["']\s*\)""")


@dataclass(frozen=True)
class Especificacion:
    """Lo que realmente queremos, escrito donde no lo vamos a olvidar."""

    id: str
    statement: str
    propiedades: tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class Cobertura:
    """El resultado de contrastar specs contra tests."""

    fantasma: frozenset[str]  # anclas que ninguna spec declara (¿typo?)
    olvidadas: frozenset[str]  # propiedades que ningún test verifica

    @property
    def limpia(self) -> bool:
        return not self.fantasma and not self.olvidadas


def cargar_especificaciones(directorio: Path) -> dict[str, Especificacion]:
    """Lee todos los *.md del directorio y devuelve {id: Especificacion}.

    Las propiedades son las anclas `[[...]]` en filas de tabla; los links
    `[[...]]` en prosa son referencias cruzadas, no propiedades.
    """
    specs: dict[str, Especificacion] = {}
    for ruta in sorted(Path(directorio).glob("*.md")):
        texto = ruta.read_text(encoding="utf-8")
        m_id = _FRONTMATTER_ID.search(texto)
        if not m_id:
            raise ValueError(f"{ruta}: falta `id:` en el frontmatter")
        m_statement = _FRONTMATTER_STATEMENT.search(texto)
        filas_de_tabla = (
            linea for linea in texto.splitlines() if linea.lstrip().startswith("|")
        )
        propiedades = tuple(
            ancla
            for linea in filas_de_tabla
            for ancla in _ANCLA.findall(linea)
        )
        spec = Especificacion(
            id=m_id.group(1).strip(),
            statement=(m_statement.group(1) if m_statement else ""),
            propiedades=propiedades,
        )
        specs[spec.id] = spec
    return specs


def anclas_de_directorio(directorio: Path) -> set[str]:
    """Escanea los *.py y devuelve las anclas declaradas con @especifica."""
    anclas: set[str] = set()
    for ruta in sorted(Path(directorio).rglob("*.py")):
        anclas |= set(_DECORADOR.findall(ruta.read_text(encoding="utf-8")))
    return anclas


def cobertura(
    specs: dict[str, Especificacion], anclas: set[str]
) -> Cobertura:
    """Contrasta anclas declaradas en tests contra propiedades de specs."""
    propiedades = {p for s in specs.values() for p in s.propiedades}
    return Cobertura(
        fantasma=frozenset(anclas - propiedades),
        olvidadas=frozenset(propiedades - anclas),
    )


# Registro poblado en import-time por el decorador.
ESPECIFICADAS: set[str] = set()


def especifica(ancla: str):
    """Declara que este test verifica la propiedad `ancla` de una spec.

    El registro alimenta la verificación de correspondencia; el escáner
    (`anclas_de_directorio`) es la fuente de verdad para los reportes.
    """

    def decorador(test):
        ESPECIFICADAS.add(ancla)
        return test

    return decorador
