## Bio / Perfil

Sasha es licenciado en Física por la UBA, consultor en software científico e inteligencia artificial y cofundador de Phorma, donde ayuda a equipos de investigación a convertir sus modelos y experimentos en software que puedan usar, mantener y compartir.

Tiene más de 7 años de experiencia desarrollando software científico y financiero en J.P. Morgan, Qontigo, SimCorp y Mercado Libre. Trabajó en bibliotecas de cálculo, optimización de rendimiento y formación de equipos. Recientemente fue Senior AI Engineer en AstraZeneca, donde desarrolló integraciones y evaluaciones para una plataforma de agentes de IA aplicada a investigación y desarrollo en oncología.

Participa como orador en PyConAr, PyDay, SciPy Latam y meetups de Python y Julia. En sus charlas comparte experiencias y herramientas para entender mejor el código, probarlo y trabajar en equipo, tanto para quienes recién empiezan como para quienes llevan años programando.

---

# Research Software Engineering: prácticas que nadie enseña en el lab

## Short Abstract (300 caracteres)

¿Tu script funcionaba la semana pasada y hoy no reproduce los resultados? Vamos a ver cómo aplicar prácticas de ingeniería al código científico: tests, entornos reproducibles y formas de organizar el código para que puedas modificarlo y rastrear qué versión produjo cada resultado.

## Long Description

¿Cuántas veces corriste un script analítico que funcionaba perfecto la semana pasada y hoy no reproduce los mismos resultados? ¿O heredaste código de alguien que ya no está en el equipo y no tenés idea por dónde empezar a tocar?

En investigación necesitamos cambiar hipótesis y probar ideas rápido. Muchas veces el código crece a medida que exploramos, y dejamos para después los tests, la documentación o el registro del entorno. El problema aparece cuando queremos repetir un resultado o compartir el trabajo con alguien más.

En esta charla vamos a hablar sobre el Research Software Engineering (RSE). Vamos a agarrar metodologías ya validadas en la industria del software tradicional y ver cómo aplicarlas al código científico y analítico sin agregar burocracia innecesaria.

Te vas a llevar herramientas prácticas para dejar de escribir código descartable y empezar a producir software que sea:

- **Probado:** que alguien más (incluido tu "yo" del futuro) pueda verificar que funciona.
- **Habitable:** que se deje leer y modificar seis meses después sin dolor.
- **Operable:** que corra sin problemas en otra máquina.
- **Robusto:** que sobreviva al cambio constante de hipótesis.
- **Mantenible:** que no termine siendo un monolito intocable.
- **Auditable:** que permita rastrear exactamente qué versión de código produjo qué resultado.

## Audiencia

Ideal para estudiantes avanzados, personas que trabajan en investigación y cualquiera que escriba código para análisis de datos, tesis o experimentos. Nivel básico-intermedio de Python.

## Labels

Research Software Engineering, Ciencia reproducible, Buenas prácticas, Análisis de datos, Metodologías ágiles, Python

# Software científico e IA: cómo usar LLMs sin romper todo

## Short Abstract (300 caracteres)

¿Usás IA para escribir código científico? Vamos a ver qué tareas podés delegar, cómo darle contexto y cómo revisar lo que genera. Ejemplos de uso de modelos de lenguaje y agentes para diseñar, probar y entender código sin perder de vista la reproducibilidad de los resultados.

## Long Description

En investigación solemos aprender a programar mientras resolvemos otro problema. Los modelos de lenguaje y los agentes de programación pueden ayudarnos a explorar diseños, escribir tests y entender código que no conocemos. ¿Cómo los usamos sin perder el control sobre los resultados?

Si los usamos solo para autocompletar líneas o generar scripts sueltos, dejamos afuera buena parte de esas posibilidades. Vamos a ver cómo darles el contexto del proyecto y pedir cambios que podamos revisar y probar.

En esta charla vamos a ver cómo integrar estas herramientas a un proceso de trabajo que necesita resultados reproducibles. Qué restricciones conviene explicitar, qué verificaciones podemos automatizar y qué decisiones siguen necesitando nuestra revisión.

La idea es usar la IA para diseñar, validar y aprender, además de generar código.

En la charla vamos a ver:

- Qué tareas del ciclo científico podemos delegarle a la IA y cuáles definitivamente no.
- Cómo estructurar el contexto y registrar el entorno para poder verificar los resultados.
- Estrategias y herramientas para aplicar prácticas de Research Software Engineering (RSE) con IA y mantener bases de código existentes.
- Cómo usar los modelos para entender los problemas a fondo en lugar de solo pedirles la solución.

## Audiencia

Todas las seniorities. Especialmente útil para estudiantes y investigadores que ya usan IA en su flujo de trabajo y quieren sacarle más partido sin perder rigor.

## Labels

Inteligencia Artificial, LLMs, Coding Agents, Research Software Engineering, Ciencia reproducible, Productividad

# Specs de placer

## Short Abstract (300 caracteres)

Pedirle código a un agente lleva segundos. ¿Cómo verificás que hace lo que querías? Vamos a ver cómo escribir especificaciones: qué incluir, qué dejar abierto y cómo usarlas para guiar el desarrollo y revisar los resultados con tests y criterios concretos.

## Long Description

Pedirle código a un agente de IA toma segundos. Asegurarse de que ese código haga lo que uno quería, en el contexto de una base existente y sin romper nada, es otro deporte. A veces pedimos con la misma precisión con la que le contestamos un mail. Y aunque el pedido sea claro, el agente puede equivocarse: necesitamos una forma de comprobar qué hizo.

En esta charla vamos a hablar de especificaciones: escribir, antes de programar, qué hay que construir, bajo qué restricciones y cómo se verifica que quedó bien. Vamos a ver qué conviene dejar por escrito para que un agente pueda trabajar y vos puedas revisar el resultado.

Vamos a usar la especificación como referencia para revisar el código generado y comprobar si cumple lo que pedimos. También vamos a discutir qué pasa cuando cambia el pedido o cuando descubrimos que habíamos dejado algo sin definir.

En la charla vamos a ver:

- Qué hace buena a una especificación: criterios verificables, restricciones explícitas, alcance acotado.
- Qué conviene dejar abierto y qué necesitamos definir antes de delegar.
- Cómo validar que los agentes realmente siguen la especificación (y detectar cuando se la saltean).
- Cómo integrar specs al flujo de trabajo: del ticket a la revisión, con tests como contrato.
- Errores comunes al arrancar y cómo evitarlos.

## Audiencia

Todas las seniorities. Especialmente útil para quienes ya usan agentes o asistentes de IA en su trabajo y quieren poder verificar mejor el resultado, y para estudiantes que quieren aprender a trabajar así desde el arranque.

## Labels

Spec-Driven Development, Inteligencia Artificial, Coding Agents, Buenas prácticas, Testing, Metodologías
