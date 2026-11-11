"""Propiedades del atomizador determinista (espeja bajan: atomic claim units)."""

from conocimiento.atomizador import (
    MAX_UNIDAD,
    MIN_UNIDAD,
    proponer_afirmaciones_atomicas,
    unidades_de,
)
from conocimiento.modelo import Episodio


def episodio(texto: str, seccion: str = "prueba") -> Episodio:
    return Episodio(id="ep-001", seccion=seccion, linea=1, texto=texto)


def test_unidades_son_subcadenas_verbatim() -> None:
    texto = "La inscripción es obligatoria. Los formularios abren el lunes."
    unidades = unidades_de(texto)
    assert unidades, "el texto debe producir al menos una unidad"
    for unidad in unidades:
        assert unidad in texto, f"no verbatim: {unidad!r}"


def test_unidades_reconstruyen_el_texto_sin_espacios() -> None:
    texto = "Primera oración. Segunda oración; con conector. Fin."
    unidades = unidades_de(texto)
    reconstruido = " ".join(u.strip() for u in unidades)
    sin_espacios = lambda s: " ".join(s.split())
    assert sin_espacios(reconstruido) == sin_espacios(texto)


def test_fragments_cortos_se_fusionan_hacia_adelante() -> None:
    # Semántica de bajan: la unidad bajo mínimo absorbe la siguiente oración
    # y deja de absorber apenas alcanza el mínimo.
    texto = "Dr. Juan llegó temprano. Todos los participantes firmaron la lista de asistencia."
    unidades = unidades_de(texto)
    assert len(unidades) == 2
    assert unidades[0].startswith("Dr. Juan"), "el fragmento 'Dr.' se fusiona hacia adelante"
    assert len(unidades[0]) >= MIN_UNIDAD


def test_fragmento_final_corto_se_fusiona_hacia_atras() -> None:
    texto = "Las clases comienzan a las 18:00 en el salón del club. ¡Vamos!"
    unidades = unidades_de(texto)
    assert len(unidades) == 1
    assert unidades[0].endswith("¡Vamos!")


def test_unidad_larga_se_divide_en_conector_punto_y_coma() -> None:
    cuerpo = "x" * (MAX_UNIDAD + 10)  # sin puntos dentro; debe dividir en '; '
    texto = f"Parte izquierda larga {cuerpo}; parte derecha también muy larga {cuerpo}."
    unidades = unidades_de(texto)
    assert len(unidades) == 2
    assert unidades[0].endswith(";"), "el ';' queda con la parte izquierda"
    for unidad in unidades:
        assert unidad in texto, "la división es verbatim, mejor esfuerzo"


def test_texto_sin_puntuacion_final_es_una_unidad() -> None:
    # Los encabezados no llevan punto: el extractor los propone igual
    # (el defecto conocido que la visualización hace visible).
    assert unidades_de("Horarios y lugares") == ["Horarios y lugares"]


def test_min_unidad_coincide_con_bajan() -> None:
    # Espeja ATOMIZER_MIN_UNIT_CHARS = 20 y MAX = 300 de bajan.
    assert MIN_UNIDAD == 20
    assert MAX_UNIDAD == 300


def test_extractor_atomico_devuelve_afirmaciones_con_evidencia() -> None:
    episodio_ = episodio("La inscripción es obligatoria. Los formularios abren el lunes.")
    afirmaciones = proponer_afirmaciones_atomicas(episodio_)
    assert len(afirmaciones) == 2
    for a in afirmaciones:
        assert a.texto in episodio_.texto  # evidencia verbatim
        assert a.evidencia.seccion == "prueba"
        assert a.evidencia.linea >= 1
        assert a.evidencia.cita == a.texto


def test_extractor_declara_su_version_para_el_cache() -> None:
    # Espeja bajan: la versión del extractor es identidad de caché.
    from conocimiento.atomizador import EXTRACTOR_ATOMICO

    assert EXTRACTOR_ATOMICO.version().startswith("atomico-")


def test_preguntas_sobreviven_como_candidatas() -> None:
    # El defecto conocido: las preguntas se extraen como si fueran conocimiento.
    episodio_ = episodio("¿Qué pasa si no puedo asistir a una clase?")
    afirmaciones = proponer_afirmaciones_atomicas(episodio_)
    assert len(afirmaciones) == 1
    assert afirmaciones[0].texto.startswith("¿")
