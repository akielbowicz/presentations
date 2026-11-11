# Demo — After Chatbon (PyDay Hurlingham 2026)

Dos lados, un mismo experimento: procesar conocimiento con evidencia.

```
demo/
├── lab/     Lado A · Python + uv  · documentos → conocimiento JSON
└── visor/   Lado B · Vanilla JS   · SPA para explorar ese conocimiento
```

## Guion (mapeado a las diapositivas)

### Slide 4 — Python + uv · ~1:30

```bash
cd lab
uv sync                      # entorno reproducible desde el lockfile
uv run python -m pytest -q   # 22 tests verdes: el contrato está protegido
```

Contar: el contrato `Extractor` (`version()` + `proponer(episodio)`) es la
costura — espeja el contrato real de **bajan**. El pipeline valida y registra;
los extractores solo proponen candidatos.

### Slide 5 — Romper sin miedo · ~1:30

En vivo, con red de seguridad:

1. Abrir `src/conocimiento/atomizador.py`, cambiar `MIN_UNIDAD = 20` → `100`.
2. `uv run python -m pytest -q` → **rojo**: el test `test_min_unidad_coincide_con_bajan` avisa.
3. `git restore src/conocimiento/atomizador.py` → verde otra vez.

Mensaje: equivocarse cuesta un `git restore`. Las reglas son parámetros para
experimentar; los tests defienden lo que decidimos no negociar.

### Slide 6 — Experimentar con conocimiento · ~2:00

```bash
uv run conocimiento procesar datos/talleres.md --extractor atomico --salida salida/conocimiento.json
uv run conocimiento evaluar salida/conocimiento.json evals/corpus-dorado.json
```

Resultado esperado: **18 afirmaciones · precisión 39% · recall 100%**.

El corpus dorado (6 afirmaciones adjudicadas a mano) y la evaluación espejan
los evals reales de bajan (75,2% precisión / 88,4% recall sobre su corpus).

### Slide 7 — Cambio de lado · ~1:30

Pregunta al público: *"¿cuánto conocimiento pueden descubrir mirando un JSON?"*
Mostrar `salida/conocimiento.json` crudo un segundo. Cambiar de lado.

### Slides 8–10 — Vanilla JS · ~4:30

```bash
python3 -m http.server 8642 --directory visor
# abrir http://localhost:8642
```

Recorrido: chips de secciones → filtrar → click en una afirmación → panel de
evidencia (cita verbatim + línea). La SPA no juzga: solo hace visible lo que
el extractor produjo.

### Slide 11 — Descubrir algo que no sabíamos · ~1:30

Lo que la exploración revela sobre los 18 candidatos:

| Hallazgo | Dónde se ve |
|---|---|
| 5 encabezados convertidos en "conocimiento" | chip `título` / `encabezado` |
| 2 preguntas extraídas como afirmaciones | tag roja `pregunta` |
| 1 duplicada (inscripción, dos secciones) | chips `Inscripción` + `Cupos` |

Hipótesis nueva: *"si usamos la estructura del documento, mejora la precisión
sin perder recall"*. Probarla en vivo:

```bash
uv run conocimiento procesar datos/talleres.md --extractor estructura --salida salida/conocimiento-estructura.json
uv run conocimiento evaluar salida/conocimiento-estructura.json evals/corpus-dorado.json
```

**39% → 64% de precisión, recall 100% constante.** En el visor: botón
`estructura` (o `?data=conocimiento-estructura.json`).

### Slide 12 — Cierre

El código puede cambiar de extractor; el corpus, los tests y lo aprendido
sobreviven. Eso es el software como sustrato para pensar.

## Preguntas al público

- **Apertura (slide 2)**: ¿quién tuvo un script de 20 líneas que se volvió
  inmanejable? ¿quién generó código con IA que funcionaba pero no estaba
  seguro de que resolviera el problema correcto?
- **Flip (slide 7)**: ¿cuánto conocimiento descubren mirando un JSON?
- **Cierre (slide 12)**: ¿qué idea que tienen en la cabeza podrían convertir
  en algo ejecutable esta semana?

## Plan B (si falla algo en vivo)

- Las salidas ya están generadas y copiadas: `lab/salida/*.json` = `visor/data/*.json`.
- Si `uv run conocimiento` falla: mostrar el JSON generado y saltar al visor.
- Si el server no arranca: `cd visor && python3 -m http.server` (los datos van embebidos en el repo).
- Los números de la evaluación están en este README: se pueden narrar sin terminal.

## Regenerar todo desde cero

```bash
cd lab
uv sync
uv run python -m pytest -q
uv run conocimiento procesar datos/talleres.md --extractor atomico --salida salida/conocimiento.json
uv run conocimiento procesar datos/talleres.md --extractor estructura --salida salida/conocimiento-estructura.json
cp salida/*.json ../visor/data/
```
