---
id: estructura.hipotesis
kind: intent
statement: "WHEN a candidate comes from titles, headings or questions THE structure extractor SHALL discard it while keeping body sentences, to improve precision without losing recall"
---

# modelo

La hipótesis que nació de mirar la salida del extractor atómico: si además
del texto usamos la estructura del documento, la precisión mejora sin
perder recall. Es una hipótesis, no un dogma: el corpus dorado es el juez.

| propiedad | alcance | se cumple cuando |
|---|---|---|
| [[estructura.hipotesis.sin-titulos]] | descarte | los episodios de títulos y encabezados no producen candidatos |
| [[estructura.hipotesis.sin-preguntas]] | descarte | las preguntas no son conocimiento |
| [[estructura.hipotesis.cuerpo]] | conservación | los enunciados del cuerpo (incluidos items de lista) se conservan |
