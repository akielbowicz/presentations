"""El extractor por estructura: hipótesis alternativa para mejorar precisión."""

from conocimiento.estructura import proponer_afirmaciones_estructura
from conocimiento.modelo import Episodio


def episodio(texto: str, seccion: str = "cuerpo") -> Episodio:
    return Episodio(id="ep-002", seccion=seccion, linea=2, texto=texto)


def test_descarta_titulos_y_navegacion() -> None:
    episodio_ = episodio("Horarios y lugares", seccion="título")
    assert proponer_afirmaciones_estructura(episodio_) == []


def test_descarta_preguntas() -> None:
    episodio_ = episodio("¿Los talleres son gratuitos?")
    assert proponer_afirmaciones_estructura(episodio_) == []


def test_conserva_oraciones_enunciativas_del_cuerpo() -> None:
    episodio_ = episodio("La inscripción es obligatoria. Los formularios abren el lunes.")
    afirmaciones = proponer_afirmaciones_estructura(episodio_)
    assert len(afirmaciones) == 2
    assert all(not a.texto.startswith("¿") for a in afirmaciones)


def test_conserva_items_de_lista() -> None:
    episodio_ = episodio("Los talleres de robótica funcionan en la biblioteca.")
    afirmaciones = proponer_afirmaciones_estructura(episodio_)
    assert len(afirmaciones) == 1


def test_version_para_cache() -> None:
    from conocimiento.estructura import EXTRACTOR_ESTRUCTURA

    assert EXTRACTOR_ESTRUCTURA.version().startswith("estructura-")
