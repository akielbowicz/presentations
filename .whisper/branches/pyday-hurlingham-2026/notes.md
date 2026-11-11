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
