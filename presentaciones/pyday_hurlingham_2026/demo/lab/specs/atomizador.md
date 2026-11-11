---
id: atomizador.units
kind: intent
statement: "WHEN an episode text is segmented THE atomizador SHALL produce deterministic claim-sized units that are verbatim substrings of the source and re-concatenate to it modulo whitespace"
---

# modelo

Espeja `bajan::extract::atomic_claim_units` (bajan-5zy): límites de oración,
fusión de fragmentos cortos hacia adelante, fusión del fragmento final corto
hacia atrás y división de unidades largas en conectores `; ` (mejor esfuerzo,
nunca a mitad de palabra). Misma entrada → mismas unidades: el determinismo
es requisito de la caché.

El defecto conocido NO es un bug: los encabezados (sin puntuación final) y
las preguntas se proponen como candidatas. La evaluación y la visualización
son los que lo hacen visible.

| propiedad | alcance | se cumple cuando |
|---|---|---|
| [[atomizador.units.verbatim]] | unidad | toda unidad es subcadena verbatim del texto |
| [[atomizador.units.reconstruccion]] | unidades | las unidades re-concatenan al texto módulo espacios |
| [[atomizador.units.fusion-adelante]] | fusión | la unidad bajo mínimo absorbe a la siguiente |
| [[atomizador.units.fusion-atras]] | fusión | el fragmento final corto se fusiona hacia atrás |
| [[atomizador.units.division-conector]] | división | las unidades largas se dividen en '; ' de forma verbatim |
| [[atomizador.units.sin-puntuacion]] | encabezados | texto sin puntuación final → unidad única |
| [[atomizador.units.constantes-bajan]] | constantes | MIN_UNIDAD=20 y MAX_UNIDAD=300 coinciden con bajan |
| [[atomizador.units.evidencia]] | candidatos | cada candidato lleva sección, línea y cita verbatim |
| [[atomizador.units.preguntas-sobreviven]] | defecto conocido | las preguntas se proponen como candidatas |
