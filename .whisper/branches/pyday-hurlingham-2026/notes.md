- 2026-11-11T13:52:55Z [id:993e36b507779d27f2270f1996ce516e09970c913cf3acdb248fa5fd4105fb2f] (#resume-after-chatbon) Format: 1
  Timestamp: 2026-11-11T00:00:00Z (verificar con date si importa)
  Repo: github.com/akielbowicz/presentations (~/para/areas/dev/gh/ak/presentations)
  Branch: pyday-hurlingham-2026
  HEAD: 378a471
  Session: 01a1c7e9-2d30-73f2-b509-b0500b78f4f2
  Task: Charla "After Chatbon" — PyDay Hurlingham 2026 (sáb 14/11, 12:30–13:00, 20 min + Q&A)
  
  ## Objetivo
  Charla de 20 min estructurada como el disco *After Chabón* de Sumo: 2 lados × 6 tracks = 12 secciones, con epígrafes de letras. Dos mensajes que la audiencia debe llevarse: (1) la experiencia no se descarga, se construye (ambientes para romper sin miedo); (2) el software es un sustrato para pensar.
  
  ## Fase actual: red/green completa en demo; slides pendientes (redacción)
  
  ## Estado
  - Demo COMPLETA en `presentaciones/pyday_hurlingham_2026/demo/` (commits 35adeab + 378a471):
  - `lab/` Lado A Python+uv: contrato Extractor espejando bajan, atomizador determinista, extractor estructura, corpus dorado (6), eval → atómico 18 afirmaciones/39% precisión/recall 100% → estructura 11/64%/100%. specs/*.md formato bajan (5 specs, 20 propiedades [[ancla]]) + `conocimiento specs` (correspondencia spec↔test, exit 1 con fantasmas/olvidadas). 29 tests verdes, TDD.
  - `visor/` Lado B vanilla JS SPA: chips por sección, búsqueda, evidencia verbatim, switch atómico/estructura (?data=). Bugs plantados para slide 11: 5 encabezados, 2 preguntas, 1 duplicada.
  - `demo/README.md` guion completo mapeado a las 12 diapositivas + preguntas al público + plan B.
  - `slides.md` SIN commitear: esqueleto con 12 títulos de canciones de los Redondos, sin contenido. Intacto en working tree (no tocar sin leer el diff).
  - Conversación fuente sincronizada en ~/cotorreo (conv chatgpt 6aed3a99-…, transcript 11208 líneas): ahí están la tabla final de 12 diapositivas, epígrafes de letras por track, ritmo 2'/6,5'/1,5'/8'/2', y los dos mensajes.
  
  ## Próxima acción exacta
  Reescribir `slides.md`: portada/bio intactas + rellenar las 12 secciones (epígrafe de letra + contenido de la tabla final del transcript + NOTES + preguntas al público en slides 2, 7 y 12) + actualizar README.md e index.md del repo. Luego ensayo apuntando a terminar en 18:30.
  
  ## Decisiones/constraint claves
  - DEMO DE PÉNDULO/SensorLog/Pyodide DESCARTADA (evolución temprana de la conversación); el ejemplo conductor es procesar conocimiento (bajan/whisper como referencia real, NO como demo en vivo).
  - En la máquina de Sasha `uv run pytest` resuelve pytest de usuario: usar SIEMPRE `uv run python -m pytest`.
  - Diferenciarse de la charla de 16:15 (curiosidad/qué no delegar): nosotros = qué podemos HACER.
  - bash tool de esta sesión: cwd = raíz del repo; specs tooling (ah_*) disponible pero espectacular real NO entra en la demo (se menciona verbalmente).
  
  ## Validación
  `uv run python -m pytest -q` → 29 passed; `uv run conocimiento specs` → exit 0 (20/20). Última corrida: hoy, en este HEAD.
  
  ## Bloqueos
  Ninguno conocido. Fecha límite dura: ensayo 13/11, charla 14/11 12:30.
  
  ## Referencias condicionales
  - Guion: presentaciones/pyday_hurlingham_2026/demo/README.md
  - Transcript conversación: ~/cotorreo/raw/_conversations/chatgpt/6aed3a99-59cc-83e9-935a-94b77179bf54/transcript.md
  - Propuesta: propuestas/pyday_hurlingham_2026.md
  
  Previous entry: none
- 2026-11-11T15:13:49Z [id:7ad1e2fbbc8a651540ac610c41770cd27c744b05a5d0a7c1cd571ed27b73f6ad] (#incitacionales) Format: 1
  UTC: 2026-11-11T14:05:00Z
  Repo: ak/presentations (origin ak:akielbowicz/presentations.git)
  Branch: pyday-hurlingham-2026
  HEAD: 9068732 (pusheado a origin)
  Session: 01a1cae2 (2026-11-11T13-53-22Z)
  Task: charla PyDay Hurlingham 2026 "After Chabón" (Sumo) — deck reveal.js (superseded by 7924f7055baa3d3245fc732dd639bb7abc7cd5b6ace2d5d0e084a2a3607eaa4f)
  
  ## Objetivo
  Charla 20 min estructurada como el disco After Chabón: 12 secciones (2 mensajes: la experiencia no se construye sola/se descarga... se construye en ambientes para romper sin miedo; el software es sustrato para pensar).
  
  ## Fase actual: TEMA COMPLETO Y PUSHEADO; contenido de slides pendiente
  ## Estado
  - Tema Sumo TERMINADO en presentaciones/pyday_hurlingham_2026/ (phorma-theme.css + index.html, commits 4a76faf..9068732, push ok):
  - Paleta medida de la tapa: negro #1A1917, blanco #FBFAFA, rojo #C83534 (mismo rojo ambos temas)
  - Marco rojo (0.3vw, inset 2.7vw) sobre capa .backgrounds + regla .pdf-page para PDF; RECORTE de esquina inf-der (parche ::before px 180x130) para que no se superpongan las flechas de reveal — como la figura que rompe el marco en la tapa
  - Títulos (h1-h3 first-of-type) abajo-izquierda, rojo, Poiret One uppercase tracking 0.3em, bold+itálica sintetizados; contenido centrado vía flex; display:flex !important scopeado a .present (reveal pone display:block INLINE en la slide visible; en .past/.future el display:none inline es el mecanismo de ocultado)
  - Chrome rojo: flechas controls, progress span (reveal 5.0.4 trae progress:true por default), toggle sol/luna como SVG currentColor (emoji no recolorean); ícono seteado también en camino light
  - Deck 1280x720 (16:9); default dark + override ?theme=light|dark; utilidad .sumo-red; h4+ siguen mono
  - slides.md en working tree: esqueleto intacto SIN commitear (portada/bio + 12 títulos Redondos). HEAD tiene versión vieja (~1048 líneas) — leer diff antes de tocar
  - Verificación usada: servir deck con python http.server + flatpak chromium headless screenshots (--window-size 1600x900 --virtual-time-budget 15000) + asserts de píxel con magick (marco/título/fondos exactos)
  
  ## Próxima acción exacta
  Reescribir slides.md: rellenar las 12 secciones (epígrafe de letra + contenido de la tabla final del transcript + NOTES + preguntas al público en slides 2, 7 y 12), decidir "Chatbon" vs "Chabón" (portada y slug URL dicen chatbon; el disco es Chabón — hoy puse "Chabón" en el <title>), luego README.md e index.md del repo. Ensayo apuntando a 18:30.
  
  ## Decisiones/constraints claves
  - uv run python -m pytest SIEMPRE (nunca uv run pytest) en la máquina de Sasha
  - bash tool cwd = raíz del repo; espectacular NO entra en la demo (verbal)
  - Diferenciarse de la charla de 16:15 (qué no delegar): nosotros = qué podemos HACER
  - Export PDF pendiente: ?print-pdf no engancha en chromium headless --print-to-pdf (pre-existente, no bloquea; los .pdf-page ya estilados para cuando funcione)
  
  ## Validación
  - Tema: screenshots headless + asserts de píxel (marco #C83534 exacto, fondos, sin solapamientos) — verde
  - Demo: `uv run python -m pytest -q` → 29 passed y `uv run conocimiento specs` → exit 0 (NO re-corridos esta sesión; el tema no tocó demo/)
  
  ## Bloqueos
  Ninguno. Fecha límite dura: ensayo 13/11, charla 14/11 12:30.
  
  ## Referencias condicionales
  - Guion: presentaciones/pyday_hurlingham_2026/demo/README.md
  - Transcript: ~/cotorreo/raw/_conversations/chatgpt/6aed3a99-59cc-83e9-935a-94b77179bf54/transcript.md
  - Propuesta: propuestas/pyday_hurlingham_2026.md
  - Tema: presentaciones/pyday_hurlingham_2026/phorma-theme.css + index.html
  - Actualiza el handoff anterior de este topic (ID desconocido; su próxima acción sigue siendo redactar slides.md)
  Previous entry: none
- 2026-11-11T15:50:11Z [id:7924f7055baa3d3245fc732dd639bb7abc7cd5b6ace2d5d0e084a2a3607eaa4f] (#incitacionales) Format: 1
  UTC: 2026-11-11T16:05:00Z
  Repo: ak/presentations (origin ak:akielbowicz/presentations.git)
  Branch: pyday-hurlingham-2026
  HEAD: 825c30c (demo making-of commiteada; master deployado en de6a138)
  Session: esta (post 01a1cae2)
  Task: charla PyDay Hurlingham 2026 "After Chatbon" (Sumo) — deck reveal.js
  
  ## Objetivo
  Charla 20 min como After Chatbon: 12 tracks. Dos mensajes: (1) la experiencia no se descarga, se construye en ambientes para romper sin miedo; (2) el software es sustrato para pensar. "Chatbon" es el nombre correcto (decidido).
  
  ## Fase actual: DEMO REDEFINIDA Y DEPLOYADA; slides.md pendiente (redacción)
  ## Estado
  - DECISIÓN GRANDE: la demo NO es en vivo. Sasha solo narra; el público explora después. Método: bloques de código crecientes con salida real capturada (estilo pyday_la_plata_2026, data-transition none + fragments).
  - DOCUMENTO NUEVO: datos/conversacion.md = transcript crudo de la conversación ChatGPT que diseñó la charla (~/cotorreo conv 6aed3a99, 11208 líneas). talleres.md quedó obsoleto para la charla (fixture didáctico).
  - Números reales: atómico 5430 afirmaciones · precisión 4/5430 (~0.07%) · recall 67% (4/6). Estructura: 5073 · 0 preguntas · 0 encabezados · recall 67% constante. Duplicadas 659→474.
  - Hallazgos reales slide 11: 331 encabezados-as-conocimiento, 22 preguntas, 659 duplicadas (conversaciones pegadas dentro del transcript), sección-insecto URL-Zep (152 huérfanas) y LOS DOS MENSAJES de la charla pegados al residuo de markup ("Se construye. </title>") — el corpus humano los rescata. El arco honesto: filtros limpian lo evidente, pero el hallazgo está en EXPLORAR.
  - Corpus dorado: 6 decisiones verbatim del making-of (naming Chatbon L5, voz de Sumo L2084, SPA sin framework L10758, conservamos corpus/contrato L10087, mensaje1 L11189, mensaje2 L11194).
  - DEPLOYADO (Público): Pages sirve desde MASTER root con CNAME charlas.saxa.xyz (¡no gh-pages!). Making-of en master de6a138 bajo presentaciones/pyday_hurlingham_2026/demo/ (layout del branch, mergea sin conflicto). URLs: https://charlas.saxa.xyz/presentaciones/pyday_hurlingham_2026/demo/ (landing), .../demo/visor/, .../demo/conversacion.txt (11208 líneas verificadas). Push a master BYPASÓ regla de PR (avisar a Sasha).
  - Visor: parcheado para 189 secciones (chips top-12 + activa visible + truncado CSS). Verificado con screenshot headless.
  - slides.md: esqueleto intacto SIN commitear (portada/bio + 12 títulos Redondos). HEAD tiene versión vieja.
  - Validación: uv run python -m pytest -q → 29 passed; conocimiento specs exit 0; screenshots headless verde. Corridos HOY en este trabajo.
  
  ## Próxima acción exacta
  1. Actualizar demo/README.md (guion): nuevo documento, números reales, método bloques-de-código narrados, URLs públicas, plan B. 2. Reescribir slides.md: 12 secciones (letra como título + argumento subtítulo + bloque de código con salida real + NOTES; preguntas al público en 2, 7 y 12; cierre con URL del making-of). 3. Commit + push branch. 4. Ensayar apuntando a 18:30.
  
  ## Decisiones/constraints claves
  - uv run python -m pytest SIEMPRE (nunca uv run pytest). bash cwd = raíz del repo.
  - Transcript crudo (no normalizar): la fealdad es parte del punto.
  - PENDIENTE decidir para slides: (a) jerarquía título: letra como título grande vs epígrafe chico; (b) pregunta de cierre: "¿qué idea convertirías en ejecutable esta semana?" vs "¿qué podrías aprender si tuvieras dónde experimentar sin miedo?".
  - Epígrafes propuestos por track (transcript L2040): 01 "Come on London, here we come" / 02 "Do they know why they go?" / 03 "lo entendido es lo que no entiendo" / 04 "No tengas miedo, no" / 05 "Hello Frank, how're you doing?" / 06 "Think it, don't think it" / 07 "No sé lo que quiero, pero lo quiero ya" / 08 "Sing the song today" / 09 "usan radar" / 10 "real life is inside" / 11 "Sueña un sueño imposible" / 12 "everyday is Sunday". Roce abierto: "No tengas miedo, no" (04) calza mejor en slide 5 (Romper sin miedo) que "Hello Frank".
  - Diferenciarse de la charla de 16:15 (qué no delegar): nosotros = qué podemos HACER.
  
  ## Bloqueos
  Ninguno. Ensayo 13/11, charla 14/11 12:30.
  
  ## Referencias condicionales
  - Guion viejo (a reescribir): presentaciones/pyday_hurlingham_2026/demo/README.md
  - Transcript: ~/cotorreo/raw/_conversations/chatgpt/6aed3a99-59cc-83e9-935a-94b77179bf54/transcript.md
  - Epígrafes y tabla final: transcript L2036-2145 y L11121-11208
  - Tema: presentaciones/pyday_hurlingham_2026/phorma-theme.css + index.html
  Previous entry: 7ad1e2fbbc8a651540ac610c41770cd27c744b05a5d0a7c1cd571ed27b73f6ad (supersedes 7ad1e2fbbc8a651540ac610c41770cd27c744b05a5d0a7c1cd571ed27b73f6ad)
- 2026-11-11T18:44:59Z [id:29d273256181688b65d2713e23914194afde8d88acd10ee20fac1230bc94fd8d] (#incitacionales) Format: 1
  UTC: 2026-11-11T18:55:00Z
  Repo: ak/presentations (origin ak:akielbowicz/presentations.git)
  Branch: pyday-hurlingham-2026
  HEAD: c1bb256 (demo nueva commiteada; slides.md skeleton sigue sin commitear)
  Session: esta (post 7924f705)
  Task: charla PyDay Hurlingham 2026 "After Chatbon" (Sumo) — deck reveal.js
  ## Objetivo
  Charla 20 min, 12 tracks Sumo, 2 mensajes: (1) la experiencia no se descarga, se construye en ambientes para romper sin miedo; (2) el software es sustrato para pensar. Demo 8 min (tracks 4-11) como ejemplo conductor.
  ## Fase actual: DEMO NUEVA COMPLETA (lab TDD + visor + guion); slides pendientes
  ## Estado
  - Ejemplo ANTERIOR (registro de conocimiento) DESCARTADO por Sasha: "no aporta impacto, algo más simple de entender". Evaluados y descartados: cronograma PyDay (single track, sin superposición) y péndulo (derivación temprana, no un kill razonado).
  - Ejemplo NUEVO: el problema de diseño de sensor-log (JAMS) — qué sample rate hace falta según la dinámica (velocidad/aceleración) para no acumular data-ruido.
  - lab/ TDD: 15 tests verdes. Parser CSV sensor-log (formato real de jams/sensor-log/app.js), integrador a→v (la gravedad sin quitar deriva 588 m/s/60s — test dedicado), recomendador (piso_ruido, redundancia, f_optima), CLI sintetizar/analizar + contrato JSON lab→visor.
  - REGLA DESCUBIERTA (codificada en test): f_opt ≈ (4-8)·f_dyn, f_dyn = a_max/(2π·v_max). Nyquist (2x) basta para existir; 4-8x para no mentir. 27% de la data a 60Hz alcanza (quieto 1Hz / caminando 15Hz / temblor 50Hz).
  - visor/ vanilla JS verificado con screenshot headless: chips por tramo, señal 60Hz vs recomendada superpuestas, tabla de la regla. Tema Sumo dark.
  - demo/README.md guion completo mapeado a tracks 4-12 + instrucciones de captura real (15 min, sensor-log 60Hz: quieto/caminando/quieto/temblor/caminando) + plan B con datos sintéticos.
  - slides.md: esqueleto SIN commitear en working tree (portada/bio + 12 títulos). tracks 4-11 sin contenido.
  ## Próxima acción exacta
  (1) Captura real con sensor-log (drop-in: lab/datos/captura.csv) o confirmar uso del sintético; (2) rellenar slides.md: tracks 4-11 con el guion nuevo (demo/README.md), tracks 1-3 y 12 desde la tabla final del transcript (~/cotorreo conv chatgpt 6aed3a99); (3) ensayo 13/11 apuntando a 18:30.
  ## Decisiones/constraints claves
  - Demo NO en vivo: Sasha narra, bloques de código crecientes con salidas reales capturadas (estilo pyday_la_plata_2026).
  - specs/espectacular NO entra en la demo (verbal). Diferenciarse de la charla de 16:15: nosotros = qué podemos HACER.
  - SIEMPRE `uv run python -m pytest` (nunca uv run pytest).
  - La métrica de f_optima tomó 3 intentos (max-error y suavizado pareado sesgaban); la historia de commits la documenta — no "arreglar" sin leer.
  ## Validación
  uv run python -m pytest -q → 15 passed (hoy, este HEAD). Visor: screenshot headless chromium (flatpak org.chromium.Chromium, output a $HOME porque /tmp es sandbox).
  ## Bloqueos
  Ninguno conocido. Ensayo 13/11, charla 14/11 12:30.
  ## Referencias condicionales
  - Guion+captura+plan B: presentaciones/pyday_hurlingham_2026/demo/README.md
  - Formato CSV sensor-log: jams/sensor-log/app.js _exportSessionData
  - Transcript conversación fuente: ~/cotorreo/raw/_conversations/chatgpt/6aed3a99-59cc-83e9-935a-94b77179bf54/transcript.md (tabla final 12 diapositivas)
  Previous entry: 7924f7055baa3d3245fc732dd639bb7abc7cd5b6ace2d5d0e084a2a3607eaa4f (superseded by 7311e441b5803eceafe4874298ebfef97e83d621dcf144ea5705f3525ffb4204)
- 2026-11-11T18:48:42Z [id:7311e441b5803eceafe4874298ebfef97e83d621dcf144ea5705f3525ffb4204] (#incitacionales) Format: 1
  UTC: 2026-11-11T18:48:24Z
  Repo: ak/presentations (origin ak:akielbowicz/presentations.git)
  Branch: pyday-hurlingham-2026
  HEAD: c1bb256 (demo nueva completa; slides esqueleto quedó commiteado en af4221a — drift registrado)
  Session: esta (post 29d27325, stash /next)
  Task: charla PyDay Hurlingham 2026 "After Chatbon" (Sumo) — deck reveal.js
  ## Objetivo
  Charla 20 min, 12 tracks Sumo, 2 mensajes: (1) la experiencia no se descarga, se construye en ambientes para romper sin miedo; (2) el software es sustrato para pensar. Demo 8 min (tracks 4-11) como ejemplo conductor.
  ## Fase actual: DEMO NUEVA COMPLETA; redacción de slides pendiente (ahora sobre esqueleto ya commiteado)
  ## Estado
  - Ejemplo nuevo de la demo: el problema de diseño de sensor-log (JAMS) — qué sample rate hace falta según la dinámica (velocidad/aceleración) para no acumular data-ruido. Descartados antes: registro de conocimiento (Sasha: sin impacto), cronograma PyDay (single track), péndulo.
  - lab/ TDD: 15 tests verdes. Parser CSV sensor-log (formato real de jams/sensor-log/app.js), integrador a→v (gravedad sin quitar deriva 588 m/s en 60s — test dedicado), recomendador (piso_ruido, redundancia, f_optima), CLI sintetizar/analizar + contrato JSON lab→visor.
  - REGLA DESCUBIERTA (en test): f_opt ≈ (4-8)·f_dyn, f_dyn = a_max/(2π·v_max). Nyquist basta para existir; 4-8x para no mentir. 27% de la data a 60Hz alcanza (quieto 1Hz / caminando 15Hz / temblor 50Hz).
  - visor/ vanilla JS verificado headless (chips por tramo, 60Hz vs recomendada superpuestas, tabla de la regla, tema Sumo dark).
  - demo/README.md guion completo tracks 4-12 + instrucciones captura real (15 min sensor-log 60Hz: quieto/caminando/quieto/temblor/caminando) + plan B con sintético.
  - DRIFT REGISTRADO (motivo de este stash): af4221a ("parser CSV — verde") arrastró vía git add -A repo-wide el esqueleto de slides.md Y el store .whisper/ al historial. Contenido intacto (working tree limpio contra HEAD); no hay push de estos commits. Pendiente decidir: .whisper queda trackeado o git rm --cached.
  - Commits de esta sesión: b1d474f (fuera demo vieja), 7989144, baabc51, a6ad943, 7e367e7, 371ebcf, af4221a, c1bb256.
  ## Próxima acción exacta
  (1) Captura real con sensor-log (drop-in lab/datos/captura.csv) o confirmar sintético; (2) rellenar slides.md: tracks 4-11 con el guion nuevo (demo/README.md), tracks 1-3 y 12 desde la tabla final del transcript (~/cotorreo conv chatgpt 6aed3a99); decidir .whisper trackeado sí/no; (3) ensayo 13/11 apuntando a 18:30.
  ## Decisiones/constraints claves
  - Demo NO en vivo: Sasha narra, bloques de código crecientes con salidas capturadas (estilo pyday_la_plata_2026). specs/espectacular NO entra (verbal). Diferenciarse de la charla 16:15: nosotros = qué podemos HACER.
  - SIEMPRE `uv run python -m pytest` (nunca uv run pytest).
  - La métrica de f_optima tomó 3 intentos (max-error y suavizado pareado sesgaban); historia de commits la documenta — no "arreglar" sin leer.
  ## Validación
  uv run python -m pytest -q → 15 passed (hoy, este HEAD). Visor: screenshot headless (flatpak org.chromium.Chromium; output a $HOME porque /tmp es sandbox).
  ## Bloqueos
  Ninguno conocido. Ensayo 13/11, charla 14/11 12:30.
  ## Referencias condicionales
  - Guion+captura+plan B: presentaciones/pyday_hurlingham_2026/demo/README.md
  - Transcript conversación fuente: ~/cotorreo/raw/_conversations/chatgpt/6aed3a99-59cc-83e9-935a-94b77179bf54/transcript.md (tabla final 12 diapositivas)
  - Formato CSV sensor-log: jams/sensor-log/app.js _exportSessionData
  Previous entry: 29d273256181688b65d2713e23914194afde8d88acd10ee20fac1230bc94fd8d (supersedes 29d273256181688b65d2713e23914194afde8d88acd10ee20fac1230bc94fd8d)
- 2026-11-11T19:20:07Z [id:2fb0103d78ed90a6ec826159811338e59bee2d00bddc16f5c2d97f09ff80e53e] Format: 1
  UTC: 2026-11-11T19:20:07Z
  Repo: ak/presentations (origin ak:akielbowicz/presentations.git)
  Branch: pyday-hurlingham-2026
  HEAD: 5e06de0 (captura real commiteada sobre c1bb256)
  Session: esta (otra sesión; previa 7311e441 de 18:48Z sigue válida como contexto, no la invalido)
  Task: charla PyDay Hurlingham 2026 "After Chabon" (Sumo) — deck reveal.js
  ## Objetivo
  Charla 20 min, 12 tracks Sumo, 2 mensajes: (1) la experiencia no se descarga, se construye en ambientes para romper sin miedo; (2) el software es sustrato para pensar. Demo 8 min (tracks 4-11) como ejemplo conductor.
  ## Fase actual: CAPTURA REAL INTEGRADA (acción 1 del handoff previo COMPLETA); redacción de slides pendiente
  ## Estado
  - Sasha capturó con sensor-log (~/Downloads/sl): 5 CSVs (accelerometer/compass/gps/linearAccel/orientation), sesión 2026-11-11T18:59Z, ~46s, 60Hz declarada / 59.9Hz medida, 2774 muestras. La captura NO siguió el guion de 15 min del README (5 fases); es una toma corta con dinámicas variadas: actividad, sacudida fuerte (|a| hasta 166 m/s² ~39-42s), quieto (12-24s), cierre quieto.
  - Integrada: accelerometer → lab/datos/captura.csv (parser coincide exacto: BOM + # + timestamp_ms,x,y,z). Pipeline verde sobre datos reales: 10 tramos de 5s, f_opt 1→40 Hz (quieto 90% redundante, sacudida 40Hz), alcanzan 1027/2774 muestras (37%). Contrato JSON idéntico al sintético (meta/segmentos/senial); visor consume sin cambios.
  - Verificado headless: visor con captura real renderiza chips por tramo + señal 60Hz vs recomendada + regla. IMPORTANTE: fetch de data/recomendacion.json falla bajo file:// — servir con http.server (python3 -m http.server) para el screenshot/ensayo. Screenshots en ~/visor-captura-real.png (file://, vacío) y ~/visor-http.png (http, completo).
  - Commit 5e06de0: captura.csv + salida/recomendacion.json + visor/data/recomendacion.json. NO pusheado. Los otros 4 CSVs de ~/Downloads/sl quedan sin usar (el pipeline solo usa accelerometer).
  - Pendiente NO resuelto: decisión .whisper/ trackeado sí/no (entró al historial en af4221a por accidente; sin push).
  ## Próxima acción exacta
  Rellenar slides.md (esqueleto commiteado): tracks 4-11 con el guion de demo/README.md actualizado a la captura real (37%, f_medida 59.9 vs 60 declarada, f_opt 1-40Hz por tramo), tracks 1-3 y 12 desde la tabla final del transcript (~/cotorreo conv chatgpt 6aed3a99). Luego ensayo 13/11 apuntando a 18:30 — servir visor por http.
  ## Decisiones/constraints claves
  - Demo NO en vivo: Sasha narra, bloques de código crecientes con salidas capturadas. specs/espectacular NO entra (verbal). Diferenciarse de la charla 16:15: nosotros = qué podemos HACER.
  - SIEMPRE uv run python -m pytest (nunca uv run pytest).
  - La métrica f_optima tomó 3 intentos (max-error y suavizado pareado sesgaban); no "arreglar" sin leer la historia de commits.
  - La captura real reemplaza la historia del sintético en los slides: los números del guion (27%, tramos quieto/caminando/temblor etiquetados) cambian a 37% y tramos t=Xs sin etiqueta (no hay verdad para captura real).
  ## Validación
  uv run python -m pytest -q → 15 passed (hoy, HEAD 5e06de0). Visor: screenshot headless chromium via http.server 8137 (OK, ~/visor-http.png).
  ## Bloqueos
  Ninguno. Ensayo 13/11, charla 14/11 12:30.
  ## Referencias condicionales
  - Guion: presentaciones/pyday_hurlingham_2026/demo/README.md
  - Transcript fuente: ~/cotorreo/raw/_conversations/chatgpt/6aed3a99-59cc-83e9-935a-94b77179bf54/transcript.md (tabla final 12 diapositivas)
  - Capturas crudas: ~/Downloads/sl (solo accelerometer en uso)
  Previous entry: 7311e441b5803eceafe4874298ebfef97e83d621dcf144ea5705f3525ffb4204
- 2026-11-11T19:30:40Z [id:d1881146f13ca7e69e522ee6b42dacd89e59d4a4435be38ad752ab8f98a3222a] Format: 1
  UTC: 2026-11-11T19:30:40Z
  Repo: ak/presentations (origin ak:akielbowicz/presentations.git)
  Branch: pyday-hurlingham-2026
  HEAD: 44ede3d (visor simplificado sobre 5e06de0)
  Session: esta (continúa 2fb0103d de esta misma sesión)
  Task: charla PyDay Hurlingham 2026 "After Chabon" (Sumo) — deck reveal.js
  ## Objetivo
  Charla 20 min, 12 tracks Sumo, 2 mensajes: (1) la experiencia no se descarga, se construye en ambientes para romper sin miedo; (2) el software es sustrato para pensar. Demo 8 min (tracks 4-11) como ejemplo conductor.
  ## Fase actual: VISOR LEGIBLE PARA NOVATOS (feedback de Sasha aplicado); guion tracks 4-7 y slides con números reales pendientes
  ## Estado
  - Feedback Sasha: "es difícil entender la aplicación, tiene que ser más fácil". Diagnóstico: jerga del contrato en la UI (f_opt, k, sigma, redundancia incoherente), escala Y fijada al sigma del sintético que SATURABA el gráfico con la captura real (picos 17g), y chips t=0s sin significado.
  - Aplicado en commit 44ede3d (visor/app.js reescrito, index.html, style.css):
  - Clasificador palabras-del-día desde f_opt (solo para tramos t=Xs de capturas reales; el sintético conserva sus nombres): <=3 quieto, <=16 se mueve poco, <=30 se mueve mucho, >30 sacudón.
  - Escala Y centrada en media con techo en desvío 98.5% de muestras (clamped). El gráfico ahora muestra formas: planos en quieto, explosiones en sacudón.
  - Frase narrada por tramo, leyenda (— toda la data 60Hz · ● lo que alcanza guardar), grilla de tiempo (0/12/23/35/46 s), chips "quieto 20–25 s · alcanzan 1 Hz".
  - Redundancia_pct eliminada de la UI (su número no cuadraba con el titular). k/f_dyn solo en la tabla.
  - Caja de error si fetch falla (file:// bloqueado): instrucción de python3 -m http.server. Verificado en screenshots: ~/visor-simple.png (bien), ~/visor-error.png (file://).
  - README track 8-10 recorrido sincronizado con captura real: titular 1027/2774 (37%), click quieto (línea plana, misma historia), click sacudón (40 Hz no miente). El beat de aliasing (temblor miente a 15 Hz) queda para el SINTÉTICO (regenerar + copiar a visor/data + recargar).
  - Contrato JSON y lab intactos: 15 tests verdes.
  ## Decisión pendiente para Sasha (bloquea slides, no el visor)
  ¿La demo abre con el sintético etiquetado (quieto/caminando/temblor, historia didáctica con aliasing) y la captura real como payoff final ("37% en datos reales"), o va directo todo sobre la captura real? Tracks 4-7 del README aún tienen números del sintético (27%, caminando 15 Hz); tracks 8-10 ya quedaron escritos para la real.
  ## Próxima acción exacta
  Decidir lo anterior, rellenar slides.md (esqueleto commiteado): tracks 4-11 con guion actualizado (README), tracks 1-3 y 12 desde la tabla final del transcript (~/cotorreo conv chatgpt 6aed3a99). Ensayo 13/11 apuntando a 18:30: servir visor con python3 -m http.server 8642 --directory visor.
  ## Decisiones/constraints claves
  - Demo NO en vivo: Sasha narra, bloques de código crecientes. specs/espectacular NO entra (verbal). Diferenciarse de la charla 16:15: nosotros = qué podemos HACER.
  - SIEMPRE uv run python -m pytest. La métrica f_optima tomó 3 intentos; no "arreglar" sin leer la historia de commits.
  - El visor traduce el contrato a palabras; el JSON no cambia (regla de la casa escrita en el header de app.js).
  ## Validación
  uv run python -m pytest -q → 15 passed (hoy, HEAD 44ede3d). Visor verificado por screenshot headless con http.server: ~/visor-simple.png; error file://: ~/visor-error.png.
  ## Bloqueos
  Ninguno técnico. Ensayo 13/11, charla 14/11 12:30.
  ## Referencias condicionales
  - Guion: presentaciones/pyday_hurlingham_2026/demo/README.md
  - Transcript fuente: ~/cotorreo/raw/_conversations/chatgpt/6aed3a99-59cc-83e9-935a-94b77179bf54/transcript.md (tabla final 12 diapositivas)
  - Capturas crudas: ~/Downloads/sl (solo accelerometer en uso)
  Previous entry: 2fb0103d78ed90a6ec826159811338e59bee2d00bddc16f5c2d97f09ff80e53e (supersedes 2fb0103d78ed90a6ec826159811338e59bee2d00bddc16f5c2d97f09ff80e53e)
- 2026-11-11T19:54:35Z [id:b8975bc9d9685e78402e3ff17c300d5d8e75122de178ad4fd99ef28abf047b32] Format: 1
  UTC: 2026-11-11T19:54:35Z
  Repo: ak/presentations (origin ak:akielbowicz/presentations.git)
  Branch: pyday-hurlingham-2026
  HEAD: db0a454 (slides completos sobre 44ede3d)
  Session: esta (continúa d1881146 de esta misma sesión)
  Task: charla PyDay Hurlingham 2026 "After Chabon" (Sumo) — deck reveal.js
  ## Objetivo
  Charla 20 min, 12 tracks Sumo, 2 mensajes: (1) la experiencia no se descarga, se construye; (2) el software es sustrato para pensar. Demo 8 min sobre la CAPTURA REAL (decisión de Sasha: "vamos con la real").
  ## Fase actual: SLIDES COMPLETOS Y VERIFICADOS; falta ensayo y pulido menor
  ## Estado
  - Sasha decidió: toda la demo sobre la captura real (46s, 2774 lecturas, 37%). El sintético queda solo para el aliasing didáctico (documentado en README).
  - slides.md COMPLETO (commit db0a454): portada/bio intactas + 12 tracks con epígrafes verificados con citas del transcript ("Come on London...", "Do they know why they go?", "lo entendido es lo que no entiendo", "No tengas miedo, no", "Hello Frank...", "Think it don't think it", "No sé lo que quiero...", "Sing the song today", "usan radar", "real life is inside", "Sueña un sueño imposible", "everyday is Sunday"), tabla final "Las doce diapositivas revisadas" (transcript línea ~11149) como mapa de funciones, mensajes/cierre del transcript. Contenido tracks 4-11 con números de la captura real. NOTES con timings (~20 min) y beats del guion. Fragments para narrar avanzando.
  - README sincronizado: track 4 usa datos/captura.csv, track 6 tabla real (quieto 1Hz / se mueve poco 12 / mucho 25 / sacudón 40), titular 1027/2774 (37%), captura real como la demo.
  - Deck verificado por screenshots headless (http.server): portada, apertura 01, tabla 06 y visor 09 renderizan limpios. Ajustes hechos: argumentos como h4 (h1-h3 first-of-type son absolutos abajo — SOLO un título por slide, el epígrafe), tabla a 0.78em, imagen del visor con max-height 60vh, screenshots SIEMPRE con --hide-scrollbars (el scrollbar del source page queda cocinado en el png).
  - 15 tests del lab en verde. Contrato JSON intacto.
  ## Próxima acción exacta
  Ensayo 13/11 (apuntar a 18:30): python3 -m http.server 8642 --directory visor + abrir el deck por http igual. Ajustar en el ensayo: timings reales vs NOTES, tamaño de la imagen del visor en vivo (proyector), si track 02 (preguntas) toma más de 2 min recortar track 03.
  ## Decisiones/constraints claves
  - h1-h3 first-of-type = tapa del disco (absolutos abajo): NUNCA dos h2/h3 en la misma slide; argumentos van como h4.
  - El visor traduce el contrato a palabras; el JSON no cambia.
  - SIEMPRE uv run python -m pytest. f_optima: 3 intentos, historia en commits — no arreglar sin leer.
  - Demo NO en vivo: bloques crecientes + outputs capturados. specs/espectacular verbal. Diferenciarse de la charla 16:15: qué podemos HACER.
  ## Validación
  uv run python -m pytest -q → 15 passed (HEAD db0a454). Deck: screenshots ~/deck-e-10.png (09), ~/deck-c-7.png (06), ~/deck-b-2.png (01), ~/deck-0.png (portada). Visor: ~/visor-slide2.png.
  ## Bloqueos
  Ninguno técnico. Ensayo 13/11, charla 14/11 12:30. Pendiente menor: .whisper/ trackeado sí/no (sigue en el historial desde af4221a, sin push).
  ## Referencias condicionales
  - Guion: presentaciones/pyday_hurlingham_2026/demo/README.md
  - Transcript (tabla final + epígrafes con citas): ~/cotorreo/raw/_conversations/chatgpt/6aed3a99-59cc-83e9-935a-94b77179bf54/transcript.md
  - Epígrafes verificados: líneas 2036-2060 del transcript (tabla con Cite refs)
  Previous entry: d1881146f13ca7e69e522ee6b42dacd89e59d4a4435be38ad752ab8f98a3222a (supersedes d1881146f13ca7e69e522ee6b42dacd89e59d4a4435be38ad752ab8f98a3222a)
- 2026-11-11T22:30:37Z [id:2b276d4598cfe66e98a75ca5f9d7bfef835a947ce2b9a09d2c60d30ffa9d4798] Format: 1
  UTC: 2026-11-11T22:30:37Z
  Repo: ak/presentations (origin ak:akielbowicz/presentations.git)
  Branch: pyday-hurlingham-2026
  HEAD: 7e35026 (estilo de código sobre db0a454)
  Session: esta (continúa b8975bc9 de esta misma sesión)
  Task: charla PyDay Hurlingham 2026 "After Chabon" (Sumo) — deck reveal.js
  ## Objetivo
  Charla 20 min, 12 tracks Sumo. Demo 8 min sobre la captura real. Slides completos (db0a454).
  ## Fase actual: LISTO PARA ENSAYO
  ## Estado
  - Feedback Sasha: bloques de código mal formateados (cruzaban el marco, fondo oscuro). Resuelto en 7e35026 (phorma-theme.css): tarjeta blanca letra negra max-width 82% centrada dentro del marco, en AMBOS temas (data-theme dark/light del toggle sol/luna).
  - Gotcha documentado: los stylesheets hljs github/github-dark del toggle dejan tokens claros sobre tarjeta blanca → tokens forzados a monocromo negro con acento sumo-rojo desde el theme css. Si se cambia la tarjeta, revisar esa sección del css.
  - Verificado headless en dark y ?theme=light: ~/code-dark.png, ~/code-light.png, ~/code-js.png. 15 tests lab verdes.
  ## Próxima acción exacta
  Ensayo 13/11 apuntando a 18:30 (visor y deck por http, nunca file://). Ajustar timings vs NOTES, imagen del visor en proyector, track 02 preguntas ≤2 min.
  ## Decisiones/constraints claves
  - h1-h3 first-of-type = tapa del disco: UN título por slide, argumentos como h4.
  - Código siempre con tarjeta clara (legibilidad proyector) en ambos temas.
  - SIEMPRE uv run python -m pytest. f_optima: no arreglar sin leer historia de commits.
  ## Validación
  pytest 15 passed (HEAD 7e35026). Screenshots dark/light del bloque de código OK.
  ## Bloqueos
  Ninguno. Ensayo 13/11, charla 14/11 12:30. Menor: .whisper/ trackeado sí/no.
  ## Referencias condicionales
  - Guion: presentaciones/pyday_hurlingham_2026/demo/README.md
  - Transcript: ~/cotorreo/raw/_conversations/chatgpt/6aed3a99-59cc-83e9-935a-94b77179bf54/transcript.md
  Previous entry: b8975bc9d9685e78402e3ff17c300d5d8e75122de178ad4fd99ef28abf047b32 (supersedes b8975bc9d9685e78402e3ff17c300d5d8e75122de178ad4fd99ef28abf047b32)
- 2026-11-11T22:36:21Z [id:c5cdff9987af24016a10be7a1a584e45dad7fd6e92611b8bf927e02a3c483c1e] Format: 1
  UTC: 2026-11-11T22:36:21Z
  Repo: ak/presentations (origin ak:akielbowicz/presentations.git)
  Branch: pyday-hurlingham-2026
  HEAD: df4e100 (tarjetas de código pulidas sobre 7e35026)
  Session: esta (continúa 2b276d45 de esta misma sesión)
  Task: charla PyDay Hurlingham 2026 "After Chabon" (Sumo) — deck reveal.js
  ## Objetivo
  Charla 20 min, 12 tracks Sumo. Demo sobre captura real. Slides completos (db0a454), estilos de código resueltos.
  ## Fase actual: LISTO PARA ENSAYO (pulido de código OK)
  ## Estado
  - Segundo feedback sobre bloques de código: tarjetas disparejas (shrink-to-fit) y con aire de más abajo. Resuelto en df4e100:
  - pre a width 82% FIJO: todas las tarjetas iguales y alineadas.
  - code con height:auto + min-height:0: un height/min-height heredado imponía ~2.6 líneas a bloques de una (code 110px dentro de pre 68px, medido con debug script temporal — ya quitado).
  - index.html: Reveal.on(ready) recorta whitespace/<br> finales en pre code (el \n de cierre de cada fence quedaba como línea vacía).
  - Verificado: ~/code-final2.png (tarjeta compacta, una línea, uniforme, dentro del marco). 15 tests lab verdes.
  ## Próxima acción exacta
  Ensayo 13/11 apuntando a 18:30 (todo por http.server, nunca file://). Ajustar timings vs NOTES, imagen del visor en proyector, track 02 preguntas ≤2 min.
  ## Decisiones/constraints claves
  - h1-h3 first-of-type = tapa del disco: UN título por slide, argumentos como h4.
  - Código: tarjeta SIEMPRE clara (fondo --sumo-white, letra --sumo-black, max-width 82%), tokens hljs monocromo negro + acento sumo-rojo forzados desde theme css (los stylesheets del toggle sol/luna pegan colores ilegibles sobre blanco).
  - SIEMPRE uv run python -m pytest. f_optima: no arreglar sin leer historia de commits.
  ## Validación
  pytest 15 passed (HEAD df4e100). ~/code-final2.png.
  ## Bloqueos
  Ninguno. Ensayo 13/11, charla 14/11 12:30. Menor: .whisper/ trackeado sí/no.
  ## Referencias condicionales
  - Guion: presentaciones/pyday_hurlingham_2026/demo/README.md
  - Transcript: ~/cotorreo/raw/_conversations/chatgpt/6aed3a99-59cc-83e9-935a-94b77179bf54/transcript.md
  Previous entry: 2b276d4598cfe66e98a75ca5f9d7bfef835a947ce2b9a09d2c60d30ffa9d4798 (supersedes 2b276d4598cfe66e98a75ca5f9d7bfef835a947ce2b9a09d2c60d30ffa9d4798)
- 2026-11-11T22:39:29Z [id:f84c7762fa706fc4566a59211773a5c19facfe8bcbae3d531167ad141206456c] (#incitacionales) Format: 1
  UTC: 2026-11-11T22:39:00Z
  Repo: ak/presentations (origin ak:akielbowicz/presentations.git)
  Branch: pyday-hurlingham-2026
  HEAD: df4e100 (tarjetas de código pulidas)
  Session: esta — stash de cierre /next (continúa 2b276d45; última entrada completa c5cdff99)
  Task: charla PyDay Hurlingham 2026 "After Chabon" (Sumo) — deck reveal.js
  ## Objetivo
  Charla 20 min, 12 tracks Sumo, 2 mensajes: la experiencia no se descarga, se construye / el software es sustrato para pensar. Demo 8 min toda sobre la CAPTURA REAL (46s, 2774 lecturas, 37%).
  ## Fase actual: LISTO PARA ENSAYO — stash de cierre, nada en vuelo crítico
  ## Estado
  - Commits de la sesión: 5e06de0 (captura real integrada), 44ede3d (visor legible: palabras/escala/leyenda), db0a454 (slides completos: 12 tracks, epígrafes verificados con citas del transcript, NOTES con timings), 7e35026 (código: tarjeta blanca/negra dentro del marco, tokens hljs monocromo+rojo), df4e100 (tarjetas uniformes 82% + compactas). Nada pusheado.
  - Working tree SIN commitear: .whisper/notes.md (implícito: el store, siempre se mueve) y slides.md con UN BACKTICK SUELTO solo en línea ~41 (sección 01, tras el kicker) — parece typo accidental de Sasha al revisar; decidir: borrarlo o commit aparte.
  - Pendiente menor de siempre: .whisper/ trackeado sí/no (en historial desde af4221a, sin push).
  ## Próxima acción exacta
  (1) Resolver el backtick suelto de slides.md y commitear; (2) ENSAYO 13/11 apuntando a 18:30: deck y visor SIEMPRE por http.server (file:// bloquea fetch y fetch del visor falla silencioso → hay caja de error), ajustar timings vs NOTES de los slides, imagen del visor en proyector, track 02 (preguntas) ≤2 min o recortar track 03; (3) charla 14/11 12:30.
  ## Decisiones/constraints claves
  - h1-h3 first-of-type = tapa del disco (absolutos abajo): UN título por slide, argumentos como h4.
  - Código: tarjeta SIEMPRE clara (fondo --sumo-white, letra --sumo-black, width 82%), tokens hljs monocromo negro + acento sumo-rojo forzados desde theme css — si se toca, revisar esa sección (los stylesheets github/github-dark del toggle sol/luna dejan colores ilegibles sobre blanco).
  - El visor traduce el contrato a palabras (quieto/se mueve/sacudón); el JSON del lab no cambia.
  - SIEMPRE uv run python -m pytest. f_optima: 3 intentos, historia en commits — no arreglar sin leer.
  - Demo NO en vivo: bloques crecientes + outputs capturados. specs/espectacular verbal. Diferenciarse de la charla 16:15: qué podemos HACER.
  ## Validación
  uv run python -m pytest -q → 15 passed (HEAD df4e100). Deck/visor verificados por screenshot headless con http.server (~/code-final2.png y previos).
  ## Bloqueos
  Ninguno. Ensayo 13/11, charla 14/11 12:30.
  ## Referencias condicionales
  - Guion: presentaciones/pyday_hurlingham_2026/demo/README.md
  - Transcript (tabla final + epígrafes): ~/cotorreo/raw/_conversations/chatgpt/6aed3a99-59cc-83e9-935a-94b77179bf54/transcript.md
  - Capturas crudas: ~/Downloads/sl (solo accelerometer en uso)
  Previous entry: c5cdff9987af24016a10be7a1a584e45dad7fd6e92611b8bf927e02a3c483c1e (supersedes c5cdff9987af24016a10be7a1a584e45dad7fd6e92611b8bf927e02a3c483c1e)
- 2026-11-12T15:33:31Z [id:93ea40c1a0c4e9d157b9b9a46827823d7981b7331cbe0a7bc56e939f4302010a] (#incitacionales) Format: 1
  UTC: 2026-11-12T15:32:23Z
  Repo: ak/presentations (origin ak:akielbowicz/presentations.git)
  Branch: pyday-hurlingham-2026
  HEAD: 1bdafc3 (centrado vertical completo; franja del título por diapo)
  Session: 01a1ccc4-b2a9-73f2-b509-b05bc333c8a1 (stash /next; continúa el estado de f84c7762, sesión anterior ya commiteada)
  Task: charla PyDay Hurlingham 2026 "After Chatbon" (Sumo) — foco comercial Phorma + theme de títulos
  ## Objetivo
  Cerrar la charla con foco comercial Phorma (decidido: vende Phorma, no Sasha contractor) sin romper el concepto de disco, y mover H2/H3 a la esquina superior derecha como la palabra SUMO de la tapa (H1 intacto abajo).
  ## Fase actual: green/commit — cambios commiteados y verificados por screenshot; quedan decisiones de negocio
  ## Estado
  - Commits de esta sesión: 87a0a54 (H2/H3 al rincón + toggle abajo-izq), 1639f01 (title de página After Chatbon + charla-after-chatbon/index.html redirect para el QR que daba 404), 8a1d72b (cierre comercial: bisagra, 1 logo, oferta con cursos reales 83/44/75, CTA dos ramas, fuera Capacitación Técnica trucha y slide vacía; fusión 09+10; backtick línea 41 fuera), 1bdafc3 (fuera padding-top global que bajaba el centro 10%; franjas por diapo vía <!-- .slide: style="padding-top" --> en 03/05/09+10/11; track 06 sin punchline Nyquist —redundante con track 11— y tabla 0.64em; bio con Phorma Scientific al rincón, edición de Sasha).
  - Working tree SIN commitear: ediciones en vuelo de Sasha en slides.md (sacó el kicker del track 01; slide Gracias con link+mail como fragments) + el store .whisper. NO commitearlas sin preguntar: son su iteración viva.
  - 16 commits ahead de origin. NADA PUSHEADO: el QR/CTA y la rama "el código está publicado" dependen del push (charlas.saxa.xyz es GitHub Pages). Push requiere autorización explícita.
  ## Próxima acción exacta
  (1) Pedir/obtener OK de push y pushear; (2) definir precio del "diagnóstico de una hora" (la slide lo calla a propósito); (3) recortar ~1 min vs slot de 20 (candidatos: preguntas track 02 o viñetas de bio); (4) listar la charla en index.md del sitio; (5) ensayo 13/11 siempre por http.server, charla 14/11 12:30.
  ## Decisiones/constraints claves
  - "AFTER CHATBON" NO es typo: es el título aceptado (propuestas/pyday_hurlingham_2026.md:42). No tocar kickers.
  - NO volver a poner padding-top global en phorma-theme.css: baja el centro visual ~10% en todas las diapos. Franja solo por diapo; .titulo-abajo es el opt-out documentado para diapos densas.
  - Audiencia declarada de la charla = estudiantes (propuestas:65): el comprador real es docente/lab/institución; el estudiante es canal (rama "rompé el repo" del CTA).
  - SIEMPRE uv run python -m pytest (15 passed). f_optima: no arreglar sin leer historia.
  - Herramientas: read/edit ENOENT intermitente en paths absolutos de este repo → usar python/bash relativo. pkill -f se mata a sí mismo si el patrón está en el comando (usar corchetes). Servidores http.server huérfanos de otras sesiones: 8123/2345/8347/8402/8642/8742 y un 8137 ajeno.
  ## Validación
  uv run python -m pytest -q → 15 passed (HEAD 1bdafc3). Screenshots headless 1280x720 (/tmp/nuevo-*.png, servidor propio 8941 ya matado): 0, 1/0, 6/0, 7/0, 10/0, 11/0, 13, 14/1, 14/2 sin colisiones ni desbordes; bio centrada en 360/720 medida por bounding box.
  ## Bloqueos
  Push sin autorización; precio sin definir; ~1 min sobre el slot (NOTES dicen 20 min + 8-10 de preguntas: slot real sin confirmar con organizadores).
  ## Referencias condicionales
  - Deck: presentaciones/pyday_hurlingham_2026/{slides.md,phorma-theme.css,index.html}; redirect: charla-after-chatbon/index.html
  - Catálogo real Phorma: ~/para/areas/dev/gh/phorma/phormasci.github.io/content/trainees/es/{83,44,75}-*.md; tiers: AIC_STRATEGY.md §5 (Bronze = audit fixed scope)
  - Review Rule-of-5 de la propuesta: hallazgos CORR-001/003 y DRAFT-001 ya resueltos en estos commits
  Previous entry: none (superseded by 0fcb8a0b0945eac40c6fb5dfc46c5faa3af3235a4a458efb21eaaa28d46546eb)
- 2026-11-12T19:30:53Z [id:0fcb8a0b0945eac40c6fb5dfc46c5faa3af3235a4a458efb21eaaa28d46546eb] (#incitacionales) Format: 1
  UTC: 2026-11-12T16:15Z
  Repo: ak/presentations (origin ak:akielbowicz/presentations.git)
  Branch: pyday-hurlingham-2026
  HEAD: fa571df (notes: store whisper — PUSHEADO, todo commiteado, árbol limpio)
  Session: 01a1d065-2c52-73f2-b509-b05c23b4ffb3
  Task: charla PyDay Hurlingham 2026 "After Chatbon" — visor con veredictos, grabador adaptativo y tabla de memoria
  ## Objetivo
  Hacer que la demo muestre el PROBLEMA, no solo la solución: visor interactivo con veredictos, grabador adaptativo causal (la promesa del track 11) y la cuenta en memoria en el deck.
  ## Fase actual: commit+push completos; resta logística de charla
  ## Estado
  - Commits de esta sesión (TODOS PUSHEADOS, 55f17b6..fa571df):
  - 313cd04+e3dd1f7+2b2f2d5+55f17b6: visor — slider "¿y si mido a… Hz?" con veredicto (alcanza/existe pero miente/miente, umbrales f_opt y 2·f_dyn del contrato), deep-links ?tramo=&tasa=, guardias del review Rule-of-5 (tramo fraccional, f_dyn null, hint sin "(1 de cada 1)"), refactor porQue sobre razon única.
  - 6be957c+6c93346: track 4 ganó página vertical con tabla de memoria (1/10/30/60 min, 60 Hz vs 37%: 9,1 MB/hora, 5,7 MB de ruido; 42 B = fila CSV real). Verificada sin overflow por píxeles.
  - e9729ce: lab — muestreo grabar: GrabadorAdaptativo causal (ventana 2 s, decide cada 0.5 s con f_optima sobre la ventana — sin regla k: los k reales llegan a 19.6; histéresis subir-inmediato/bajar-2-ticks; pacing en UNIDADES DE MUESTRA enteras — pacing flotante daba aliasing 30 Hz; re-decimado del buffer RAM en cada subida — pre-buffer de cámara de auto). Real: 1615/2774 (58%), error 4.1% RMS.
  - 9543e60: visor tercer acto — sección grabador (verdad gris + puntos persistidos + escalón de tasa + ventana 2 s deslizándose), botón ▶ (46 s→14 s), deep-link ?reproducir, contrato data/grabacion.json con su test.
  - fa571df: store whisper.
  - 25 passed en lab. Nada pendiente de código.
  ## Próxima acción exacta
  (1) ENSAYO 13/11: deck + visor SIEMPRE por http.server; probar el recorrido track 11 completo (grabar en terminal → ?reproducir → frase "decidir sin futuro cuesta 21 puntos y no miente") y el QR; (2) definir precio del diagnóstico (la slide lo calla); (3) recortar ~1 min del slot 20; (4) listar la charla en index.md de master; (5) charla 14/11 12:30.
  ## Decisiones/constraints claves
  - QR 404 en vivo hasta deploy: charlas.saxa.xyz sirve master; master es ancestro directo de la rama → fast-forward limpio de un comando. Decidido: "mantengamos en la branch" — NO deployar sin pedido explícito.
  - Push requiere autorización explícita (esta vez dada, hecho).
  - Regla de la casa intacta: el contrato es el JSON, el visor lo traduce a palabras; grabacion.json es contrato nuevo con test en test_cli.
  - SIEMPRE uv run python -m pytest. No tocar kickers ni padding-top global. "AFTER CHATBON" no es typo.
  - El offline dice f_opt=40 sobre 59.9 Hz y significa paso=1 (60 Hz reales): la grilla se interpreta con round(tasa_medida/f) en TODAS las capas — así quedó el grabador.
  ## Validación
  uv run python -m pytest -q → 25 passed (HEAD fa571df). Visor/deck verificados headless (dump-dom + screenshots + estadísticas de píxel). git status limpio, rama en sync con origin.
  ## Bloqueos
  Ninguno técnico. Precio sin definir; slot ~1 min arriba; deploy a master a propósito pendiente.
  ## Referencias condicionales
  - Guion: presentaciones/pyday_hurlingham_2026/demo/README.md (tracks 4, 8–11 actualizados)
  - Grabador: demo/lab/src/muestreo/grabador.py (docstring = explicación completa)
  - Visor: demo/visor/app.js (sección "Tercer acto" al final)
  Previous entry: 93ea40c1a0c4e9d157b9b9a46827823d7981b7331cbe0a7bc56e939f4302010a (supersedes 93ea40c1a0c4e9d157b9b9a46827823d7981b7331cbe0a7bc56e939f4302010a)
- 2026-11-13T20:14:53Z [id:c88d389d83fab864b56858ff5ca05ec3cb23e5923361eb8c017ea29dfa9f6924] (#incitacionales) Format: 1
  UTC: 2026-11-13T20:16Z
  Repo: ak/presentations (origin ak:akielbowicz/presentations.git)
  Branch: pyday-hurlingham-2026
  HEAD: 900e410 (PUSHEADO, sync con origin, árbol limpio)
  Session: 01a1d142-d9e3-73f2-b509-b05e7fdb0776
  Task: charla PyDay Hurlingham 2026 "After Chatbon" — sección Charly Vibes en el deck (iframe sensor-log + tabla memoria 1 sensor vs 6)
  ## Objetivo
  Sumar al deck una sección Charly Vibes con el sensor-log embebido y tabla de memoria comparando 1 sensor vs los 6 sensores de la app.
  ## Fase actual: commit completo (900e410); sin trabajo en vuelo
  ## Estado
  - Esta sesión: arreglé iframe malformado (sin src=, sin tamaño, sin cierre) → <iframe src="https://charly-vibes.github.io/jams/sensor-log/" width="880" height="480" title="Sensor Log"></iframe> (slides.md:67); re-ejeé la tabla de memoria: columnas ahora "1 sensor" vs "los 6 sensores" (antes frecuencia), rótulo "memoria a 60 Hz:" (slides.md:73-82); regla guard de centrado de iframes en phorma-theme.css:431.
  - Números fundamentados en el código real de la app: SENSOR_DEFS tiene 6 sensores (accelerometer, gyroscope, gravity, linearAccel, orientation, compass); fila CSV 3-ejes ~44 B + compass ~24 B ≈ 244 B/tick a 60 Hz → 0,9 MB/min, 53 MB/h. Columna 1 sensor = captura real medida (42 B/fila). FREQ_OPTIONS=[1,5,10,30,60].
  - Commits de Sasha después (0db4e1f..900e410): limpieza bio/track 03, ELIMINARON la tabla de frecuencia (ritmo justo ya no existe en el deck — la única tabla que queda es la nueva, líneas 76-82) e iframe NUEVO en slides.md:194 con el visor LOCAL embebido (./demo/visor/index.html 880×480).
  - Centrado verificado por DOM probe: tabla centro exacto x=640, margin auto ~282px por lado; estilo inline width: fit-content; margin: 0 auto.
  - Trampas descubiertas: (1) chrome headless reutiliza --disk-cache-dir entre corridas y sirve slides.md VIEJO — cache dir fresco por corrida; (2) el elemento en x=47 que parece "no centrado" es un logo del tema, no contenido; (3) para geometría exacta usar página sonda (iframe same-origin + getBoundingClientRect) en vez de screenshots/píxeles; (4) tabla con margin auto SÍ centra en Chrome.
  ## Próxima acción exacta
  (1) Verificar en proyector el iframe del visor local (slides.md:194) y el sensor-log remoto — http.server obligatorio (file:// rompe fetch); (2) charla 14/11 12:30 según logística ya planificada; (3) si se comenta la tabla en vivo: los 6 sensores corriendo SIMULTÁNEOS a 60 Hz es el supuesto del caso peor.
  ## Decisiones/constraints claves
  - No deploy a master sin pedido explícito; push requiere autorización (rama ya en sync).
  - SIEMPRE uv run python -m pytest. No tocar kickers ni padding-top global.
  - Iframe no renderiza en PDF export: la URL desnuda bajo el iframe es el fallback (slides.md:70).
  - Pytest NO corrido esta sesión (no toqué lab; 25 passed siguen válidos en lab).
  ## Bloqueos
  Ninguno conocido.
  ## Referencias condicionales
  - Sección Charly Vibes: presentaciones/pyday_hurlingham_2026/slides.md líneas 56-82
  - Visor local embebido: slides.md:194
  - Guion: presentaciones/pyday_hurlingham_2026/demo/README.md
  Previous entry: 0fcb8a0b0945eac40c6fb5dfc46c5faa3af3235a4a458efb21eaaa28d46546eb
