# Demo — After Chatbon (PyDay Hurlingham 2026)

**El problema de diseño de sensor-log (JAMS): ¿qué sample rate hace falta de verdad?**
Muestrear de más no es ser riguroso: es acumular data que es ruido. Muestrear
de menos hace que la medición mienta. La frontera la pone la dinámica
(velocidad y aceleración), no el capricho del configurador.

```
demo/
├── lab/     Lado A · Python + uv  · señal → contracto JSON con la recomendación
└── visor/   Lado B · Vanilla JS   · la señal 60 Hz contra la recomendada, por tramo
```

## La captura real (ya integrada — la demo va sobre esta captura)

Con sensor-log (del propio JAMS), acelerómetro a 60 Hz, 46 s, 2774 muestras
(`lab/datos/captura.csv`, commiteada en 5e06de0). Para recapturar:

```bash
cd lab
uv sync
uv run python -m pytest -q                # todos los tests del lab
uv run muestreo analizar datos/captura.csv --salida salida/recomendacion.json
cp salida/recomendacion.json ../visor/data/
```

El sintético (`datos/sintetico.csv`) queda como recurso didáctico opcional:
trae tramos etiquetados (quieto/caminando/temblor) para mostrar aliasing.
Regenerarlo: `uv run muestreo sintetizar datos/sintetico.csv`.

## Guion (mapeado a las diapositivas)

### Track 4 — Mañana en el Abasto · entra el ejemplo (~2:00)

El teléfono es un laboratorio, y sensor-log es nuestra herramienta: graba
aceleración a 60 Hz. Todo empezó como un script de 20 líneas que leía el CSV.

```bash
cd lab && uv sync
uv run muestreo analizar datos/captura.csv
```

La pregunta que guía el resto: **¿a 60 Hz la medición es mejor, o solo más grande?**

### Track 5 — Hola Frank · romper sin miedo (~1:30)

La red de seguridad con dos roturas:

1. Cambiar `TASAS_BASE` (quitar el 15) → el test del contrato avisa en rojo.
2. Cambiar `VENTANA_SUAVIZADO_S` a 0.02 → `test_la_regla_k_es_estable_entre_regimenes`
   avisa: la regla dejó de sostenerse.
3. `git restore` → verde otra vez.

Mensaje: equivocarse cuesta un `git restore`. La verdad conocida (señal
sintética) es el oráculo; los tests defienden lo que decidimos no negociar.

### Track 6 — Ojos de terciopelo · entender el sistema (~1:30)

Los números del análisis (salida del CLI, ya en pantalla si hace falta):

| qué pasaba | ventana | f_dyn | alcanzan | guardan |
|---|---|---|---|---|
| quieto | 20–25 s | 0.8 Hz | 1 Hz | 5/300 |
| se mueve poco | 0–5 s | 0.9 Hz | 12 Hz | 60/300 |
| se mueve mucho | 5–10 s | 3 Hz | 25 Hz | 125/300 |
| sacudón | 40–45 s | 5.5 Hz | 40 Hz | 200/300 |

**1027 de 2774 muestras (37%) alcanzan.** La regla que emerge: f_opt ≈ (4–8)·f_dyn,
con f_dyn = a_max/(2π·v_max) — solo velocidad y aceleración.

### Track 7 — Lo quiero ya · cambio de lado (~1:30)

Pregunta al público: *"¿cuánto sabés de una medición mirando un JSON crudo?"*
Mostrar `salida/recomendacion.json` un segundo. El visor lo hace visible.

### Tracks 8–10 — Vanilla JS · el visor (~4:00)

```bash
python3 -m http.server 8642 --directory visor
# abrir http://localhost:8642
```

Recorrido con la captura real (46 s a 60 Hz, 2774 lecturas): titular (alcanzan
1027 de 2774 muestras, 37%) → chips en palabras (quieto · se mueve poco ·
se mueve mucho · sacudón) → click en *quieto* (20–25 s): con 1 lectura por
segundo alcanza, y el gráfico era una línea plana — **son la misma historia**.
Click en *sacudón* (40–45 s): recién con 40 Hz no miente.
El aliasing didáctico (el *temblor* etiquetado del sintético mintiendo a 15 Hz)
vive en la captura sintética: `uv run muestreo sintetizar datos/sintetico.csv`,
analizar, copiar a `visor/data/` y recargar el server.

### Track 11 — Noche de paz · descubrir algo que no sabíamos (~1:30)

El descubrimiento codificado en un test: **Nyquist no alcanza**. Con 2× la
dinámica la señal existe, pero su forma miente. La regla honesta (4–8×) salió
de los datos, no de un libro — y hoy le diría a sensor-log qué sample rate
usar en cada tramo de una grabación real: muestreo adaptativo.

### Track 12 — Percussion baby · cierre

El código puede reescribirse; el oráculo, los tests y la regla aprendida
sobreviven. Eso es el software como sustrato para pensar.

## Preguntas al público

- **Apertura (slide 2)**: ¿quién tuvo un script de 20 líneas que se volvió
  inmanejable?
- **Flip (track 7)**: ¿cuánto sabés de una medición mirando un JSON crudo?
- **Cierre (track 12)**: ¿qué idea que tienen en la cabeza podrían convertir
  en algo ejecutable esta semana?

## Plan B (si falla algo en vivo)

- Las salidas ya están generadas: `lab/salida/*.json` = `visor/data/*.json`.
- Si `uv run muestreo` falla: abrir el visor y narrar los números de este README.
- Si el server no arranca: los números del análisis están acá arriba.
- La captura real es la demo: los números de arriba y del visor son reales.
  El sintético solo entra si hay que mostrar aliasing con tramos etiquetados.

## Decisiones registradas

- Nyquist (2×) como piso conceptual; la regla medida (4–8×, 10% RMS con
  interpolación lineal) como hallazgo. La constante salió de la curva de
  error, tres intentos de métrica quedaron registrados en la historia de
  commits (max-error y suavizado pareado sesgaban).
- La gravedad sin quitar es la deriva dramática: 60 s quieto → 588 m/s "de
  vuelo" (`test_gravedad_sin_quitar_deriva_absurdamente`).
- Los tests SIEMPRE: `uv run python -m pytest -q` (nunca `uv run pytest`).
