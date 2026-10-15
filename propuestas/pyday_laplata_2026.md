## Bio / Perfil

Sasha es Consultor y Arquitecto Científico con formación en Física (UBA). Se especializa en Cómputo de Alto Rendimiento, IA Agéntica y Arquitectura de Sistemas Cuantitativos. Cuenta con más de 7 años de experiencia construyendo motores matemáticos de nivel productivo y bibliotecas core en instituciones financieras de primer nivel y empresas tecnológicas (como Qontigo, J.P. Morgan, Mercado Libre, AstraZeneca). Actualmente, diseña la integración y los marcos de evaluación para que los Modelos de Lenguaje puedan procesar datos científicos y financieros sin alucinaciones, buscando siempre reducir la brecha entre la "Investigación" y la "Producción".

Expositor regular en conferencias y meetups de tecnología (PyConAr, PyDay, SciPy Latam), donde comparte experiencias sobre patrones de diseño, clean code, formación de equipos y buenas prácticas de desarrollo aplicadas a problemas reales.

---

# Research Software Engineering: prácticas que nadie enseña en el lab

## Short Abstract (300 caracteres)

¿Corriste un script que funcionaba perfecto la semana pasada y hoy no reproduce los resultados? Son prácticas de ingeniería que nadie enseña en el lab. Metodologías validadas en la industria aplicadas al código científico: código probado, habitable, operable, robusto, mantenible y auditable, sin burocracia.

## Long Description

¿Cuántas veces corriste un script analítico que funcionaba perfecto la semana pasada y hoy no reproduce los mismos resultados? ¿O heredaste código de alguien que ya no está en el equipo y no tenés idea por dónde empezar a tocar?

Esto no es mala suerte, ni culpa de los datos. Es la ausencia de prácticas de ingeniería aplicadas a la investigación y experimentación. El software para ciencia y análisis de datos tiene ciclos de vida distintos al software comercial, y la necesidad de poder pivotar hipótesis rápido muchas veces atenta contra la robustez del código.

En esta charla vamos a hablar sobre el Research Software Engineering (RSE). Vamos a agarrar metodologías ya validadas en la industria del software tradicional y ver cómo bajarlas a la trinchera del código científico y analítico sin burocracia innecesaria.

Te vas a llevar herramientas prácticas para dejar de escribir código descartable y empezar a producir software que sea:
- **Probado:** que alguien más (incluido tu "yo" del futuro) pueda verificar que funciona.
- **Habitable:** que se deje leer y modificar seis meses después sin dolor.
- **Operable:** que corra sin problemas en otra máquina.
- **Robusto:** que sobreviva al cambio constante de hipótesis.
- **Mantenible:** que no termine siendo un monolito intocable.
- **Auditable:** que permita rastrear exactamente qué versión de código produjo qué resultado.

## Audiencia
Ideal para estudiantes avanzados, investigación académica y cualquiera que escriba código para análisis de datos, tesis o experimentos. Nivel básico-intermedio de Python.

## Labels
Research Software Engineering, Ciencia reproducible, Buenas prácticas, Análisis de datos, Metodologías ágiles, Python

# Software científico e IA: cómo usar LLMs sin romper todo

## Short Abstract (300 caracteres)

Generar código con buenas prácticas es el eslabón débil en proyectos de investigación, pero está cambiando: los LLMs y Coding Agents saben más de arquitectura que la mayoría de la academia. Cómo estructurar el contexto, qué delegar a la IA y qué no, y cómo usarla para validar y aprender, no solo para autocompletar.

## Long Description

Generar código que siga las buenas prácticas de ingeniería suele ser el eslabón débil en los proyectos de investigación. Pero eso está cambiando: hoy los LLMs y Coding Agents saben más de arquitectura de software que la mayoría de la academia.

El problema no es el modelo de lenguaje, sino que nadie nos enseñó a usarlo para otra cosa que no sea autocompletar líneas sueltas o generar scripts descartables. Si queremos producir código de mejor calidad (y no solo código en mayor cantidad), tenemos que cambiar la forma en la que interactuamos con la IA.

En esta charla vamos a ver cómo extraer el conocimiento de arquitectura de los LLMs metiéndolos en procesos donde prima el determinismo y la reproducibilidad científica. Vamos a explorar qué fricciones y restricciones hay que agregarle intencionalmente a la "mesa de trabajo" del modelo para que vaya por el camino que a nosotros nos interesa.

Básicamente, vamos a dejar de usar la IA como un pasante que tipea rápido y vamos a empezar a usarla como una herramienta de validación, diseño y aprendizaje continuo.

En la charla vamos a ver:
- Qué tareas del ciclo científico podemos delegarle a la IA y cuáles definitivamente no.
- Cómo estructurar el contexto para recuperar determinismo sin perder velocidad.
- Estrategias y herramientas para que la IA aplique RSE y mantenga bases de código existentes.
- Cómo usar los modelos para entender los problemas a fondo en lugar de solo pedirles la solución.

## Audiencia
Todas las seniorities. Especialmente útil para estudiantes y investigadores que ya usan IA en su flujo de trabajo y quieren sacarle más partido sin perder rigor.

## Labels
Inteligencia Artificial, LLMs, Coding Agents, Research Software Engineering, Ciencia reproducible, Productividad

# Specs de placer

## Short Abstract (300 caracteres)

Delegar código a agentes es fácil; asegurarse de que hagan lo que uno quiere, no. Cómo escribir especificaciones que los agentes realmente sigan: qué incluir, qué omitir, cómo validarlas y cómo convertir la especificación en la fuente de verdad del desarrollo asistido por IA.

## Long Description

Pedirle código a un agente de IA toma segundos. Asegurarse de que ese código haga lo que uno quería, en el contexto de una base existente y sin romper nada, es otro deporte. El problema casi nunca es el modelo: es que pedimos con la misma precisión con la que le contestamos un mail.

En esta charla vamos a hablar de especificaciones: la práctica de escribir, antes de programar, qué hay que construir, bajo qué restricciones y cómo se verifica que quedó bien. No como burocracia, sino como la herramienta más rentable que tenemos para dirigir agentes de IA.

La tesis es simple: una buena especificación convierte el desarrollo asistido por IA de una lotería en un proceso verificable. La especificación pasa a ser la fuente de verdad, y el código —generado por la máquina— pasa a ser un detalle de implementación que se valida contra ella.

Vamos a ver:
- Qué hace buena a una especificación: criterios verificables, restricciones explícitas, alcance acotado.
- Qué omitir: especificar demasiado temprano también mata.
- Cómo validar que los agentes realmente siguen la especificación (y detectar cuando se la saltean).
- Cómo integrar specs al flujo de trabajo: del ticket a la revisión, con tests como contrato.
- Errores comunes al arrancar y cómo evitarlos.

## Audiencia
Todas las seniorities. Especialmente útil para quienes ya usan agentes o asistentes de IA en su trabajo y sienten que el resultado es una caja misteriosa, y para estudiantes que quieren aprender a trabajar así desde el arranque.

## Labels
Spec-Driven Development, Inteligencia Artificial, Coding Agents, Buenas prácticas, Testing, Metodologías
