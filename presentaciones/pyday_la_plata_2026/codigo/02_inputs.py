"""Purpose: Mostrar cómo guardar los parámetros de un experimento.
Responsibilities: Escribir un diccionario en entrada.json.
Rationale: JSON permite registrar inputs sin definir clases ni una CLI.
"""

import json
from pathlib import Path

entrada = {"velocidad": 10, "angulo": 45, "gravedad": 10}
Path("entrada.json").write_text(json.dumps(entrada, indent=2), encoding="utf-8")
