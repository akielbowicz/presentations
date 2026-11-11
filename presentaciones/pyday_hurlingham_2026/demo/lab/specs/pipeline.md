---
id: pipeline.contract
kind: intent
statement: "WHEN a markdown document is processed THE pipeline SHALL emit episodes and candidate affirmations whose evidence locates verbatim in a line of the original document"
---

# modelo

El pipeline es dueño de los ids, de la validación y del JSON de salida;
los extractores solamente proponen (ver [[extractor.seam]]). Los
encabezados episodian aparte del cuerpo: el título del documento como
`título`, los demás como `encabezado`, el cuerpo con el nombre de su
sección. Cada episodio y cada afirmación recuerdan su línea de origen.

| propiedad | alcance | se cumple cuando |
|---|---|---|
| [[pipeline.contract.episodios-titulos]] | episodios | títulos, encabezados y cuerpos episodian por separado |
| [[pipeline.contract.json-claves]] | contrato | el JSON tiene exactamente documento/extractor/episodios/afirmaciones |
| [[pipeline.contract.evidencia-linea]] | evidencia | toda cita es verbatim y localiza en su línea del documento |
