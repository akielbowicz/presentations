"""Correspondencia spec ↔ test: lo que queremos no se divorcia de lo verificamos.

Espeja la idea de espectacular y de los specs de bajan: cada propiedad
de una spec tiene al menos un test que la verifica, y cada ancla que un
test declara existe en alguna spec. Sin fantasmas, sin olvidadas.
"""

import sys
from pathlib import Path

TESTS = Path(__file__).parent
sys.path.insert(0, str(TESTS))  # los módulos de tests importan como top-level

import test_atomizador  # noqa: E402,F401  (importar llena el registro de anclas)
import test_estructura  # noqa: E402,F401
import test_evaluar  # noqa: E402,F401
import test_pipeline  # noqa: E402,F401
from conocimiento.especificaciones import (  # noqa: E402
    ESPECIFICADAS,
    Especificacion,
    anclas_de_directorio,
    cargar_especificaciones,
    cobertura,
)

LAB = TESTS.parent
SPECS = LAB / "specs"


def escribir_spec(tmp_path: Path, contenido: str) -> Path:
    (tmp_path / "specs").mkdir()
    ruta = tmp_path / "specs" / "cosa.md"
    ruta.write_text(contenido, encoding="utf-8")
    return tmp_path / "specs"


def test_parser_extrae_id_statement_y_propiedades(tmp_path) -> None:
    directorio = escribir_spec(
        tmp_path,
        "---\n"
        "id: cosa.base\n"
        "kind: intent\n"
        'statement: "THE cosa SHALL funcionar"\n'
        "---\n"
        "\n"
        "# modelo\n"
        "\n"
        "| propiedad | alcance |\n"
        "|---|---|\n"
        "| [[cosa.base.uno]] | primera |\n"
        "| [[cosa.base.dos]] | segunda |\n",
    )
    specs = cargar_especificaciones(directorio)
    assert "cosa.base" in specs
    spec = specs["cosa.base"]
    assert isinstance(spec, Especificacion)
    assert spec.statement == "THE cosa SHALL funcionar"
    assert spec.propiedades == ("cosa.base.uno", "cosa.base.dos")


def test_cobertura_marca_fantasmas_y_olvidadas(tmp_path) -> None:
    directorio = escribir_spec(
        tmp_path,
        "---\n"
        "id: cosa.base\n"
        "kind: intent\n"
        'statement: "THE cosa SHALL funcionar"\n'
        "---\n"
        "| [[cosa.base.uno]] |\n",
    )
    specs = cargar_especificaciones(directorio)
    anclas = {"cosa.base.uno", "cosa.base.virbatim"}  # typo: fantasma
    reporte = cobertura(specs, anclas)
    assert reporte.fantasma == {"cosa.base.virbatim"}
    assert reporte.olvidadas == set()


def test_cobertura_marca_propiedades_olvidadas(tmp_path) -> None:
    directorio = escribir_spec(
        tmp_path,
        "---\n"
        "id: cosa.base\n"
        "kind: intent\n"
        'statement: "THE cosa SHALL funcionar"\n'
        "---\n"
        "| [[cosa.base.uno]] |\n"
        "| [[cosa.base.olvidada]] |\n",
    )
    specs = cargar_especificaciones(directorio)
    reporte = cobertura(specs, {"cosa.base.uno"})
    assert reporte.olvidadas == {"cosa.base.olvidada"}
    assert reporte.fantasma == set()


def test_los_links_en_prosa_no_son_propiedades(tmp_path) -> None:
    directorio = escribir_spec(
        tmp_path,
        "---\n"
        "id: cosa.base\n"
        "kind: intent\n"
        'statement: "THE cosa SHALL funcionar"\n'
        "---\n"
        "\n"
        "La prosa puede referenciar [[cosa.otra]] sin que sea una propiedad.\n"
        "\n"
        "| propiedad |\n"
        "|---|\n"
        "| [[cosa.base.uno]] | primera |\n",
    )
    specs = cargar_especificaciones(directorio)
    assert specs["cosa.base"].propiedades == ("cosa.base.uno",)


def test_anclas_de_directorio_escanea_decoradores(tmp_path) -> None:
    tests = tmp_path / "tests"
    tests.mkdir()
    # El decorador se arma por concatenación para que este mismo archivo
    # no contenga un @especifica literal que el escáner pueda confundir.
    decorador = "@" + "especifica" + '("x.base.uno")'
    (tests / "test_x.py").write_text(
        "from conocimiento.especificaciones import especifica\n"
        "\n"
        f"{decorador}\n"
        "def test_uno():\n"
        '    mensaje = "no confundir con strings comunes"\n'
        "\n"
        "def test_sin_ancla():\n"
        "    pass\n",
        encoding="utf-8",
    )
    assert anclas_de_directorio(tests) == {"x.base.uno"}


def test_la_especificacion_real_esta_cubierta_completa() -> None:
    """La suite real: sin fantasmas, sin olvidadas, registro ≡ escaneo."""
    specs = cargar_especificaciones(SPECS)
    anclas = set(ESPECIFICADAS)
    reporte = cobertura(specs, anclas)
    assert reporte.fantasma == set(), f"anclas sin spec: {reporte.fantasma}"
    assert reporte.olvidadas == set(), f"propiedades sin test: {reporte.olvidadas}"
    assert anclas_de_directorio(TESTS) == anclas, (
        "el escaneo del código y el registro difieren: ¿hay un @especifica "
        "mal escrito o un test importado de más?"
    )


def test_toda_spec_declara_al_menos_una_propiedad() -> None:
    specs = cargar_especificaciones(SPECS)
    assert specs, "el directorio specs/ no puede quedar vacío"
    for spec in specs.values():
        assert spec.propiedades, f"la spec {spec.id} no declara propiedades"
        assert spec.statement, f"la spec {spec.id} no declara statement"
