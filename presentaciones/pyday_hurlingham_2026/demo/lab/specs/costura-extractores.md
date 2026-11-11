---
id: extractor.seam
kind: intent
statement: "WHEN a new extractor is implemented THE pipeline SHALL accept it as a drop-in replacement identified by its version, without the extractor owning validation, caching or lineage"
---

# modelo

La costura de bajan (`bajan::extract::Extractor`): el pipeline valida,
cachea, registra y proyecta lineage; los extractores solamente proponen
candidatos para UN episodio por llamada. La versión del extractor es
identidad de caché: cambiarla re-extrae todo bajo la clave nueva.

| propiedad | alcance | se cumple cuando |
|---|---|---|
| [[extractor.seam.version-cache]] | versión | `version()` declara la identidad (`atomico-*`, `estructura-*`) |
| [[extractor.seam.un-episodio]] | lote | `proponer()` recibe un episodio y devuelve candidatos con evidencia |
