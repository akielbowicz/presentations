"""Generador de señales sintéticas con verdad conocida.

Tres regímenes, 50 s @ 60 Hz:
  quieto    0-10s   ruido de sensor (σ = 0.15 m/s²), no pasa nada
  caminando 10-30s  oscilación de marcha: 1.5·sin(2π·2·t) + ruido
  temblor   40-50s  vibración de mano:  8.0·sin(2π·10·t) + ruido

La verdad de cada régimen incluye a_max y v_max teóricos; de ahí sale
la frecuencia característica f_dyn = a_max / (2π·v_max), que para una
oscilación es exactamente su frecuencia.
"""

from __future__ import annotations

import json
import random
from dataclasses import dataclass
from pathlib import Path

from .csv_sensorlog import Serie

SIGMA_RUIDO = 0.04
F_CAPTURA = 60.0

REGIMENES = [
    ("quieto", 0.0, 10.0, 0.0),
    ("caminando", 10.0, 30.0, 1.5),
    ("quieto", 30.0, 40.0, 0.0),
    ("temblor", 40.0, 50.0, 8.0),
]
FRECUENCIAS = {"caminando": 2.0, "temblor": 10.0}


@dataclass
class Sintetica:
    serie: Serie
    verdad: dict  # nombre → {desde_s, hasta_s, a_max, v_max, f_dyn}

    def __iter__(self):
        yield self.serie
        yield self.verdad


def generar(especificacion=REGIMENES, seed: int = 7) -> Sintetica:
    rng = random.Random(seed)
    t: list[float] = []
    ax: list[float] = []
    ay: list[float] = []
    az: list[float] = []
    verdad: dict = {}
    for nombre, desde, hasta, a_max in especificacion:
        n = int((hasta - desde) * F_CAPTURA)
        f_osc = FRECUENCIAS.get(nombre, 0.0)
        t0 = len(t) / F_CAPTURA
        for i in range(n):
            tiempo = t0 + i / F_CAPTURA
            senal = a_max * math_sin_2pi_f(tiempo, f_osc) if f_osc else 0.0
            ax.append(senal + rng.gauss(0.0, SIGMA_RUIDO))
            ay.append(rng.gauss(0.0, SIGMA_RUIDO))
            az.append(rng.gauss(0.0, SIGMA_RUIDO))
            t.append(tiempo)
        if f_osc:
            v_max = a_max / (2 * 3.141592653589793 * f_osc)
            verdad[nombre] = {
                "desde_s": desde,
                "hasta_s": hasta,
                "a_max": a_max,
                "v_max": v_max,
                "f_dyn": f_osc,
            }
    serie = Serie(
        t=t, ax=ax, ay=ay, az=az, f_captura=F_CAPTURA, f_medida=F_CAPTURA
    )
    return Sintetica(serie=serie, verdad=verdad)


def math_sin_2pi_f(t: float, f: float) -> float:
    import math

    return math.sin(2 * math.pi * f * t)


def escribir_sensorlog(sintetica: Sintetica, ruta: Path) -> None:
    """CSV en el formato exacto que exporta sensor-log, para el visor y el demo."""
    serie = sintetica.serie
    lineas = [
        "# SensorLog Export - Accelerometer",
        f"# Session: sintetica | Frequency: {serie.f_captura:.0f}Hz | Samples: {serie.n_muestras}",
        "timestamp_ms,x,y,z",
    ]
    for i, ti in enumerate(serie.t):
        lineas.append(
            f"{int(ti * 1000)},{serie.ax[i]:.6f},{serie.ay[i]:.6f},{serie.az[i]:.6f}"
        )
    ruta.write_text("\n".join(lineas) + "\n", encoding="utf-8")
    ruta.with_suffix(".verdad.json").write_text(
        json.dumps(sintetica.verdad, indent=2) + "\n", encoding="utf-8"
    )
