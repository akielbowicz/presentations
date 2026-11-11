"""Parser del CSV que exporta sensor-log (JAMS).

Formato: BOM UTF-8, dos comentarios `#` (nombre y meta con frecuencia),
fila de encabezado `timestamp_ms,x,y,z` y una fila por muestra.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

_COMENTARIO_FREQ = re.compile(r"Frequency:\s*([0-9.]+)\s*Hz")


@dataclass
class Serie:
    """Aceleraciones muestradas: t en segundos (relativo), a en m/s²."""

    t: list[float]
    ax: list[float]
    ay: list[float]
    az: list[float]
    f_captura: float  # declarada en el comentario del export
    f_medida: float  # deducida de los timestamps reales

    @property
    def duracion_s(self) -> float:
        return self.t[-1] - self.t[0] if len(self.t) >= 2 else 0.0

    @property
    def n_muestras(self) -> int:
        return len(self.t)

    def magnitud(self) -> list[float]:
        return [( (x * x + y * y + z * z) ** 0.5) for x, y, z in zip(self.ax, self.ay, self.az)]


def leer_sensorlog(ruta: Path) -> Serie:
    lineas = ruta.read_text(encoding="utf-8-sig").splitlines()
    f_captura = 0.0
    filas: list[tuple[float, float, float, float]] = []
    for linea in lineas:
        if linea.startswith("#"):
            m = _COMENTARIO_FREQ.search(linea)
            if m:
                f_captura = float(m.group(1))
            continue
        partes = linea.split(",")
        if len(partes) != 4 or partes[0] == "timestamp_ms":
            continue
        ts, x, y, z = (float(p) for p in partes)
        filas.append((ts, x, y, z))  # timestamp en ms; a segundos recién tras restar t0
    if not filas:
        raise ValueError(f"{ruta}: sin muestras")
    t0_ms = filas[0][0]
    t = [(f[0] - t0_ms) / 1000.0 for f in filas]
    f_medida = (len(t) - 1) / t[-1] if t[-1] > 0 else 0.0
    return Serie(
        t=t,
        ax=[f[1] for f in filas],
        ay=[f[2] for f in filas],
        az=[f[3] for f in filas],
        f_captura=f_captura,
        f_medida=round(f_medida, 1),
    )
