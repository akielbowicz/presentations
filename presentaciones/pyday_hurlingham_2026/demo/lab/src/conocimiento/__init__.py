"""Laboratorio de conocimiento: documentos → afirmaciones con evidencia."""

from .modelo import Afirmacion, Episodio, Evidencia, Extractor
from .pipeline import episodios_de, procesar, escribir

__all__ = [
    "Afirmacion",
    "Episodio",
    "Evidencia",
    "Extractor",
    "episodios_de",
    "procesar",
    "escribir",
]
