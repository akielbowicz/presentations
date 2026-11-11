"""Pipeline extremo a extremo: documento → episodios → afirmaciones → JSON."""

import json
from pathlib import Path

from conocimiento.atomizador import EXTRACTOR_ATOMICO
from conocimiento.especificaciones import especifica
from conocimiento.pipeline import episodios_de, procesar

FIXTURE = Path(__file__).parent / "fixtures" / "documento.md"


@especifica("pipeline.contract.episodios-titulos")
def test_episodios_separan_titulos_del_cuerpo() -> None:
    texto = FIXTURE.read_text(encoding="utf-8")
    episodios = episodios_de(texto)
    titulo = [e for e in episodios if e.seccion == "título"]
    assert titulo and titulo[0].texto == "Documento de prueba"
    encabezados = [e for e in episodios if e.seccion == "encabezado"]
    assert "Inscripción" in [e.texto for e in encabezados]
    cuerpo = [e for e in episodios if e.seccion == "Inscripción"]
    assert cuerpo and "La inscripción es obligatoria" in cuerpo[0].texto


@especifica("pipeline.contract.json-claves")
def test_procesar_produce_json_con_contrato_estable() -> None:
    documento = procesar(FIXTURE, EXTRACTOR_ATOMICO)
    serializado = json.dumps(documento, ensure_ascii=False)
    datos = json.loads(serializado)
    assert set(datos) == {"documento", "extractor", "episodios", "afirmaciones"}
    afirmacion = datos["afirmaciones"][0]
    assert set(afirmacion) == {"id", "texto", "seccion", "linea", "cita"}
    assert set(datos["extractor"]) == {"version"}


@especifica("pipeline.contract.evidencia-linea")
def test_toda_afirmacion_cita_texto_verbatim_del_documento() -> None:
    texto = FIXTURE.read_text(encoding="utf-8")
    documento = procesar(FIXTURE, EXTRACTOR_ATOMICO)
    lineas = texto.splitlines()
    for a in documento["afirmaciones"]:
        assert a["cita"] == a["texto"], "la evidencia es la afirmación misma, verbatim"
        linea = lineas[a["linea"] - 1]
        assert a["texto"] in linea, f"la cita debe localizar en su línea: {a['texto']!r}"


@especifica("pipeline.contract.evidencia-linea")
def test_cada_episodio_registra_linea_de_origen() -> None:
    episodios = episodios_de(FIXTURE.read_text(encoding="utf-8"))
    for e in episodios:
        assert e.linea >= 1
