# lab — conocimiento

Lado A de la demo de *After Chatbon*: un proyecto Python mínimo (con `uv`)
que convierte documentos en afirmaciones con evidencia verbatim.

Espeja los conceptos del contrato de **bajan**: episodios, candidatos de
afirmaciones, costura de extractores (`version()` + `proponer()`), corpus
dorado y evaluación.

```bash
uv sync
uv run python -m pytest -q
uv run conocimiento procesar datos/talleres.md --extractor atomico --salida salida/conocimiento.json
uv run conocimiento evaluar salida/conocimiento.json evals/corpus-dorado.json
```

Ver el guion completo en `../README.md`.
