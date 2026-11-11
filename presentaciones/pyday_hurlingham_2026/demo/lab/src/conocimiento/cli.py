"""CLI del laboratorio: procesar y evaluar.

    uv run conocimiento procesar datos/talleres.md --extractor atomico --salida salida/conocimiento.json
    uv run conocimiento evaluar salida/conocimiento.json evals/corpus-dorado.json
"""

import argparse
import json
from pathlib import Path

from rich.console import Console
from rich.table import Table

from .atomizador import EXTRACTOR_ATOMICO
from .estructura import EXTRACTOR_ESTRUCTURA
from .especificaciones import anclas_de_directorio, cargar_especificaciones, cobertura
from .evaluar import evaluar
from .pipeline import procesar, escribir

EXTRACTORES = {
    "atomico": EXTRACTOR_ATOMICO,
    "estructura": EXTRACTOR_ESTRUCTURA,
}

console = Console()


def _procesar(args: argparse.Namespace) -> None:
    extractor = EXTRACTORES[args.extractor]
    documento = procesar(Path(args.dato), extractor)
    salida = escribir(documento, Path(args.salida))
    console.print(
        f"[bold]{documento['documento']}[/bold] → {salida}\n"
        f"extractor [cyan]{documento['extractor']['version']}[/cyan]: "
        f"{len(documento['episodios'])} episodios, "
        f"{len(documento['afirmaciones'])} afirmaciones"
    )


def _evaluar(args: argparse.Namespace) -> None:
    producidas = json.loads(Path(args.producido).read_text(encoding="utf-8"))[
        "afirmaciones"
    ]
    dorado = json.loads(Path(args.dorado).read_text(encoding="utf-8"))
    precisión, recall = evaluar(producidas, dorado)

    tabla = Table(title=f"Corpus dorado: {Path(args.dorado).name}", show_lines=False)
    tabla.add_column("afirmación producida")
    tabla.add_column("coincide")
    dorado_norm = {" ".join(d["texto"].split()) for d in dorado}
    for p in producidas:
        coincide = " ".join(p["texto"].split()) in dorado_norm
        tabla.add_row(p["texto"], "[green]sí[/green]" if coincide else "[red]no[/red]")
    console.print(tabla)
    console.print(
        f"precisión: [bold]{precisión:.0%}[/bold] ({precisión * len(producidas):.0f}"
        f"/{len(producidas)}) · recall: [bold]{recall:.0%}[/bold] "
        f"({recall * len(dorado):.0f}/{len(dorado)})"
    )


def _specs(args: argparse.Namespace) -> None:
    """Reporte de correspondencia spec ↔ test (la idea de espectacular)."""
    specs = cargar_especificaciones(Path(args.specs))
    anclas = anclas_de_directorio(Path(args.tests))
    reporte = cobertura(specs, anclas)

    tabla = Table(title="Correspondencia spec ↔ test", show_lines=False)
    tabla.add_column("spec")
    tabla.add_column("statement")
    tabla.add_column("verificadas", justify="right")
    for spec in specs.values():
        cubiertas = sum(1 for p in spec.propiedades if p in anclas)
        tabla.add_row(
            spec.id,
            spec.statement,
            f"{cubiertas}/{len(spec.propiedades)}",
        )
    console.print(tabla)

    ok = True
    if reporte.fantasma:
        ok = False
        console.print(
            "[red]anclas sin spec (¿typo?):[/red] " + ", ".join(sorted(reporte.fantasma))
        )
    if reporte.olvidadas:
        ok = False
        console.print(
            "[red]propiedades sin test:[/red] " + ", ".join(sorted(reporte.olvidadas))
        )
    if ok:
        console.print(
            f"[green]todo cubierto:[/green] {len(anclas)} anclas verifican "
            f"{sum(len(s.propiedades) for s in specs.values())} propiedades "
            f"de {len(specs)} especificaciones"
        )
    else:
        raise SystemExit(1)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        prog="conocimiento",
        description="Laboratorio: documentos → conocimiento estructurado con evidencia.",
    )
    sub = parser.add_subparsers(dest="comando", required=True)

    p_procesar = sub.add_parser("procesar", help="documento → conocimiento JSON")
    p_procesar.add_argument("dato", help="ruta del documento de entrada")
    p_procesar.add_argument(
        "--extractor", choices=sorted(EXTRACTORES), default="atomico"
    )
    p_procesar.add_argument("--salida", required=True, help="ruta del JSON de salida")

    p_evaluar = sub.add_parser("evaluar", help="afirmaciones producidas vs. corpus dorado")
    p_evaluar.add_argument("producido", help="JSON producido por `procesar`")
    p_evaluar.add_argument("dorado", help="JSON con el corpus dorado")

    p_specs = sub.add_parser(
        "specs",
        help="correspondencia spec ↔ test: sin fantasmas, sin olvidadas",
    )
    p_specs.add_argument("--specs", default="specs", help="directorio de specs")
    p_specs.add_argument("--tests", default="tests", help="directorio de tests")

    args = parser.parse_args(argv)
    if args.comando == "procesar":
        _procesar(args)
    elif args.comando == "evaluar":
        _evaluar(args)
    elif args.comando == "specs":
        _specs(args)


if __name__ == "__main__":
    main()
