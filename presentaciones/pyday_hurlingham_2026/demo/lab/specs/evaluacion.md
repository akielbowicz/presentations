---
id: eval.corpus
kind: intent
statement: "WHEN produced affirmations are compared against the golden corpus THE evaluator SHALL report precision and recall matching on whitespace-collapsed text and fail honestly on empty inputs"
---

# modelo

Espeja los evals de bajan: corpus dorado adjudicado a mano, precisión y
recall por coincidencia de texto. Simple de explicar en una charla,
honesto sobre sus límites: mide contra un corpus, no contra el mundo.
Un resultado negativo también es conocimiento.

| propiedad | alcance | se cumple cuando |
|---|---|---|
| [[eval.corpus.colapso-espacios]] | coincidencia | el match colapsa espacios en ambos lados |
| [[eval.corpus.precision-recall]] | métricas | precisión = producidas precisas / producidas; recall = doradas encontradas / doradas |
| [[eval.corpus.vacio]] | honestidad | entradas vacías devuelven 0.0, nunca explotan |
