"""Purpose: Mostrar cómo registrar los inputs y outputs de un experimento.
Responsibilities: Leer entrada.json, simular y guardar resultado.json.
Rationale: Usar archivos fijos deja visible la serialización sin manejo de CLI.
"""

import json
from pathlib import Path

from tiro_parabolico import simular

entrada = json.loads(Path("entrada.json").read_text(encoding="utf-8"))
salida = simular(**entrada)
registro = {"entrada": entrada, "salida": salida}
Path("resultado.json").write_text(json.dumps(registro, indent=2), encoding="utf-8")
