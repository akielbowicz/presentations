"""CLI de muestreo: sintetizar y analizar.

    uv run muestreo sintetizar datos/sintetico.csv
    uv run muestreo analizar datos/sintetico.csv --salida salida/recomendacion.json

El JSON de salida es el CONTRATO con el visor (Lado B): si cambia, el
test del contrato avisa.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

from .csv_sensorlog import leer_sensorlog
from .grabador import GrabadorAdaptativo
from .integrador import integrar, quita_tendencia
from .recomendador import f_optima, piso_ruido, redundancia
from .senales import escribir_sensorlog, generar

TASAS_BASE = (60, 50, 40, 30, 25, 20, 15, 12, 10, 8, 6, 5, 4, 3, 2, 1)
VENTANA_S = 5.0
PUNTOS_VISOR = 1500


def sintetizar(ruta_csv: Path, seed: int = 7) -> Path:
    escribir_sensorlog(generar(seed=seed), ruta_csv)
    return ruta_csv


def _verdad_si_existe(ruta_csv: Path) -> list:
    candidato = ruta_csv.with_suffix(".verdad.json")
    if candidato.exists():
        return json.loads(candidato.read_text())
    return []


def _nombre_ventana(desde_s: float, hasta_s: float, tramos: list) -> str:
    medio = (desde_s + hasta_s) / 2
    for tramo in tramos:
        if tramo["desde_s"] <= medio < tramo["hasta_s"]:
            return tramo["nombre"]
    return f"t={desde_s:.0f}s"


def analizar(ruta_csv: Path, ruta_salida: Path | None = None) -> dict:
    serie = leer_sensorlog(ruta_csv)
    a = serie.a
    f_medida = max(1.0, round(serie.f_medida))
    tasas = tuple(t for t in TASAS_BASE if t <= f_medida)

    # el piso de ruido del sensor lo revela la ventana más quieta
    paso_ventana = int(VENTANA_S * f_medida)
    sigma = min(
        piso_ruido(a[i : i + paso_ventana])
        for i in range(0, len(a) - paso_ventana + 1, paso_ventana)
    )

    tramos = _verdad_si_existe(ruta_csv)
    segmentos = []
    for inicio in range(0, len(a) - 1, paso_ventana):
        sub_t = serie.t[inicio : inicio + paso_ventana]
        sub_a = a[inicio : inicio + paso_ventana]
        if len(sub_t) < 10:
            break
        f_opt = f_optima(sub_t, sub_a, tasas, sigma)

        # dinámica: quitar gravedad/bias e integrar → velocidad;
        # a la velocidad se le quita la media (una deriva constante no
        # cambia la dinámica, pero infla el pico si la ventana no cierra
        # en fase)
        a_lin = quita_tendencia(sub_a, ventana=max(3, int(2.0 * f_medida)))
        v = integrar(sub_t, a_lin)
        v_media = sum(v) / len(v)
        v_max = max(abs(x - v_media) for x in v)
        a_max = max(abs(x) for x in a_lin)
        f_dyn = a_max / (2 * math.pi * v_max) if v_max > sigma else None
        k = round(f_opt / f_dyn, 1) if f_dyn else None

        segmentos.append(
            {
                "nombre": _nombre_ventana(sub_t[0], sub_t[-1], tramos),
                "desde_s": round(sub_t[0], 2),
                "hasta_s": round(sub_t[-1], 2),
                "f_opt": f_opt,
                "k": k,
                "a_max": round(a_max, 3),
                "v_max": round(v_max, 3),
                "f_dyn": round(f_dyn, 2) if f_dyn else None,
                "redundancia_pct": round(100 * redundancia(sub_a, sigma)),
                "muestras_60hz": len(sub_a),
                "muestras_f_opt": round(len(sub_a) * f_opt / f_medida),
            }
        )

    paso_visor = max(1, math.ceil(len(a) / PUNTOS_VISOR))
    contrato = {
        "meta": {
            "fuente": ruta_csv.name,
            "f_captura": serie.f_captura,
            "f_medida": round(serie.f_medida, 1),
            "duracion_s": round(serie.duracion_s, 1),
            "n_muestras": serie.n_muestras,
            "sigma": round(sigma, 4),
        },
        "segmentos": segmentos,
        "senial": {
            "t": [round(t, 2) for t in serie.t[::paso_visor]],
            "a": [round(x, 4) for x in a[::paso_visor]],
        },
    }
    if ruta_salida is not None:
        ruta_salida.parent.mkdir(parents=True, exist_ok=True)
        ruta_salida.write_text(json.dumps(contrato, ensure_ascii=False) + "\n")
    return contrato


def grabar(ruta_csv: Path, ruta_salida: Path | None = None) -> dict:
    """Simula el grabador adaptativo sobre el stream de una captura.

    El sensor muestrea a plena tasa en RAM; el grabador decide qué se
    persiste, muestra a muestra, sin ver futuro. Devuelve la traza de
    decisiones, la cuenta de guardadas y el error de reconstrucción.
    Con --salida, además escribe el CONTRATO de grabación para el visor.
    """
    serie = leer_sensorlog(ruta_csv)
    a = serie.a
    f_medida = max(1.0, round(serie.f_medida))
    tasas = tuple(t for t in TASAS_BASE if t <= f_medida)
    g = GrabadorAdaptativo(f_captura=f_medida, tasas=tasas)
    for t, x in zip(serie.t, a):
        g.ofrecer(t, x)
    resumen = {
        "decisiones": g.decisiones,
        "guardadas": len(g.a_guardadas),
        "totales": serie.n_muestras,
        "pct": round(100 * len(g.a_guardadas) / serie.n_muestras),
        "error_reconstruccion_pct": round(g.error_reconstruccion_pct(serie.t, a), 1),
    }
    if ruta_salida is not None:
        paso_visor = max(1, math.ceil(len(a) / PUNTOS_VISOR))
        contrato = {
            "meta": {
                "fuente": ruta_csv.name,
                "f_captura": serie.f_captura,
                "f_medida": round(serie.f_medida, 1),
                "duracion_s": round(serie.duracion_s, 1),
                "n_muestras": serie.n_muestras,
                "ventana_muestras": g.ventana.maxlen,
                "decision_cada_muestras": g.decision_cada,
                "bajadas_para_bajar": g.bajadas_para_bajar,
            },
            "resumen": resumen,
            "decisiones": [[round(t, 2), f] for t, f in g.decisiones],
            "guardadas": {
                "t": [round(t, 3) for t in g.t_guardadas],
                "a": [round(x, 4) for x in g.a_guardadas],
            },
            "senial": {
                "t": [round(t, 2) for t in serie.t[::paso_visor]],
                "a": [round(x, 4) for x in a[::paso_visor]],
            },
        }
        ruta_salida.parent.mkdir(parents=True, exist_ok=True)
        ruta_salida.write_text(json.dumps(contrato, ensure_ascii=False) + "\n")
    return resumen


def main() -> None:
    parser = argparse.ArgumentParser(description="¿Qué sample rate hace falta de verdad?")
    sub = parser.add_subparsers(dest="comando", required=True)

    p_sin = sub.add_parser("sintetizar", help="señal sintética con verdad conocida")
    p_sin.add_argument("salida", type=Path)
    p_sin.add_argument("--seed", type=int, default=7)

    p_ana = sub.add_parser("analizar", help="recomendar sample rate por ventana")
    p_ana.add_argument("csv", type=Path)
    p_ana.add_argument("--salida", type=Path, default=None)

    p_gra = sub.add_parser(
        "grabar", help="simula el grabador adaptativo causal sobre el stream"
    )
    p_gra.add_argument("csv", type=Path)
    p_gra.add_argument("--salida", type=Path, default=None)

    args = parser.parse_args()
    if args.comando == "sintetizar":
        print(f"señal sintética → {sintetizar(args.salida, seed=args.seed)}")
    elif args.comando == "grabar":
        r = grabar(args.csv, args.salida)
        print(f"grabador adaptativo (causal, solo pasado) sobre {args.csv.name}:")
        for t, f in r["decisiones"]:
            print(f"  {t:6.2f}s → {f:.0f} Hz")
        print(
            f"  persistidas {r['guardadas']} de {r['totales']} muestras "
            f"({r['pct']}%)"
        )
        print(f"  error de reconstrucción: {r['error_reconstruccion_pct']}% RMS (tolerancia 10%)")
    else:
        contrato = analizar(args.csv, args.salida)
        destino = args.salida or "stdout"
        total_60 = sum(s["muestras_60hz"] for s in contrato["segmentos"])
        total_opt = sum(s["muestras_f_opt"] for s in contrato["segmentos"])
        print(f"contrato → {destino}")
        for s in contrato["segmentos"]:
            k = f" k={s['k']}" if s["k"] else ""
            print(
                f"  {s['desde_s']:6.1f}-{s['hasta_s']:6.1f}s  {s['nombre']:<10} "
                f"f_opt={s['f_opt']:<4.0f}{k:<6} redundancia={s['redundancia_pct']}%"
            )
        print(f"  data recomendada: {total_opt} de {total_60} muestras "
              f"({100 * total_opt / total_60:.0f}%)")


if __name__ == "__main__":
    main()
