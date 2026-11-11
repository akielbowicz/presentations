"""El pipeline: documento → episodios → extractores → afirmaciones → JSON.

El pipeline es dueño de la validación y de los ids; los extractores
solamente proponen candidatos (la costura de bajan).
"""

import json
import re
from dataclasses import asdict
from pathlib import Path

from .modelo import Afirmacion, Episodio, Evidencia, Extractor, linea_de

_ENCABEZADO = re.compile(r"#{1,6}\s+(.*)")


def episodios_de(texto_md: str) -> list[Episodio]:
    """Separa encabezados (episodios propios) del cuerpo de cada sección.

    El primer encabezado del documento episodia como "título"; los demás
    como "encabezado". El cuerpo de cada sección episodia con el nombre
    de su sección. Cada episodio recuerda su línea de origen.
    """
    lineas = texto_md.splitlines()
    episodios: list[Episodio] = []
    contador = 0
    seccion_actual: str | None = None
    cuerpo: list[str] = []
    inicio_cuerpo = 0
    titulo_ya_visto = False

    def nuevo_episodio(seccion: str, linea: int, texto: str) -> None:
        nonlocal contador
        contador += 1
        episodios.append(
            Episodio(id=f"ep-{contador:03d}", seccion=seccion, linea=linea, texto=texto)
        )

    def flush_cuerpo() -> None:
        texto = "\n".join(cuerpo).strip()
        if texto and seccion_actual is not None:
            nuevo_episodio(seccion_actual, inicio_cuerpo, texto)

    for i, linea in enumerate(lineas, start=1):
        m = _ENCABEZADO.match(linea)
        if m:
            flush_cuerpo()
            cuerpo = []
            titulo = m.group(1).strip()
            seccion = "encabezado" if titulo_ya_visto else "título"
            titulo_ya_visto = True
            nuevo_episodio(seccion, i, titulo)
            seccion_actual = titulo
        else:
            if (
                seccion_actual is not None
                and linea.strip()
                and not any(l.strip() for l in cuerpo)
            ):
                inicio_cuerpo = i
            cuerpo.append(linea)
    flush_cuerpo()
    return episodios


def procesar(ruta: Path, extractor: Extractor) -> dict:
    """Convierte un documento en el JSON de conocimiento del contrato."""
    ruta = Path(ruta)
    texto = ruta.read_text(encoding="utf-8")
    episodios = episodios_de(texto)

    afirmaciones: list[dict] = []
    contador = 0
    for episodio in episodios:
        for candidato in extractor.proponer(episodio):
            contador += 1
            linea = linea_de(candidato.texto, episodio)
            afirmacion = Afirmacion(
                id=f"af-{contador:03d}",
                texto=candidato.texto,
                evidencia=Evidencia(
                    seccion=episodio.seccion, linea=linea, cita=candidato.texto
                ),
            )
            afirmaciones.append(afirmacion.to_dict())

    return {
        "documento": ruta.name,
        "extractor": {"version": extractor.version()},
        "episodios": [asdict(e) for e in episodios],
        "afirmaciones": afirmaciones,
    }


def escribir(documento: dict, salida: Path) -> Path:
    salida = Path(salida)
    salida.parent.mkdir(parents=True, exist_ok=True)
    salida.write_text(
        json.dumps(documento, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return salida
