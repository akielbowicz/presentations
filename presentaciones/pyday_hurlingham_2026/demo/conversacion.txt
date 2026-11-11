# Estructurar diez ideas

## User

Lets start creating a 25min markdown presentation for After Chatbon. Lets do some top-down structuring. Fisrt lets define the top 10 ideas to express

## Tool

[L1] ## Bio / Perfil

[L3] Sasha es licenciado en Física por la UBA, consultor en software científico e inteligencia artificial y cofundador de Phorma, donde ayuda a equipos de investigación a convertir sus modelos y experimentos en software que puedan usar, mantener y compartir.

[L5] Tiene más de 7 años de experiencia desarrollando software científico y financiero en J.P. Morgan, Qontigo, SimCorp y Mercado Libre. Trabajó en bibliotecas de cálculo, optimización de rendimiento y formación de equipos. Recientemente fue Senior AI Engineer en AstraZeneca, donde desarrolló integraciones y evaluaciones para una plataforma de agentes de IA aplicada a investigación y desarrollo en oncología.

[L7] Participa como orador en PyConAr, PyDay, SciPy Latam y meetups de Python y Julia. En sus charlas comparte experiencias y herramientas para entender mejor el código, probarlo y trabajar en equipo, tanto para quienes recién empiezan como para quienes llevan años programando.

---

[L11] # El río sin orillas: revelando las abstracciones de tu sistema

[L13] ## Short Abstract (300 caracteres)

[L15] Un cover en español y Python de "Nothing is Something", de Sandi Metz. Vamos a refactorizar un ejemplo paso a paso para ver cómo reemplazar condicionales por objetos y cuándo conviene usar composición. Ideas para reconocer abstracciones y simplificar tu código.

[L17] ## Long Description

[L19] Hay código que al leerlo te hace pensar que el problema que resolvía era extremadamente difícil. Y hay código que, al leerlo, hace que el mismo problema parezca que siempre fue simple. La diferencia rara vez es el lenguaje ni el framework; la diferencia está en el diseño.

[L21] Hay presentaciones que te hacen clic en la cabeza y merecen ser replicadas. Hace más de 10 años, Sandi Metz dio "Nothing is Something". Esta charla es un cover en español y en Python, donde vamos a repasar sus ideas de diseño orientado a objetos para construir sistemas más fáciles de combinar y modificar.

[L23] Vamos a refactorizar un ejemplo paso a paso y ver cómo cada cambio nos ayuda a reconocer las abstracciones que simplifican el problema.

[L25] La idea es que puedas reconocer esas mismas oportunidades de mejora en tu código.

[L27] Puntualmente vamos a ver:

[L29] - Cómo reemplazar una maraña de condicionales en favor del polimorfismo.
[L30] - Cuándo tiene sentido usar herencia y cuándo hay que preferir la composición con inyección de dependencias.
[L31] - Cómo avanzar con cambios chicos sin reescribir todo el sistema.
[L32] - Cómo evaluar si un cambio hace que el código sea más fácil de leer, modificar y probar.

[L34] ## Audiencia

[L36] Todas las seniorities. Especialmente recomendada para estudiantes y quienes están dando sus primeros pasos en diseño de software. Se recomienda conocer funciones y clases en Python para seguir los ejemplos.

[L38] ## Labels

[L40] Diseño Orientado a Objetos, Patrones de diseño, Refactoring, Clean Code, Artesanía de software, Python

[L42] # After Chatbon

[L44] ## Short Abstract (300 caracteres)

[L46] Si podemos generar código en segundos, ¿qué vale la pena aprender? Vamos a repasar prácticas de ingeniería y ciencia para revisar lo que genera la IA, decidir qué construir y aprovechar la variación entre respuestas para explorar, aprender y prototipar.

[L48] ## Long Description

[L50] Entre chatbots, asistentes y agentes, podemos generar un archivo con código plausible en lo que tardamos en escribir un mail. Pero todavía tenemos que decidir qué construir, verificar que funciona y mantenerlo cuando cambian los requisitos. ¿Qué vale la pena aprender para hacer ese trabajo?

[L52] En esta charla vamos a discutir qué tenemos que aprender ahora, después del Chatbon. Vamos a repasar las prácticas de ingeniería y de ciencia que nos ayudan a decidir qué pedirle a la IA, revisar lo que genera y mantener el software que construimos.

[L54] También vamos a hablar de qué cambia cuando trabajamos con un proceso probabilístico: el mismo pedido puede producir resultados distintos. ¿Cómo verificamos esos resultados y cómo aprovechamos esa variación para explorar alternativas?

[L56] En la charla vamos a discutir:

[L58] - Qué prácticas de ingeniería y ciencia nos sirven cuando la IA genera buena parte del código.
[L59] - En qué cosas tenemos que fijarnos cuando la IA genera: tests, reproducibilidad, diseño, dependencias, seguridad.
[L60] - Cómo trabajar con un proceso probabilístico: iterar, verificar y decidir dónde hace falta revisar antes de seguir.
[L61] - Cómo puede esa misma aleatoriedad jugar a nuestro favor para explorar, aprender y prototipar más rápido.

[L63] ## Audiencia

[L65] Todas las seniorities. Pensada para estudiantes y quienes están definiendo qué aprender, pero también para profesionales que quieren revisar cómo trabajan y qué les conviene aprender.

[L67] ## Labels

[L69] Inteligencia Artificial, Prácticas de ingeniería, Vibe Coding, Aprendizaje, Software Craftsmanship, Ciencia reproducible

Use ref_id "turn0file0" to reference this file. For broad questions or unknown locations, retrieve relevant chunks with `files.search` scoped to this file. Use `files.find` only for exact text, and use `files.read` for a known range or to expand relevant results. Full file size: 70 file lines.

## Assistant

# After Chatbon
<text color="secondary" size="sm">Estructura conceptual · Charla de 25 minutos · Primera iteración</text>

Partiendo del abstract de *After Chatbon*, propongo organizar la charla alrededor de una pregunta central:

**Si generar código se volvió barato, ¿qué necesitamos aprender para construir software que entendamos, podamos verificar y mantener?**

La charla debería evitar convertirse en una enumeración de buenas prácticas. Conviene construir un argumento: **la IA cambia qué nos cuesta, qué necesitamos saber y cómo podemos trabajar.**

## Las 10 ideas principales

<box gap={3}>
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="lg" padding={2} width="40px" align="center">
      **01**
    </box>
    <box flex="1" gap={1}>
      **El código dejó de ser la parte más cara de producir.**

      Podemos generar implementaciones en segundos, pero entender el problema, elegir qué construir y evaluar resultados sigue requiriendo trabajo. El cuello de botella se desplaza.
    </box>
  </row>
  <divider color="subtle"/>
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="lg" padding={2} width="40px" align="center">
      **02**
    </box>
    <box flex="1" gap={1}>
      **Código plausible no es software correcto.**

      Que compile, ejecute y produzca una respuesta convincente no demuestra que resuelva nuestro problema. Necesitamos distinguir entre funcionamiento aparente, corrección y adecuación al propósito.
    </box>
  </row>
  <divider color="subtle"/>
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="lg" padding={2} width="40px" align="center">
      **03**
    </box>
    <box flex="1" gap={1}>
      **Saber qué queremos es más importante que saber pedirlo.**

      Antes del prompt necesitamos entender objetivos, supuestos, restricciones y criterios de aceptación. Una especificación útil no es necesariamente un documento extenso: puede empezar con ejemplos y propiedades.
    </box>
  </row>
  <divider color="subtle"/>
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="lg" padding={2} width="40px" align="center">
      **04**
    </box>
    <box flex="1" gap={1}>
      **La IA introduce variación: el mismo pedido no garantiza el mismo resultado.**

      Trabajamos con una herramienta probabilística. No alcanza con que una generación haya funcionado; debemos decidir qué variaciones toleramos y qué propiedades deben mantenerse.
    </box>
  </row>
  <divider color="subtle"/>
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="lg" padding={2} width="40px" align="center">
      **05**
    </box>
    <box flex="1" gap={1}>
      **El método científico nos enseña a trabajar con incertidumbre.**

      Formular hipótesis, diseñar experimentos, comparar contra referencias y tratar de refutar nuestras propias conclusiones. Podemos trasladar estas prácticas a nuestro proceso de desarrollo.
    </box>
  </row>
  <divider color="subtle"/>
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="lg" padding={2} width="40px" align="center">
      **06**
    </box>
    <box flex="1" gap={1}>
      **Los tests son una especificación ejecutable, no una garantía absoluta.**

      Nos ayudan a comunicar comportamientos esperados y detectar regresiones. Pero también debemos cuestionar los tests generados: pueden confirmar supuestos equivocados o reproducir errores de la implementación.
    </box>
  </row>
  <divider color="subtle"/>
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="lg" padding={2} width="40px" align="center">
      **07**
    </box>
    <box flex="1" gap={1}>
      **Sin reproducibilidad, no podemos investigar bien los errores.**

      Registrar datos, parámetros, dependencias, versiones y resultados nos permite comparar ejecuciones y entender qué cambió. La trazabilidad importa tanto como el resultado final.
    </box>
  </row>
  <divider color="subtle"/>
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="lg" padding={2} width="40px" align="center">
      **08**
    </box>
    <box flex="1" gap={1}>
      **El buen diseño se revela cuando necesitamos cambiar algo.**

      La IA facilita crear un primer prototipo, pero puede producir acoplamientos y dependencias difíciles de modificar. Las abstracciones, la composición y los límites entre componentes siguen teniendo valor.
    </box>
  </row>
  <divider color="subtle"/>
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="lg" padding={2} width="40px" align="center">
      **09**
    </box>
    <box flex="1" gap={1}>
      **La variación no es solamente un problema: también es una herramienta de exploración.**

      Podemos generar soluciones alternativas, contrastar diseños, experimentar y aprender más rápido. La diferencia está en comparar alternativas con criterios explícitos, en lugar de aceptar la primera.
    </box>
  </row>
  <divider color="subtle"/>
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="lg" padding={2} width="40px" align="center">
      **10**
    </box>
    <box flex="1" gap={1}>
      **Después del Chatbon, aprender a evaluar es tan importante como aprender a implementar.**

      Modelar problemas, entender fundamentos, diseñar experimentos, reconocer riesgos y evaluar compromisos son capacidades que nos permiten aprovechar la generación sin depender ciegamente de ella.
    </box>
  </row>
</box>

## El arco narrativo

Agruparía las diez ideas en cuatro movimientos:

<box border radius="xl" padding={3} gap={3}>
  <box gap={1}>
    <row align="center" justify="between">
      **Acto I — ¿Qué cambió?**
      <text color="secondary" size="xs" tabularNums>4 min</text>
    </row>
    <box background="surface-tertiary" height="6px" radius="full" width="16%"/>
    <text size="sm" color="secondary">Ideas 1–2 · Del costo de escribir código al problema de confiar en él.</text>
  </box>
  <box gap={1}>
    <row align="center" justify="between">
      **Acto II — ¿Cómo trabajamos ahora?**
      <text color="secondary" size="xs" tabularNums>12 min</text>
    </row>
    <box background="surface-tertiary" height="6px" radius="full" width="48%"/>
    <text size="sm" color="secondary">Ideas 3–7 · Intención, incertidumbre, experimentación, tests y reproducibilidad.</text>
  </box>
  <box gap={1}>
    <row align="center" justify="between">
      **Acto III — ¿Qué oportunidades aparecen?**
      <text color="secondary" size="xs" tabularNums>6 min</text>
    </row>
    <box background="surface-tertiary" height="6px" radius="full" width="24%"/>
    <text size="sm" color="secondary">Ideas 8–9 · Diseñar para evolucionar y explorar alternativas.</text>
  </box>
  <box gap={1}>
    <row align="center" justify="between">
      **Acto IV — ¿Qué vale la pena aprender?**
      <text color="secondary" size="xs" tabularNums>3 min</text>
    </row>
    <box background="surface-tertiary" height="6px" radius="full" width="12%"/>
    <text size="sm" color="secondary">Idea 10 · Síntesis y cierre.</text>
  </box>
</box>

## Una decisión conceptual importante

Hay tres posibles tesis que atraviesan esta charla:

{@body const theses = [
{title:"De generar código a generar evidencia",desc:"El foco está en cómo sabemos que una solución funciona y merece nuestra confianza."},
{title:"La IA cambia qué vale la pena aprender",desc:"El foco está en las capacidades que siguen siendo valiosas para estudiantes y profesionales."},
{title:"Del determinismo a la experimentación",desc:"El foco está en cómo aprovechar una herramienta probabilística mediante prácticas científicas."}
]}
{@body const [thesis,setThesis] = DIL.useState("1")}
<box gap={2}>
  <radio-group direction="col" value={thesis} onChange={setThesis}>
    {#each theses as t,i}
      <radio value={String(i)} key={i}>
        <box gap={1}>
          **{t.title}**
          <text size="sm" color="secondary">{t.desc}</text>
        </box>
      </radio>
    {/each}
  </radio-group>
  <button block variant="outline" onClick={()=>GenUI.issueNewTurn("Continuemos estructurando After Chatbon con la tesis central: "+theses[Number(thesis)].title+". Quiero revisar críticamente las 10 ideas, sus redundancias y construir una narrativa coherente para 25 minutos.")}>Desarrollar esta tesis <icon name="arrow-right" inline/></button>
</box>

Mi preferencia inicial es la segunda: **«La IA cambia qué vale la pena aprender»**, porque coincide mejor con el título, el abstract y la audiencia prevista. La primera sería el argumento técnico central y la tercera la idea novedosa que distingue la charla de una presentación genérica sobre buenas prácticas.

Un desafío para la próxima iteración: las ideas 3 a 7 corren el riesgo de sonar a una lista de recomendaciones. Necesitamos un ejemplo que las conecte y muestre por qué cada práctica se vuelve necesaria a medida que extendemos un programa.

## User

La premisa va a ser que practicas de autodidacta y como crear ambientes en los que pidamos experimentar sin tener miedo a rokper las cosas. Ademas de pensar en comi resolver provlemas y no solo pensar en la produccion comercial para hacer dinero

## Assistant

Esto cambia bastante la tesis de *After Chatbon*. La charla deja de ser principalmente sobre **cómo desarrollar buen software con IA** y pasa a ser sobre **cómo aprender, explorar y resolver problemas en un mundo donde podemos generar software fácilmente**.

Y me parece importante no convertirla en otra charla sobre productividad.

# After Chatbon
## Aprender, experimentar y construir después de los chatbots

**Premisa central:**

> La IA nos permite construir cosas que antes estaban fuera de nuestro alcance. Pero su mayor oportunidad quizás no sea producir más rápido, sino aprender más, experimentar libremente y animarnos a resolver problemas que antes ni siquiera intentábamos abordar.

Hay tres pilares que deberían atravesar toda la presentación:

<box gap={3}>
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="lg" size="48px" align="center" justify="center">
      <icon name="book-open" size="xl"/>
    </box>
    <box flex="1" gap={1}>
      **Aprender como autodidacta**

      Cultivar curiosidad, formular preguntas, buscar fundamentos, contrastar explicaciones y aprender haciendo, sin depender de un programa formal.
    </box>
  </row>
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="lg" size="48px" align="center" justify="center">
      <icon name="flask-conical" size="xl"/>
    </box>
    <box flex="1" gap={1}>
      **Crear ambientes donde equivocarse sea barato**

      Poder romper, modificar, observar, comparar y recomenzar. Diseñar herramientas y espacios que favorezcan la experimentación, no solamente la entrega de productos terminados.
    </box>
  </row>
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="lg" size="48px" align="center" justify="center">
      <icon name="lightbulb" size="xl"/>
    </box>
    <box flex="1" gap={1}>
      **Resolver problemas por curiosidad y necesidad**

      No todo proyecto tiene que convertirse en una startup, un SaaS o una fuente de ingresos. También construimos para comprender el mundo, ayudar a otros, jugar, investigar o satisfacer necesidades personales.
    </box>
  </row>
</box>

## Las 10 ideas, reformuladas

| # | Idea | Mensaje |
|---|---|---|
| 1 | **Programar nunca fue solamente escribir código** | Es una manera de pensar, explorar y entender problemas. |
| 2 | **La IA reduce el costo de intentar** | Podemos experimentar con ideas que antes descartábamos por dificultad, tiempo o falta de conocimientos técnicos. |
| 3 | **Aprender no es acumular respuestas** | El autodidacta aprende a formular preguntas, reconocer lo que no entiende y verificar explicaciones. |
| 4 | **La curiosidad necesita espacio** | No tenemos que justificar cada experimento mediante productividad, monetización o utilidad inmediata. |
| 5 | **Romper cosas es parte de aprender** | Los errores son información, siempre que podamos observarlos, comprenderlos y recuperarnos. |
| 6 | **Tenemos que construir laboratorios personales** | Entornos aislados, reversibles, reproducibles y accesibles donde experimentar sin consecuencias costosas. |
| 7 | **No delegar nuestra comprensión** | La IA puede implementar y explicar, pero debemos desarrollar criterio propio mediante la práctica. |
| 8 | **La variación es una oportunidad para descubrir** | Distintas respuestas de la IA nos permiten comparar caminos, descubrir supuestos y generar experimentos. |
| 9 | **Construir también es una forma de pensar** | Un programa puede ser un modelo, un experimento, una pregunta ejecutable o una herramienta para explorar hipótesis. |
| 10 | **El futuro no consiste solamente en producir más** | Consiste también en ampliar quiénes pueden crear, qué problemas pueden abordar y cuánto pueden aprender. |

## Una narrativa para 25 minutos

<box gap={3}>
  <row align="center" justify="between">
    **Acto I — Recuperar la curiosidad**
    <text color="secondary" tabularNums>5 min</text>
  </row>
  ¿Por qué programamos? ¿Para fabricar productos o también para entender cosas? ¿Qué cambia cuando la IA baja el costo de crear?

  <divider color="subtle"/>
  <row align="center" justify="between">
    **Acto II — Aprender a aprender**
    <text color="secondary" tabularNums>6 min</text>
  </row>
  Prácticas del autodidacta: descomponer problemas, formular hipótesis, consultar fuentes, contrastar respuestas, experimentar y registrar descubrimientos.

  <divider color="subtle"/>
  <row align="center" justify="between">
    **Acto III — Construir un laboratorio donde podamos romper cosas**
    <text color="secondary" tabularNums>9 min</text>
  </row>
  La parte más concreta de la charla. Mostrar cómo diseñar un ambiente con herramientas de IA, experimentos pequeños, control de versiones, tests, reproducibilidad y la posibilidad de volver atrás.

  No presentar estas prácticas como obligaciones burocráticas de ingeniería, sino como **mecanismos que nos dan libertad para explorar**.

  <divider color="subtle"/>
  <row align="center" justify="between">
    **Acto IV — ¿Qué vale la pena construir?**
    <text color="secondary" tabularNums>5 min</text>
  </row>
  Problemas cotidianos, científicos, comunitarios y personales. La posibilidad de crear herramientas para nosotros y otros, incluso cuando no existe un mercado dispuesto a pagarlas.

  Cerrar con una invitación a experimentar.

</box>

## Una inversión importante del mensaje tradicional

En muchas charlas de IA la secuencia es:

<box border radius="lg" padding={3} gap={2} align="center">
  <text color="secondary" weight="medium" size="xs">ENFOQUE DE PRODUCTIVIDAD</text>
  <row justify="center" align="center" gap={2} wrap="wrap">
    <text weight="medium">Idea</text>
    <icon name="arrow-right" color="tertiary"/>
    <text weight="medium">IA</text>
    <icon name="arrow-right" color="tertiary"/>
    <text weight="medium">Producto</text>
    <icon name="arrow-right" color="tertiary"/>
    <text weight="medium">Valor comercial</text>
  </row>
  <divider/>
  <text color="secondary" weight="medium" size="xs">PROPUESTA DE AFTER CHATBON</text>
  <svg viewBox="0 0 320 160" width="100%" xmlns="http://www.w3.org/2000/svg">
    {#each [{x:160,y:22,t:"Curiosidad"},{x:270,y:78,t:"Experimentar"},{x:160,y:136,t:"Comprender"},{x:50,y:78,t:"Construir"}] as n}
      <rect x={n.x-48} y={n.y-17} width="96" height="34" rx="8" fill="none" stroke="currentColor" strokeOpacity=".45"/>
      <text x={n.x} y={n.y+4} textAnchor="middle" fill="currentColor" fontSize="11">{n.t}</text>
    {/each}
    <g fill="none" stroke="#2D9B92" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <path d="M210 25 Q266 30 269 56"/>
      <path d="M264 50 L269 57 L274 50"/>
      <path d="M269 100 Q264 127 211 133"/>
      <path d="M216 126 L210 133 L219 137"/>
      <path d="M110 135 Q54 131 51 101"/>
      <path d="M46 108 L51 100 L56 107"/>
      <path d="M51 58 Q57 30 109 26"/>
      <path d="M101 21 L110 26 L102 32"/>
    </g>
    <text x="160" y="82" textAnchor="middle" fill="currentColor" fontSize="11" fontWeight="600">IA como</text>
    <text x="160" y="96" textAnchor="middle" fill="currentColor" fontSize="11" fontWeight="600">herramienta</text>
  </svg>
  <caption textAlign="center">Un ciclo de aprendizaje que puede terminar en un producto, pero no necesita hacerlo.</caption>
</box>

La ingeniería no desaparece de esta historia: cambia su función. Git, tests, separación de componentes y reproducibilidad ya no son solamente técnicas para entregar software confiable. También son **herramientas para reducir el costo de equivocarnos**.

Y creo que ahí está la idea más potente de la charla:

**No necesitamos aprender a no romper las cosas. Necesitamos aprender a construir espacios donde romperlas nos ayude a entenderlas.**

Eso puede convertirse en el hilo conductor de toda *After Chatbon*. En la siguiente iteración convendría depurar estas diez ideas, porque algunas se superponen, y elegir una experiencia concreta que podamos mostrar durante la charla en lugar de explicarlas todas de manera abstracta.

## User

Varias cosas para pensar: como simplificar los procesos, como entender sistemas complejos y validarlos, ayudar a que ocurran las cisas, burocracia es la forma para que las decisiones las timen a quien no les interesa el problema, como eliminamos eso o reducimos

## Assistant

Creo que estas ideas permiten encontrar una tesis más interesante para *After Chatbon*: **no se trata solamente de aprender a programar con IA, sino de recuperar nuestra capacidad de entender, transformar y actuar sobre los sistemas que nos rodean.**

Eso conecta el autodidactismo, la experimentación, la ingeniería, la resolución de problemas y la reducción de burocracia.

## 1. Una nueva premisa

> Cuando construir herramientas se vuelve más barato, podemos dedicar más esfuerzo a entender los problemas, experimentar con soluciones y eliminar las barreras que impiden llevarlas a la práctica.

Pero hay una distinción importante:

**Hacer más rápido lo que hacemos hoy no es necesariamente mejorar las cosas.**

Automatizar un proceso burocrático puede simplemente producir burocracia más rápido. La oportunidad está en cuestionar por qué existe cada paso, qué decisión representa y si realmente aporta valor.

## 2. Cinco ideas que incorporaría

<box gap={3}>
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="lg" padding={2}>
      <icon name="scissors" size="lg"/>
    </box>
    <box flex="1" gap={1}>
      **Simplificar antes de automatizar**

      No necesitamos convertir cada formulario en un chatbot. Quizás el formulario no debería existir, o quizás cinco autorizaciones pueden reemplazarse por una decisión verificable.
    </box>
  </row>
  <divider color="subtle"/>
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="lg" padding={2}>
      <icon name="network" size="lg"/>
    </box>
    <box flex="1" gap={1}>
      **Aprender a entender sistemas complejos**

      Un problema no existe aisladamente. Hay actores, reglas, dependencias, información incompleta e incentivos. La IA puede ayudarnos a construir modelos para pensar sobre esas relaciones, no solamente generar soluciones.
    </box>
  </row>
  <divider color="subtle"/>
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="lg" padding={2}>
      <icon name="flask-conical" size="lg"/>
    </box>
    <box flex="1" gap={1}>
      **Experimentar con los sistemas antes de modificarlos**

      Simular escenarios, buscar contraejemplos y probar hipótesis en ambientes seguros. Podemos equivocarnos muchas veces en un modelo para reducir las consecuencias de equivocarnos en la realidad.
    </box>
  </row>
  <divider color="subtle"/>
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="lg" padding={2}>
      <icon name="users" size="lg"/>
    </box>
    <box flex="1" gap={1}>
      **Acercar las decisiones a quienes entienden los problemas**

      La burocracia puede separar a quienes experimentan un problema de quienes tienen autoridad para resolverlo. Necesitamos mecanismos que permitan actuar localmente sin perder responsabilidad, coordinación ni garantías.
    </box>
  </row>
  <divider color="subtle"/>
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="lg" padding={2}>
      <icon name="rocket" size="lg"/>
    </box>
    <box flex="1" gap={1}>
      **Ayudar a que las cosas ocurran**

      El valor no está necesariamente en el software producido. Puede estar en que alguien consiga realizar un experimento, organizar una actividad, resolver una necesidad comunitaria o superar una barrera que antes le parecía imposible.
    </box>
  </row>
</box>

## 3. La burocracia como problema de diseño

Tu formulación es provocadora:

> La burocracia es una forma de hacer que las decisiones las tome gente a la que no le interesa el problema.

Creo que funciona como provocación para la charla, pero la afinaría.

No toda burocracia nace del desinterés. Algunas reglas protegen derechos, garantizan imparcialidad, distribuyen responsabilidades o evitan decisiones arbitrarias. El problema aparece cuando **el procedimiento termina teniendo más autoridad que el propósito que debía cumplir**.

<box border radius="lg" padding={3} gap={2}>
  <text color="secondary" weight="medium" size="xs">SISTEMA BUROCRÁTICO DISFUNCIONAL</text>
  <box background="surface-secondary" padding={3} radius="md" align="center" gap={2}>
    **Persona con un problema**
    <icon name="arrow-down"/>
    **Procedimientos, intermediarios, autorizaciones**
    <icon name="arrow-down"/>
    **Alguien distante decide**
  </box>
  <divider color="subtle"/>
  <text color="secondary" weight="medium" size="xs">SISTEMA ORIENTADO A RESOLVER PROBLEMAS</text>
  <box background="surface-secondary" padding={3} radius="md" align="center" gap={2}>
    **Persona con un problema**
    <icon name="arrow-down"/>
    **Herramientas para comprender, experimentar y validar**
    <icon name="arrow-down"/>
    **Decisión cercana al problema, con garantías y responsabilidad**
  </box>
</box>

Un principio interesante podría ser:

**Cada restricción debería poder explicar qué protege; cada paso debería poder justificar por qué es necesario.**

Esto nos da un criterio concreto para usar IA: identificar dependencias innecesarias, modelar procesos, verificar restricciones y facilitar decisiones. No sustituir automáticamente a las personas.

## 4. Cómo quedarían las diez ideas

Propongo reformular la estructura, priorizando el argumento por encima de las herramientas:

| # | Idea fundamental |
|---|---|
| 1 | La tecnología debería ampliar nuestra capacidad de actuar, no solamente nuestra productividad. |
| 2 | Aprender a aprender es más valioso que memorizar herramientas. |
| 3 | La curiosidad y los problemas reales son motores del aprendizaje autodidacta. |
| 4 | Necesitamos ambientes donde experimentar, equivocarnos y recomenzar sea barato. |
| 5 | Comprender un sistema requiere modelar sus relaciones, restricciones y comportamientos. |
| 6 | Para confiar en nuestras soluciones necesitamos intentar refutarlas, no solamente demostrar que funcionan una vez. |
| 7 | Simplificar un problema puede tener mucho más valor que producir una implementación sofisticada. |
| 8 | Hay que cuestionar los procesos que alejan las decisiones de quienes conocen el problema. |
| 9 | La IA puede ayudarnos a explorar alternativas, construir modelos y convertir ideas en acciones. |
| 10 | No todo lo valioso necesita convertirse en un producto comercial. |

## 5. Una narrativa más unificada para 25 minutos

Esta estructura permite una progresión natural:

<box gap={3}>
  <row align="start" gap={3}>
    <title size="xl" color="secondary" width="50px" tabularNums>5'</title>
    <box flex="1" gap={1}>
      **¿Para qué queremos construir cosas?**

      De la productividad y el software comercial a la curiosidad, el aprendizaje y la capacidad de resolver problemas.
    </box>
  </row>
  <divider color="subtle"/>
  <row align="start" gap={3}>
    <title size="xl" color="secondary" width="50px" tabularNums>6'</title>
    <box flex="1" gap={1}>
      **Aprender experimentando**

      Autodidactismo, preguntas, hipótesis, errores, herramientas y laboratorios personales.
    </box>
  </row>
  <divider color="subtle"/>
  <row align="start" gap={3}>
    <title size="xl" color="secondary" width="50px" tabularNums>8'</title>
    <box flex="1" gap={1}>
      **Entender para simplificar**

      Modelar sistemas, validar comportamientos, reconocer complejidad accidental y descubrir procesos innecesarios.
    </box>
  </row>
  <divider color="subtle"/>
  <row align="start" gap={3}>
    <title size="xl" color="secondary" width="50px" tabularNums>6'</title>
    <box flex="1" gap={1}>
      **De comprender a hacer que las cosas ocurran**

      Autonomía, colaboración, decisiones cercanas al problema y tecnología orientada a ampliar posibilidades.
    </box>
  </row>
</box>

## 6. El riesgo que veo

Estamos ampliando mucho el alcance de la charla: educación autodidacta, epistemología, ingeniería de software, sistemas complejos, burocracia, organización institucional e IA.

Todos estos temas pueden relacionarse, pero **no podemos enseñarlos en 25 minutos**. Necesitamos una idea que los una y un ejemplo que los haga tangibles.

Mi propuesta es convertir la charla en una defensa de la **capacidad de intervención**:

- **Comprender:** aprender a observar, preguntar y modelar.
- **Experimentar:** construir entornos seguros para probar hipótesis.
- **Transformar:** simplificar los procesos y modificar lo que no funciona.
- **Actuar:** permitir que las personas resuelvan problemas sin depender innecesariamente de intermediarios.

La IA aparece como un instrumento que reduce barreras para recorrer ese ciclo, no como protagonista.

Y cerraría con una pregunta que me parece más poderosa que «¿qué deberíamos aprender a programar después de ChatGPT?»:

**¿Qué problemas empezaríamos a resolver si tuviéramos las herramientas, el conocimiento y la libertad de experimentar sin miedo a romper las cosas?**

Esa pregunta también nos permite recuperar el propósito original de *After Chatbon*: qué vale la pena aprender cuando podemos generar tanto código, pero todavía nos cuesta entender, decidir y hacer que las cosas ocurran.

## User

ok, cómo podemos ordenarla para que sea valiosa en el contexto del pyday hurlingham 2026

## Assistant

{"query":"Find prior conversations or decisions about PyDay Hurlingham 2026: event context, intended audience, conference theme or organizer expectations, talk format and positioning, other talks or content constraints. I need this to order the user's 25-minute 'After Chatbon' presentation so it is specifically valuable and appropriately differentiated for that event. Return only directly relevant details and distinguish explicit facts from assumptions."}

## Assistant

Creo que para **PyDay Hurlingham 2026** tenemos que hacer una elección importante: no presentar *After Chatbon* como una charla genérica sobre IA, ni como una clase de ingeniería de software, ni como una reflexión abstracta sobre la burocracia.

Tiene que ser una charla que deje a los asistentes con ganas de salir a construir algo, experimentar y aprender de una manera diferente.

El valor para esta audiencia está en conectar tres mundos:

1. **La cultura de Python:** aprender haciendo, automatizar, explorar, compartir herramientas y resolver problemas.
2. **La cultura científica:** curiosidad, hipótesis, experimentación, modelos, evidencia y reproducibilidad.
3. **La cultura de construir:** autonomía, colaboración, proyectos personales y capacidad de transformar situaciones concretas.

El público previsto incluye estudiantes que están decidiendo qué aprender y profesionales que quieren revisar sus prácticas. Eso nos permite hablar a distintos niveles sin asumir que todos tienen experiencia avanzada. <FileCite ref_id="turn0file0" line_range_start={63} line_range_end={66}/>

Mi propuesta es que la charla tenga una progresión muy clara:

**De consumidores de tecnología a personas capaces de comprender, experimentar y transformar sistemas.**

Hay un detalle del programa que me parece especialmente importante para tomar esta decisión: tu charla está programada el sábado 14 de noviembre, de 12:30 a 13:00, justo antes del almuerzo. Antes habrán presentado aplicaciones de Python para música, computación cuántica, robótica autónoma y adaptación de GPS a teléfonos antiguos. Por la tarde habrá otra charla sobre curiosidad y qué no conviene delegar a la IA. <Cite refs={["turn893629search0"]}/>

Eso nos da una oportunidad bastante buena: **mostrar qué podemos hacer nosotros con estas nuevas capacidades, más allá de las aplicaciones técnicas y de la productividad.**

# 1. Posicionamiento para PyDay

Yo definiría la charla así:

<box border radius="lg" padding={3} gap={2}>
  <title size="2xl">After Chatbon</title>
  <title size="lg" weight="medium" color="secondary">Aprender, experimentar y hacer que las cosas ocurran.</title>
  Cuando construir software se vuelve más accesible, podemos dedicar más tiempo a entender problemas, experimentar con soluciones y transformar los sistemas que nos rodean.
</box>

La pregunta que debería responder la charla:

**¿Qué podríamos hacer si tuviéramos la capacidad de construir nuestras propias herramientas para entender y resolver los problemas que nos importan?**

Esta pregunta es relevante tanto para alguien que está aprendiendo Python como para alguien que lleva veinte años programando.

# 2. Qué valor debería llevarse cada asistente

No quiero que salgan pensando simplemente que tienen que usar más IA.

Quiero que salgan con cuatro capacidades que puedan empezar a practicar.

<box gap={3}>
  <row align="start" gap={3}>
    <title color="secondary" size="2xl">01</title>
    <box flex="1" gap={1}>
      **Aprender cualquier cosa**

      No esperar a saber suficiente para empezar. Aprender a investigar, formular preguntas, construir modelos y adquirir conocimientos a través de experimentos.
    </box>
  </row>
  <row align="start" gap={3}>
    <title color="secondary" size="2xl">02</title>
    <box flex="1" gap={1}>
      **Entender antes de automatizar**

      Reconocer que los problemas tienen estructuras, actores, restricciones y relaciones. Aprender a simplificar antes de construir soluciones.
    </box>
  </row>
  <row align="start" gap={3}>
    <title color="secondary" size="2xl">03</title>
    <box flex="1" gap={1}>
      **Experimentar sin miedo**

      Construir pequeños laboratorios donde podamos probar ideas, romper implementaciones, observar resultados y volver atrás.
    </box>
  </row>
  <row align="start" gap={3}>
    <title color="secondary" size="2xl">04</title>
    <box flex="1" gap={1}>
      **Convertir ideas en acciones**

      No esperar a tener una empresa, presupuesto, equipo o permiso para empezar. Construir herramientas que resuelvan problemas reales, aunque sean pequeños.
    </box>
  </row>
</box>

# 3. El orden narrativo que recomiendo

No empezaría explicando qué es el autodidactismo ni enumerando buenas prácticas. Empezaría con una provocación y construiría las ideas a partir de ella.

<box gap={3}>
  <box gap={1}>
    <row align="center" justify="between">
      **Acto I. Tenemos nuevas posibilidades**
      <badge color="info">3 min</badge>
    </row>
    <title size="xl">¿Qué harías si construir algo fuera mucho más barato?</title>
    - Antes necesitábamos conocimientos especializados, mucho tiempo y recursos para intentar determinadas ideas.
    - Ahora podemos generar implementaciones, explorar alternativas y construir prototipos rápidamente.
    - Pero generar código no significa entender el problema ni resolverlo.

    **Mensaje:** la IA reduce el costo de intentar. ¿Qué hacemos con esa oportunidad?
  </box>
  <divider color="subtle"/>
  <box gap={1}>
    <row align="center" justify="between">
      **Acto II. Aprender a aprender**
      <badge color="info">5 min</badge>
    </row>
    <title size="xl">No necesitamos saberlo todo para empezar.</title>
    - El autodidacta aprende investigando, preguntando y experimentando.
    - La programación es una herramienta para pensar, no solamente para producir aplicaciones.
    - Podemos utilizar la IA como interlocutor, asistente de investigación y generador de alternativas.
    - Pero tenemos que desarrollar criterio propio.

    **Mensaje:** no deleguemos nuestro aprendizaje; usemos las herramientas para aprender más.
  </box>
  <divider color="subtle"/>
  <box gap={1}>
    <row align="center" justify="between">
      **Acto III. Entender y simplificar**
      <badge color="info">6 min</badge>
    </row>
    <title size="xl">El problema casi nunca es solamente el código.</title>
    - Los sistemas tienen actores, dependencias, reglas, incentivos y restricciones.
    - Aprender a modelarlos nos permite encontrar dónde está realmente el problema.
    - Antes de automatizar un proceso, preguntarnos por qué existe.
    - Distinguir las restricciones necesarias de la complejidad accidental.
    - Acercar las decisiones a quienes entienden y viven el problema.

    **Mensaje:** muchas veces la mejor solución es eliminar pasos, no escribir más código.
  </box>
  <divider color="subtle"/>
  <box gap={1}>
    <row align="center" justify="between">
      **Acto IV. Construir laboratorios**
      <badge color="info">7 min</badge>
    </row>
    <title size="xl">Tenemos que poder romper cosas.</title>
    - Probar hipótesis pequeñas.
    - Crear ambientes aislados y reversibles.
    - Usar Git, tests y reproducibilidad como mecanismos de libertad.
    - Comparar diferentes implementaciones.
    - Buscar activamente errores y contraejemplos.
    - Validar contra la realidad, no solamente contra el resultado esperado por el código.

    **Mensaje:** la ingeniería no debería impedir experimentar; debería hacer que experimentar sea seguro y barato.
  </box>
  <divider color="subtle"/>
  <box gap={1}>
    <row align="center" justify="between">
      **Acto V. Hacer que las cosas ocurran**
      <badge color="info">4 min</badge>
    </row>
    <title size="xl">No todo tiene que ser un producto.</title>
    - Podemos construir para resolver problemas personales.
    - Podemos ayudar a nuestra comunidad.
    - Podemos facilitar investigaciones y experimentos.
    - Podemos eliminar fricciones de organizaciones y procesos.
    - Podemos compartir herramientas sin necesitar un modelo de negocio.

    **Mensaje:** la tecnología también sirve para ampliar nuestra autonomía y capacidad de actuar.
  </box>
</box>

<text color="secondary" size="xs">Total: 25 minutos de exposición. El cronograma reserva 30 minutos, por lo que quedan 5 minutos para preguntas o transición.</text>

# 4. Necesitamos un ejemplo que conecte todo

Esta es probablemente la decisión más importante para que la charla funcione.

No haría diez diapositivas con diez conceptos independientes. Elegiría un problema concreto y lo utilizaría como hilo conductor.

Una posibilidad interesante es:

**Organizar una actividad comunitaria gratuita.**

<AsyncImageGroup query={["community volunteer workshop people organizing event around table","simple event registration spreadsheet laptop","community makerspace people collaborating building project"]} aspectRatio="5:4" layout="carousel"/>

Imaginemos que un grupo quiere organizar talleres gratuitos, pero tiene dificultades con inscripciones, cupos, cancelaciones y comunicaciones.

Podemos recorrer todo el argumento:

| Pregunta | Lo que aprendemos |
|---|---|
| ¿Qué queremos conseguir? | Identificar el problema real. |
| ¿Cómo funciona actualmente? | Modelar el sistema y sus actores. |
| ¿Qué pasos son innecesarios? | Simplificar antes de automatizar. |
| ¿Podemos construir algo? | Utilizar Python y la IA para prototipar. |
| ¿Cómo sabemos que funciona? | Tests, casos límite y validación. |
| ¿Qué pasa si rompemos algo? | Ambientes reversibles y experimentación. |
| ¿Para qué sirve? | Ayudar a que una iniciativa ocurra. |

No necesitamos vender nada. No necesitamos crear una startup. La herramienta puede ser pequeña y descartable.

Este ejemplo tiene una ventaja adicional: es fácil de entender para alguien que está empezando a programar y suficientemente rico para discutir diseño, sistemas, validación y organización.

# 5. Qué evitaría en esta charla

Hay algunas trampas que conviene evitar, especialmente considerando el resto del programa.

| Evitar | Reemplazar por |
|---|---|
| Una introducción general a los LLMs | Qué nuevas posibilidades habilitan. |
| Una lista de herramientas de IA | Un método para aprender y experimentar. |
| Una clase sobre testing | Cómo verificar nuestras hipótesis. |
| Una defensa abstracta del software craftsmanship | Cómo el buen diseño permite experimentar. |
| Una crítica general a la burocracia | Cómo identificar y eliminar fricciones innecesarias. |
| Una charla sobre productividad | Una charla sobre autonomía y capacidad de resolver problemas. |
| Una discusión sobre qué no delegar a la IA | Cómo aprovecharla sin delegar nuestra comprensión. |

Este último punto también ayuda a diferenciarla de la charla de las 16:15, que explícitamente aborda curiosidad y qué no conviene delegar a la IA. <Cite refs={["turn893629search0"]}/>

# 6. Mi propuesta de estructura de diapositivas

Apuntaría a unas 12 diapositivas, con muy poco texto y una narrativa visual.

| # | Diapositiva | Función |
|---:|---|---|
| 1 | After Chatbon | Presentar la pregunta central. |
| 2 | ¿Qué harías si intentar fuera barato? | Provocar. |
| 3 | El código ya no es el cuello de botella | Presentar el cambio. |
| 4 | Aprender es experimentar | Autodidactismo. |
| 5 | Primero entendamos el problema | Modelado de sistemas. |
| 6 | ¿Podemos eliminar pasos? | Simplificación y burocracia. |
| 7 | Construyamos un laboratorio | Experimentación segura. |
| 8 | Hagamos algo que pueda romperse | Prototipos y reversibilidad. |
| 9 | ¿Cómo sabemos que funciona? | Validación y evidencia. |
| 10 | No todo necesita convertirse en un producto | Propósito y autonomía. |
| 11 | De la curiosidad a la acción | Síntesis del método. |
| 12 | ¿Qué vas a intentar? | Cierre. |

---

# 7. La idea que quiero preservar por encima de todas

Hay una frase que puede funcionar como columna vertebral de toda la charla:

<box background="surface" border radius="xl" padding={4} gap={3}>
  <title size="2xl" weight="medium">La tecnología debería permitirnos hacer más cosas, pero también debería permitirnos necesitar menos permiso para hacerlas.</title>
  <divider color="subtle"/>
  Aprender a entender problemas, construir herramientas, experimentar con seguridad y compartir soluciones nos da autonomía.
</box>

Esto conecta Python, software libre, ciencia, educación, IA y organización comunitaria sin reducirlos a productividad o rentabilidad.

Y tiene una relación muy natural con el espíritu de un PyDay: una comunidad que se reúne gratuitamente para compartir conocimiento, proyectos y posibilidades.

**Mi recomendación:** antes de escribir Markdown o diseñar las diapositivas, trabajaría el ejemplo conductor y los mensajes de apertura y cierre. Si esos tres elementos funcionan, el resto de la presentación debería resultar mucho más fácil de ordenar.

El siguiente paso sería construir el storyboard completo de las 12 diapositivas, con el mensaje que debe quedar en cada una y el ejemplo que la acompaña.

---

<text color="secondary" size="xs">Fuente de contexto: <Link ref="turn893629search0" title="Programa oficial PyDay Hurlingham 2026"/> · <Link ref="turn893629search3" title="Contexto institucional de UNAHUR y PyDay"/>.</text>

<SuggestAutomation label="Recordarme ensayar After Chatbon el 13 de noviembre"/>

## User

revisa el estilo de estas diapositivas para que creemos esta nueva charla

## Tool

[L1] <!-- .slide: id="titulo" -->

[L3] ## Software científico e IA: cómo usar LLMs sin romper todo

[L5] **PyDay La Plata**

[L7] **7 de Noviembre 2026**

[L9] [saxa.xyz/charla-scia](https://saxa.xyz/charla-scia)

---

[L13] <!-- .slide: data-transition="none" -->

[L15] ### Sasha

[L17] Consultor independiente

[L19] **[Phorma Scientific](https://phorma.sh)**

--

[L23] - Estudié Física en la UBA
[L24] - Trabajé como Desarrollador de Software en **JP Morgan**
[L25] - Trabajé como Lead Quant Developer en **Qontigo/Simcorp** *(Quantitative Pricing and Risk Analytics)*
[L26] - Trabajé como Líder Técnico en **Mercado Libre** *(IT Staff, Financial Planning & Analysis)*
[L27] - Trabajé como Senior AI Engineer en **AstraZeneca** *(R&D Oncology)*

[L29] NOTES:
[L30] Acá tengo que mencionar un par de cosas de que me interesa y que motiva esta charla

--

[L34] No me gusta programar,

[L36] me gusta resolver problemas.
[L37] <!-- .element: class="fragment" -->

--

[L41] Los generadores (probabilísticos) de texto¹ son una gran ayuda.

[L43] <div style="font-size: 0.55em;">¹ Grandes Modelos de Lenguaje o LLMs</div>

---

[L47] <!-- 3	Presentación del problema	3 min -->

[L49] El Software Científico y su desarrollo tiene características muy distintas a los de una aplicación
[L50] comercial.

[L52] <div class="fragment">
<ul>
[L54] <li>Dinámico</li>
[L55] <li>Repetitivo</li>
[L56] <li>Experimental</li>
</ul>
[L58] </div>

--

[L62] <!-- .slide: id="script-inicial" -->

```py
[L65] from math import cos, radians, sin
[L66] import matplotlib.pyplot as plt

[L68] velocidad = 10.0  # m/s
[L69] angulo = radians(45.0)
[L70] GRAVEDAD = 10.0  # m/s²

[L72] vx = velocidad * cos(angulo)
[L73] vy = velocidad * sin(angulo)
[L74] duracion = 2.0 * vy / GRAVEDAD
[L75] t = [duracion * i / 100.0 for i in range(101)]
[L76] x = [vx * instante for instante in t]
[L77] y = [vy * instante - GRAVEDAD * instante**2 / 2.0 for instante in t]

[L79] plt.plot(x, y)
[L80] plt.savefig("trayectoria.png")
```

[L83] <img class="fragment" src="./images/trayectoria.png">

--

[L87] ¿Cuáles son las prácticas de Ingeniería y Arquitectura de Software que podemos utilizar para mejorar nuestras herramientas?

--

[L91] ### Artesanía de Software

[L93] > Prácticas y metodologías para producir artefactos de mejor calidad.
[L94] <!-- .element: class="fragment" -->

[L96] NOTES:
[L97] Importante mencionar la escala del software.

[L99] En investigación no conocemos todo el problema al empezar: hacemos un script para
[L100] responder una pregunta, vemos el resultado y aparecen nuevas preguntas. Con IA ese
[L101] ciclo se acelera muchísimo. La pregunta para la audiencia: ¿el software está
[L102] evolucionando junto con nuestra comprensión del problema, o solo acumulamos código?

---

[L106] <!-- 4	IA como herramienta	3 min -->

[L108] Cuando trabajamos con madera:
[L109] <!-- .element: class="fragment" -->

[L111] <div class="fragment">
[L112] <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 1rem; align-items: center;">
[L113] <img src="./images/serrucho.jpg" style="width: 100%; height: auto;">
[L114] -> <img class="fragment" src="./images/sierra-circular.jpg" style="width: 100%; height: auto;">
[L115] </div>
[L116] </div>

[L118] Cuando trabajamos con software:
[L119] <!-- .element: class="fragment" -->

[L121] > Escribir código -> Generar código
[L122] <!-- .element: class="fragment" -->

[L124] NOTES:
[L125] Necesitamos mucho más control sobre lo que hacemos.

--

[L129] Lo que cambió es el sustrato sobre el que trabajamos:

[L131] <div class="fragment">
[L132] <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 1rem; align-items: center;">
[L133] <img src="./images/madera.jpg" style="width: 60%; height: 60%;">
->
[L135] <img class="fragment" src="./images/melamina.jpg" style="width: 60%; height: 60%;">
[L136] </div>
[L137] </div>
[L138] <!-- .element: class="fragment" -->

[L140] El sustrato es más uniforme, homogéneo, fácil de trabajar.
[L141] <!-- .element: class="fragment" -->

--

[L145] Al poder producir de manera probabilística el código, <span class="fragment">
[L146] necesitamos establecer protocolos</span><span class="fragment">, procedimientos que nos ayuden a
[L147] definir</span><span class="fragment">, elegir,</span><span class="fragment"> evaluar,</span><span class="fragment"> verificar lo que se produce.</span>

[L149] NOTES:
[L150] En esta charla vamos a hablar de Regla y Escuadra y no de Serrucho y Martillo
[L151] No se trata de producir más código, necesitamos producir cosas de mayor calidad.

--

[L155] El valor del código es despreciable, es como el plástico, es algo descartable.

[L157] Lo que tiene valor es lo que produce.
[L158] <!-- .element: class="fragment" -->

[L160] En vez de crear un montón de cosas, tenemos que enfocarnos en mejorar la calidad.
[L161] <!-- .element: class="fragment" -->

--

[L165] <h2 style="color: #e53935;">WARNING</h2>

[L167] Los proveedores de tokens quieren que utilicemos sus herramientas lo más que se pueda, están diseñadas para ser adictivas.  <!-- .element: class="fragment" -->

[L169] Piensen en los Chats en los mismos términos que Facebook, Instagram, TikTok, X/Twitter.... <!-- .element: class="fragment" -->

[L171] - ¿Cuántas horas al día lo utilizan? <!-- .element: class="fragment" -->
[L172] - ¿Cuántas menos interacciones con otros seres humanos tienen? <!-- .element: class="fragment" -->
[L173] - ¿Qué información le están entregando? <!-- .element: class="fragment" -->

---

[L177] <!-- 5	Fricción: serialización	3 min -->

[L179] ## Principios para describir un mejor software

--
[L182] Lo más importante es lograr un código bien modularizado, que nos permita
[L183] abstraer componentes.

[L185] <div class="fragment">
[L186] <img src="./images/flujo-serializacion.svg" class="light-theme-logo" style="width: 80%;">
[L187] <img src="./images/flujo-serializacion-dark.svg" class="dark-theme-logo" style="width: 80%;">
[L188] </div>

--

[L192] <!-- .slide: data-transition="none" -->

[L194] Lo más importante es lograr un código bien modularizado, que nos permita
[L195] abstraer componentes.


[L198] <div class="fragment">
[L199] <img src="./images/intercambio-componente.svg" class="light-theme-logo" style="width: 80%;">
[L200] <img src="./images/intercambio-componente-dark.svg" class="dark-theme-logo" style="width: 80%;">
[L201] </div>

[L203] intercambiar un componente sin romper nada  <!-- .element: class="fragment" -->

--

```py
[L208] from math import cos, radians, sin
[L209] import matplotlib.pyplot as plt

[L211] velocidad = 10.0  # m/s
[L212] angulo = radians(45.0)
[L213] GRAVEDAD = 10.0  # m/s²

[L215] vx = velocidad * cos(angulo)
[L216] vy = velocidad * sin(angulo)
[L217] duracion = 2.0 * vy / GRAVEDAD
[L218] t = [duracion * i / 100.0 for i in range(101)]
[L219] x = [vx * instante for instante in t]
[L220] y = [vy * instante - GRAVEDAD * instante**2 / 2.0 for instante in t]

[L222] plt.plot(x, y)
[L223] plt.savefig("trayectoria.png")
```

[L226] Paso 1: Necesitamos registrar los inputs y los outputs
[L227] <!-- .element: class="fragment" -->

--

```py
[L232] from math import cos, radians, sin
[L233] import matplotlib.pyplot as plt

[L235] velocidad = 10.0  # m/s
[L236] angulo = radians(45.0)
[L237] GRAVEDAD = 10.0  # m/s²

[L239] vx = velocidad * cos(angulo)
[L240] vy = velocidad * sin(angulo)
[L241] duracion = 2.0 * vy / GRAVEDAD
[L242] t = [duracion * i / 100.0 for i in range(101)]
[L243] x = [vx * instante for instante in t]
[L244] y = [vy * instante - GRAVEDAD * instante**2 / 2.0 for instante in t]

[L246] plt.plot(x, y)
[L247] plt.savefig("trayectoria.png")
```

--

[L252] <!-- .slide: data-transition="none" -->

```py
[L255] from math import cos, radians, sin
[L256] import matplotlib.pyplot as plt
```

```py
[L260] velocidad = 10.0  # m/s
[L261] angulo = radians(45.0)
[L262] GRAVEDAD = 10.0  # m/s²

[L264] vx = velocidad * cos(angulo)
[L265] vy = velocidad * sin(angulo)
[L266] duracion = 2.0 * vy / GRAVEDAD
[L267] t = [duracion * i / 100.0 for i in range(101)]
[L268] x = [vx * instante for instante in t]
[L269] y = [vy * instante - GRAVEDAD * instante**2 / 2.0 for instante in t]

[L271] plt.plot(x, y)
[L272] plt.savefig("trayectoria.png")
```

--

[L277] <!-- .slide: data-transition="none" -->

```py
[L280] velocidad = 10.0  # m/s
[L281] angulo = radians(45.0)
[L282] GRAVEDAD = 10.0  # m/s²

[L284] vx = velocidad * cos(angulo)
[L285] vy = velocidad * sin(angulo)
[L286] duracion = 2.0 * vy / GRAVEDAD
[L287] t = [duracion * i / 100.0 for i in range(101)]
[L288] x = [vx * instante for instante in t]
[L289] y = [vy * instante - GRAVEDAD * instante**2 / 2.0 for instante in t]

[L291] plt.plot(x, y)
[L292] plt.savefig("trayectoria.png")
```

--

[L297] <!-- .slide: data-transition="none" -->

```py
[L300] velocidad = 10.0  # m/s
[L301] angulo = radians(45.0)
[L302] GRAVEDAD = 10.0  # m/s²
```

```py
[L306] vx = velocidad * cos(angulo)
[L307] vy = velocidad * sin(angulo)
[L308] duracion = 2.0 * vy / GRAVEDAD
[L309] t = [duracion * i / 100.0 for i in range(101)]
[L310] x = [vx * instante for instante in t]
[L311] y = [vy * instante - GRAVEDAD * instante**2 / 2.0 for instante in t]

[L313] plt.plot(x, y)
[L314] plt.savefig("trayectoria.png")
```

--

[L319] <!-- .slide: data-transition="none" -->

```py
[L322] velocidad = 10.0  # m/s
[L323] angulo = radians(45.0)
[L324] GRAVEDAD = 10.0  # m/s²
```

```py
[L328] vx = velocidad * cos(angulo)
[L329] vy = velocidad * sin(angulo)
[L330] duracion = 2.0 * vy / GRAVEDAD
[L331] t = [duracion * i / 100.0 for i in range(101)]
[L332] x = [vx * instante for instante in t]
[L333] y = [vy * instante - GRAVEDAD * instante**2 / 2.0 for instante in t]
```

```py
[L337] plt.plot(x, y)
[L338] plt.savefig("trayectoria.png")
```

--

[L343] <!-- .slide: data-transition="none" -->

```py
[L346] velocidad = 10.0  # m/s
[L347] angulo = radians(45.0)
[L348] GRAVEDAD = 10.0  # m/s²
```

```py
[L352] vx = velocidad * cos(angulo)
[L353] vy = velocidad * sin(angulo)
[L354] duracion = 2.0 * vy / GRAVEDAD
[L355] t = [duracion * i / 100.0 for i in range(101)]
[L356] x = [vx * instante for instante in t]
[L357] y = [vy * instante - GRAVEDAD * instante**2 / 2.0 for instante in t]
```

```py
[L361] resultado = {"x":x, "y": y}
```

--

[L366] <!-- .slide: data-transition="none" -->

```py
[L369] parametros = {"velocidad": 10.0, "angulo": 45.0 }

[L371] velocidad = parametros["velocidad"]
[L372] angulo = parametros["angulo"]
[L373] GRAVEDAD = 10.0  # m/s²
```

```py

[L378] angulo_rad = radians(angulo)
[L379] vx = velocidad * cos(angulo_rad)
[L380] vy = velocidad * sin(angulo_rad)
[L381] duracion = 2.0 * vy / GRAVEDAD
[L382] t = [duracion * i / 100.0 for i in range(101)]
[L383] x = [vx * instante for instante in t]
[L384] y = [vy * instante - GRAVEDAD * instante**2 / 2.0 for instante in t]



```

```py
[L391] resultado = {"x":x, "y": y}
```

--

[L396] <!-- .slide: data-transition="none" -->

```py
[L399] parametros = {"velocidad": 10.0, "angulo": 45.0 }

[L401] velocidad = parametros["velocidad"]
[L402] angulo = parametros["angulo"]
[L403] GRAVEDAD = 10.0  # m/s²
```

```py

[L408] angulo_rad = radians(angulo)
[L409] vx = velocidad * cos(angulo_rad)
[L410] vy = velocidad * sin(angulo_rad)
[L411] duracion = 2.0 * vy / GRAVEDAD
[L412] t = [duracion * i / 100.0 for i in range(101)]
[L413] x = [vx * instante for instante in t]
[L414] y = [vy * instante - GRAVEDAD * instante**2 / 2.0 for instante in t]
[L415] resultado = {"x":x, "y": y}


```

```py

```

--

[L426] <!-- .slide: data-transition="none" -->

```py
[L429] parametros = {"velocidad": 10.0, "angulo": 45.0 }

[L431] velocidad = parametros["velocidad"]
[L432] angulo = parametros["angulo"]
[L433] GRAVEDAD = 10.0  # m/s²
```

```py

[L438]     angulo_rad = radians(angulo)
[L439]     vx = velocidad * cos(angulo_rad)
[L440]     vy = velocidad * sin(angulo_rad)
[L441]     duracion = 2.0 * vy / GRAVEDAD
[L442]     t = [duracion * i / 100.0 for i in range(101)]
[L443]     x = [vx * instante for instante in t]
[L444]     y = [vy * instante - GRAVEDAD * instante**2 / 2.0 for instante in t]
[L445]     resultado = {"x":x, "y": y}


```

```py

```

--

[L456] <!-- .slide: data-transition="none" -->


```py
[L460] parametros = {"velocidad": 10.0, "angulo": 45.0 }

[L462] velocidad = parametros["velocidad"]
[L463] angulo = parametros["angulo"]
[L464] GRAVEDAD = 10.0  # m/s²
```

```py
[L468] def simular(velocidad, angulo):
[L469]     angulo_rad = radians(angulo)
[L470]     vx = velocidad * cos(angulo_rad)
[L471]     vy = velocidad * sin(angulo_rad)
[L472]     duracion = 2.0 * vy / GRAVEDAD
[L473]     t = [duracion * i / 100.0 for i in range(101)]
[L474]     x = [vx * instante for instante in t]
[L475]     y = [vy * instante - GRAVEDAD * instante**2 / 2.0 for instante in t]
[L476]     resultado = {"x":x, "y": y}
[L477]     return resultado
```

```py

```

--
[L485] <!-- .slide: data-transition="none" -->


```py
[L489] parametros = {"velocidad": 10.0, "angulo": 45.0 }

[L491] velocidad = parametros["velocidad"]
[L492] angulo = parametros["angulo"]
[L493] GRAVEDAD = 10.0  # m/s²
```

```py
[L497] def simular(velocidad, angulo):
[L498]     angulo_rad = radians(angulo)
[L499]     vx = velocidad * cos(angulo_rad)
[L500]     vy = velocidad * sin(angulo_rad)
[L501]     duracion = 2.0 * vy / GRAVEDAD
[L502]     t = [duracion * i / 100.0 for i in range(101)]
[L503]     x = [vx * instante for instante in t]
[L504]     y = [vy * instante - GRAVEDAD * instante**2 / 2.0 for instante in t]
[L505]     resultado = {"x":x, "y": y}
[L506]     return resultado
```

```py

```

--

[L515] <!-- .slide: data-transition="none" -->

```py
[L518] parametros = {"velocidad": 10.0, "angulo": 45.0 }

[L520] velocidad = parametros["velocidad"]
[L521] angulo = parametros["angulo"]
[L522] GRAVEDAD = 10.0  # m/s²
```

```py
[L526] def simular(velocidad, angulo):
    ...
```

```py

```

--

[L536] <!-- .slide: data-transition="none" -->

```py
[L539] parametros = {"velocidad": 10.0, "angulo": 45.0 }

[L541] velocidad = parametros["velocidad"]
[L542] angulo = parametros["angulo"]
[L543] GRAVEDAD = 10.0  # m/s²
```

```py
[L547] def simular(velocidad, angulo):
    ...
```

```py
[L552] resultado = simular(**parametros)
```

--

[L557] <!-- .slide: data-transition="none" -->

```py
[L560] parametros = {"velocidad": 10.0, "angulo": 45.0 }

[L562] GRAVEDAD = 10.0  # m/s²
```

```py
[L566] resultado = simular(**parametros)
```

```py
[L570] experimento = {"parametros":parametros, "resultado":resultado }
```

--

[L575] <!-- .slide: data-transition="none" -->

```
[L578] import json
```

```py
[L582] parametros = {"velocidad": 10.0, "angulo": 45.0 }

[L584] GRAVEDAD = 10.0  # m/s²
```

```py
[L588] resultado = simular(**parametros)
```

```py
[L592] experimento = {"parametros":parametros, "resultado":resultado }
```

--

[L597] <!-- .slide: data-transition="none" -->

```
[L600] import json
```

```py
[L604] parametros = {"velocidad": 10.0, "angulo": 45.0 }

[L606] GRAVEDAD = 10.0  # m/s²
```

```py
[L610] resultado = simular(**parametros)
```

```py
[L614] experimento = {"parametros":parametros, "resultado":resultado }
[L615] serializado = json.dumps(experimento)
```

--

[L620] <!-- .slide: data-transition="none" -->

```py
[L623] import json
[L624] from pathlib import Path
```

```py
[L628] parametros = {"velocidad": 10.0, "angulo": 45.0 }
[L629] GRAVEDAD = 10.0  # m/s²
```

```py
[L633] resultado = simular(**parametros)
```

```py
[L637] experimento = {"parametros":parametros, "resultado":resultado }
[L638] serializado = json.dumps(experimento)
[L639] Path("experimento.json").write_text(serializado, encoding="utf-8")
```

[L642] Requerimos que nuestros componentes tengan inputs y outputs serializables.<!-- .element: class="fragment" -->

--

[L646] # REGLA 1

[L648] Requerimos que nuestros componentes tengan inputs y outputs serializables.

[L650] Este cambio en las restricciones que le imponemos a nuestro código nos permite pensar en nuestro sistema de manera modular y componible. <!-- .element: class="fragment" -->

---

[L654] <!-- 6	Diseño / Implementación / Verificación	4 min -->

[L656] Ahora que **delegamos** la implementación de los componentes. 

[L658] ¿qué tenemos que hacer nosotros? <!-- .element: class="fragment" data-fragment-index="0" -->

<h5>
[L661] <span class="fragment" data-fragmen

## Assistant

Revisé la estructura completa de `slides.md`. Hay un estilo bastante reconocible y creo que vale la pena conservarlo. No empezaría *After Chatbon* desde cero: **la nueva charla debería sentirse como una evolución de la anterior, pero con un argumento más amplio y menos centrado en la ingeniería de software.**

Hay una característica especialmente valiosa en tu presentación: no es una colección de diapositivas que explican conceptos. Es una argumentación que va construyendo evidencia delante de la audiencia.

# 1. Identidad del estilo

Lo describiría como una combinación de:

- **Ensayo técnico:** defendés una posición, no solamente transmitís información.
- **Demostración progresiva:** mostrás una transformación y extraés principios de ella.
- **Artesanía visual:** diagramas, analogías, código y resultados concretos.
- **Voz personal:** opiniones fuertes, preguntas provocadoras y referencias culturales.
- **Rigor científico:** las afirmaciones importantes se conectan con experimentos, propiedades y evidencia.

Hay cinco recursos que me parecen particularmente importantes.

## 1.1. Abrir con una posición personal

La frase:

<box background="surface-secondary" radius="lg" padding={4} gap={2}>
  <title size="2xl" weight="medium">No me gusta programar,</title>
  <title size="2xl" weight="medium">me gusta resolver problemas.</title>
</box>

Es una muy buena apertura porque inmediatamente establece una perspectiva. No empieza explicando quién sos ni qué es un LLM. Primero establece qué te importa.

Después presentás los generadores probabilísticos como una herramienta que ayuda a ese propósito. <FileCite ref_id="turn1file0" line_range_start={34} line_range_end={43}/>

**Para After Chatbon:** mantendría este recurso. Incluso podría utilizar una frase que expanda la idea:

> No quiero producir más software. Quiero poder hacer más cosas.

Es una hipótesis sobre el propósito de la tecnología, no una conclusión sobre sus capacidades.

## 1.2. Utilizar analogías visuales para explicar cambios conceptuales

La comparación entre trabajar con madera y trabajar con software es un recurso muy bueno:

<AsyncImageGroup query={["traditional hand saw cutting wood workshop","modern circular power saw woodworking","natural wood grain timber texture","white melamine laminated board texture"]} aspectRatio="5:4"/>

No explicás primero las propiedades de los generadores probabilísticos. Mostrás una transformación que la audiencia puede comprender intuitivamente.

Después introducís el concepto de cambio de sustrato y extraés las consecuencias para la ingeniería. <FileCite ref_id="turn1file0" line_range_start={106} line_range_end={160}/>

**Para After Chatbon:** podemos utilizar esta misma técnica para explicar:

- Automatizar un proceso frente a eliminarlo.
- Construir un prototipo frente a construir un producto.
- Un laboratorio controlado frente a experimentar directamente en producción.
- Un sistema de procedimientos frente a un sistema orientado a resolver problemas.

La analogía tiene que hacer trabajo conceptual, no ser simplemente decorativa.

## 1.3. Mostrar una transformación, no una explicación

Esta es probablemente la característica más fuerte de la presentación anterior.

El ejemplo de tiro parabólico empieza con un script sencillo y evoluciona progresivamente:

<box border radius="lg" padding={3} gap={3}>
  <list connector="solid" marker="number" gap={2}>
    <list-item>
      **Script inicial**

      <text color="secondary" size="sm">Un programa que calcula y grafica una trayectoria.</text>
    </list-item>
    <list-item>
      **Separación de inputs y outputs**

      <text color="secondary" size="sm">Hacer explícitos los datos de entrada y los resultados.</text>
    </list-item>
    <list-item>
      **Serialización**

      <text color="secondary" size="sm">Registrar experimentos y poder intercambiar componentes.</text>
    </list-item>
    <list-item>
      **Verificación**

      <text color="secondary" size="sm">Introducir tests, propiedades y oráculos independientes.</text>
    </list-item>
    <list-item>
      **Experimentación**

      <text color="secondary" size="sm">Ejecutar Monte Carlo y analizar resultados.</text>
    </list-item>
    <list-item>
      **Evolución**

      <text color="secondary" size="sm">Extender el modelo y cambiar implementaciones sin perder garantías.</text>
    </list-item>
  </list>
</box>

Cada transformación introduce una nueva necesidad y permite descubrir un principio de diseño. No presentás las reglas como dogmas: las derivás del ejemplo. <FileCite ref_id="turn1file0" line_range_start={204} line_range_end={649}/> <FileCite ref_id="turn1file0" line_range_start={696} line_range_end={755}/>

**Para After Chatbon:** conservaría exactamente esta metodología didáctica.

La transformación ahora podría ser:

`Problema → Comprensión → Simplificación → Experimento → Validación → Acción`

## 1.4. Extraer reglas explícitas

La presentación tiene dos momentos muy claros:

- REGLA 1: inputs y outputs serializables.
- REGLA 2: acreción.

Son fáciles de recordar y convierten una demostración concreta en conocimiento transferible. <FileCite ref_id="turn1file0" line_range_start={642} line_range_end={650}/> <FileCite ref_id="turn1file0" line_range_start={1028} line_range_end={1052}/>

Para la nueva charla propondría tres reglas:

<box border radius="lg" padding={3} gap={3}>
  <box gap={1}>
    <title size="xl">REGLA 1</title>
    **Entender antes de automatizar.**

    No reproduzcas un proceso sin entender por qué existe.
  </box>
  <divider color="subtle"/>
  <box gap={1}>
    <title size="xl">REGLA 2</title>
    **Hacé que equivocarse sea barato.**

    Construí ambientes donde experimentar, romper y volver atrás sea fácil.
  </box>
  <divider color="subtle"/>
  <box gap={1}>
    <title size="xl">REGLA 3</title>
    **Validá contra la realidad.**

    Que un programa funcione no significa que hayas resuelto el problema correcto.
  </box>
</box>

## 1.5. Terminar con una idea que trascienda la técnica

La cita de Fabián Casas funciona muy bien porque amplía el significado de todo lo anterior:

> Una técnica que te sirve para escribir te tiene que servir también para vivir.

Y el cierre «Estructura sobre el Caos» le da identidad a la presentación. <FileCite ref_id="turn1file0" line_range_start={1169} line_range_end={1184}/>

Para *After Chatbon* buscaría un cierre con esa misma característica: que conecte programación, aprendizaje y vida cotidiana.

---

# 2. Gramática visual que conservaría

A partir del Markdown, identifico estas convenciones:

| Recurso | Cómo se utiliza | Qué conservar |
|---|---|---|
| Frases grandes | Una afirmación por diapositiva | Sí |
| `fragment` | Revelar argumentos progresivamente | Sí |
| Diagramas SVG | Explicar relaciones y transformaciones | Sí |
| Código Python | Mostrar implementaciones concretas | Cuando aporte |
| Imágenes comparativas | Analogías y contrastes | Sí |
| Slides consecutivas | Mostrar evolución paso a paso | Sí |
| Preguntas | Hacer pensar a la audiencia | Sí |
| `NOTES` | Separar guion oral de contenido visual | Absolutamente |
| `REGLA N` | Extraer principios memorables | Sí |

La presentación está construida con Reveal.js y Markdown, usando separadores de diapositivas, HTML puntual y fragmentos incrementales. No hace falta cambiar ese formato para la nueva charla.

Una limitación: estoy evaluando el lenguaje visual y narrativo a partir del Markdown y sus referencias a imágenes, no el renderizado final. Para evaluar tipografía, paleta, legibilidad y composición real necesitaría también el PDF o los estilos del tema.

# 3. Qué cambiaría para After Chatbon

No trasladaría la cantidad de código de la presentación anterior. En aquella charla, el código era el objeto de estudio. En esta, el objeto de estudio es nuestra capacidad de resolver problemas.

Mi propuesta:

<box border radius="lg" padding={3} gap={3}>
  **Distribución del contenido visual**
  <box gap={1}>
    <row justify="between">
      **Frases y afirmaciones**
      <text tabularNums weight="medium">30%</text>
    </row>
    <box background="surface-tertiary" height="9px" radius="full" clip>
      <box background="#3987BA" width="30%" height="100%" radius="full"/>
    </box>
  </box>
  <box gap={1}>
    <row justify="between">
      **Diagramas y modelos**
      <text tabularNums weight="medium">30%</text>
    </row>
    <box background="surface-tertiary" height="9px" radius="full" clip>
      <box background="#3987BA" width="30%" height="100%" radius="full"/>
    </box>
  </box>
  <box gap={1}>
    <row justify="between">
      **Demostraciones y experimentos**
      <text tabularNums weight="medium">25%</text>
    </row>
    <box background="surface-tertiary" height="9px" radius="full" clip>
      <box background="#3987BA" width="25%" height="100%" radius="full"/>
    </box>
  </box>
  <box gap={1}>
    <row justify="between">
      **Fotografías y analogías**
      <text tabularNums weight="medium">15%</text>
    </row>
    <box background="surface-tertiary" height="9px" radius="full" clip>
      <box background="#3987BA" width="15%" height="100%" radius="full"/>
    </box>
  </box>
  <caption>Propuesta orientativa de recursos visuales, no una medición de la presentación anterior.</caption>
</box>

Los diagramas van a cobrar más importancia porque ahora queremos hablar de sistemas complejos, actores, dependencias, procesos y decisiones.

También reduciría la cantidad de slides con bloques de texto explicativo. Las explicaciones más largas deberían estar en `NOTES`.

# 4. Un primer storyboard siguiendo el estilo anterior

Esta sería mi traducción del estilo a la nueva charla:

<box gap={3}>
  <row align="start" gap={3}>
    <AsyncImage query="minimalist dark cinematic photograph open road horizon landscape" aspectRatio="5:4" maxWidth="108px"/>
    <box flex="1" gap={1}>
      **01 — After Chatbon**

      Aprender, experimentar y hacer que las cosas ocurran.
      <text color="secondary" size="xs">Portada sencilla, fecha, PyDay Hurlingham.</text>
    </box>
  </row>
  <divider color="subtle"/>
  <row align="start" gap={3}>
    <AsyncImage query="person tinkering electronics workbench hands tools workshop" aspectRatio="5:4" maxWidth="108px"/>
    <box flex="1" gap={1}>
      **02 — No quiero producir más software.**

      Quiero poder hacer más cosas.
      <text color="secondary" size="xs">Declaración personal, como en la charla anterior.</text>
    </box>
  </row>
  <divider color="subtle"/>
  <row align="start" gap={3}>
    <AsyncImage query="complex tangled cables messy bureaucracy paperwork desk" aspectRatio="5:4" maxWidth="108px"/>
    <box flex="1" gap={1}>
      **03 — ¿Por qué cuesta tanto resolver problemas?**

      Introducir fricción, procesos y barreras.
      <text color="secondary" size="xs">Una pregunta provocadora.</text>
    </box>
  </row>
  <divider color="subtle"/>
  <row align="start" gap={3}>
    <AsyncImage query="scientist notebook sketching diagrams laboratory" aspectRatio="5:4" maxWidth="108px"/>
    <box flex="1" gap={1}>
      **04 — Aprender es experimentar.**

      El autodidactismo como método.
      <text color="secondary" size="xs">Conectar curiosidad, hipótesis y herramientas.</text>
    </box>
  </row>
  <divider color="subtle"/>
  <row align="start" gap={3}>
    <AsyncImage query="simple systems flow diagram on whiteboard sticky notes" aspectRatio="5:4" maxWidth="108px"/>
    <box flex="1" gap={1}>
      **05 — Entender el sistema.**

      Actores, relaciones, reglas y restricciones.
      <text color="secondary" size="xs">Primera demostración de modelado.</text>
    </box>
  </row>
  <divider color="subtle"/>
  <row align="start" gap={3}>
    <AsyncImage query="minimal process flowchart before after process simplification whiteboard" aspectRatio="5:4" maxWidth="108px"/>
    <box flex="1" gap={1}>
      **06 — ¿Y si eliminamos el proceso?**

      Simplificar antes de automatizar.
      <text color="secondary" size="xs">Primera regla.</text>
    </box>
  </row>
  <divider color="subtle"/>
  <row align="start" gap={3}>
    <AsyncImage query="small isolated software development test lab laptop terminal workspace" aspectRatio="5:4" maxWidth="108px"/>
    <box flex="1" gap={1}>
      **07 — Construir un laboratorio.**

      Hacer que equivocarse sea barato.
      <text color="secondary" size="xs">Segunda regla, con demostración progresiva.</text>
    </box>
  </row>
  <divider color="subtle"/>
  <row align="start" gap={3}>
    <AsyncImage query="scientific experiment data visualization plots laptop" aspectRatio="5:4" maxWidth="108px"/>
    <box flex="1" gap={1}>
      **08 — ¿Cómo sabemos que funciona?**

      Verificación, validación y evidencia.
      <text color="secondary" size="xs">Tercera regla.</text>
    </box>
  </row>
  <divider color="subtle"/>
  <row align="start" gap={3}>
    <AsyncImage query="community makerspace people collaborating building something workshop" aspectRatio="5:4" maxWidth="108px"/>
    <box flex="1" gap={1}>
      **09 — Hacer que las cosas ocurran.**

      Construir para resolver problemas, no solamente para vender.
      <text color="secondary" size="xs">Aplicación del método.</text>
    </box>
  </row>
  <divider color="subtle"/>
  <row align="start" gap={3}>
    <AsyncImage query="person looking at sunrise mountain landscape contemplative horizon" aspectRatio="5:4" maxWidth="108px"/>
    <box flex="1" gap={1}>
      **10 — ¿Qué vas a intentar?**

      Cierre y llamada a la acción.
      <text color="secondary" size="xs">Una pregunta, no un resumen de diapositivas.</text>
    </box>
  </row>
</box>

# 5. Una decisión editorial importante

Hay algo de la charla anterior que no deberíamos perder: tu posición crítica frente a las herramientas.

Por ejemplo, la advertencia sobre los proveedores de tokens y la economía de la atención. No es un tema central para la nueva charla, pero sí expresa una idea relevante: no debemos permitir que las herramientas definan nuestros objetivos. <FileCite ref_id="turn1file0" line_range_start={155} line_range_end={173}/>

La nueva charla podría llevar esa crítica un paso más allá:

- No todo lo que se puede automatizar merece automatizarse.
- No todo lo que podemos construir merece construirse.
- No todo problema tiene que convertirse en una oportunidad comercial.
- No necesitamos permiso de un mercado para experimentar.
- No debemos confundir actividad con progreso.

Esto le da una identidad propia a *After Chatbon*.

---

## Mi recomendación final

Mantendría la misma identidad formal de la charla de PyDay La Plata:

- Markdown + Reveal.js.
- Diapositivas de afirmaciones fuertes.
- Frases cortas y revelaciones progresivas.
- Analogías visuales.
- Una demostración que evoluciona.
- Reglas derivadas de la experiencia.
- Referencias y notas para el expositor.
- Un cierre que conecte la técnica con algo más amplio.

Pero cambiaría el centro de gravedad:

<box border radius="lg" padding={3} gap={2}>
  <text color="secondary" size="xs" weight="medium">PYDAY LA PLATA</text>
  **Cómo construir software científico que podamos entender, verificar y mantener.**
  <divider color="subtle"/>
  <text color="secondary" size="xs" weight="medium">PYDAY HURLINGHAM</text>
  **Cómo aprender, experimentar y construir herramientas que nos permitan resolver los problemas que nos importan.**
</box>

**El siguiente paso no debería ser escribir las diapositivas todavía.** Primero elegiría el ejemplo conductor y diseñaría su transformación completa, desde el problema original hasta una solución que podamos experimentar y validar. Esa será la columna vertebral de la nueva presentación, igual que el tiro parabólico lo fue en la anterior.

## User

la charla juega con [https://es.wikipedia.org/wiki/After_Chab%C3%B3n](https://es.wikipedia.org/wiki/After_Chab%C3%B3n) podemos darle la estructura del disco

## Assistant

Sí. Y creo que puede darle a la charla una identidad mucho más fuerte: **que *After Chatbon* no sea solamente un título, sino la estructura narrativa de la charla**.

Podemos tomar el disco como una dramaturgia: cada tema abre una escena o una pregunta, y el argumento de la charla avanza siguiendo ese recorrido. No hace falta que cada canción tenga una equivalencia literal con una diapositiva; algunas pueden funcionar como transiciones, otras como capítulos y otras como contrapuntos.

La clave sería conservar dos cosas a la vez: que alguien que conoce el disco reconozca el juego, y que alguien que nunca escuchó a Sumo pueda seguir una charla coherente por sí misma.

Sí. Además, hay algo muy aprovechable: el vinilo está organizado en **dos lados de seis temas**. Podemos usar el cambio de lado como el giro central de la charla. La lista y esa división aparecen en las ediciones en vinilo del disco. <Cite refs={["turn750533view0","turn539822search1","turn539822search0"]}/>

# After Chatbon
*Doce temas para aprender, experimentar y hacer que las cosas ocurran.*

La propuesta sería respetar el orden del disco y convertir cada canción en una escena. No sería una interpretación literal de las letras: usaríamos los títulos, el orden y las asociaciones que evocan para construir nuestro propio relato.

## Lado A — El mundo que irrumpe

<badge color="info">01–06</badge> **Del impacto a comprender qué tenemos delante.**

| Pista | Capítulo | Qué contamos |
|---|---|---|
| **01. Crua Chan** | Algo cambió | Apertura fuerte. La IA reduce el costo de intentar cosas que antes eran demasiado caras, difíciles o inaccesibles. No es simplemente una nueva herramienta: cambia lo que podemos intentar. |
| **02. No tan distintos** | Seguimos siendo nosotros | La tecnología no elimina la necesidad de aprender, pensar, tener criterio y entender problemas. No nos convierte mágicamente en otra cosa. |
| **03. Banderitas y globos** | El espectáculo | La euforia, las promesas y el ruido alrededor de la IA. Demos espectaculares, productividad, automatización. ¿Qué queda cuando termina el espectáculo? |
| **04. Mañana en el Abasto** | Los problemas reales | Bajamos a tierra. Un problema concreto, cotidiano, situado. Presentamos el ejemplo que va a atravesar la charla. |
| **05. Hola Frank** | Empezar una conversación | Interactuar con una máquina para explorar una idea, preguntar, construir un primer prototipo. No esperar a tener todo resuelto para empezar. |
| **06. Ojos de terciopelo** | Aprender a mirar | Antes de automatizar, observar. Entender actores, procesos, dependencias, restricciones y motivos. Aprender a ver el sistema, no solamente sus formularios. |

<box border radius="lg" padding={3} gap={2}>
  <row align="center" gap={2}>
    <icon name="disc-3" size="xl"/>
    **Flip the record**
    <spacer/>
    <badge>Mitad de la charla</badge>
  </row>
  Hasta acá vimos el cambio, el ruido y un problema real. Ahora damos vuelta el disco: dejamos de hablar de lo que la tecnología promete y empezamos a hablar de lo que podemos hacer con ella.
</box>

## Lado B — Del apuro a la acción

<badge color="success">07–12</badge> **De querer una solución a tener capacidad de intervenir.**

| Pista | Capítulo | Qué contamos |
|---|---|---|
| **07. Lo quiero ya** | La trampa de la velocidad | Queremos automatizar inmediatamente. Pero hacer más rápido un proceso absurdo no es resolver el problema. |
| **08. La gota en el ojo** | La pequeña fricción | Encontrar el obstáculo concreto. A veces no necesitamos una plataforma: necesitamos eliminar un paso, una espera o una intermediación innecesaria. |
| **09. El cieguito volador** | Experimentar sin tener todo el mapa | No hace falta comprenderlo todo para empezar a investigar. Podemos formular hipótesis, construir modelos y probar alternativas sin fingir que sabemos todo. |
| **10. No te pongas azul** | Perder el miedo a romper | Laboratorios, entornos aislados, Git, tests, rollback. Hacer que equivocarse sea barato y reversible. |
| **11. Noche de paz** | La tranquilidad de comprobar | Validar. ¿Funciona? ¿Resuelve el problema? ¿Qué pasa en los casos límite? ¿Lo puede usar otra persona? La realidad es el juez. |
| **12. Percusion Baby** | Encontrar el ritmo | No es una persona ni una IA haciendo todo. Es gente, herramientas y conocimientos combinándose para hacer cosas que antes no ocurrían. |

## El arco completo

<box border radius="lg" padding={3} gap={3}>
  <box gap={1}>
    <text color="secondary" weight="semibold" size="xs">LADO A</text>
    **Descubrir que podemos intentar más cosas.**
    <text color="secondary" size="sm">Impacto → humanidad → espectáculo → realidad → diálogo → comprensión</text>
  </box>
  <divider color="subtle"/>
  <box gap={1}>
    <text color="secondary" weight="semibold" size="xs">LADO B</text>
    **Descubrir cómo hacer que esas cosas ocurran.**
    <text color="secondary" size="sm">Urgencia → fricción → experimento → seguridad → validación → acción</text>
  </box>
  <divider color="subtle"/>
  <title size="xl" textAlign="center">De consumir posibilidades a crear posibilidades.</title>
</box>

## Algunas decisiones que me parecen importantes

**1. El ejemplo conductor debería aparecer en «Mañana en el Abasto».** No como una demo que interrumpimos para explicar teoría, sino como una historia que evoluciona durante el disco. En «Hola Frank» empezamos a intervenir; en «Ojos de terciopelo» entendemos el sistema; en el lado B lo transformamos, experimentamos y validamos.

**2. «Banderitas y globos» tiene que ser un contrapunto, no una charla anti-IA.** La pregunta no es si las promesas son verdaderas o falsas, sino qué podemos hacer concretamente una vez que dejamos de mirar el espectáculo.

**3. «Lo quiero ya» es un buen punto de inflexión.** Es la tentación de confundir velocidad con progreso. Ahí podemos introducir una idea central: antes de automatizar un proceso, preguntémonos si hace falta que exista.

**4. «Percusion Baby» debería cerrar con energía.** No terminar con una lista de recomendaciones técnicas, sino con una invitación a hacer algo: aprender, investigar, construir, colaborar, resolver problemas propios o de la comunidad, incluso cuando no hay un negocio detrás.

Hay también una coincidencia interesante: Wikipedia recoge que Luca consideraba este su mejor disco porque no tenía un éxito único. <Cite ref="turn750533view0"/> Me gusta trasladar esa idea a la charla: **no hay una demo milagrosa, una herramienta definitiva ni una técnica que resuelva todo. Hay una combinación de prácticas que nos da más libertad para actuar.**

## Una posible última diapositiva

<AsyncImage query="Sumo After Chabon 1987 original vinyl album cover" aspectRatio="5:4" width="100%" fit="contain"/>

> No quiero que la IA haga todo por mí.
>
> Quiero aprender cosas que todavía no sé.
>
> Quiero probar ideas que antes no podía probar.
>
> Quiero poder cambiar las cosas que no funcionan.
>
> **Quiero hacer que las cosas ocurran.**

Y terminar con la pregunta:

**¿Qué harías mañana si intentar resolver ese problema dejara de ser tan difícil?**

---

Creo que esta estructura es bastante más interesante que la de diez diapositivas que teníamos. Tiene una progresión, un giro narrativo en el medio y un cierre que se siente ganado.

El próximo paso sería elegir **el problema concreto de «Mañana en el Abasto»**: tiene que ser lo suficientemente pequeño para mostrarlo en vivo, pero lo suficientemente real para que el público entienda por qué vale la pena resolverlo.

## User

en vez de tener cada uno de los titulos de las canciones podemos tener una frase de la letra que guie la seecion

## Assistant

Sí. De hecho, me parece una mejora: **que los títulos desaparezcan y que cada sección empiece con una frase de la canción que funcione como epígrafe**.

Así el disco deja de ser un índice temático y pasa a ser una voz que acompaña la charla. La frase no tiene que explicar literalmente el contenido: puede funcionar como metáfora, pregunta, advertencia o contrapunto.

Mantendría el recorrido de los dos lados del vinilo, pero las secciones tendrían títulos propios, relacionados con el argumento de *After Chatbon*. La letra aportaría el tono y la resonancia.

Haría una primera selección siguiendo exactamente el orden del álbum. En las diapositivas no aparecerían los nombres de las canciones: solamente el fragmento, que funcionaría como epígrafe, y el tema que nosotros queremos desarrollar.

## Lado A — Descubrir

| Pista | Frase de la letra | La sección que guía |
|---:|---|---|
| 01 | “Come on London, here we come” <Cite ref="turn667821search8"/> | **El salto.** Entramos en un territorio nuevo: ahora podemos intentar cosas que antes ni siquiera estaban a nuestro alcance. |
| 02 | “Do they know why they go?” <Cite ref="turn667821search5"/> | **¿Hacia dónde vamos?** ¿Estamos resolviendo problemas o simplemente haciendo más cosas, más rápido? |
| 03 | “lo entendido es lo que no entiendo” <Cite ref="turn667821search7"/> | **El ruido no es comprensión.** El espectáculo de la IA, las promesas y la confusión entre lo que parece posible y lo que realmente entendemos. |
| 04 | “No tengas miedo, no” <Cite ref="turn167468search7"/> | **Volver a los problemas reales.** Salir de las abstracciones y mirar lo que ocurre en la vida cotidiana. |
| 05 | “Hello Frank, how’re you doing?” <Cite ref="turn167468search9"/> | **Pensar en diálogo.** Conversar, preguntar, explorar una idea y construir un primer intento. |
| 06 | “Think it, don’t think it” <Cite ref="turn167468search14"/> | **Aprender a mirar.** Desarrollar criterio, cuestionar lo que damos por sentado y entender el sistema antes de intervenir. |

## Lado B — Hacer

| Pista | Frase de la letra | La sección que guía |
|---:|---|---|
| 07 | “No sé lo que quiero, pero lo quiero ya” <Cite ref="turn667821search4"/> | **La trampa de la urgencia.** Automatizar antes de entender; acelerar procesos que quizá ni siquiera deberían existir. |
| 08 | “Sing the song today” <Cite ref="turn667821search11"/> | **Empezar a hacer.** No esperar a tener el diseño perfecto: construir algo pequeño y concreto. |
| 09 | “usan radar” <Cite ref="turn667821search0"/> | **Experimentar sin tener el mapa.** Formular hipótesis, construir modelos y orientarnos mediante observaciones y feedback. |
| 10 | “real life is inside” <Cite ref="turn167468search5"/> | **La realidad como criterio.** Validar contra el mundo, no contra la respuesta convincente de una máquina. |
| 11 | “Sueña un sueño imposible” <Cite ref="turn667821search1"/> | **Volver a imaginar.** Atreverse a pensar en problemas que antes parecían demasiado costosos o difíciles de abordar. |
| 12 | “everyday is Sunday” <Cite ref="turn167468search4"/> | **Hacer por el placer de hacer.** Curiosidad, juego, ciencia, comunidad y creación sin necesitar una justificación comercial. |

## Cómo lo llevaría a las diapositivas

No pondría la frase como un título convencional. Le daría un tratamiento distinto:

<box border radius="lg" padding={4} gap={3}>
  <text color="secondary" weight="medium" size="xs">AFTER CHATBON · LADO B</text>
  <title size="2xl" weight="semibold">No sé lo que quiero,</title>
  <title size="2xl" weight="semibold" italic>pero lo quiero ya.</title>
  <divider color="subtle"/>
  <title size="xl">La trampa de la urgencia</title>
  <text color="secondary" size="sm">Hacer más rápido no es necesariamente resolver mejor.</text>
</box>

La frase abre la sección; el subtítulo es nuestro argumento. Después, las diapositivas desarrollan la idea sin necesidad de seguir mostrando referencias al disco.

**Hay cuatro fragmentos que me parecen especialmente potentes para sostener toda la charla:**

- “Do they know why they go?” — la pregunta sobre nuestra relación con el trabajo y la tecnología.
- “lo entendido es lo que no entiendo” — la incertidumbre como punto de partida.
- “real life is inside” — la obligación de volver a la realidad y validar.
- “everyday is Sunday” — el cierre sobre crear por curiosidad, placer y libertad.

Una observación: no forzaría todas las frases si alguna no funciona al probarla en voz alta. El disco debería darle una segunda lectura a la charla, no convertirse en un acertijo que el público tenga que resolver.

**Mi preferencia es que las frases permanezcan en el idioma original de cada canción**, con el argumento de la sección en castellano. Eso conserva la voz de Sumo y evita que la charla parezca una traducción explicativa de las letras.

## User

ok, podemos pensar en el problema a usar, quizas algo de [https://charly-vibes.github.io/jams/](https://charly-vibes.github.io/jams/)**&#xA0;o algo que nos permita utilizar pyodide**

## Assistant

Sí. Me gusta más esta dirección que inventar un ejemplo artificial de gestión de eventos. **Podemos usar algo que ya hayas construido o que responda a una curiosidad real**, y convertirlo en el hilo conductor de la charla.

Además, Pyodide abre una posibilidad narrativa muy buena: que el público vea cómo una idea pasa de ser una página web a convertirse en un pequeño laboratorio ejecutable en el navegador, con Python, sin instalar nada ni necesitar un servidor para ejecutar el código.

Evaluaría dos caminos: aprovechar una experiencia de Jams que ya exista, o construir un experimento nuevo que use Pyodide. Lo importante es que no sea una demo de tecnología: tiene que mostrar cómo entender, explorar y resolver un problema que valga la pena.

Miré el repositorio de JAMS y hay un candidato que sobresale: **SensorLog**. No es solo una aplicación de ejemplo: ya resuelve una tarea concreta, registrar datos de sensores del teléfono, con persistencia, visualización temporal y exportación a CSV. La especificación contempla acelerómetro, giroscopio, gravedad, orientación, brújula y GPS, con frecuencias de hasta 60 Hz. <Cite ref="turn530622view0"/>

Eso permite una combinación bastante natural:

- **El teléfono mide el mundo.**
- **Pyodide permite analizar las mediciones con Python en el navegador.**
- **La persona formula una pregunta, experimenta y contrasta una hipótesis.**

La historia ya no sería «miren qué impresionante es Pyodide», sino «tenemos un laboratorio en el bolsillo; ¿qué podemos averiguar con él?».

## El problema conductor que elegiría

<box gap={2}>
  <badge color="success">Mi recomendación</badge>
  <title size="2xl">¿Podemos convertir el teléfono que llevamos en el bolsillo en un laboratorio científico?</title>
  No necesitamos comprar un instrumento, instalar Python, configurar Jupyter ni contratar un servicio. Tenemos sensores, un navegador y una pregunta que queremos responder.
</box>

Elegiría un experimento sencillo: **medir el período de un péndulo con el teléfono y comprobar si coincide con el modelo físico**.

<AsyncImageGroup query={["simple pendulum physics experiment smartphone accelerometer setup","simple pendulum oscillation laboratory experiment diagram","scientific time series oscillation accelerometer graph"]} aspectRatio="5:4" layout="carousel"/>

### Cómo se desarrolla la historia

1. **La pregunta.** ¿De qué depende el período de un péndulo? ¿De su longitud? ¿De su masa? ¿De cuánto lo desplazamos inicialmente?
2. **El instrumento.** Usamos SensorLog para registrar el giroscopio del teléfono mientras oscila. Ya tiene selección de sensores y frecuencias de muestreo, persistencia y exportación CSV. <Cite ref="turn530622view0"/>
3. **El laboratorio.** Abrimos una página web que acepta ese CSV y ejecuta Python mediante Pyodide.
4. **El análisis.** Calculamos períodos a partir de la señal, detectamos máximos, estimamos incertidumbre y representamos los resultados.
5. **La hipótesis.** Comparamos las mediciones con:

   \[
   T = 2\pi\sqrt{\frac{L}{g}}
   \]

6. **La validación.** Cambiamos la longitud, repetimos y vemos si los resultados acompañan al modelo. No alcanza con que el gráfico sea lindo.

El detalle importante es que SensorLog exporta datos con marcas de tiempo y valores por eje, en archivos CSV separados por sensor. Eso nos da una interfaz bastante limpia entre la adquisición y el análisis. <Cite ref="turn155874view0"/>

## Qué papel tendría Pyodide

<box border radius="lg" padding={3} gap={3}>
  <box background="surface-secondary" radius="md" padding={3} align="center" gap={1}>
    <icon name="smartphone" size="2xl"/>
    **SensorLog**
    <text color="secondary" size="sm">Adquisición de datos físicos</text>
  </box>
  <box align="center">
    <icon name="arrow-down" color="secondary" size="lg"/>
    <text color="secondary" size="xs">CSV · timestamp + mediciones</text>
  </box>
  <box background="surface-secondary" radius="md" padding={3} align="center" gap={1}>
    <icon name="globe" size="2xl"/>
    **Una página web**
    <text color="secondary" size="sm">Carga el archivo y presenta el experimento</text>
  </box>
  <box align="center">
    <icon name="arrow-down" color="secondary" size="lg"/>
    <text color="secondary" size="xs">Ejecución local</text>
  </box>
  <box background="surface" border radius="md" padding={3} align="center" gap={1}>
    <icon name="code" size="2xl"/>
    **Pyodide + Python**
    <text color="secondary" size="sm">NumPy · SciPy · Matplotlib</text>
  </box>
  <box align="center">
    <icon name="arrow-down" color="secondary" size="lg"/>
  </box>
  <box background="surface-secondary" radius="md" padding={3} align="center" gap={1}>
    <icon name="chart-scatter" size="2xl"/>
    **Resultados**
    <text color="secondary" size="sm">Gráficos, períodos, incertidumbre y comparación con el modelo</text>
  </box>
</box>

Pyodide es CPython compilado a WebAssembly. Permite ejecutar Python en el navegador y cargar paquetes científicos como NumPy, SciPy y Matplotlib. Para cálculos más pesados puede ejecutarse en un Web Worker, sin bloquear la interfaz. <Cite refs={["turn411967view2","turn262334view2","turn216380view0"]}/>

Esto nos da una demo interesante: una página estática, sin backend, en la que alguien puede cargar sus propios datos y ejecutar un análisis científico con Python.

Hay límites que conviene respetar: los paquetes deben estar disponibles para Pyodide, algunas capacidades del sistema operativo no existen en WebAssembly y el primer arranque requiere descargar el runtime y los paquetes. Por eso usaría una versión fijada, cargaría únicamente lo necesario y llevaría un CSV preparado como respaldo. <Cite ref="turn262334view3"/>

## Otras opciones de JAMS

No descartaría estos caminos, pero los ordenaría así:

<box gap={3}>
  <row align="start" gap={3}>
    <AsyncImage query="smartphone wifi signal heatmap floor plan visualization" aspectRatio="1:1" maxWidth="104px"/>
    <box flex="1" gap={1}>
      **2. Encontrar el mejor lugar para un repetidor Wi-Fi**

      <badge color="warning">Interesante, con reservas</badge>
      Problema cotidiano y fácil de explicar. Se pueden comparar mediciones repetidas por ubicación y analizar su variabilidad con Python. Pero el `signal-heatmap` actual no mide directamente la potencia de señal Wi-Fi: combina estimaciones de conexión y pruebas de descarga. Habría que revisar el modelo de medición antes de presentar sus resultados como una medida de calidad. <Cite refs={["turn530622view1","turn544633view1"]}/>
    </box>
  </row>
  <divider color="subtle"/>
  <row align="start" gap={3}>
    <AsyncImage query="person using smartphone voice shopping grocery list app" aspectRatio="1:1" maxWidth="104px"/>
    <box flex="1" gap={1}>
      **3. Hacer una lista de compras hablando**

      <badge color="success">Mejor problema cotidiano</badge>
      Listar tiene un problema muy reconocible: pasar de una conversación a una lista estructurada sin tener que escribir. Whisper transcribe y un splitter determinista extrae los artículos. Es un buen ejemplo de IA más reglas y revisión humana, pero Pyodide sería innecesario: el código central ya es JavaScript puro. <Cite ref="turn530622view3"/>
    </box>
  </row>
  <divider color="subtle"/>
  <row align="start" gap={3}>
    <AsyncImage query="handwritten poetry notebook annotated syllables poem" aspectRatio="1:1" maxWidth="104px"/>
    <box flex="1" gap={1}>
      **4. Analizar la métrica de un poema**

      Un problema interesante para hablar de reglas, excepciones, lenguaje y validación. Se podría ampliar el `poem-analyzer` para castellano, con sinalefas, hiatos y acentuación. Pero tampoco necesita Python necesariamente.
    </box>
  </row>
</box>

## Por qué JAMS es especialmente útil para esta charla

Hay una coincidencia conceptual importante: el propio repositorio define sus aplicaciones como experimentos pequeños, de una idea y una sesión. También declara que el código fue generado por un LLM, mientras que la contribución humana está en los requisitos, las decisiones de diseño y la revisión. <Cite ref="turn262743view0"/>

Eso ya es una demostración concreta de la tesis de *After Chatbon*: no se trata de que la máquina programe por nosotros, sino de que podamos dedicar nuestra energía a decidir qué vale la pena intentar, entender qué construimos y comprobar si funciona.

## Mi propuesta para la charla

No haría una demo de Pyodide aislada. Haría un pequeño proyecto nuevo dentro de JAMS, provisionalmente llamado **`laboratorio`**:

- Reutiliza SensorLog para capturar mediciones.
- Importa CSV desde el navegador.
- Ejecuta análisis Python con Pyodide.
- Permite cambiar parámetros y repetir el experimento.
- Muestra tanto resultados como código y supuestos.

Y prepararía el experimento del péndulo antes de la charla, para no depender de sensores, permisos o conectividad durante la presentación.

La frase que podría resumir esa parte sería:

> **No necesitaba una aplicación. Necesitaba una manera de averiguar algo.**

Me parece que eso conecta mejor con el espíritu de la charla que mostrar una aplicación terminada.

El siguiente paso sería definir el experimento exacto y su conjunto de datos: qué medimos, qué hipótesis intentamos refutar, qué análisis ejecutamos y cómo sabemos que no nos estamos engañando.

## User

Ok creo que tengo una mejor idea. Revisemos bajan y whisper como metodologia para pensar junto con IA y relacionarlo con [https://muratbuffalo.blogspot.com/2026/11/writing-as-thinking-tool.html](https://muratbuffalo.blogspot.com/2026/11/writing-as-thinking-tool.html) y lo que tenemos que hacer es un programa que nos ayude a entender lo que tenemos

## Assistant

bash -lc python - <<'PY'
import zipfile, os
for p in ['/mnt/data/bajan-main(2).zip','/mnt/data/whisper-main.zip']:
    print('\n###',p, 'exists=',os.path.exists(p), 'size=',os.path.getsize(p) if os.path.exists(p) else None)
    if os.path.exists(p):
        z=zipfile.ZipFile(p)
        names=z.namelist()
        print('entries',len(names))
        for n in names[:100]: print(n)
PY

## Tool

### /mnt/data/bajan-main(2).zip exists= True size= 599987
entries 304
bajan-main/
bajan-main/.beads.gate.lock
bajan-main/.beads/
bajan-main/.beads/config.yaml
bajan-main/.beads/issues.jsonl
bajan-main/.cargo/
bajan-main/.cargo/config.toml
bajan-main/.claude/
bajan-main/.claude/settings.json
bajan-main/.espectacular/
bajan-main/.espectacular/AGENTS.md
bajan-main/.espectacular/config.toml
bajan-main/.espectacular/contradiction-review/
bajan-main/.espectacular/contradiction-review/p-human-resolution.toml
bajan-main/.espectacular/contradiction-review/p-proposal-entry.toml
bajan-main/.espectacular/contradiction-review/p-queue-transparency.toml
bajan-main/.espectacular/contradiction-review/p-repropose-guard.toml
bajan-main/.espectacular/contradiction-review/p-scan-untouched.toml
bajan-main/.espectacular/entity-review/
bajan-main/.espectacular/entity-review/p-human-resolution.toml
bajan-main/.espectacular/entity-review/p-merge-preserves.toml
bajan-main/.espectacular/entity-review/p-queue-entry.toml
bajan-main/.espectacular/entity-review/p-queue-transparency.toml
bajan-main/.espectacular/entity-review/p-reject-drops-edge.toml
bajan-main/.espectacular/entity-review/p-repropose-guard.toml
bajan-main/.espectacular/entity-review/p-review-schema.toml
bajan-main/.espectacular/eval-claims/
bajan-main/.espectacular/eval-claims/p-deterministic-scoring.toml
bajan-main/.espectacular/eval-claims/p-golden-corpus.toml
bajan-main/.espectacular/eval-claims/p-hedge-scoring.toml
bajan-main/.espectacular/eval-claims/p-precision-recall.toml
bajan-main/.espectacular/eval-claims/p-readonly.toml
bajan-main/.espectacular/eval-claims/p-results-checked-in.toml
bajan-main/.espectacular/eval-claims/p-results-schema.toml
bajan-main/.espectacular/extraction-claims/
bajan-main/.espectacular/extraction-claims/p-deterministic-structure.toml
bajan-main/.espectacular/extraction-claims/p-evidence-containment.toml
bajan-main/.espectacular/extraction-claims/p-mutation-proposal.toml
bajan-main/.espectacular/extraction-claims/p-no-llm-post.toml
bajan-main/.espectacular/extraction-claims/p-output-schema.toml
bajan-main/.espectacular/extraction-claims/p-park-requeue.toml
bajan-main/.espectacular/extraction-claims/p-reflection.toml
bajan-main/.espectacular/extraction-claims/p-run-record.toml
bajan-main/.espectacular/extraction-claims/p-section-filter.toml
bajan-main/.espectacular/extraction-claims/p-single-call.toml
bajan-main/.espectacular/extraction-claims/p-supersession.toml
bajan-main/.espectacular/extraction-claims/p-tag-inheritance.toml
bajan-main/.espectacular/extraction-claims/p-typed-gate.toml
bajan-main/.espectacular/graph-model/
bajan-main/.espectacular/graph-model/p-contradicts-provenance.toml
bajan-main/.espectacular/graph-model/p-deterministic-er.toml
bajan-main/.espectacular/graph-model/p-embedded-store.toml
bajan-main/.espectacular/graph-model/p-hedge-anchor.toml
bajan-main/.espectacular/graph-model/p-human-adopt.toml
bajan-main/.espectacular/graph-model/p-lineage-survives.toml
bajan-main/.espectacular/graph-model/p-merge-keeps.toml
bajan-main/.espectacular/graph-model/p-reified.toml
bajan-main/.espectacular/graph-model/p-relation-typing.toml
bajan-main/.espectacular/graph-model/p-schema-v2.toml
bajan-main/.espectacular/ingestion-contract/
bajan-main/.espectacular/ingestion-contract/p-batch-duplicate.toml
bajan-main/.espectacular/ingestion-contract/p-batch-resume.toml
bajan-main/.espectacular/ingestion-contract/p-corrected-resubmit.toml
bajan-main/.espectacular/ingestion-contract/p-date-fidelity.toml
bajan-main/.espectacular/ingestion-contract/p-deleted-recreate.toml
bajan-main/.espectacular/ingestion-contract/p-deleted-tombstone.toml
bajan-main/.espectacular/ingestion-contract/p-empty-stream.toml
bajan-main/.espectacular/ingestion-contract/p-id-canon.toml
bajan-main/.espectacular/ingestion-contract/p-idempotent.toml
bajan-main/.espectacular/ingestion-contract/p-malformed.toml
bajan-main/.espectacular/ingestion-contract/p-mutated-resubmit.toml
bajan-main/.espectacular/ingestion-contract/p-no-format-parsing.toml
bajan-main/.espectacular/ingestion-contract/p-order-insensitive.toml
bajan-main/.espectacular/ingestion-contract/p-outcome-schema.toml
bajan-main/.espectacular/ingestion-contract/p-section-tags.toml
bajan-main/.espectacular/ingestion-contract/p-state-orthogonal.toml
bajan-main/.espectacular/ingestion-contract/p-stream-schema.toml
bajan-main/.espectacular/ingestion-contract/p-unique-id.toml
bajan-main/.espectacular/ingestion-contract/p-verbatim.toml
bajan-main/.espectacular/query-tools/
bajan-main/.espectacular/query-tools/p-bounded-traversal.toml
bajan-main/.espectacular/query-tools/p-contradiction-query.toml
bajan-main/.espectacular/query-tools/p-lineage-traceable.toml
bajan-main/.espectacular/query-tools/p-query-schema.toml
bajan-main/.espectacular/query-tools/p-ranking.toml
bajan-main/.espectacular/query-tools/p-readonly.toml
bajan-main/.espectacular/query-tools/p-scope-filtering.toml
bajan-main/.genesis/
bajan-main/.genesis/tools.toml
bajan-main/.github/
bajan-main/.github/workflows/
bajan-main/.github/workflows/ci.yml
bajan-main/.github/workflows/pages.yml
bajan-main/.github/workflows/release.yml
bajan-main/.gitignore
bajan-main/.wai/
bajan-main/.wai/.gitignore
bajan-main/.wai/.pipeline-run
bajan-main/.wai/AGENTS.md
bajan-main/.wai/PLUGINS.md

### /mnt/data/whisper-main.zip exists= True size= 278478
entries 273
whisper-main/
whisper-main/.beads/
whisper-main/.beads/.gitignore
whisper-main/.beads/README.md
whisper-main/.beads/config.yaml
whisper-main/.beads/interactions.jsonl
whisper-main/.beads/issues.jsonl
whisper-main/.beads/metadata.json
whisper-main/.claude/
whisper-main/.claude/settings.json
whisper-main/.ddl/
whisper-main/.ddl/config.toml
whisper-main/.ddl/manifest.json
whisper-main/.espectacular/
whisper-main/.espectacular/AGENTS.md
whisper-main/.espectacular/config-precedence/
whisper-main/.espectacular/config-precedence/config-found-in-a-parent.toml
whisper-main/.espectacular/config-precedence/fresh-machine.toml
whisper-main/.espectacular/config-precedence/nested-config-shadows-the-repo-root.toml
whisper-main/.espectacular/config-precedence/repo-joins-a-group.toml
whisper-main/.espectacular/config-precedence/repo-overrides-the-workspace-root.toml
whisper-main/.espectacular/config.toml
whisper-main/.espectacular/knowledge-append/
whisper-main/.espectacular/knowledge-append/empty-input-rejected.toml
whisper-main/.espectacular/knowledge-append/first-append-creates-the-file.toml
whisper-main/.espectacular/knowledge-append/piped-input.toml
whisper-main/.espectacular/knowledge-append/subsequent-appends-extend.toml
whisper-main/.espectacular/knowledge-append/trailing-whitespace-collapse.toml
whisper-main/.espectacular/managed-block/
whisper-main/.espectacular/managed-block/content-matches-resolve.toml
whisper-main/.espectacular/managed-block/file-override.toml
whisper-main/.espectacular/managed-block/first-sync-creates-the-block.toml
whisper-main/.espectacular/managed-block/re-sync-updates-in-place.toml
whisper-main/.espectacular/managed-block/target-file-missing.toml
whisper-main/.espectacular/shared-store/
whisper-main/.espectacular/shared-store/bundle-carries-no-transport-state.toml
whisper-main/.espectacular/shared-store/deterministic-pack.toml
whisper-main/.espectacular/shared-store/legacy-bundle-unpacks-into-current-resolution.toml
whisper-main/.espectacular/shared-store/merge-into-an-existing-workspace.toml
whisper-main/.espectacular/shared-store/pack-group-scope-with-no-active-group.toml
whisper-main/.espectacular/shared-store/pack-refuses-private-resolved-scopes.toml
whisper-main/.espectacular/shared-store/pack-with-private-content.toml
whisper-main/.espectacular/shared-store/round-trip-into-a-fresh-workspace.toml
whisper-main/.espectacular/shared-store/unpack-never-writes-into-the-private-zone.toml
whisper-main/.espectacular/workspace-maintenance/
whisper-main/.espectacular/workspace-maintenance/canonical-dir-absent.toml
whisper-main/.espectacular/workspace-maintenance/check-flags-legacy-variants.toml
whisper-main/.espectacular/workspace-maintenance/fresh-init-adds-the-rule.toml
whisper-main/.espectacular/workspace-maintenance/fresh-init.toml
whisper-main/.espectacular/workspace-maintenance/idempotent-ignore-rule.toml
whisper-main/.espectacular/workspace-maintenance/idempotent-re-init.toml
whisper-main/.espectacular/workspace-maintenance/leak-shaped-content-in-public-files.toml
whisper-main/.espectacular/workspace-maintenance/merge-extends-without-duplicating.toml
whisper-main/.espectacular/workspace-maintenance/private-zone-not-effectively-ignored.toml
whisper-main/.espectacular/workspace-maintenance/status-is-side-effect-free.toml
whisper-main/.espectacular/workspace-maintenance/tracked-file-under-the-private-zone.toml
whisper-main/.espectacular/workspace-maintenance/unrelated-colon-dirs-are-safe.toml
whisper-main/.espectacular/workspace-routing/
whisper-main/.espectacular/workspace-routing/bare-repo.toml
whisper-main/.espectacular/workspace-routing/branch-scope-resolves-into-the-checkout.toml
whisper-main/.espectacular/workspace-routing/consolidate-cannot-reach-the-private-zone.toml
whisper-main/.espectacular/workspace-routing/doctor-flags-stale-checkout-layer-content-under-machine-local.toml
whisper-main/.espectacular/workspace-routing/feature-branch.toml
whisper-main/.espectacular/workspace-routing/global-escape-hatch.toml
whisper-main/.espectacular/workspace-routing/group-scope-without-an-active-group.toml
whisper-main/.espectacular/workspace-routing/https-remote.toml
whisper-main/.espectacular/workspace-routing/init-under-machine-local-routing-provisions-only-the-store.toml
whisper-main/.espectacular/workspace-routing/linked-worktree-shares-the-slot.toml
whisper-main/.espectacular/workspace-routing/machine-local-routing-is-the-persistent-default.toml
whisper-main/.espectacular/workspace-routing/no-remote.toml
whisper-main/.espectacular/workspace-routing/pre-existing-global-store-knowledge-stays-servable.toml
whisper-main/.espectacular/workspace-routing/private-routing-flag.toml
whisper-main/.espectacular/workspace-routing/recall-serves-private-knowledge-locally.toml
whisper-main/.espectacular/workspace-routing/repo-local-remains-the-default-without-a-routing-key.toml
whisper-main/.espectacular/workspace-routing/ssh-remote.toml
whisper-main/.espectacular/workspace-routing/store-major-composition-order.toml
whisper-main/.espectacular/workspace-routing/the-private-zone-override-composes-over-the-declared-mode.toml
whisper-main/.espectacular/workspace-routing/unknown-routing-mode-is-rejected-with-the-valid-values.toml
whisper-main/.espectacular/workspace-routing/unknown-scope-rejected.toml
whisper-main/.genesis/
whisper-main/.genesis/tools.toml
whisper-main/.github/
whisper-main/.github/workflows/
whisper-main/.github/workflows/ci.yml
whisper-main/.github/workflows/docs.yml
whisper-main/.github/workflows/release.yml
whisper-main/.gitignore
whisper-main/.turu/
whisper-main/.turu/skills/
whisper-main/.turu/skills/whisper/
whisper-main/.turu/skills/whisper/subs/
whisper-main/.turu/skills/whisper/subs/append.md
whisper-main/.turu/skills/whisper/subs/consolidate-manual.md
whisper-main/.turu/skills/whisper/subs/decommission-manual.md
whisper-main/.turu/skills/whisper/subs/doctor.md
whisper-main/.turu/skills/whisper/subs/init.md
whisper-main/.turu/skills/whisper/subs/key.md
whisper-main/.turu/skills/whisper/subs/link-manual.md
whisper-main/.turu/skills/whisper/subs/resolve.md
whisper-main/.turu/skills/whisper/subs/status.md

## Assistant

bash -lc python - <<'PY'
import zipfile, os
for zpath in ['/mnt/data/bajan-main(2).zip','/mnt/data/whisper-main.zip']:
    z=zipfile.ZipFile(zpath)
    print('\n###',os.path.basename(zpath))
    for n in z.namelist():
        if n.endswith('/') or '/.git/' in n: continue
        base=n.split('/')[-1]
        if (n.count('/')<=2 and (base.lower().startswith(('readme','architecture','design','concept','manifest','cargo','pyproject','package','justfile','makefile','agents','todo','roadmap','changelog')) or base.endswith(('.md','.toml','.yaml','.yml')))):
            print(n)
PY

## Tool

### bajan-main(2).zip
bajan-main/.beads/config.yaml
bajan-main/.cargo/config.toml
bajan-main/.espectacular/AGENTS.md
bajan-main/.espectacular/config.toml
bajan-main/.genesis/tools.toml
bajan-main/.wai/AGENTS.md
bajan-main/.wai/PLUGINS.md
bajan-main/.wai/config.toml
bajan-main/AGENTS.md
bajan-main/CHANGELOG.md
bajan-main/CLAUDE.md
bajan-main/Cargo.lock
bajan-main/Cargo.toml
bajan-main/README.md
bajan-main/converters/Cargo.lock
bajan-main/converters/Cargo.toml
bajan-main/converters/README.md
bajan-main/docs/knowledge-assistant-ears-spec.md
bajan-main/evals/results.md
bajan-main/justfile
bajan-main/knowledge-graphs-report.md
bajan-main/lefthook.yml
bajan-main/openspec/AGENTS.md
bajan-main/openspec/project.md
bajan-main/pretender.toml
bajan-main/specodelic/contradiction-review.toml
bajan-main/specodelic/entity-review.toml
bajan-main/specodelic/eval-claims.toml
bajan-main/specodelic/extraction-claims.toml
bajan-main/specodelic/graph-model.toml
bajan-main/specodelic/ingestion-contract.toml
bajan-main/specodelic/query-tools.toml
bajan-main/specs/contradiction-review.md
bajan-main/specs/entity-review.md
bajan-main/specs/eval-claims.md
bajan-main/specs/extraction-claims.md
bajan-main/specs/graph-model.md
bajan-main/specs/ingestion-contract.md
bajan-main/specs/query-tools.md
bajan-main/testaruda.toml

### whisper-main.zip
whisper-main/.beads/README.md
whisper-main/.beads/config.yaml
whisper-main/.ddl/config.toml
whisper-main/.ddl/manifest.json
whisper-main/.espectacular/AGENTS.md
whisper-main/.espectacular/config.toml
whisper-main/.genesis/tools.toml
whisper-main/.wai/AGENTS.md
whisper-main/.wai/PLUGINS.md
whisper-main/.wai/config.toml
whisper-main/.whisper/env.md
whisper-main/AGENTS.md
whisper-main/CHANGELOG.md
whisper-main/CLAUDE.md
whisper-main/Cargo.lock
whisper-main/Cargo.toml
whisper-main/README.md
whisper-main/book.toml
whisper-main/justfile
whisper-main/lefthook.yml
whisper-main/openspec/AGENTS.md
whisper-main/openspec/project.md
whisper-main/pretender.toml
whisper-main/testaruda.toml
whisper-main/versions.ddl.toml

## Assistant

bash -lc python - <<'PY'
import zipfile
for zpath in ['/mnt/data/bajan-main(2).zip','/mnt/data/whisper-main.zip']:
 z=zipfile.ZipFile(zpath)
 print('\n###',zpath)
 roots=set()
 for n in z.namelist():
  if n.endswith('/'): continue
  parts=n.split('/')
  if len(parts)>1 and parts[1] not in {'.git','.beads','.cargo','.claude','.espectacular','.genesis','.github','.wai','.turu','.ddl','.whisper','target'}:
   roots.add(parts[1])
 print('\n'.join(sorted(roots)))
 print('\nSource files sample:')
 for n in z.namelist():
  if '/src/' in n and not n.endswith('/'):
   print(n)
PY

## Tool

### /mnt/data/bajan-main(2).zip
.beads.gate.lock
.gitignore
AGENTS.md
CHANGELOG.md
CLAUDE.md
Cargo.lock
Cargo.toml
LICENSE
README.md
converters
docs
evals
justfile
knowledge-graphs-report.md
lefthook.yml
openspec
pretender.toml
proptest-regressions
scripts
site
specodelic
specs
src
testaruda.toml
tests
tools

Source files sample:
bajan-main/converters/src/bin/epub2bajan.rs
bajan-main/converters/src/bin/html2bajan.rs
bajan-main/converters/src/bin/md2bajan.rs
bajan-main/converters/src/bin/pdf2bajan.rs
bajan-main/converters/src/lib.rs
bajan-main/src/cli.rs
bajan-main/src/config.rs
bajan-main/src/contradict.rs
bajan-main/src/eval.rs
bajan-main/src/extract.rs
bajan-main/src/ingest.rs
bajan-main/src/lib.rs
bajan-main/src/llm.rs
bajan-main/src/main.rs
bajan-main/src/propose.rs
bajan-main/src/query.rs
bajan-main/src/resolve.rs
bajan-main/src/review.rs
bajan-main/src/store/mod.rs
bajan-main/src/store/nodes.rs
bajan-main/src/store/sqlite.rs

### /mnt/data/whisper-main.zip
.gitignore
AGENTS.md
CHANGELOG.md
CLAUDE.md
Cargo.lock
Cargo.toml
LICENSE
README.md
book.toml
docs
justfile
lefthook.yml
llm.txt
llms.txt
openspec
pretender-baseline.json
pretender.toml
scripts
src
testaruda.toml
tests
theme
versions.ddl.toml

Source files sample:
whisper-main/docs/src/SUMMARY.md
whisper-main/docs/src/cli.md
whisper-main/docs/src/configuration.md
whisper-main/docs/src/getting-started.md
whisper-main/docs/src/index.md
whisper-main/docs/src/status.md
whisper-main/src/bundle.rs
whisper-main/src/cmds/admin.rs
whisper-main/src/cmds/knowledge.rs
whisper-main/src/cmds/mod.rs
whisper-main/src/cmds/support.rs
whisper-main/src/config.rs
whisper-main/src/distill.rs
whisper-main/src/doctor/checks.rs
whisper-main/src/doctor/content.rs
whisper-main/src/doctor/leaks.rs
whisper-main/src/doctor/managed.rs
whisper-main/src/doctor/mod.rs
whisper-main/src/doctor/routing.rs
whisper-main/src/doctor/tests.rs
whisper-main/src/entry.rs
whisper-main/src/lib.rs
whisper-main/src/main.rs
whisper-main/src/recall.rs
whisper-main/src/serving.rs
whisper-main/src/skill_pack.rs
whisper-main/src/usage.rs
whisper-main/src/workspace/block.rs
whisper-main/src/workspace/init.rs
whisper-main/src/workspace/layout.rs
whisper-main/src/workspace/mod.rs
whisper-main/src/workspace/resolve.rs
whisper-main/src/workspace/scope.rs
whisper-main/src/workspace/tests.rs

## Assistant

bash -lc python - <<'PY'
import zipfile
files = {
'bajan-main(2).zip': ['bajan-main/README.md','bajan-main/AGENTS.md','bajan-main/Cargo.toml','bajan-main/docs/knowledge-assistant-ears-spec.md','bajan-main/specs/graph-model.md','bajan-main/specs/ingestion-contract.md','bajan-main/specs/extraction-claims.md','bajan-main/specs/query-tools.md','bajan-main/specs/contradiction-review.md','bajan-main/specs/entity-review.md','bajan-main/specs/eval-claims.md','bajan-main/src/lib.rs','bajan-main/src/cli.rs','bajan-main/src/ingest.rs','bajan-main/src/extract.rs','bajan-main/src/query.rs','bajan-main/src/contradict.rs','bajan-main/src/propose.rs','bajan-main/src/review.rs','bajan-main/src/resolve.rs','bajan-main/src/store/mod.rs','bajan-main/src/store/nodes.rs','bajan-main/src/store/sqlite.rs','bajan-main/src/llm.rs','bajan-main/CHANGELOG.md','bajan-main/evals/results.md'],
'whisper-main.zip': ['whisper-main/README.md','whisper-main/AGENTS.md','whisper-main/Cargo.toml','whisper-main/docs/src/index.md','whisper-main/docs/src/getting-started.md','whisper-main/docs/src/cli.md','whisper-main/docs/src/configuration.md','whisper-main/docs/src/status.md','whisper-main/src/lib.rs','whisper-main/src/main.rs','whisper-main/src/entry.rs','whisper-main/src/cmds/knowledge.rs','whisper-main/src/cmds/admin.rs','whisper-main/src/recall.rs','whisper-main/src/serving.rs','whisper-main/src/distill.rs','whisper-main/src/skill_pack.rs','whisper-main/src/workspace/mod.rs','whisper-main/src/workspace/layout.rs','whisper-main/src/workspace/resolve.rs','whisper-main/src/workspace/scope.rs','whisper-main/src/workspace/block.rs','whisper-main/src/workspace/init.rs','whisper-main/CHANGELOG.md']
}
for zp, paths in files.items():
 z=zipfile.ZipFile('/mnt/data/'+zp)
 print('\n\n######## ARCHIVE',zp)
 for p in paths:
  try: s=z.read(p).decode('utf-8')
  except: continue
  print('\n\n'+'='*30+' '+p+' '+'='*30)
  # avoid overwhelming by per file limits
  lines=s.splitlines()
  lim=220 if p.endswith('README.md') or p.endswith('index.md') else 180
  if len(lines)>lim:
   print('\n'.join(f'{i+1}: {x}' for i,x in enumerate(lines[:lim])))
   print(f'... [truncated {len(lines)-lim} lines; total {len(lines)}]')
  else:
   print('\n'.join(f'{i+1}: {x}' for i,x in enumerate(lines)))
PY

## Tool

######## ARCHIVE bajan-main(2).zip


============================== bajan-main/README.md ==============================
1: # bajan
2: 
3: A spec-driven knowledge-graph pipeline CLI — ingest sources, extract claims,
4: query the graph. Rust, SQLite-backed triple store, provenance as graph
5: structure.
6: 
7: Encodes the best practices from
8: [`knowledge-graphs-report.md`](knowledge-graphs-report.md) as enforced,
9: lint-checked specifications (`specs/`, `openspec/`).
10: 
11: Part of the charly-vibes suite; emits suite-envelope JSON on every command.
12: 
13: ## Status
14: 
15: **v0.1.0 — early release.** The deterministic pipeline is spec-complete and
16: CI-gated (specodelic lint, contract tests, property tests). The LLM
17: extraction path is smoke-tested against real providers at book scale but
18: young — see [Known limitations](#known-limitations) before relying on it.
19: 
20: ## Install
21: 
22: ```sh
23: cargo install --path .          # from a checkout — the bajan CLI only
24: cargo install bajan             # once published
25: ```
26: 
27: Requires Rust 1.85+ (edition 2024). The source converters live in the
28: separate `converters/` crate and are built separately:
29: 
30: ```sh
31: cargo build --release --manifest-path converters/Cargo.toml
32: # binaries land in converters/target/release/{epub,html,md,pdf}2bajan
33: ```
34: 
35: ## Data & state
36: 
37: Your whole graph is one SQLite file — **`bajan.db` in the current directory**
38: by default. Point every command at the same file (or a different one) with
39: the global `--db` flag: `bajan --db corpus.db extract`. Claims are referenced
40: by numeric **claim keys**, which appear in extract/query output — text mode
41: shows them as `#N` in the hit list.
42: 
43: ## Workspace config (`bajan.toml`)
44: 
45: An optional strict settings file in the current directory tunes a workspace
46: without touching code. Flat `key = <integer>` lines and `#` comments only —
47: unknown keys, table headers, quotes, and non-integers are refused at startup
48: with a `config_parse` envelope and exit 1. Resolution order is **CLI flag >
49: file > built-in default**; no file is byte-identical default behavior.
50: 
51: ```toml
52: # bajan.toml — workspace tuning (bajan-bku)
53: staleness_window_days = 90   # qt_ranking demotion window (default 365)
54: default_budget = 64          # bounded-traversal budget when --budget is absent (default 256)
55: max_attempts = 5             # LLM retry budget per episode per pass (default 3)
56: ```
57: 
58: API keys never go in this file — the strict key set refuses anything but
59: these three keys; keys stay env-var-NAME based (`BAJAN_EXTRACTOR_*`). Config
60: is not store state: dump-recreate is unaffected.
61: 
62: ## Quickstart
63: 
64: Every command writes a JSON suite envelope to stdout; add `--json` after the
65: subcommand for machine consumption (text mode renders the same envelope in a
66: short human form — same content, never a second format).
67: 
68: ```sh
69: # 1. Convert a source into a normalized episode stream (JSON array)
70: converters/target/release/epub2bajan book.epub > episodes.json
71: 
72: # 2. Ingest — episodes persist verbatim, each gets an outcome record
73: bajan ingest < episodes.json
74: 
75: # 3. Extract claims (default: deterministic `atomic` extractor)
76: bajan extract
77: 
78: # or the LLM extractor (OpenAI-compatible endpoint):
79: # BAJAN_MAX_SPEND_USD is REQUIRED — without it the extractor refuses to
80: # run; when a call would push known spend past the cap, the pass stops
81: # (later episodes stay pending; rerun with a raised cap to resume).
82: # BAJAN_EXTRACTOR_TIMEOUT_SECS raises the per-call HTTP timeout from the
83: # 120s default — reasoning models under load exceed it (must be a
84: # positive integer; misconfiguration refuses at selection).
85: BAJAN_EXTRACTOR=llm \
86: BAJAN_EXTRACTOR_MODEL=deepseek/deepseek-v4-flash \
87: BAJAN_EXTRACTOR_BASE_URL=https://openrouter.ai/api/v1 \
88: BAJAN_EXTRACTOR_API_KEY_ENV=OPENROUTER_API_KEY \
89: BAJAN_MAX_SPEND_USD=0.50 \
90: BAJAN_EXTRACTOR_TIMEOUT_SECS=600 \
91: bajan extract
92: 
93: # 4. Human-in-the-loop adoption of staged claims
94: #    (claim keys come from the extract output / `bajan query` hit list)
95: bajan adopt 1 2 3
96: 
97: # 5. Episode deletion / revival — operator maintenance (ic_deleted_tombstone)
98: bajan delete <episode_id> --actor you   # refused while a claim supports the episode
99: bajan revive <episode_id> --actor you   # the only path that clears a tombstone
100: # A deleted id is retired: every later submission is rejected with the
101: # machine-readable deleted_id reason until revive — re-ingest never
102: # resurrects, and dump-recreate carries the tombstone across rebuilds.
103: 
104: # 6. Entity-review queue — the only human-only resolutions in the pipeline
105: bajan review list
106: bajan review approve <from> <to> --actor you   # merge a duplicate pair
107: bajan review reject <from> <to> --actor you    # drop the merge candidate
108: 
109: # 7. Query — ranked hits with lineage-traceable provenance
110: bajan query "profit" --scope workspace:dev
111: bajan query "profit" --json | jq '.data.hits'
112: 
113: # 8. Contradictions — closed rule set over specific claims, plus an
114: #    optional LLM proposal pass
115: bajan contradict 1 2
116: bajan scan                                     # deterministic contradicts pass
117: bajan propose            # LLM-assisted: stages proposals, never writes edges
118: bajan proposal list
119: bajan proposal approve <from> <to> --actor you  # writes the contradicts edge
120: 
121: # 9. Score an extraction run against a golden corpus (see
122: #    "Evaluating extraction quality" below; the adjudicated corpus
123: #    lives in evals/fixtures/gold-fi4e-v1.json)
124: bajan eval claims --corpus evals/fixtures/gold-fi4e-v1.json --run run.json
125: ```
126: 
127: Concepts:
128: 
129: - **Episode** — a normalized span of source text with a locator and
130:   authority metadata; persisted verbatim, never rewritten.
131: - **Claim** — a claim node derived from episodes, staged until adopted;
132:   lineage edges make provenance part of the graph structure.
133: - **Envelope** — every command answers `{ok, envelope_version, envelope_kind,
134:   data}`; exit status mirrors `ok`.
135: 
136: ## Evaluating extraction quality
137: 
138: `bajan eval claims` scores an extraction run against a **golden corpus** —
139: a versioned fixture of episodes whose true claim sets a human adjudicated
140: (`specs/eval-claims.md`). It publishes precision, recall, and hedge
141: preservation with raw counts, one per-case judgment per candidate. Scoring
142: is deterministic: no embeddings, no LLM judgment, no store access, no wall
143: clock — identical inputs reproduce byte-identical results, and an eval run
144: can never touch a real graph.
145: 
146: The golden corpus is a JSON file; every episode carries the claims the
147: text **should** yield. Constraints: the corpus `version` is required,
148: episode ids and claim texts/spans must be non-empty and unique, `source_count`
149: must be ≥ 1, and `hedges` may only use the anchored vocabulary `may, might,
150: could, possibly, appears, seems, signals, estimates, reportedly, tentative,
151: uncertain` (anything else is rejected):
152: 
153: ```json
154: {
155:   "id": "gold-fi4e", "version": "1",
156:   "episodes": [{
157:     "id": "ep-1", "text": "Profits may vary by run.",
158:     "golden_claims": [{
159:       "text": "Profits may vary by run.", "source_count": 1,
160:       "evidence_span": "Profits may vary by run.", "hedges": ["may"]
161:     }]
162:   }]
163: }
164: ```
165: 
166: The run manifest is the extraction output to score — candidates with their
167: evidence spans, stamped with the run and extractor identities. Export a real
168: manifest from a store with `bajan eval manifest` (bajan-t6z): it carries the
169: store's live candidates (staged and active claims) for the extractor version
170: you name, skipping unknown-evidence candidates and reporting the skip count.
171: With one extra
...[truncated]...
 {
130:         Routing::RepoLocal => global_store_scopes(facts),
131:         Routing::MachineLocal => Vec::new(),
132:     };
133:     for scope in store_scopes {
134:         let target = global_store_target(scope, facts, resolved);
135:         record_ensure(target, report)?;
136:     }
137:     Ok(())
138: }
139: 
140: /// Ensure a target exists and record it as created or existing.
141: fn record_ensure(target: Target, report: &mut InitReport) -> Result<()> {
142:     if target.ensure().map_err(WhisperError::from)? {
143:         report.created.push(target.path);
144:     } else {
145:         report.existing.push(target.path);
146:     }
147:     Ok(())
148: }
149: 
150: /// Branch slot also carries context.md and plan.md per the skill layout;
151: /// it follows the branch scope's resolved home (checkout or store).
152: fn provision_branch_files(
153:     facts: &Facts,
154:     resolved: &Resolved,
155:     report: &mut InitReport,
156: ) -> Result<()> {
157:     let branch_dir = resolve(Scope::Branch, facts, resolved)?
158:         .path
159:         .parent()
160:         .expect("branch target always has a parent (the branch dir)")
161:         .to_path_buf();
162:     for name in ["context.md", "plan.md"] {
163:         let path = branch_dir.join(name);
164:         if !path.exists() {
165:             std::fs::create_dir_all(&branch_dir)?;
166:             std::fs::File::create(&path)?;
167:             report.created.push(path);
168:         } else {
169:             report.existing.push(path);
170:         }
171:     }
172:     Ok(())
173: }
174: 
175: /// Legacy repo-key directory variants for this repo (non-canonical dirs
176: /// under `repos/` that plausibly refer to the same repo).
177: pub fn legacy_variants(facts: &Facts, resolved: &Resolved) -> Vec<String> {
178:     let repos_dir = resolved.knowledge_root().join("repos");
179:     let Ok(entries) = std::fs::read_dir(&repos_dir) else {
180:         return Vec::new();
... [truncated 157 lines; total 337]


============================== whisper-main/CHANGELOG.md ==============================
1: # Changelog
2: 
3: All notable changes to this project will be documented in this file.
4: 
5: The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
6: and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
7: 
8: ## [0.6.0] - 2026-09-17
9: 
10: ### Added
11: 
12: - `turu feedback <kind> [--from-last-error] [--dry-run]` (`whisper-1ug`) — file a well-contexted GitHub issue via `genesis::feedback`: kind validation with typo suggestions, content from piped stdin or error-scratch recall, `--dry-run` preview of the redacted body and `gh` command; kind-specific error suggestions (Rule-of-5)
13: - Error-scratch contract: failing turu commands persist a best-effort second-precision scratch record (same shape as the genesis Guide's ErrorSink) so `turu feedback bug --from-last-error` has data to recall
14: - Managed block generator lists `turu feedback <kind>`; genesis API compatibility fixture (vampiro's pattern)
15: 
16: ## [0.5.0] - 2026-09-17
17: 
18: ### Added
19: 
20: - `turu.shadowed-global` doctor check (`whisper-122`) — when a repo-private `workspace_root` override is active, surfaces that it shadows the global scope: a hidden global `rules.md` warns, diverged copies warn with both paths, in-sync copies pass informationally
21: - `turu check` warns when the repo-private root hides or diverges from the global `rules.md` (previously only `turu doctor` reported it)
22: 
23: ### Fixed
24: 
25: - A repo-private `workspace_root` with a **relative** path now anchors to the directory containing the repo config instead of the process cwd (GH #1) — `turu` invoked from a subdirectory no longer materializes a stray `<subdir>/.whisper/` workspace tree; absolute and `~` paths are unchanged
26: 
27: ## [0.4.0] - 2026-09-15
28: 
29: ### Added
30: 
31: - Structured, idempotent knowledge entries (`add-entry-model`): every appended fact becomes a ledger line carrying a full sha2 id (scope + second-precision UTC + text), a timestamp, an optional `--topic` key, and mechanical `--supersedes` marking; duplicate appends are no-ops reported as `duplicate`; freeform content is preserved verbatim; `TURU_NOW` env override gives reproducible timestamps
32: - `turu recall <scope> [--topic] [--budget] [--include-superseded]` (`add-recall-serving`) — ranked, whole-entry-atomic slice serving; `all` composes scopes in precedence order; the envelope reports the context-horizon boundary (`served_bytes`, `budget_unused`, `entries_skipped`, `freeform_skipped`) so the agent can decide when to load memory at all
33: - `turu distill <scope> --begin|--commit --revision <id>` (`add-distill-contract`) — two-phase contract: turu snapshots the scope into immutable revisions and guards the commit against concurrent drift; the calling agent performs the semantic rewrite into the working file; replay is a reported no-op; revisions are never pruned
34: - `turu bundle pack|unpack` (`add-shared-bundle`) — deterministic, transport-agnostic knowledge bundles keyed by the canonical repo key; unpack merges extend-without-duplicate and never overwrites (strategic transport fork documented as open in `openspec/changes/add-shared-bundle/design.md`)
35: - doctor checks: `turu.entry-format` (unmanaged freeform lines), `turu.distill-pending` (revisions begun but not committed)
36: - `openspec/` baseline specs for existing behavior (workspace-routing, knowledge-append, config-precedence, managed-block, workspace-maintenance) + lifecycle change proposals
37: 
38: ### Changed
39: 
40: - `turu append` writes structured entry lines instead of verbatim text; appends use a single O_APPEND write so concurrent agents cannot lose each other's entries (full rewrite only for `--supersedes` marking); multi-line input is normalized (per-line leading whitespace stripped, id computed over the normalized text)
41: - envelope `appended_bytes` reports the rendered line length actually written, not the raw input length
42: - entry parsing requires canonical RFC-3339 seconds timestamps — malformed lines degrade to unmanaged freeform instead of corrupting recency ordering
43: 
44: ## [0.3.0] - 2026-02-20
45: 
46: ### Added
47: 
48: - `turu skill install [<dir>]` — first-party whisper skill pack shipped from this repo (dont's `skill_pack` pattern): deterministic generation, content hashes, 11 files (router + 10 sub-skills including manual fallbacks for link/decommission/consolidate)
49: - `turu.managed-skills` doctor check — flags stale packs via content hashes (missing pack passes as optional)
50: - Incitaciones whisper skill converted to a thin pointer that delegates to the CLI
51: 
52: ## [0.2.0] - 2026-02-20
53: 
54: ### Added
55: 
56: - `turu doctor` — deep workspace diagnostics via genesis doctor conventions: rules file, repo/branch slots, legacy key variants, group health, managed block presence (each check carries a fix hint)
57: - `turu sync` — inject/refresh the `<!-- TURU:START -->` managed block in AGENTS.md with the deterministic routing map, so agents read paths from a file instead of re-deriving them
58: 
59: ### Changed
60: 
61: - **Main command renamed to `turu`** (the song's turututu riff); `turututu` and `whisper` ship as alias bins
62: 
63: ## [0.1.0] - 2026-02-20
64: 
65: ### Added
66: 
67: - `whisper key` — canonical repo key, branch slug, and worktree slot derived deterministically from git facts
68: - `whisper resolve <scope>` — exact destination path for a knowledge scope (`global | repo | branch | worktree | group`)
69: - `whisper append <scope>` — verbatim extend-don't-duplicate writes with parent creation
70: - `whisper init` — workspace layout creation, never overwrites
71: - `whisper status` — full path map and existence flags in one envelope
72: - `whisper check` — legacy key-variant detection and missing-file warnings
73: - Layered config: global (`~/.config/whisper/config.toml`) > group (`[groups.*]`) > repo (`.whisper/config.toml`, gitignored)
74: - Genesis envelope output: `--json` / `--human` with progressive verbosity

## Assistant

bash -lc mkdir -p /tmp/review && cd /tmp/review && unzip -oq /mnt/data/bajan-main\(2\).zip && unzip -oq /mnt/data/whisper-main.zip && echo extracted && find bajan-main/src whisper-main/src -type f | sort

## Tool

extracted
bajan-main/src/cli.rs
bajan-main/src/config.rs
bajan-main/src/contradict.rs
bajan-main/src/eval.rs
bajan-main/src/extract.rs
bajan-main/src/ingest.rs
bajan-main/src/lib.rs
bajan-main/src/llm.rs
bajan-main/src/main.rs
bajan-main/src/propose.rs
bajan-main/src/query.rs
bajan-main/src/resolve.rs
bajan-main/src/review.rs
bajan-main/src/store/mod.rs
bajan-main/src/store/nodes.rs
bajan-main/src/store/sqlite.rs
whisper-main/src/bundle.rs
whisper-main/src/cmds/admin.rs
whisper-main/src/cmds/knowledge.rs
whisper-main/src/cmds/mod.rs
whisper-main/src/cmds/support.rs
whisper-main/src/config.rs
whisper-main/src/distill.rs
whisper-main/src/doctor/checks.rs
whisper-main/src/doctor/content.rs
whisper-main/src/doctor/leaks.rs
whisper-main/src/doctor/managed.rs
whisper-main/src/doctor/mod.rs
whisper-main/src/doctor/routing.rs
whisper-main/src/doctor/tests.rs
whisper-main/src/entry.rs
whisper-main/src/lib.rs
whisper-main/src/main.rs
whisper-main/src/recall.rs
whisper-main/src/serving.rs
whisper-main/src/skill_pack.rs
whisper-main/src/usage.rs
whisper-main/src/workspace/block.rs
whisper-main/src/workspace/init.rs
whisper-main/src/workspace/layout.rs
whisper-main/src/workspace/mod.rs
whisper-main/src/workspace/resolve.rs
whisper-main/src/workspace/scope.rs
whisper-main/src/workspace/tests.rs

## Assistant

bash -lc python - <<'PY'
from pathlib import Path
paths = [
'/tmp/review/bajan-main/README.md','/tmp/review/bajan-main/knowledge-graphs-report.md','/tmp/review/bajan-main/specs/graph-model.md','/tmp/review/bajan-main/specs/ingestion-contract.md','/tmp/review/bajan-main/specs/extraction-claims.md','/tmp/review/bajan-main/specs/query-tools.md','/tmp/review/bajan-main/specs/contradiction-review.md','/tmp/review/bajan-main/specs/entity-review.md','/tmp/review/bajan-main/docs/knowledge-assistant-ears-spec.md',
'/tmp/review/whisper-main/README.md','/tmp/review/whisper-main/docs/src/index.md','/tmp/review/whisper-main/docs/src/getting-started.md','/tmp/review/whisper-main/docs/src/cli.md','/tmp/review/whisper-main/docs/src/configuration.md','/tmp/review/whisper-main/docs/src/status.md']
for p in paths:
 s=Path(p).read_text()
 print('\n\n### '+p+' ('+str(len(s.splitlines()))+' lines)')
 lines=s.splitlines()
 # select max 200 lines each
 for i,l in enumerate(lines[:200],1): print(f'{i}: {l}')
 if len(lines)>200: print(f'... TRUNCATED {len(lines)-200} more lines')
PY

## Tool

### /tmp/review/bajan-main/README.md (269 lines)
1: # bajan
2: 
3: A spec-driven knowledge-graph pipeline CLI — ingest sources, extract claims,
4: query the graph. Rust, SQLite-backed triple store, provenance as graph
5: structure.
6: 
7: Encodes the best practices from
8: [`knowledge-graphs-report.md`](knowledge-graphs-report.md) as enforced,
9: lint-checked specifications (`specs/`, `openspec/`).
10: 
11: Part of the charly-vibes suite; emits suite-envelope JSON on every command.
12: 
13: ## Status
14: 
15: **v0.1.0 — early release.** The deterministic pipeline is spec-complete and
16: CI-gated (specodelic lint, contract tests, property tests). The LLM
17: extraction path is smoke-tested against real providers at book scale but
18: young — see [Known limitations](#known-limitations) before relying on it.
19: 
20: ## Install
21: 
22: ```sh
23: cargo install --path .          # from a checkout — the bajan CLI only
24: cargo install bajan             # once published
25: ```
26: 
27: Requires Rust 1.85+ (edition 2024). The source converters live in the
28: separate `converters/` crate and are built separately:
29: 
30: ```sh
31: cargo build --release --manifest-path converters/Cargo.toml
32: # binaries land in converters/target/release/{epub,html,md,pdf}2bajan
33: ```
34: 
35: ## Data & state
36: 
37: Your whole graph is one SQLite file — **`bajan.db` in the current directory**
38: by default. Point every command at the same file (or a different one) with
39: the global `--db` flag: `bajan --db corpus.db extract`. Claims are referenced
40: by numeric **claim keys**, which appear in extract/query output — text mode
41: shows them as `#N` in the hit list.
42: 
43: ## Workspace config (`bajan.toml`)
44: 
45: An optional strict settings file in the current directory tunes a workspace
46: without touching code. Flat `key = <integer>` lines and `#` comments only —
47: unknown keys, table headers, quotes, and non-integers are refused at startup
48: with a `config_parse` envelope and exit 1. Resolution order is **CLI flag >
49: file > built-in default**; no file is byte-identical default behavior.
50: 
51: ```toml
52: # bajan.toml — workspace tuning (bajan-bku)
53: staleness_window_days = 90   # qt_ranking demotion window (default 365)
54: default_budget = 64          # bounded-traversal budget when --budget is absent (default 256)
55: max_attempts = 5             # LLM retry budget per episode per pass (default 3)
56: ```
57: 
58: API keys never go in this file — the strict key set refuses anything but
59: these three keys; keys stay env-var-NAME based (`BAJAN_EXTRACTOR_*`). Config
60: is not store state: dump-recreate is unaffected.
61: 
62: ## Quickstart
63: 
64: Every command writes a JSON suite envelope to stdout; add `--json` after the
65: subcommand for machine consumption (text mode renders the same envelope in a
66: short human form — same content, never a second format).
67: 
68: ```sh
69: # 1. Convert a source into a normalized episode stream (JSON array)
70: converters/target/release/epub2bajan book.epub > episodes.json
71: 
72: # 2. Ingest — episodes persist verbatim, each gets an outcome record
73: bajan ingest < episodes.json
74: 
75: # 3. Extract claims (default: deterministic `atomic` extractor)
76: bajan extract
77: 
78: # or the LLM extractor (OpenAI-compatible endpoint):
79: # BAJAN_MAX_SPEND_USD is REQUIRED — without it the extractor refuses to
80: # run; when a call would push known spend past the cap, the pass stops
81: # (later episodes stay pending; rerun with a raised cap to resume).
82: # BAJAN_EXTRACTOR_TIMEOUT_SECS raises the per-call HTTP timeout from the
83: # 120s default — reasoning models under load exceed it (must be a
84: # positive integer; misconfiguration refuses at selection).
85: BAJAN_EXTRACTOR=llm \
86: BAJAN_EXTRACTOR_MODEL=deepseek/deepseek-v4-flash \
87: BAJAN_EXTRACTOR_BASE_URL=https://openrouter.ai/api/v1 \
88: BAJAN_EXTRACTOR_API_KEY_ENV=OPENROUTER_API_KEY \
89: BAJAN_MAX_SPEND_USD=0.50 \
90: BAJAN_EXTRACTOR_TIMEOUT_SECS=600 \
91: bajan extract
92: 
93: # 4. Human-in-the-loop adoption of staged claims
94: #    (claim keys come from the extract output / `bajan query` hit list)
95: bajan adopt 1 2 3
96: 
97: # 5. Episode deletion / revival — operator maintenance (ic_deleted_tombstone)
98: bajan delete <episode_id> --actor you   # refused while a claim supports the episode
99: bajan revive <episode_id> --actor you   # the only path that clears a tombstone
100: # A deleted id is retired: every later submission is rejected with the
101: # machine-readable deleted_id reason until revive — re-ingest never
102: # resurrects, and dump-recreate carries the tombstone across rebuilds.
103: 
104: # 6. Entity-review queue — the only human-only resolutions in the pipeline
105: bajan review list
106: bajan review approve <from> <to> --actor you   # merge a duplicate pair
107: bajan review reject <from> <to> --actor you    # drop the merge candidate
108: 
109: # 7. Query — ranked hits with lineage-traceable provenance
110: bajan query "profit" --scope workspace:dev
111: bajan query "profit" --json | jq '.data.hits'
112: 
113: # 8. Contradictions — closed rule set over specific claims, plus an
114: #    optional LLM proposal pass
115: bajan contradict 1 2
116: bajan scan                                     # deterministic contradicts pass
117: bajan propose            # LLM-assisted: stages proposals, never writes edges
118: bajan proposal list
119: bajan proposal approve <from> <to> --actor you  # writes the contradicts edge
120: 
121: # 9. Score an extraction run against a golden corpus (see
122: #    "Evaluating extraction quality" below; the adjudicated corpus
123: #    lives in evals/fixtures/gold-fi4e-v1.json)
124: bajan eval claims --corpus evals/fixtures/gold-fi4e-v1.json --run run.json
125: ```
126: 
127: Concepts:
128: 
129: - **Episode** — a normalized span of source text with a locator and
130:   authority metadata; persisted verbatim, never rewritten.
131: - **Claim** — a claim node derived from episodes, staged until adopted;
132:   lineage edges make provenance part of the graph structure.
133: - **Envelope** — every command answers `{ok, envelope_version, envelope_kind,
134:   data}`; exit status mirrors `ok`.
135: 
136: ## Evaluating extraction quality
137: 
138: `bajan eval claims` scores an extraction run against a **golden corpus** —
139: a versioned fixture of episodes whose true claim sets a human adjudicated
140: (`specs/eval-claims.md`). It publishes precision, recall, and hedge
141: preservation with raw counts, one per-case judgment per candidate. Scoring
142: is deterministic: no embeddings, no LLM judgment, no store access, no wall
143: clock — identical inputs reproduce byte-identical results, and an eval run
144: can never touch a real graph.
145: 
146: The golden corpus is a JSON file; every episode carries the claims the
147: text **should** yield. Constraints: the corpus `version` is required,
148: episode ids and claim texts/spans must be non-empty and unique, `source_count`
149: must be ≥ 1, and `hedges` may only use the anchored vocabulary `may, might,
150: could, possibly, appears, seems, signals, estimates, reportedly, tentative,
151: uncertain` (anything else is rejected):
152: 
153: ```json
154: {
155:   "id": "gold-fi4e", "version": "1",
156:   "episodes": [{
157:     "id": "ep-1", "text": "Profits may vary by run.",
158:     "golden_claims": [{
159:       "text": "Profits may vary by run.", "source_count": 1,
160:       "evidence_span": "Profits may vary by run.", "hedges": ["may"]
161:     }]
162:   }]
163: }
164: ```
165: 
166: The run manifest is the extraction output to score — candidates with their
167: evidence spans, stamped with the run and extractor identities. Export a real
168: manifest from a store with `bajan eval manifest` (bajan-t6z): it carries the
169: store's live candidates (staged and active claims) for the extractor version
170: you name, skipping unknown-evidence candidates and reporting the skip count.
171: With one extraction run in the store the version is picked automatically;
172: with s
...[truncated]...
te/` — readable locally, structurally never pushed (repo/branch only)
17: 
18: ## `turu append <scope> --text "..."`
19: 
20: Append text to a scope's file (extend, don't duplicate). Entries are
21: structured and idempotent: sha2 ids over scope + second-precision UTC + text;
22: freeform content preserved verbatim.
23: 
24: - `--text` — text to append (repeatable)
25: - `--stdin` — read the text from stdin instead of `--text`
26: - `--topic <k>` — optional topic key (bare word, no whitespace/parens/#)
27: - `--supersedes <id>` — mark the entry with this id as superseded by the new entry
28: - `--global` / `--private` — as `resolve`
29: 
30: ## `turu recall <scope>`
31: 
32: Serve a ranked, budget-bounded slice of a scope's entries. Whole entries only
33: (never truncated); reports `served_bytes`, `budget_unused`, `entries_skipped`.
34: 
35: - scope may be `all` — composes scopes in precedence order
36: - `--topic <k>` — only entries with this topic key
37: - `--budget <bytes>` — byte budget
38: - `--include-superseded` — include superseded entries
39: - `--read-only` — skip usage telemetry (sidecar untouched)
40: 
41: ## `turu distill <scope>`
42: 
43: Two-phase distill contract: snapshot, agent rewrites, guarded commit.
44: 
45: - `--begin` — snapshot the current state and return the working paths
46: - `--commit --revision <id>` — install the distilled working file for this revision
47: - Guards the commit against concurrent drift between snapshot and commit
48: 
49: ## `turu bundle pack|unpack`
50: 
51: Deterministic, transport-agnostic knowledge bundles keyed by repo key.
52: Unpack merges extend-without-duplicate and never overwrites.
53: 
54: ## `turu init`
55: 
56: Create the workspace layout for this checkout (never overwrites).
57: 
58: ## `turu status`
59: 
60: One envelope with every relevant path and existence flag.
61: 
62: ## `turu check`
63: 
64: Detect legacy key variants, undefined groups, and missing files.
65: 
66: ## `turu consolidate`
67: 
68: Migrate legacy repo-key directories into the canonical key.
69: 
70: ## `turu doctor`
71: 
72: Deep workspace diagnostics: layout integrity, group health, legacy keys,
73: managed block, skill pack staleness, and the private-zone contract
74: (`private-ignore`, `private-tracked`, `private-leaks`).
75: 
76: ## `turu sync`
77: 
78: Inject/refresh the turu managed block (`<!-- TURU:START -->`) in the
79: agent-facing file (default: `AGENTS.md` at the repo root), so agents read
80: paths from a file instead of re-deriving them.
81: 
82: ## `turu feedback <kind>`
83: 
84: File a well-contexted GitHub issue (`bug`, `feature`, `question`, `chore`):
85: redacted context bundle, optional `--from-last-error` scratch recall,
86: `--dry-run` preview (via `genesis::feedback`).
87: 
88: ## `turu skill install`
89: 
90: Ship the whisper skill from this repo: router + sub-skills (including manual
91: fallbacks), content-hashed so `turu doctor` flags staleness. Targets
92: `~/.claude/skills` or any dir; incitaciones keeps a thin pointer to it.


### /tmp/review/whisper-main/docs/src/configuration.md (59 lines)
1: # Configuration
2: 
3: Where knowledge gets written is layered. Precedence: **repo > group > global**.
4: 
5: ## Global
6: 
7: `~/.config/whisper/config.toml`:
8: 
9: ```toml
10: workspace_root = "~/.whisper"   # default
11: 
12: [groups.cv-tools]
13: root = "~/para/areas/dev/gh/charly/knowledge"
14: repos = ["cv/charly-vibes/whisper"]   # explicit membership (optional)
15: ```
16: 
17: A **group** routes knowledge from a set of repos into one shared workspace
18: directory instead of each repo's private slot.
19: 
20: ## Repo (private)
21: 
22: `<repo>/.whisper/config.toml` (gitignored — never committed):
23: 
24: ```toml
25: group = "cv-tools"              # join a group defined in the global config
26: workspace_root = "/path/to/dir" # or fully override the workspace root
27: ```
28: 
29: A repo can join a group two ways: privately, via its own `.whisper/config.toml`,
30: or centrally, by listing its canonical key in the group's `repos` array.
31: 
32: > **Note:** a repo-private `workspace_root` overrides *everything* — including
33: > the global scope, so the repo's `rules.md` resolves inside the private root
34: > instead of the shared workspace. `turu doctor` reports this shadowing and
35: > warns when the two `rules.md` files diverge. A relative `workspace_root` is
36: > anchored to the directory containing the repo config (not the process cwd),
37: > so calls from any subdirectory resolve to the same root.
38: 
39: ## Knowledge transport & the private zone
40: 
41: | Scope | In a checkout (default) | `--global` escape hatch |
42: |---|---|---|
43: | `repo` | `<repo>/.whisper/env.md` (committed) | `<workspace>/repos/<key>/env.md` |
44: | `branch` | `<repo>/.whisper/branches/<slug>/notes.md` (committed) | `<workspace>/repos/<key>/branches/<slug>/notes.md` |
45: | `--private` repo/branch | `<repo>/.whisper/private/…` — **gitignored, never pushed** | — |
46: 
47: Transport decision: the repo's own git carries the shared knowledge. Repo-local
48: publication assumes a pushable checkout — `--global` is the fallback for
49: read-only checkouts (CI, no-push contributors).
50: 
51: The private zone is enforced by `turu doctor` with three checks:
52: 
53: - `turu.private-ignore` — the zone is *effectively* ignored (warning + fix hint otherwise)
54: - `turu.private-tracked` — **fails prominently** if any file under `private/` is tracked
55: - `turu.private-leaks` — advisory lint for machine paths, hostnames, and token-shaped strings in public repo-local files (surfaces via `warnings[]`)
56: 
57: Git history is forever — prevention only. No turu verb can retract committed
58: knowledge; that is exactly why the private zone exists and why the tracked-files
59: check fails instead of warning.


### /tmp/review/whisper-main/docs/src/status.md (43 lines)
1: # Status
2: 
3: `whisper` **[current release](./release.md)** — Status: **beta**. Core (key/resolve/append/recall/distill)
4: works and is used in anger by other ecosystem tools; surface may still shift
5: before 1.0.
6: 
7: ## Implemented
8: 
9: | Command | Status | Notes |
10: |---|---|---|
11: | `turu key` | stable | pure function of remote URL; determinism core |
12: | `turu resolve` | stable | all five scopes + `--global`/`--private` |
13: | `turu append` | stable | idempotent sha2 ids, topics, supersede chain |
14: | `turu recall` | stable | budget-bounded slices, `all` precedence composition, horizon boundary reported |
15: | `turu distill` | stable | two-phase begin/commit with drift guard |
16: | `turu bundle` | stable | pack/unpack, extend-without-duplicate merge |
17: | `turu init` | stable | never overwrites |
18: | `turu status` | stable | single envelope, existence flags |
19: | `turu check` | stable | legacy keys, undefined groups, missing files |
20: | `turu consolidate` | beta | migration of legacy repo-key dirs |
21: | `turu doctor` | stable | layout, groups, managed block, skill staleness, privacy contract |
22: | `turu sync` | stable | TURU managed block in AGENTS.md |
23: | `turu feedback` | beta | genesis::feedback, kinds bug/feature/question/chore |
24: | `turu skill install` | beta | router + sub-skills, content-hashed staleness check |
25: 
26: ## In progress
27: 
28: - Consolidate rollout across repos with legacy key directories (see the
29:   whisper workspace hygiene item in incitaciones' inbox).
30: 
31: ## Mapped to specs
32: 
33: - Envelope/config/feedback conventions: [genesis-vibes](https://github.com/charly-vibes/genesis)
34: - Skill contract: incitaciones `whisper` skill (thin pointer to `turu skill install` output)
35: 
36: ## Dogfooding
37: 
38: - **incitaciones** — the distilled `whisper` skill is a thin pointer to this
39:   repo's skill pack (`turu skill install`)
40: - **session/renew skill** (org agent config) — calls `turu key`, `turu recall
41:   repo/branch` for session history before journal greps
42: - whisper's own CI runs `just ci` (fmt, clippy, tests, locked build); pinned
43:   ecosystem installs tracked in `versions.ddl.toml`

## Assistant

bash -lc sed -n '1,320p' /tmp/review/bajan-main/specs/graph-model.md && printf '\n\n===== INGESTION =====\n' && sed -n '1,300p' /tmp/review/bajan-main/specs/ingestion-contract.md && printf '\n\n===== EXTRACTION =====\n' && sed -n '1,320p' /tmp/review/bajan-main/specs/extraction-claims.md

## Tool

---
id: graph.model
kind: intent
statement: "THE bajan knowledge graph SHALL represent every material claim as a reified claim node linked by lineage edges to verbatim episode nodes and entity nodes"
---

# model

The knowledge model follows the industry practices synthesized in
`knowledge-graphs-report.md`: schema-first beats schema-less; provenance
lives in graph structure, not logs; entity resolution is the cost center.
Claims are reified as nodes — never typed triples between entities — so
multi-source lineage, contradiction edges, and invalidation are
first-class. This supersedes the markdown-page knowledge base of the
earlier knowledge-assistant spec (`docs/knowledge-assistant-ears-spec.md`)
while carrying over its defect classes as graph invariants: verbatim
evidence, source-faithful dating, no silent merges, deletion only by
lineage walk. Deletion leaves a tombstone (`ic_deleted_tombstone` in
ingestion.contract): re-ingest never resurrects a deleted episode, and
recreation requires the explicit revive action — the same
no-automated-recovery discipline as superseded claims' explicit
re-stage. Claims are proposed from the episode stream published by the
`ingestion.contract` spec; the proposal mechanism is specced in
`extraction.claims` and out of scope here. Adoption into the graph is
human-only: the actor requirement (`gm_human_adopt`) follows fpa's
kb-store/kb-review pipeline (`openspec/changes/update-extraction-provenance/design.md`
D2), which independently arrived at the same no-automated-accept rule.

## Constraints

| id | kind | expr | traces_to |
|----|------|------|-----------|
| gm_reified | invariant | every claim is a node with at least one `derived_from` edge to an episode node; a claim synthesized from N sources carries N lineage edges, one per episode | [[graph.model]] |
| gm_human_adopt | invariant | a claim moves from `proposed` to `active` only through an explicit human accept action (CLI `bajan adopt`; batch accepts of multiple claims in one session are permitted) — no automated stage, re-ingest, or merge may set `active` — and every accepted claim's transition is individually recorded with actor and timestamp, one audit record per claim | [[graph.model]] |
| gm_lineage_survives | invariant | invalidation sets `invalid_at` and never destroys lineage; a claim is deleted only when no episode supports it any longer; episode deletion — permitted only when no claim supports the episode — records a tombstone for its stable id per `ic_deleted_tombstone` in ingestion.contract, so re-ingest never resurrects a deleted episode and recreation requires the explicit revive action per `ic_deleted_recreate` | [[graph.model]] |
| gm_deterministic_er | invariant | entity resolution is deterministic (normalization plus curated alias lists); unmatched mentions create new entity nodes; merge candidates are proposed as `possible_duplicate_of` edges into a review queue; no silent or automatic merge | [[graph.model]] |
| gm_merge_keeps | invariant | a merge is performed only after explicit human resolution of a review candidate, and it preserves every lineage edge from both sides; rejecting a candidate removes only its `possible_duplicate_of` edge | [[graph.model]] |
| gm_schema_v2 | invariant | claim nodes carry exactly: text, valid_at, invalid_at, data_cutoff, status, scope, source_type, evidence — evidence is a verbatim span of the supporting episode text plus its episode locator, or the typed absent marker (never a value that can collide with a real span) when sentence alignment failed — source_type inherited from the episode; no confidence field and no vector blob on any node | [[graph.model]] |
| gm_embedded_store | invariant | the graph persists as plain rows in a single embedded SQLite database — including deletion tombstones — and is fully rebuildable from the episode stream plus extraction output plus tombstones, so a dump-recreate reproduces deletions and never resurrects a deleted episode | [[graph.model]] |
| gm_hedge_anchor | invariant | epistemic strength lives only in verbatim episode text; derived artifacts must not upgrade a hedged source statement to an unhedged claim; an evidence span must not drop a hedge marker present in the supporting episode text within the span's coverage | [[graph.model]] |
| gm_contradicts_provenance | invariant | a `contradicts` edge is written in-pipeline only by the deterministic contradiction-scan pass (closed edit classes over normalized texts: negation-marker present/absent, or a single differing numeral token — no fuzzy subject detection), and every such edge carries the producing pass identity and detection rule as provenance; no other pipeline stage writes `contradicts` edges — the one sanctioned exception is the human-gated path of [[contradiction.review.cr_human_resolution]], where resolving an approved LLM proposal writes the edge carrying `llm:<model_id>` producer provenance | [[graph.model]] |
| gm_relation_typing | extension_point | the claim relation vocabulary (`mentions`, `contradicts`, `supports`, `derived_from`, `possible_duplicate_of`) is published for query-tool specs to conform to | [[graph.model]] |

## Model

### States

- `proposed`
- `active`
- `invalid`
- `rejected`

### Transitions

| id | from | to | guard |
|----|------|----|-------|
| adopt | proposed | active | [[graph.model.gm_human_adopt]] [[graph.model.gm_reified]] |
| discard | proposed | rejected | [[graph.model.gm_reified]] |
| invalidate | active | invalid | [[graph.model.gm_lineage_survives]] |
| repropose | invalid | proposed | [[graph.model.gm_lineage_survives]] |

## Properties

| id | kind | derives_from | generator | predicate |
|----|------|--------------|-----------|-----------|
| p_reified | unit | [[graph.model.gm_reified]] | claims extracted from synthetic corpora with known source counts N in 1..4 | every claim node has exactly N lineage edges matching its known source count; a zero-source claim is never persisted |
| p_lineage_survives | unit | [[graph.model.gm_lineage_survives]] | random sequences of invalidation and episode-deletion operations over a seeded graph | after every operation: each surviving claim's episode edge count equals its supporting-episode count; a claim disappears only when its last supporting episode is deleted |
| p_deterministic_er | unit | [[graph.model.gm_deterministic_er]] | mention streams mixing known aliases, unmatched names, and near-duplicates | entity node count changes only via explicit new-node creation or reviewed merges; queue contents equal candidate pairs |
| p_merge_keeps | unit | [[graph.model.gm_merge_keeps]] | human-reviewed merge and rejection operations over seeded entity pairs | approved merges preserve the union of both sides' lineage edges; rejected candidates lose only their `possible_duplicate_of` edge |
| p_schema_v2 | unit | [[graph.model.gm_schema_v2]] | claim records with extra, missing, and mistyped fields | stored claim nodes expose exactly the eight schema fields with types preserved; evidence is a verbatim span with locator or the typed absent marker |
| p_embedded_store | unit | [[graph.model.gm_embedded_store]] | seeded graphs of arbitrary size, with and without deletion tombstones | dump-then-recreate from episode stream plus extraction output plus tombstones reproduces the graph exactly, deletions included |
| p_hedge_anchor | unit | [[graph.model.gm_hedge_anchor]] | episode texts containing hedged statements (may, signals, estimates) | no derived claim text drops a hedge marker present in its supporting episode; evidence spans preserve hedge markers within their coverage |
| p_human_adopt | unit | [[graph.model.gm_human_adopt]] | adopt attempts driven through every automated path (pipeline stage, re-ingest, merge) and through the human CLI, single and batch | only explicit human accept actions move a claim to `active`; every transition record carries actor and timestamp, one per claim; automated attempts leave the claim `proposed` |
| p_relation_typing | unit | [[graph.model.gm_relation_typing]] | edge records sampled from the published vocabulary | every edge label is a member of the publish
...[truncated]...
ure, every candidate rejection at the validation gate) carries a machine-readable reason stored on the run or rejection record, never on a claim node | [[extraction.claims]] |
| ex_evidence_containment | invariant | every candidate claim carries an evidence span — a verbatim span of the supporting episode text plus its episode locator, or the typed absent marker when sentence alignment failed — validated by containment after whitespace collapse (all whitespace runs become a single space) of both span and episode text; a span failing containment is rejected with reason `evidence-not-contained`, never repaired; a typed-absent span persists but is flagged by the deterministic pass (`ex_reflection` extended), not treated as a violation | [[extraction.claims]] |
| ex_no_llm_post | invariant | normalization, dedup, entity matching, and conflict detection after the extraction call are deterministic; normalization rules appear both as prompt instructions and in a deterministic post-pass, because prompts are not bulletproof | [[extraction.claims]] |
| ex_mutation_proposal | invariant | a candidate claim that conflicts with an existing active claim stages an invalidation proposal carrying its causing-episode lineage; the existing claim is not mutated by the extractor | [[extraction.claims]] |
| ex_reflection | advisory | the single extraction call includes a self-check that verifies candidate claims against the episode text and enriches change lineage, rendered as flags by a deterministic pass; it flags unsupported candidates and never introduces new ones, and it is not a second LLM call | [[extraction.claims]] |
| ex_tag_inheritance | invariant | workspace tags and source metadata on an episode are inherited by every claim derived from it as a projection — the union over its lineage edges, resolved by walking `derived_from` at query time — and are never stored on the claim node | [[extraction.claims]] |
| ex_deterministic_structure | invariant | structure the converter already supplied (heading anchors, section boundaries, links) is consumed deterministically and never re-extracted by the LLM | [[extraction.claims]] |
| ex_section_filter | invariant | the deterministic post-pass rejects every candidate of an episode whose tags include a non-knowledge section-kind tag — `section-kind:praise`, `section-kind:copyright`, `section-kind:acknowledgments` — with machine-readable reason `section-filtered` on the run record (never on a claim node, per `ex_run_record`); the deny set is fixed in code, never an LLM judgment (`ex_no_llm_post` holds); untagged episodes stage unchanged, and a fully filtered episode still caches as extracted-empty per the `ex_single_call` cache economics | [[extraction.claims]] |
| ex_output_schema | extension_point | the candidate-claim record schema (field names, types, requiredness) is published for eval-harness specs to conform to | [[extraction.claims]] |

## Model

### States

- `pending`
- `extracted`
- `validated`
- `staged`
- `rejected`

### Transitions

| id | from | to | guard |
|----|------|----|-------|
| run | pending | extracted | [[extraction.claims.ex_single_call]] |
| gate | extracted | validated | [[extraction.claims.ex_typed_gate]] |
| abort | pending | rejected | [[extraction.claims.ex_single_call]] |
| requeue | rejected | pending | [[extraction.claims.ex_park_requeue]] |
| refuse | extracted | rejected | [[extraction.claims.ex_typed_gate]] |
| supersede | staged | rejected | [[extraction.claims.ex_supersession]] |
| stage | validated | staged | [[extraction.claims.ex_no_llm_post]] |
| refuse_section | extracted | rejected | [[extraction.claims.ex_section_filter]] |

## Properties

| id | kind | derives_from | generator | predicate |
|----|------|--------------|-----------|-----------|
| p_single_call | unit | [[extraction.claims.ex_single_call]] | episode corpora ingested, re-ingested unchanged, and re-ingested with a bumped extractor version | exactly one successful call per (episode id, extractor version); re-ingest at the same version produces no new call and reuses cached output; a version bump re-extracts |
| p_park_requeue | unit | [[extraction.claims.ex_park_requeue]] | episodes parked after retry-budget exhaustion, re-submitted unchanged, then re-run through extraction passes that fail again and succeed | the re-attempt pass starts a fresh retry budget and writes new run rows while prior parked rows persist with their reasons; success caches the output and ends the requeue cycle; renewed exhaustion parks again with a recorded reason; the unchanged re-submission itself emits `already_persisted` and changes neither graph nor run state |
| p_section_filter | unit | [[extraction.claims.ex_section_filter]] | candidate batches from episodes tagged with each deny-set section kind and from untagged episodes | tagged episodes stage zero claims and their run rows carry the `section-filtered` reason; untagged episodes stage unchanged; a fully filtered episode is cached as extracted so the pass never re-calls it |
| p_typed_gate | unit | [[extraction.claims.ex_typed_gate]] | candidate records mixing schema-valid, schema-violating, lineage-less, evidence-less, and zero-candidate episodes | only schema-valid lineage-bearing candidates with a passing evidence span reach `validated`; every violation lands in `rejected` unmodified; a zero-candidate episode caches as legitimately empty |
| p_supersession | unit | [[extraction.claims.ex_supersession]] | episode corpora re-extracted at bumped extractor versions with prior output in `staged`, `active`, and `rejected` states | only prior-version `staged` claims become `rejected` with reason `superseded-by-reextraction`, lineage and evidence remaining queryable; `active` and `rejected` claims from any version never change status; active conflicts stage invalidation proposals; superseded claims re-enter `staged` only via explicit re-stage |
| p_run_record | unit | [[extraction.claims.ex_run_record]] | extraction calls with success, repeated-failure, and gate-rejection outcomes | every call writes exactly one run row with episode id, extractor version, model id when present, timestamps, and finish status; every parked episode and gate rejection carries a machine-readable reason; claim nodes expose no reason field |
| p_evidence_containment | unit | [[extraction.claims.ex_evidence_containment]] | candidate spans that are contained, non-contained after whitespace collapse, and typed-absent | contained spans persist verbatim; non-contained spans reject with reason `evidence-not-contained` and are never repaired; typed-absent spans persist flagged by the reflection pass and are never reported as violations |
| p_no_llm_post | unit | [[extraction.claims.ex_no_llm_post]] | candidate sets containing near-duplicates (simhash distance) and unnormalized fields | identical post-pass inputs produce identical outputs and no LLM call occurs after the extraction step |
| p_mutation_proposal | unit | [[extraction.claims.ex_mutation_proposal]] | candidate claims conflicting with seeded active claims | every conflict stages an invalidation proposal citing its causing episode; seeded claims are unchanged until the proposal is applied |
| p_reflection | unit | [[extraction.claims.ex_reflection]] | extracted candidates containing unsupported statements and dropped hedges | reflection flags each unsupported candidate; the post-reflection candidate set introduces no new claims |
| p_tag_inheritance | unit | [[extraction.claims.ex_tag_inheritance]] | episodes with varying tag sets, derived claim sets, and multi-source claims | every derived claim resolves to exactly the union of its supporting episodes' tag sets via lineage walk; no tag is stored on the claim node |
| p_deterministic_structure | unit | [[extraction.claims.ex_deterministic_structure]] | episodes with converter-supplied structure markers | structural relations derive from markers alone, independent of extraction output |
| p_output_schema | unit | [[extraction.claims.ex_output_schema]] | candidate-claim records sampled from the published schema | the published schema validates every emitted candidate record |

## Assistant

bash -lc sed -n '197,290p' /tmp/review/bajan-main/README.md; printf '\n===== QUERY SPEC =====\n'; sed -n '1,260p' /tmp/review/bajan-main/specs/query-tools.md; printf '\n===== CONTRADICTION REVIEW =====\n'; sed -n '1,240p' /tmp/review/bajan-main/specs/contradiction-review.md; printf '\n===== ENTITY REVIEW =====\n'; sed -n '1,220p' /tmp/review/bajan-main/specs/entity-review.md; printf '\n===== KNOWLEDGE ASSISTANT =====\n'; sed -n '1,240p' /tmp/review/bajan-main/docs/knowledge-assistant-ears-spec.md

## Tool

Scoring semantics, in order:

1. **Content match** — candidate text equals a golden claim's text after
   whitespace-collapse + lowercase with hedge-marker words ignored on both
   sides (a candidate that adds or drops a hedge still locates its target).
2. **Span check** — the candidate's `evidence_span` must locate inside the
   episode text (whitespace-collapsed containment, same predicate as
   extraction's evidence gate). Fails → `content-miss`, never a match.
3. **Hedge fidelity** — every hedge marker the golden claim lists must
   appear in the candidate text. Missing → `hedge-dropped`: a precision
   failure distinct from a content miss, and the golden claim stays open
   for a later clean candidate.
4. Otherwise → `matched`. Unmatched candidates score `spurious`.

The example pair above demonstrates the strictest rule: the candidate
dropped the hedge its golden claim lists, so it scores `hedge-dropped` —
precision 0, recall 0, hedge preservation 0, never a plain match.

Denominators are always reported in `counts`; a metric with a zero
denominator (no candidates, no golden claims, no hedge-bearing golden
claims) is `null` **and** named in `unknown_metrics` — never invented.
Run with `--json` for the machine envelope (`data.counts`,
`data.unknown_metrics`); text mode renders the same content in human form.
`data.results_row` is the ready-to-append row for the eval-claims table in
`evals/results.md` — the date cell is a placeholder you fill at append
time (scoring itself never reads the wall clock, so reruns reproduce the
row byte-for-byte). Gold labels are human sign-off by design: no
model-generated gold labels, and gold fixtures land in a reviewed commit
before any metrics run.

## Design in one line

Deterministic-first: no LLM where traditional IR/NLP works; NLP/IR crates are
exact-pinned so a rebuild reproduces the same store; LLM passes only propose —
humans approve. Specifications under `specs/` are linted by
[specodelic](https://crates.io/crates/specodelic) and gate every commit.

## Known limitations

- **Parked episodes are visible but passive.** When the LLM extractor
  hits transient provider overload it parks 10–24% of episodes per
  pass; the extract report now names each parked episode with its
  failure class (timeout / http-N / transport / schema) and attempt
  count (bajan-gso). Retries back off 2s·2^(n−1) with jitter, capped at
  60s (bajan-266); a rerun recovers parked episodes (cache intact;
  burn-in reruns recovered 2/12).
- **Spend cap needs `usage.cost`.** The LLM extractor requires
  `BAJAN_MAX_SPEND_USD` and stops the pass when known spend reaches the
  cap (bajan-8cc) — but providers that do not report per-call cost in
  `usage.cost` (e.g. plain OpenAI) cannot be accounted: one
  unaccountable call fails the next call closed (never silently
  unbounded). Bound spend at the provider as well.
- **Extraction precision/recall numbers are not published yet.** The eval
  harness is built (`bajan eval claims`, bajan-2k4) but no golden corpus
  has been adjudicated yet — gold labels are human sign-off; until a
  corpus lands and a run is scored, adopt with judgment.
- **Per-call costs are logged, not reported.** The extractor logs one
  stderr line per successful LLM call carrying the response's exact
  `usage.cost` and the running spend against the cap (bajan-3w4);
  aggregate spend surfaces on the extract report only when a cap stops
  the pass (bajan-8cc).
- Burn-in findings and failure profile:
  [`docs/burnin-deepseek-v4-flash-profit-first.org`](docs/burnin-deepseek-v4-flash-profit-first.org).

## Development

```sh
just ci        # full gate: fmt, clippy, tests, spec lint, hooks parity
just --list    # all recipes
```

Issue tracking and burn-in history live in `.beads/`; the spec corpus is
under `specs/` with change proposals under `openspec/`.

===== QUERY SPEC =====
---
id: query.tools
kind: intent
statement: "WHEN a read command executes against the claim graph THE bajan query surface SHALL return only claims whose full lineage is traceable to their supporting episodes, ordered by authority-then-recency within the queried scope and under a bounded traversal budget"
---

# queries

The read side of bajan: the search/read/grep/outline surface over the
claim graph, graph-native rather than document-native. It consumes the
`gm_relation_typing` extension point published by `graph.model` (edge
vocabulary: `mentions`, `contradicts`, `supports`, `derived_from`,
`possible_duplicate_of`) and the tag-inheritance projection of
`ex_tag_inheritance` from `extraction.claims` — tags are resolved by
walking lineage at query time, never stored on the claim. The retrieval
discipline is carried over from the EARS oracle
(`docs/knowledge-assistant-ears-spec.md`): bounded budget with an honest
stopping rule (WR-USE.1), per-hit recency surfacing with stale warnings
(WR-TIME.3), authority-then-recency ranking with staleness demotion
(WR-RANK.1/.2), and scope discipline (WR-SCOPE.1) — re-expressed for a
provenance graph: ranking uses the episode's source metadata
(authority tier, data cutoff) reachable through lineage, and scope
filtering uses the resolved tag projection. Read commands never mutate:
every query is a lineage walk over stored rows, and a contradiction
query is a traversal of `contradicts` edges plus invalidation proposals,
not a semantic judgment — the graph says what conflicts, the human says
what's true.

## Constraints

| id | kind | expr | traces_to | satisfies |
|----|------|------|-----------|-----------|
| qt_lineage_traceable | invariant | every claim returned by a read command resolves, at query time, through its `derived_from` edges to at least one persisted supporting episode; a claim whose lineage walk reaches no episode is invisible to the query surface (deletion by lineage walk per `gm_lineage_survives`) | [[query.tools]] | |
| qt_bounded_traversal | invariant | every read command executes under a bounded traversal budget — a maximum walked node count and depth — and reports a typed exhausted-budget marker when results are truncated; the stopping rule is honest: `not-found` is reported when the budget completed without a match, `budget-exhausted` when it stopped early — never a silent partial answer | [[query.tools]] | |
| qt_ranking | invariant | multi-hit read results order by the supporting episodes' metadata reachable through lineage — authority tier first, then data cutoff recency; when a comparably-relevant higher-authority source is stale (beyond the staleness window) it demotes below fresh lower-authority hits; every hit surfaces its data cutoff, and the best-scoring hit carries a staleness warning when its cutoff is stale | [[query.tools]] | |
| qt_scope_filtering | invariant | a read command scoped to a workspace tag set returns only claims whose resolved tag projection (the union over its lineage edges per `ex_tag_inheritance`) intersects the requested scope; a claim outside the requested scope is either excluded or labelled with its own scope in the result — never silently blended | [[query.tools]] | |
| qt_readonly | invariant | read commands never mutate the graph — no state transition, no audit record, no derived-from edge is written by any query; a read against a claim set with active and invalid claims returns the status of every hit verbatim, never silently dropping `invalid` claims from results | [[query.tools]] | |
| qt_contradiction_query | invariant | a contradiction query returns the claim pairs joined by `contradicts` edges plus the invalidation proposals staged against the queried claims (per `ex_mutation_proposal`), each hit carrying both sides' lineage and status; the query reports graph structure only and never adjudicates which side is true | [[query.tools]] | [[graph.model.gm_relation_typing]] |
| qt_query-schema | extension_point | the query result record schema (fields, types, requiredness, including the budget-status vocabulary `complete`, `budget-exhausted` and the staleness marker form) is published for reporting and agent-tool specs to conform to | [[query.tools]] |

## Model

### States

- `queried`
- `tr
...[truncated]...
equest and the agent's response to it; **messages** are the individual tool calls, tool
  results, and replies within a turn.
- **ledger** — a durable record tracking each raised contradiction flag through its lifecycle
  (open → resolved / unresolvable), as opposed to inert inline markers scattered in page text.
- **SLA** — service-level agreement: here, a time bound after which an unresolved contradiction
  flag is escalated by lint.
- **canonical page** — the single page designated authoritative when near-duplicates exist.
- **force-attach** — wrongly associating a source or claim with an entity it does not concern
  (e.g. via a loose substring/alias match).
- **stale** — data cutoff older than the configured staleness window. The window is
  **per-workspace configurable** (default: 365 days) and drives both the read-side staleness
  warning and the reporting lint.
- **source type & authority order** — the class of a source document, used for ranking. The
  default authority order, highest to lowest, is: **per-event bulletin ≈ curated briefing >
  presentation deck > formal publication**. Rationale: bulletins/briefings are issued more
  frequently and closer to events, so they usually carry the freshest data on a fast-moving fact;
  decks are periodic; generic publications lowest. Authority is a tiebreaker among
  comparably-recent sources, never a licence to surface stale data (WR-RANK.2).

---

## 1. Ingest fidelity & source grounding

*Surface: write path. Defect class: a synthesised page asserts more than its source, invents an
identity, or drops the source's hedging.*

### WR-INGEST.1 — Verbatim evidence is captured for every page
**When** the ingest pipeline writes or updates a knowledge-base page, the pipeline **shall**
persist a captured-evidence entry (verbatim quote + source name + locator) for each material
claim on the page.
- **Rationale:** a claim with no captured quote is unverifiable at answer time and cannot be
  cited. Provenance must be captured at write time; it cannot be reconstructed later.
- **Generic example:** ingesting Source-S that states *"7 of 91 units met the threshold"* yields a
  page whose captured evidence contains that exact sentence, attributed to Source-S.
- **Edge cases:** multi-line quotes must survive serialization (see WR-INGEST.5); a page built
  from N sources carries evidence from all N, not just the first.

### WR-INGEST.2 — Numeric claims must be anchored in a captured quote
**If** a numeric value on a generated page does not appear in any of that page's captured
evidence, **then** the ingest pipeline **shall** emit a grounding warning identifying the
unanchored value.
- **Rationale:** the single highest-severity defect is a fabricated number. Catch it where the
  page is written.
- **Generic example:** a page states *"success rate 44%"* but no captured quote contains `44` → a
  grounding warning fires.
- **Edge cases:** the check can over-flag (rounding, `44%` vs `44.0%`, values inside a quoted
  range) — at ingest it is an **advisory log, never a hard block**; percentages inside a quoted
  range must not false-fire.

### WR-INGEST.3 — Hedging is preserved, never upgraded
**When** the ingest pipeline synthesises page prose from a hedged source statement, the pipeline
**shall** preserve the source's epistemic strength (e.g. "signals of an effect" is not rewritten
as "demonstrated an effect").
- **Rationale:** silent confidence-inflation is a traceability failure even when the underlying
  number is right.
- **Generic example:** source says *"signals of activity were observed"* → the page must not read
  *"activity was demonstrated"*.
- **Edge cases:** estimates and internal assessments must retain their "estimate / internal
  assessment" framing (see WR-ANSWER.4).

### WR-INGEST.4 — Entity identity must not be fabricated
**If** the ingest synthesis cannot resolve an entity's true name from the source, **then** the
pipeline **shall not** invent a name or create a page under a fabricated identity.
- **Rationale:** a wrong-identity page silently poisons every downstream answer about that entity.
- **Generic example:** an entity referred to only by a short code must not be materialised as a
  full page under a guessed full name.
- **Edge cases:** known aliases (short-name ↔ code ↔ full name) must resolve to **one** canonical
  page with an alias list + redirect stubs; ambiguous abbreviations that could match multiple
  entities must not force-attach to any single one.

### WR-INGEST.5 — Metadata writes are lossless
**When** the pipeline stamps or rewrites page metadata, the pipeline **shall** preserve all
existing metadata fields and multi-line values intact.
- **Rationale:** a partial-line rewrite that orphans the remainder silently wipes provenance
  metadata — an invisible, corpus-wide data-loss class.
- **Generic example:** stamping a data-cutoff field onto a page whose captured-evidence block
  spans multiple lines must not truncate or orphan that block.
- **Edge cases:** multi-line values serialized as inline/flow syntax can become invalid and drop
  all metadata — such values must serialize as block form; a stamping routine must replace the
  whole logical field, not just its first physical line.

---

## 2. Temporal representation & recency

*Surface: write + read. Defect class: stale data returned as "current" with no date; newer data
present elsewhere never surfaced.*

### WR-TIME.1 — Every dated source section carries its data cutoff
**When** the pipeline ingests a source that carries a data cutoff or event date, the pipeline
**shall** stamp the generated section with a machine-readable "data as of `<YYYY-MM-DD>`" marker
and record the page's most-recent cutoff and latest source.
- **Rationale:** recency judgements are impossible without a machine-readable cutoff per section.
- **Generic example:** ingesting Event-V material dated 2024-07 stamps `data as of 2024-07-xx` —
  the source's date, **not** today's ingest date.
- **Edge cases:** the date is the source's cutoff, never the ingest timestamp; a source with no
  discoverable date is stamped `unknown`, not today.

### WR-TIME.2 — Reads surface recency up front
**When** the agent reads a time-sensitive page, the system **shall** present a recency banner
(data cutoff + status) at the top and order dated source sections newest-first.
- **Rationale:** the reader must see how old the data is before reading its content.
- **Generic example:** reading Activity-T's page shows a banner "data as of 2024-07; status:
  ongoing" above the body, with 2024 sections above 2023 ones.
- **Edge cases:** a legacy page with no dated headers cannot be reordered — this is a re-ingest
  data gap, not a code failure; the banner degrades gracefully.

### WR-TIME.3 — Search surfaces per-hit recency and warns on stale best-match
**When** the agent searches the knowledge base, the system **shall** surface each hit's data
cutoff, and **if** the best-scoring match is stale (older than the staleness window), **then** the
system **shall** emit a staleness warning on that hit.
- **Rationale:** relevance scoring is blind to age; a highly-relevant stale page must not read as
  current.
- **Generic example:** a query's top hit has cutoff 2023-01 (>1 year) → the result is tagged "⚠
  data may be stale (as of 2023-01)".
- **Edge cases:** a hit with no cutoff is neither warned nor claimed fresh; recency here is
  advisory to the agent, not a re-ranking (that is the optional WR-RANK.3).

### WR-TIME.4 — Generated data tables are dated
**When** the agent generates a data table from knowledge-base content, the agent **shall** caption
it with a sourced "data as of `<date>`" derived from the underlying sections' cutoffs.
- **Rationale:** a table stripped of its dates is the exact artifact that gets copied elsewhere and
  mis-read as current.
- **Generic example:** a comparison table built from three sources (2024-07, 2024-09, 2025-04) is
  captioned "data as of Apr 2025" or lists per-row cutoffs.
- **Edge cases:** mixed-cutoff tables should show per-row dates rather than a single misleading
  headline date.

## Assistant

bash -lc cat /tmp/review/whisper-main/README.md; printf '\n===== INDEX =====\n'; cat /tmp/review/whisper-main/docs/src/index.md; printf '\n===== GETTING STARTED =====\n'; cat /tmp/review/whisper-main/docs/src/getting-started.md; printf '\n===== ENTRY =====\n'; sed -n '1,260p' /tmp/review/whisper-main/src/entry.rs; printf '\n===== KNOWLEDGE COMMANDS =====\n'; sed -n '1,320p' /tmp/review/whisper-main/src/cmds/knowledge.rs; printf '\n===== DISTILL =====\n'; sed -n '1,320p' /tmp/review/whisper-main/src/distill.rs; printf '\n===== RECALL =====\n'; sed -n '1,320p' /tmp/review/whisper-main/src/recall.rs; printf '\n===== SERVING =====\n'; sed -n '1,320p' /tmp/review/whisper-main/src/serving.rs

## Tool

> *"Time can never mend*
> *The careless whispers of a good friend*
> *To the heart and mind, ignorance is kind*
> *There's no comfort in the truth, pain is all you'll find"*
> — George Michael, *Careless Whisper*

# whisper

`whisper` is a Rust CLI that makes the [incitaciones](https://github.com/charly-vibes/incitaciones) `whisper` skill deterministic.

The whisper skill asks an agent to manage `~/.whisper/` — canonical repo keys, branch slugs, worktree slots, and scope-based knowledge routing — by hand-rolling shell pipelines. Every invocation is a fresh chance for the model to mis-derive a path. This tool turns that mechanical layer into a binary: the skill prompts call the CLI, and the same inputs always produce the same outputs.

**The command is `turu`** — following the song's *turututu* riff. `turututu` and `whisper` run as aliases, so existing scripts and skill prompts keep working.

Part of the [charly-vibes](https://github.com/charly-vibes) tool suite; built on [genesis-vibes](https://github.com/charly-vibes/genesis) for the JSON envelope, config, and CLI conventions shared across the family.

> **Why:** agents accumulate operational knowledge across sessions, but "where does
> this note go?" is a question models answer unreliably by hand-rolling shell
> pipelines over `~/.whisper/` — every invocation is a fresh chance to mis-derive
> a canonical repo key or scope path. `turu` turns that mechanical layer into a
> deterministic binary: same inputs, same outputs, every machine.
> **Status:** [beta](docs/src/status.md) · core key/resolve/append/recall/distill shipped and used by other ecosystem tools · [Motivation & design](docs/src/index.md) · [charly-vibes Tool Ecosystem](https://charly-vibes.github.io/dulce-de-leche/ecosystem-map.html)
## What it does

- `turu key` — canonical repo key, branch slug, and worktree slot for the current checkout (the pure determinism core)
- `turu resolve <scope>` — the exact destination path for a knowledge scope: `global`, `repo`, `branch`, `worktree`, or `group`
- `turu append <scope> --text "..." [--topic k] [--supersedes id]` — structured, idempotent entries (sha2 ids over scope + second-precision UTC + text) written into the right file; freeform content preserved verbatim
- `turu recall <scope> [--topic k] [--budget bytes] [--include-superseded]` — ranked, budget-bounded slice serving (`all` composes scopes in precedence order); the envelope reports the context-horizon boundary (`served_bytes`, `budget_unused`, `entries_skipped`)
- `turu distill <scope> --begin|--commit --revision id` — two-phase contract: turu snapshots into immutable revisions and guards the commit against concurrent drift; the calling agent does the semantic rewrite into the working file
- `turu bundle pack|unpack` — deterministic, transport-agnostic knowledge bundles keyed by repo key; unpack merges extend-without-duplicate and never overwrites
- `turu init` — create the workspace layout
- `turu status` — one envelope with every relevant path and existence flag
- `turu check` — detect legacy key variants, undefined groups, missing files
- `turu doctor` — deep diagnostics: layout integrity, group health, legacy keys, managed block, skill pack staleness
- `turu sync` — inject the deterministic routing map into `AGENTS.md` as a `<!-- TURU:START -->` managed block, so agents read paths from a file instead of re-deriving them
- `turu feedback <kind>` — file a well-contexted GitHub issue (`bug`, `feature`, `question`, `chore`): redacted context bundle, optional `--from-last-error` scratch recall, `--dry-run` preview (via `genesis::feedback`)
- `turu skill install` — ship the whisper skill from this repo: router + sub-skills (including manual fallbacks), content-hashed so `turu doctor` flags staleness. Targets `~/.claude/skills` or any dir; incitaciones keeps a thin pointer to it

## Install

### Binary (curl)

```bash
V=$(basename "$(curl -fsSLI -o /dev/null -w '%{url_effective}' \
  https://github.com/charly-vibes/whisper/releases/latest)" | sed 's/^v//')
TGT="$(uname -s | tr '[:upper:]' '[:lower:]')_$(uname -m | sed 's/^x86_64$/amd64/; s/^aarch64$/arm64/')"
curl -fsSL "https://github.com/charly-vibes/whisper/releases/download/v${V}/turu_${V}_${TGT}.tar.gz" | tar xz
chmod +x turu turututu whisper && sudo mv turu turututu whisper /usr/local/bin/
```

### Cargo

```bash
cargo install whisper-vibes
```

Or from source:

```bash
git clone git@cv:charly-vibes/whisper.git && cd whisper && just install
```

## Configuration

Where knowledge gets written is layered. Precedence: **repo > group > global**.

**Global** — `~/.config/whisper/config.toml`:

```toml
workspace_root = "~/.whisper"   # default

[groups.cv-tools]
root = "~/para/areas/dev/gh/charly/knowledge"
repos = ["cv/charly-vibes/whisper"]   # explicit membership (optional)
```

A **group** routes knowledge from a set of repos into one shared workspace directory instead of each repo's private slot.

**Repo (private)** — `<repo>/.whisper/config.toml` (gitignored — never committed):

```toml
group = "cv-tools"              # join a group defined in the global config
workspace_root = "/path/to/dir" # or fully override the workspace root
```

A repo can join a group two ways: privately, via its own `.whisper/config.toml`, or centrally, by listing its canonical key in the group's `repos` array.

> **Note:** a repo-private `workspace_root` overrides *everything* — including the global scope, so the repo's `rules.md` resolves inside the private root instead of the shared workspace. `turu doctor` reports this shadowing and warns when the two `rules.md` files diverge. A relative `workspace_root` is anchored to the directory containing the repo config (not the process cwd), so calls from any subdirectory resolve to the same root.

## Knowledge transport & the private zone

Where knowledge lives depends on the scope and where the command runs:

| Scope | In a checkout (default) | `--global` escape hatch |
|---|---|---|
| `repo` | `<repo>/.whisper/env.md` (committed) | `<workspace>/repos/<key>/env.md` |
| `branch` | `<repo>/.whisper/branches/<slug>/notes.md` (committed) | `<workspace>/repos/<key>/branches/<slug>/notes.md` |
| `--private` repo/branch | `<repo>/.whisper/private/…` — **gitignored, never pushed** | — |

Transport decision: the repo's own git carries the shared knowledge. Repo-local
publication assumes a pushable checkout — `--global` is the fallback for
read-only checkouts (CI, no-push contributors).

Machine-specific knowledge (local paths, hostnames, credentials) belongs in the
**private zone**: `turu append <scope> --private` routes into
`<repo>/.whisper/private/`, which `turu init`/`turu sync` keep effectively
ignored — the rule is appended to the root `.gitignore` only when
`git check-ignore` does not already report the path (text presence is not the
truth; a nested `.gitignore` or your global excludes file counts).

`turu doctor` enforces the privacy contract with three checks:

- `turu.private-ignore` — the zone is *effectively* ignored (warning + fix hint otherwise)
- `turu.private-tracked` — **fails prominently** if any file under `private/` is tracked
- `turu.private-leaks` — advisory lint for machine paths, hostnames, and token-shaped strings in public repo-local files (surfaces via `warnings[]`)

git history is forever — prevention only. No turu verb can retract committed
knowledge; that is exactly why the private zone exists and why the tracked-files
check fails instead of warning.

## Skill integration

The distilled whisper skill in incitantes replaces its shell-snippet procedures with:

```
turu key        # derive repo key / branch slug / worktree slot
turu resolve branch
turu append repo --text "deploy requires vault login"
turu recall repo --topic deploy --budget 400   # slice, newest first, boundary reported
```

Agents in any repo with a `TURU` managed block read the routing map straight from `AGENTS.md` — no prompt bookkeeping required. `turu sync` refreshes the block; `turu doctor` flags it when it drifts.

Determinism guarantee: canonical key derivation is a pure function o
...[truncated]...
se_file(raw)
        .into_iter()
        .filter_map(|item| match item {
            Item::Entry(e) => Some(e),
            Item::Line(_) => None,
        })
        .filter(|e| query.include_superseded || e.superseded_by.is_none())
        .filter(|e| query.topic.is_none() || e.topic.as_deref() == query.topic.as_deref())
        .collect();
    scoped.sort_by(|a, b| b.ts.cmp(&a.ts));
    (scoped, freeform)
}

/// Serve the ranked slice for the requested scope(s). When `record_usage`
/// is true, every entry actually served gets one usage record appended to
/// its scope's sidecar (usage only counts what recall served).
///
/// Digest budget: explicit --budget wins; otherwise the digest default
/// caps the envelope under the harness truncation line. Usage sidecars:
/// one append per touched scope file (best-effort).
pub fn recall(
    recall_scope: &RecallScope,
    facts: &Facts,
    resolved: &Resolved,
    query: &RecallQuery,
) -> Result<Value> {
    let mut acc = Acc::new();
    let budget = if query.digest {
        query.budget.or(Some(DIGEST_DEFAULT_BUDGET))
    } else {
        query.budget
    };
    let now = entry::parse_or_now(std::env::var("TURU_NOW").ok().as_deref())?;
    serve_stores(recall_scope, facts, resolved, query, &mut acc, budget)?;

    let recorded = acc.record_usage(&now);

    // Empty-scope semantics (whisper-2c1): an empty scope is an empty
    // answer, not a hard failure — ok:true with empty data and exit 0, so
    // && chains and set -e survive it. The emptiness rides in the envelope
    // ("empty": true) and main.rs surfaces it as an advisory warning.
    Ok(render(
        recall_scope,
        query,
        &acc,
        budget,
        recorded,
        acc.nothing_served(),
    ))
}

/// Mode-specific envelope payload: digest head lines versus full entries.
fn insert_payload(m: &mut serde_json::Map<String, Value>, query: &RecallQuery, acc: &Acc) {
    if query.digest {
        m.insert("digest".into(), json!(true));
        m.insert("lines".into(), json!(acc.digest_lines));
    } else {
        m.insert("entries".into(), json!(acc.entries));
        m.insert("freeform".into(), json!(acc.lines));
    }
}


===== SERVING =====
//! Digest-line rendering and the serving accumulator shared by `recall`.
//! Split out of `recall.rs` to keep file and function sizes small.

use crate::entry;
use crate::recall::{RecallQuery, Served, ServedLine};
use crate::workspace::Scope;

/// Cap text to the head budget on a char boundary.
const DIGEST_HEAD_CAP: usize = 160;

pub(super) fn cap_head(text: &str) -> String {
    if text.len() <= DIGEST_HEAD_CAP {
        return text.to_string();
    }
    let end = (0..=DIGEST_HEAD_CAP)
        .rev()
        .find(|&i| text.is_char_boundary(i))
        .unwrap_or(DIGEST_HEAD_CAP);
    text[..end].to_string()
}

/// One capped head line for a served entry: ts, scope tag, topic, first
/// text line. Later lines never leak (a head points at the scope file —
/// the full text stays there).
pub(super) fn digest_entry_line(scope: &str, e: &entry::Entry) -> String {
    let tag = match &e.topic {
        Some(t) => format!("[{scope}#{t}]"),
        None => format!("[{scope}]"),
    };
    let first_line = e.text.split('\n').next().unwrap_or("");
    format!("{} {} {}", e.ts, tag, cap_head(first_line))
}

/// One capped head line for a served freeform line (verbatim text, capped).
pub(super) fn digest_freeform_line(scope: &str, line: &str) -> String {
    format!("[{scope}] {}", cap_head(line))
}

/// Per-store serving context: the query knobs, the scope file being served,
/// and the active byte budget.
pub(super) struct Ctx<'a> {
    pub(super) query: &'a RecallQuery,
    pub(super) path: &'a std::path::Path,
    pub(super) budget: Option<usize>,
}

/// Accumulated serving state for one recall run. Mutable internals are
/// confined to `&mut self` methods so the top-level `recall` stays a
/// composition of store loops plus one JSON render.
pub(super) struct Acc {
    pub(super) entries: Vec<Served>,
    pub(super) lines: Vec<ServedLine>,
    pub(super) digest_lines: Vec<String>,
    pub(super) served_bytes: usize,
    pub(super) entries_skipped: usize,
    pub(super) freeform_skipped: usize,
    pub(super) served_ids: std::collections::HashSet<String>,
    /// Entry ids per scope file, in first-touched order (usage sidecars).
    pub(super) usage_order: Vec<std::path::PathBuf>,
    pub(super) usage_batch: std::collections::HashMap<std::path::PathBuf, Vec<String>>,
}

impl Acc {
    pub(super) fn new() -> Self {
        Self {
            entries: Vec::new(),
            lines: Vec::new(),
            digest_lines: Vec::new(),
            served_bytes: 0,
            entries_skipped: 0,
            freeform_skipped: 0,
            served_ids: std::collections::HashSet::new(),
            usage_order: Vec::new(),
            usage_batch: std::collections::HashMap::new(),
        }
    }

    /// Budget test + serve for one entry (whole-entry atomicity).
    pub(super) fn serve_entry(&mut self, scope_name: &'static str, e: entry::Entry, ctx: &Ctx) {
        if !self.served_ids.insert(e.id.clone()) {
            return; // same entry reached through another store
        }
        let cost = match ctx.query.digest {
            true => digest_entry_line(scope_name, &e).len() + 1,
            false => e.render().len(),
        };
        if self.over_budget(ctx.budget, cost) {
            self.entries_skipped += 1;
            return;
        }
        self.served_bytes += cost;
        if ctx.query.digest {
            self.digest_lines.push(digest_entry_line(scope_name, &e));
        }
        if ctx.query.record_usage {
            self.record_served_id(ctx.path, &e.id);
        }
        self.entries.push(Served {
            scope: scope_name,
            entry: e,
        });
    }

    /// Whole-line atomicity: never serve a partial item over the budget.
    fn over_budget(&self, budget: Option<usize>, cost: usize) -> bool {
        budget.is_some_and(|b| self.served_bytes + cost > b)
    }

    /// Record one served entry id for its scope file's usage sidecar.
    fn record_served_id(&mut self, path: &std::path::Path, id: &str) {
        self.usage_batch
            .entry(path.to_path_buf())
            .or_insert_with(|| {
                self.usage_order.push(path.to_path_buf());
                Vec::new()
            })
            .push(id.to_string());
    }

    /// Budget test + serve for one freeform line (whole-line atomicity).
    pub(super) fn serve_freeform(&mut self, scope_name: &'static str, l: String, ctx: &Ctx) {
        let cost = match ctx.query.digest {
            true => digest_freeform_line(scope_name, &l).len() + 1,
            false => l.len() + 1,
        };
        if self.over_budget(ctx.budget, cost) {
            self.freeform_skipped += 1;
            return;
        }
        self.served_bytes += cost;
        if ctx.query.digest {
            self.digest_lines.push(digest_freeform_line(scope_name, &l));
        } else {
            self.lines.push(ServedLine {
                scope: scope_name,
                line: l,
            });
        }
    }

    /// Append one usage record per served id to each touched scope file's
    /// sidecar (O_APPEND; best-effort by design — recall must never fail
    /// because telemetry cannot write; read-only workspaces still recall).
    pub(super) fn record_usage(&self, now: &str) -> usize {
        self.usage_order
            .iter()
            .filter_map(|path| self.usage_batch.get(path).map(|ids| (path, ids)))
            .map(|(path, ids)| crate::usage::append(path, ids, now).unwrap_or(0))
            .sum()
    }

    pub(super) fn nothing_served(&self) -> bool {
        self.entries.is_empty()
            && self.lines.is_empty()
            && self.digest_lines.is_empty()
            && self.entries_skipped == 0
    }
}
pub(super) fn scope_name(scope: Scope) -> &'static str {
    match scope {
        Scope::Global => "global",
        Scope::Repo => "repo",
        Scope::Branch => "branch",
        Scope::Worktree => "worktree",
        Scope::Group => "group",
    }
}

## Assistant

bash -lc printf '===== BAJAN SRC OVERVIEW =====\n'; for f in src/ingest.rs src/extract.rs src/query.rs src/contradict.rs src/propose.rs src/review.rs src/resolve.rs src/store/nodes.rs src/store/sqlite.rs src/llm.rs; do echo "--- $f"; rg -n '^pub (async )?fn|^fn |^pub struct|^struct |^pub enum|^enum |^const |^pub const|^impl ' "/tmp/review/bajan-main/$f"; done; printf '\n===== WHISPER DISTILL CONTRACT =====\n'; sed -n '1,280p' /tmp/review/whisper-main/src/distill.rs; printf '\n===== WHISPER ENTRY MODEL =====\n'; sed -n '1,260p' /tmp/review/whisper-main/src/entry.rs; printf '\n===== WHISPER KNOWLEDGE CLI =====\n'; sed -n '1,280p' /tmp/review/whisper-main/src/cmds/knowledge.rs;

## Tool

===== BAJAN SRC OVERVIEW =====
--- src/ingest.rs
20:pub const SPEC: &str = "specs/ingestion-contract.md";
28:pub enum Locator {
36:impl Locator {
65:pub struct SourceMeta {
75:pub struct EpisodeRecord {
88:pub enum RejectReason {
110:impl RejectReason {
129:pub enum IngestOutcome {
145:pub fn persist(
213:pub fn persist_stream(
236:pub fn dump_stream(
--- src/extract.rs
18:pub const SPEC: &str = "specs/extraction-claims.md";
26:pub enum FailureClass {
38:impl FailureClass {
50:impl std::fmt::Display for FailureClass {
63:pub enum Reason {
85:impl Reason {
104:pub enum Finish {
122:pub struct ExtractionRun {
136:pub struct ExtractionRunStore {
140:impl ExtractionRunStore {
155:pub struct ParkedEpisode {
164:pub struct GateRejection {
176:pub struct CandidateClaim {
188:pub enum ExtractionFailure {
269:pub struct ExtractReport {
296:pub struct SpendCapStop {
310:fn classify_refusal(err: &crate::store::StoreError) -> Result<Reason, BajanError> {
318:fn epoch_millis() -> u64 {
328:pub const ATOMIZER_MIN_UNIT_CHARS: usize = 20;
334:pub const ATOMIZER_MAX_UNIT_CHARS: usize = 300;
341:pub fn atomic_default_version() -> String {
358:pub fn atomic_claim_units(text: &str) -> Vec<String> {
436:fn char_len(text: &str, start: usize, end: usize) -> usize {
448:pub struct SentenceAtomizer {
452:impl SentenceAtomizer {
460:impl Extractor for SentenceAtomizer {
495:struct LegacyProposer {
499:impl Extractor for LegacyProposer {
526:pub struct ExtractorConfig {
563:pub enum ExtractorConfigError {
580:impl ExtractorConfig {
689:pub fn run_extract(
701:pub fn run_extract_versioned(
750:pub const SECTION_FILTER_DENY: [&str; 3] = [
756:pub fn run_extract_with(
981:fn stage_mutation_proposals(
1042:pub fn check_evidence_containment(evidence: &Evidence, episode_text: &str) -> Result<(), Reason> {
1063:pub enum ReflectionFlag {
1073:pub fn reflection_flags(evidence: &Evidence) -> Vec<ReflectionFlag> {
--- src/query.rs
28:pub const STALENESS_WINDOW_DAYS: i64 = 365;
33:pub fn today_days_utc() -> i64 {
44:pub fn iso_from_days(days: i64) -> String {
62:pub fn days_from_iso(text: &str) -> Option<i64> {
84:pub const SPEC: &str = "specs/query-tools.md";
93:pub enum BudgetStatus {
106:pub struct Hit {
131:pub struct StalenessWarning {
138:pub struct SearchResult {
173:pub struct CoverageNote {
187:fn coverage_note(db: &SqliteStore) -> Result<Option<CoverageNote>, BajanQueryError> {
208:fn ranking_metadata(
231:pub fn search(
244:pub fn search_with_window(
267:pub fn search_scoped(
278:fn search_inner(
405:pub struct BajanQueryError(pub String);
411:pub struct ContradictionSide {
423:pub struct ContradictionPair {
434:pub struct StagedInvalidation {
448:pub struct ContradictionResult {
475:pub fn contradictions(
--- src/contradict.rs
27:pub const PASS_ID: &str = "contradiction-scan";
32:const NEGATION_TOKENS: [&str; 3] = ["not", "no", "never"];
36:const NUMERAL_MASK: &str = "\u{0}num\u{0}";
39:const RULE_NEGATION: &str = "negation-marker";
40:const RULE_NUMERIC: &str = "numeric-mismatch";
45:fn is_numeral(token: &str) -> bool {
60:fn stripped_form(tokens: &[&str]) -> String {
70:fn has_negation(tokens: &[&str]) -> bool {
77:fn masked_form(tokens: &[&str]) -> String {
91:pub struct ContradictionReport {
122:pub fn run_contradiction_pass(
--- src/propose.rs
21:pub const SPEC: &str = "specs/contradiction-review.md";
27:pub struct LlmContradictionOutput {
33:pub struct LlmPair {
46:pub const PROPOSER_SYSTEM_PROMPT: &str = "\
56:pub fn build_proposer_prompt(claims: &[(usize, &str)]) -> String {
69:fn parse_proposer_response(body: &str) -> Result<LlmContradictionOutput, String> {
93:pub struct LlmContradictionProposer {
103:impl std::fmt::Debug for LlmContradictionProposer {
115:impl LlmContradictionProposer {
192:pub struct ProposerConfig {
200:pub enum ProposerConfigError {
205:impl ProposerConfig {
240:pub struct ProposeReport {
264:pub fn run_propose_pass(
--- src/review.rs
23:pub fn normalize(text: &str) -> String {
35:pub struct ErReport {
74:pub fn run_er_pass(db: &SqliteStore, budget: usize, now: u64) -> Result<ErReport, BajanQueryError> {
--- src/resolve.rs
20:pub const SPEC: &str = "specs/extraction-claims.md";
29:pub struct IdentityRecord {
42:pub struct ResolutionReport {
50:pub fn resolve(db: &SqliteStore) -> Result<ResolutionReport, BajanError> {
84:pub fn restage(
--- src/store/nodes.rs
15:pub const HEDGE_MARKERS: &[&str] = &[
33:pub enum ClaimStatus {
46:pub enum EdgeLabel {
62:pub enum Evidence {
70:impl Evidence {
86:pub struct ClaimNode {
102:pub struct Lineage {
112:pub struct SupersessionRecord {
124:pub struct EpisodeTombstone {
134:pub struct RestageRecord {
145:pub struct InvalidationProposal {
153:pub struct V1ClaimNode {
168:pub struct MigrationReport {
174:impl fmt::Display for MigrationReport {
188:pub fn migrate_v1_to_v2(nodes: Vec<V1ClaimNode>) -> MigrationReport {
215:pub fn hedge_markers_in(text: &str) -> Vec<String> {
236:pub fn collapse(text: &str) -> String {
246:pub fn dropped_hedge_markers(span: &str, episode: &str) -> Vec<String> {
268:pub enum ReviewDecision {
278:pub enum ReviewStatus {
290:pub struct ReviewRecord {
309:pub struct ReviewAuditRecord {
322:pub enum EnqueueOutcome {
339:pub enum ProposalDecision {
349:pub enum ProposalStatus {
360:pub struct ContradictionProposal {
376:pub struct ContradictionAuditRecord {
389:pub enum ProposeOutcome {
402:pub enum StoreError {
--- src/store/sqlite.rs
31:pub const SPEC: &str = "specs/graph-model.md";
38:const BUSY_TIMEOUT_MS: u64 = 10_000;
40:const SCHEMA: &str = "
164:fn review_row(row: &rusqlite::Row<'_>) -> Result<ReviewRecord, StoreError> {
203:pub const CPROP_SPEC: &str = "specs/contradiction-review.md";
208:fn contradiction_proposal_row(
249:fn episode_from_row(row: &rusqlite::Row<'_>) -> Result<EpisodeRecord, StoreError> {
277:fn claim_from_row(row: &rusqlite::Row<'_>) -> Result<(usize, ClaimNode), StoreError> {
324:pub struct DumpedClaim {
334:pub struct EvalManifest {
353:pub struct ExtractionDump {
406:pub struct DumpedEdge {
418:fn migrate_edges_provenance(conn: &Connection) -> Result<(), StoreError> {
436:pub struct SqliteStore {
440:fn sql_err(e: impl std::fmt::Display) -> StoreError {
449:fn encode_edge_label(
472:impl SqliteStore {
--- src/llm.rs
29:pub const SPEC: &str = "specs/extraction-claims.md";
33:pub const LLM_PROMPT_OVERHEAD_TOKENS: usize = 512;
36:pub const LLM_DEFAULT_CONTEXT_TOKENS: usize = 8192;
41:pub const LLM_DEFAULT_MAX_ATTEMPTS: u32 = 3;
47:const LLM_BACKOFF_BASE_MS: u64 = 2_000;
50:const LLM_BACKOFF_CAP_MS: u64 = 60_000;
57:pub fn jittered_backoff(attempt: u32) -> Duration {
72:pub fn llm_version(model_id: &str) -> String {
95:pub fn llm_backoff(attempt: u32) -> Duration {
105:fn tokenizer() -> Option<&'static tiktoken_rs::CoreBPE> {
123:pub fn chunk_episode(text: &str, budget_tokens: usize) -> Vec<String> {
146:pub fn strip_json_fence(content: &str) -> &str {
168:pub struct LlmOutput {
174:pub struct LlmClaim {
189:pub const LLM_SYSTEM_PROMPT: &str = "\
200:pub fn build_user_prompt(chunks: &[String]) -> String {
223:pub struct UreqTransport {
227:impl UreqTransport {
238:impl Default for UreqTransport {
244:impl LlmTransport for UreqTransport {
275:fn classify_transport_error(raw: &str) -> crate::extract::FailureClass {
295:fn parse_response(body: &str) -> Result<(LlmOutput, Option<u64>), String> {
337:pub struct LlmExtractor {
368:impl std::fmt::Debug for LlmExtractor {
382:impl LlmExtractor {
578:impl Extractor for LlmExtractor {

===== WHISPER DISTILL CONTRACT =====
//! The distill contract: turu owns the mechanics (snapshot, revision,
//! conflict detection, install, audit); the calling agent owns the semantic
//! rewrite. Revisions are immutable and never pruned.

use serde::Serialize;
use serde_json::json;
use std::fs;

use crate::entry;
use crate::workspace::{self, Target};
use crate::{Result, WhisperError};

/// Snapshot + working paths for one revision.
#[derive(Debug, Serialize)]
pub struct Revision {
    pub id: String,
    pub snapshot_path: std::path::PathBuf,
    pub working_path: std::path::PathBuf,
    pub target_path: std::path::PathBuf,
    pub sha256: String,
    /// Per-entry usage stats (entry id → use_count/last_recalled) 
...[truncated]...
::{Cli, Commands};

use super::support::{append_scope_key, append_target, collect_text, scope_name};
use super::{Arm, Ctx};

#[allow(clippy::too_many_arguments)]
pub(crate) fn append(
    ctx: &Ctx,
    scope: workspace::Scope,
    text: Option<&str>,
    texts: &[String],
    stdin: bool,
    topic: Option<&str>,
    supersedes: Option<&str>,
    global: bool,
    private: bool,
) -> whisper::Result<Arm> {
    let text = collect_text(text, texts, stdin)?;
    reject_empty(&text)?;
    let target = append_target(scope, global, private, &ctx.facts, &ctx.resolved)?;
    let ts = entry::parse_or_now(std::env::var("TURU_NOW").ok().as_deref())?;
    let report = workspace::append_entry(
        &target,
        &append_scope_key(scope, &target, &ctx.facts, &ctx.resolved),
        &text,
        topic,
        supersedes,
        &ts,
    )?;
    Ok((
        append_data(&target, &report),
        append_warnings(&text),
        append_hint(&report),
    ))
}

/// The append envelope: scope, path, and the write report fields.
fn append_data(target: &workspace::Target, report: &workspace::AppendReport) -> serde_json::Value {
    serde_json::json!({
        "scope": target.scope,
        "path": target.path,
        "appended_bytes": report.bytes,
        "id": report.id,
        "duplicate": report.duplicate,
        "superseded": report.superseded,
    })
}

/// Advisory incident-log lint (whisper-4xl): warn, never block.
fn append_warnings(text: &str) -> Vec<String> {
    entry::incident_log_density(text).into_iter().collect()
}

/// Duplicate writes write nothing — surface that as the next step.
fn append_hint(report: &workspace::AppendReport) -> Option<String> {
    report.duplicate.then_some(
        "entry already present (same scope + second + text) — nothing written".to_string(),
    )
}

#[allow(clippy::too_many_arguments)]
pub(crate) fn recall_cmd(
    ctx: &Ctx,
    scope: &str,
    topic: Option<String>,
    budget: Option<usize>,
    digest: bool,
    include_superseded: bool,
    record_usage: bool,
) -> whisper::Result<Arm> {
    let recall_scope = recall::parse_recall_scope(scope)?;
    let data = recall::recall(
        &recall_scope,
        &ctx.facts,
        &ctx.resolved,
        &recall::RecallQuery {
            topic,
            budget,
            include_superseded,
            digest,
            record_usage,
        },
    )?;
    let warnings = empty_scope_warnings(&data);
    Ok((
        data,
        warnings,
        Some("recall serves mechanically — when to load it is your policy".into()),
    ))
}

pub(crate) fn distill_cmd(
    ctx: &Ctx,
    scope: workspace::Scope,
    begin: bool,
    commit: bool,
    revision: Option<&str>,
) -> whisper::Result<Arm> {
    if begin == commit {
        return Err(WhisperError::new("pass exactly one of --begin or --commit"));
    }
    if begin {
        distill_begin(ctx, scope)
    } else {
        distill_commit(ctx, scope, revision)
    }
}

/// `--begin`: snapshot the scope file and hand back a revision for the
/// rewrite pass. Lints entry texts (whisper-4xl) — never the raw file,
/// where [id:…] markers would false-positive.
fn distill_begin(ctx: &Ctx, scope: workspace::Scope) -> whisper::Result<Arm> {
    let ts = entry::parse_or_now(std::env::var("TURU_NOW").ok().as_deref())?;
    let rev = distill::begin_for_scope(scope, &ctx.facts, &ctx.resolved, &ts)?;
    let warnings = snapshot_lint(&rev.snapshot_path);
    Ok((
        serde_json::json!({
            "phase": "begin",
            "revision": rev.id,
            "snapshot_path": rev.snapshot_path,
            "working_path": rev.working_path,
            "target_path": rev.target_path,
            "sha256": rev.sha256,
            "recency": rev.recency,
        }),
        warnings,
        Some(format!(
            "rewrite {} with the distilled content, then: turu distill {} --commit --revision {}",
            rev.working_path.display(),
            scope_name(scope),
            rev.id
        )),
    ))
}

/// `--commit`: verify no drift, install the distilled working file.
fn distill_commit(
    ctx: &Ctx,
    scope: workspace::Scope,
    revision: Option<&str>,
) -> whisper::Result<Arm> {
    let revision = revision.ok_or_else(|| {
        WhisperError::new("--commit requires --revision <id>")
            .with_suggestion("turu distill <scope> --begin returns the revision id")
    })?;
    let report = distill::commit_for_scope(scope, &ctx.facts, &ctx.resolved, revision)?;
    Ok((
        serde_json::json!({
            "phase": "commit",
            "revision": report.revision,
            "replaced": report.replaced,
            "snapshot_path": report.snapshot_path,
            "noop": report.noop,
        }),
        vec![],
        Some(format!(
            "snapshot retained at {} (immutable)",
            report.snapshot_path.display()
        )),
    ))
}

/// Append/recall/distill arms; None when the command is not a knowledge verb.
pub(crate) fn pick_knowledge(cli: &Cli, ctx: &Ctx) -> whisper::Result<Option<Arm>> {
    if let Some(arm) = append_recall_arm(cli, ctx)? {
        return Ok(Some(arm));
    }
    distill_arm(cli, ctx)
}

/// Append and recall arms; None for other commands.
fn append_recall_arm(cli: &Cli, ctx: &Ctx) -> whisper::Result<Option<Arm>> {
    if let Some(arm) = append_arm(cli, ctx)? {
        return Ok(Some(arm));
    }
    recall_arm(cli, ctx)
}

/// The append arm.
fn append_arm(cli: &Cli, ctx: &Ctx) -> whisper::Result<Option<Arm>> {
    match &cli.command {
        Commands::Append {
            scope,
            text,
            texts,
            stdin,
            topic,
            supersedes,
            global,
            private,
        } => Ok(Some(append(
            ctx,
            scope.parse()?,
            text.as_deref(),
            texts,
            *stdin,
            topic.as_deref(),
            supersedes.as_deref(),
            *global,
            *private,
        )?)),
        _ => Ok(None),
    }
}

/// The recall arm.
fn recall_arm(cli: &Cli, ctx: &Ctx) -> whisper::Result<Option<Arm>> {
    match &cli.command {
        Commands::Recall {
            scope,
            topic,
            budget,
            digest,
            include_superseded,
            no_usage,
        } => Ok(Some(recall_cmd(
            ctx,
            scope,
            topic.clone(),
            *budget,
            *digest,
            *include_superseded,
            !*no_usage,
        )?)),
        _ => Ok(None),
    }
}

/// The distill cycle arm (exactly one of --begin/--commit).
fn distill_arm(cli: &Cli, ctx: &Ctx) -> whisper::Result<Option<Arm>> {
    match &cli.command {
        Commands::Distill {
            scope,
            begin,
            commit,
            revision,
        } => Ok(Some(distill_cmd(
            ctx,
            scope.parse()?,
            *begin,
            *commit,
            revision.as_deref(),
        )?)),
        _ => Ok(None),
    }
}

/// Empty scope (whisper-2c1): ok:true + advisory warning, never a hard
/// failure that breaks && chains or set -e.
fn empty_scope_warnings(data: &serde_json::Value) -> Vec<String> {
    if data.get("empty") == Some(&serde_json::Value::Bool(true)) {
        vec!["scope is empty — nothing to recall; append entries or check the routing block".into()]
    } else {
        Vec::new()
    }
}

/// Lint the snapshot's entry texts (whisper-4xl) — never the raw file,
/// where [id:…] markers would false-positive every well-formed file.
fn snapshot_lint(snapshot_path: &std::path::Path) -> Vec<String> {
    let snapshot = std::fs::read_to_string(snapshot_path).unwrap_or_default();
    entry::parse_file(&snapshot)
        .into_iter()
        .filter_map(|item| match item {
            entry::Item::Entry(e) => {
                entry::incident_log_density(&e.text).map(|a| format!("{}: {}", &e.id[..12], a))
            }
            _ => None,
        })
        .collect()
}

/// Loud failure when append gets no payload.
fn reject_empty(text: &str) -> whisper::Result<()> {
    if text.trim().is_empty() {
        return Err(WhisperError::new("nothing to append")

## Assistant

bash -lc sed -n '1,220p' /tmp/review/bajan-main/src/ingest.rs; printf '\n===== EXTRACT CORE =====\n'; sed -n '320,530p' /tmp/review/bajan-main/src/extract.rs; sed -n '680,980p' /tmp/review/bajan-main/src/extract.rs; printf '\n===== QUERY API =====\n'; sed -n '84,410p' /tmp/review/bajan-main/src/query.rs; printf '\n===== NODE MODEL =====\n'; sed -n '1,190p' /tmp/review/bajan-main/src/store/nodes.rs; printf '\n===== SQLITE SCHEMA =====\n'; sed -n '40,165p' /tmp/review/bajan-main/src/store/sqlite.rs

## Tool

//! Purpose: ingest pipeline module — persist a normalized episode stream
//! verbatim with its immutable source metadata (specs/ingestion-contract.md).
//! Responsibilities: the published episode-stream record schema
//! (`ic_stream-schema`), malformed-record rejection (`ic_malformed`),
//! NFC-normalized id identity (`ic_id_canon`), at most one persisted episode
//! per stable id (`ic_unique_id`), idempotent re-ingest (`ic_idempotent`),
//! tombstoned-id rejection with the machine-readable deleted-id reason
//! (`ic_deleted_tombstone`), and one outcome record per submitted episode
//! (`ic_outcome-schema`).
//! Rationale: bajan never parses source formats (`ic_no_format_parsing`);
//! the converter upstream does. The store persists only what the stream
//! carries — verbatim text, locator (or typed absent marker), and source
//! metadata whose cutoff is never the ingest time (`ic_date_fidelity`).

use crate::cli::BajanError;

use serde::{Deserialize, Serialize};
use unicode_normalization::UnicodeNormalization;

pub const SPEC: &str = "specs/ingestion-contract.md";

/// Structural locator for an episode (`ic_verbatim`): a structural anchor
/// when derivable, or the typed absent marker when none is — absent is a
/// distinct variant, never a string that could collide with a real locator
/// (`ic_stream-schema` absent-marker convention).
#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
#[serde(tag = "kind", content = "value", rename_all = "snake_case")]
pub enum Locator {
    /// A derivable structural locator: heading anchor, text fragment,
    /// page/slide reference.
    Span(String),
    /// No locator derivable — typed absent, cannot collide with a span.
    Absent,
}

impl Locator {
    /// Tag + optional value for row persistence.
    pub fn kind(&self) -> &'static str {
        match self {
            Locator::Span(_) => "span",
            Locator::Absent => "absent",
        }
    }

    pub fn value(&self) -> Option<&str> {
        match self {
            Locator::Span(s) => Some(s),
            Locator::Absent => None,
        }
    }

    /// Rebuild from stored parts.
    pub fn from_parts(kind: &str, value: Option<String>) -> Self {
        match kind {
            "span" => Locator::Span(value.unwrap_or_default()),
            _ => Locator::Absent,
        }
    }
}

/// Immutable source metadata (`ic_verbatim`): source type, data cutoff
/// (`ic_date_fidelity`: the source's cutoff or absent — never ingest time),
/// authority tier, and optional workspace tags.
#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
pub struct SourceMeta {
    pub source_type: String,
    pub data_cutoff: Option<String>,
    pub authority_tier: u8,
    pub tags: Vec<String>,
}

/// One normalized episode record from the converter stream
/// (`ic_stream-schema`): stable id, verbatim text, locator, and metadata.
#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
pub struct EpisodeRecord {
    pub id: String,
    pub text: String,
    pub locator: Locator,
    pub source: SourceMeta,
}

/// Machine-readable rejection reason (`ic_outcome_schema`): why a record
/// was refused at the ingest boundary. Stable snake_case codes. The
/// conflict/duplicate pair (`ic_mutated_resubmit`, `ic_batch_duplicate`)
/// arrived with the resubmission-policy decisions (bajan-6sw).
#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum RejectReason {
    /// No stable id: absent or whitespace-only (`ic_malformed`).
    MissingId,
    /// Verbatim text absent, empty, or whitespace-only (`ic_malformed`).
    MissingText,
    /// Required source metadata missing (`ic_malformed`).
    MissingMetadata,
    /// A stable id already persisted was re-submitted with mutated text,
    /// locator, or source metadata (`ic_mutated_resubmit`) — the persisted
    /// episode is never updated in place.
    Conflict,
    /// A later occurrence of a stable id within the same submitted stream
    /// (`ic_batch_duplicate`) — first occurrence wins, later ones are
    /// rejected per record.
    Duplicate,
    /// A deletion tombstone exists for the stable id
    /// (`ic_deleted_tombstone`): the id was explicitly deleted by an
    /// operator and every later submission — unchanged or mutated — is
    /// refused until revive clears the tombstone (`ic_deleted_recreate`).
    DeletedId,
}

impl RejectReason {
    /// Stable machine-readable snake_case code.
    pub fn code(&self) -> &'static str {
        match self {
            RejectReason::MissingId => "missing_id",
            RejectReason::MissingText => "missing_text",
            RejectReason::MissingMetadata => "missing_metadata",
            RejectReason::Conflict => "conflict",
            RejectReason::Duplicate => "duplicate",
            RejectReason::DeletedId => "deleted_id",
        }
    }
}

/// Per-episode ingest outcome (`ic_outcome-schema`): one record per
/// submitted episode — `persisted`, `already_persisted`, or `rejected`
/// with a machine-readable reason.
#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
#[serde(tag = "outcome", rename_all = "snake_case")]
pub enum IngestOutcome {
    /// Newly persisted (`ic_verbatim` accept path).
    Persisted,
    /// An episode with this stable id is already persisted
    /// (`ic_unique_id`/`ic_idempotent`); nothing was written.
    AlreadyPersisted,
    /// Refused — never persisted (`ic_malformed` reject path).
    Rejected { reason: RejectReason },
}

/// Persist one episode record (`ic_malformed`, `ic_id_canon`, `ic_unique_id`,
/// `ic_idempotent`): malformed records are rejected with a machine-readable
/// reason and never persisted; valid records persist verbatim; a repeated
/// stable id (compared on NFC-normalized form) reports `already_persisted`
/// and writes nothing — re-ingest never duplicates or mutates provenance
/// (`ic_idempotent`).
pub fn persist(
    db: &crate::store::sqlite::SqliteStore,
    record: &EpisodeRecord,
) -> Result<IngestOutcome, BajanError> {
    // ic_id_canon: id equality is decided on the NFC-normalized form.
    let normalized_id: String = record.id.nfc().collect();
    if normalized_id.trim().is_empty() {
        return Ok(IngestOutcome::Rejected {
            reason: RejectReason::MissingId,
        });
    }
    // ic_malformed: verbatim text must be present and non-whitespace.
    if record.text.trim().is_empty() {
        return Ok(IngestOutcome::Rejected {
            reason: RejectReason::MissingText,
        });
    }
    // ic_malformed: required source metadata must be present.
    if record.source.source_type.trim().is_empty() {
        return Ok(IngestOutcome::Rejected {
            reason: RejectReason::MissingMetadata,
        });
    }
    let canonical = EpisodeRecord {
        id: normalized_id,
        ..record.clone()
    };
    // ic_deleted_tombstone: a deletion tombstone retires the stable id —
    // the gate runs BEFORE any acceptance decision (the episode row is
    // gone, so an ungated insert would resurrect the deleted episode).
    // Every submission of a tombstoned id, unchanged or mutated, is
    // rejected with the machine-readable deleted-id reason; only an
    // explicit operator revive clears the tombstone (`ic_deleted_recreate`).
    if db.is_tombstoned(&canonical.id).map_err(BajanError::from)? {
        return Ok(IngestOutcome::Rejected {
            reason: RejectReason::DeletedId,
        });
    }
    let inserted = db
        .insert_episode(&canonical)
        .map_err(|e| BajanError::Store(e.to_string()))?;
    if inserted {
        return Ok(IngestOutcome::Persisted);
    }
    // ic_mutated_resubmit vs ic_idempotent: the id already exists — compare
    // the submitted record against the persisted row verbatim. Unchanged →
    // `already_persisted`; any difference in text, locator, or source
    // metadata → rejected with the machine-readable `conflict` reason. The
    // persisted episode is never updated in place and never duplicated.
    let persisted = db
        .get_episode(&canonical.id)
        .map_err(BajanError::from
...[truncated]...
 false
    }
}

/// A claim node under `gm_schema_v2` — exactly eight fields, no confidence
/// field and no vector blob.
#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct ClaimNode {
    pub text: String,
    pub valid_at: Option<String>,
    pub invalid_at: Option<String>,
    pub data_cutoff: Option<String>,
    pub status: ClaimStatus,
    pub scope: String,
    pub source_type: String,
    pub evidence: Evidence,
}

/// Lineage provenance for a stored claim (`gm_reified`): the episode it
/// derives from and the extractor version that produced it. Kept parallel
/// to the node — the claim-node schema (`gm_schema_v2`) stays closed, and
/// supersession targets claims by (episode, version) provenance.
#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
pub struct Lineage {
    pub episode_id: String,
    pub extractor_version: String,
}

/// Tombstone record for a superseded claim (`ex_supersession`): the
/// machine-readable reason lives here, never on the claim node (the
/// schema field list stays closed). The tombstoned node keeps its
/// lineage and evidence — a tombstone, not a delete (`gm_lineage_survives`).
#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
pub struct SupersessionRecord {
    pub claim_key: usize,
    pub reason: crate::extract::Reason,
    pub superseded_at: u64,
}

/// Deletion tombstone for an episode (`ic_deleted_tombstone`): the
/// stable id is retired — any later submission of the id is rejected with
/// the machine-readable deleted-id reason until an explicit operator
/// revive clears the tombstone (`ic_deleted_recreate`). The episode row
/// itself is gone; only this marker remembers the deletion.
#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
pub struct EpisodeTombstone {
    pub episode_id: String,
    pub deleted_at: u64,
}

/// Record for one explicit re-stage action (`ex_supersession`): the
/// only path from a superseded claim back to `staged`, carrying the
/// operator identity and timestamp — the human-owned counterpart of the
/// tombstone, mirroring the adopt audit trail.
#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
pub struct RestageRecord {
    pub claim_key: usize,
    pub actor: String,
    pub restaged_at: u64,
}

/// An invalidation proposal staged by a candidate claim that conflicts
/// with an existing active claim (`ex_mutation_proposal`): carries the
/// causing-episode lineage; the active claim itself is never mutated by
/// the extractor.
#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
pub struct InvalidationProposal {
    pub claim_key: usize,
    pub causing_episode_id: String,
}

/// A pre-v2 claim node — the seven frozen v1 fields (`gm_schema_v1`).
#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct V1ClaimNode {
    pub text: String,
    pub valid_at: Option<String>,
    pub invalid_at: Option<String>,
    pub data_cutoff: Option<String>,
    pub status: ClaimStatus,
    pub scope: String,
    pub source_type: String,
}

/// Result of the v1 → v2 migration. The backfill count is carried in data
/// so callers can report it loudly (`to_string` renders it); migration
/// never schedules re-extraction — `reextraction_scheduled` is pinned to
/// zero by test.
#[derive(Debug, Clone, PartialEq, Eq)]
pub struct MigrationReport {
    pub nodes: Vec<ClaimNode>,
    pub backfilled: usize,
    pub reextraction_scheduled: usize,
}

impl fmt::Display for MigrationReport {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(
            f,
            "schema v1→v2 migration: backfilled evidence=unknown on {} claim node(s); \
             unknown spans flagged for reflection, re-extraction NOT scheduled",
            self.backfilled
        )
    }
}

/// Migrate pre-v2 claim nodes to v2: backfill `evidence = unknown` on every
/// node and report the count loudly. No node is dropped or rewritten apart
/// from the evidence backfill; no re-extraction is scheduled.
pub fn migrate_v1_to_v2(nodes: Vec<V1ClaimNode>) -> MigrationReport {
    let backfilled = nodes.len();
    let nodes = nodes

===== SQLITE SCHEMA =====
const SCHEMA: &str = "
CREATE TABLE IF NOT EXISTS episodes (
    id TEXT PRIMARY KEY,
    text TEXT NOT NULL,
    locator_kind TEXT NOT NULL,
    locator TEXT,
    source_type TEXT NOT NULL,
    data_cutoff TEXT,
    authority_tier INTEGER NOT NULL,
    tags TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS claims (
    claim_key INTEGER PRIMARY KEY,
    text TEXT NOT NULL,
    valid_at TEXT,
    invalid_at TEXT,
    data_cutoff TEXT,
    status TEXT NOT NULL,
    scope TEXT NOT NULL,
    source_type TEXT NOT NULL,
    evidence_kind TEXT NOT NULL,
    evidence_text TEXT,
    evidence_locator TEXT
);
CREATE TABLE IF NOT EXISTS lineage (
    claim_key INTEGER NOT NULL,
    episode_id TEXT NOT NULL,
    extractor_version TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS extracted (
    episode_id TEXT NOT NULL,
    extractor_version TEXT NOT NULL,
    PRIMARY KEY (episode_id, extractor_version)
);
CREATE TABLE IF NOT EXISTS audits (
    claim_key INTEGER NOT NULL,
    actor TEXT NOT NULL,
    adopted_at INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS edges (
    rowid_key INTEGER PRIMARY KEY AUTOINCREMENT,
    from_claim INTEGER NOT NULL,
    label TEXT NOT NULL,
    to_claim INTEGER NOT NULL,
    provenance TEXT
);
CREATE TABLE IF NOT EXISTS invalidations (
    rowid_key INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_key INTEGER NOT NULL,
    causing_episode_id TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS supersessions (
    rowid_key INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_key INTEGER NOT NULL,
    reason TEXT NOT NULL,
    superseded_at INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS restages (
    rowid_key INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_key INTEGER NOT NULL,
    actor TEXT NOT NULL,
    restaged_at INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS reviews (
    rowid_key INTEGER PRIMARY KEY AUTOINCREMENT,
    from_claim INTEGER NOT NULL,
    to_claim INTEGER NOT NULL,
    status TEXT NOT NULL,
    evidence TEXT NOT NULL,
    fingerprint TEXT NOT NULL,
    queued_at INTEGER NOT NULL,
    resolved_at INTEGER,
    actor TEXT,
    decision TEXT
);
CREATE TABLE IF NOT EXISTS er_aliases (
    a TEXT NOT NULL,
    b TEXT NOT NULL,
    PRIMARY KEY(a, b)
);
CREATE TABLE IF NOT EXISTS review_audits (
    rowid_key INTEGER PRIMARY KEY AUTOINCREMENT,
    from_claim INTEGER NOT NULL,
    to_claim INTEGER NOT NULL,
    decision TEXT NOT NULL,
    actor TEXT NOT NULL,
    resolved_at INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS contradiction_proposals (
    rowid_key INTEGER PRIMARY KEY AUTOINCREMENT,
    from_claim INTEGER NOT NULL,
    to_claim INTEGER NOT NULL,
    status TEXT NOT NULL,
    producer TEXT NOT NULL,
    rationale TEXT NOT NULL,
    fingerprint TEXT NOT NULL,
    queued_at INTEGER NOT NULL,
    resolved_at INTEGER,
    actor TEXT,
    decision TEXT
);
CREATE TABLE IF NOT EXISTS contradiction_proposal_audits (
    rowid_key INTEGER PRIMARY KEY AUTOINCREMENT,
    from_claim INTEGER NOT NULL,
    to_claim INTEGER NOT NULL,
    decision TEXT NOT NULL,
    actor TEXT NOT NULL,
    resolved_at INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS episode_tombstones (
    episode_id TEXT PRIMARY KEY,
    deleted_at INTEGER NOT NULL
);
";

/// Row mapper shared by `episodes()` and `get_episode()`: reconstructs a
/// normalized episode record from the `episodes` table (`ic_verbatim`).
/// Read-path errors — including a corrupted tags column — map to
/// `StoreError::Sqlite` carrying the governing spec (bajan-2sj), never a
/// panic: every invocation must emit the suite envelope.
/// Row mapper shared by the review reads (`er_review-schema`): reconstruct
/// a queue record from a `reviews` row — status and decision decoded
/// strictly from the published vocabularies, a corrupt row is a store
/// error, never a silent guess.
fn review_row(row: &rusqlite::Row<'_>) -> Result<ReviewRecord, StoreError> {
    let from_claim: i64 = row.get(0).map_err(sql_err)?;

## Assistant

bash -lc printf '===== BAJAN EXTRACTION SPEC CONSTRAINTS =====\n'; sed -n '1,190p' /tmp/review/bajan-main/specs/extraction-claims.md; printf '\n===== BAJAN QUERY IMPLEMENTATION =====\n'; sed -n '90,410p' /tmp/review/bajan-main/src/query.rs; printf '\n===== BAJAN STORE METHODS =====\n'; rg -n '^    pub fn ' /tmp/review/bajan-main/src/store/sqlite.rs; printf '\n===== WHISPER DISTILL FULL =====\n'; sed -n '1,260p' /tmp/review/whisper-main/src/distill.rs; printf '\n===== WHISPER ENTRY FULL =====\n'; sed -n '1,260p' /tmp/review/whisper-main/src/entry.rs

## Tool

===== BAJAN EXTRACTION SPEC CONSTRAINTS =====
---
id: extraction.claims
kind: intent
statement: "WHEN an episode is persisted THE bajan extractor SHALL propose candidate claims typed against the published claim schema with lineage edges to their source episode"
---

# claims

The write path between a persisted episode (see `ingestion.contract`) and a
proposed claim (see `graph.model`). One extraction call per episode —
single-shot, as validated in the corpus (Chalef/Zep 206: "we've managed to
get a single-shot extraction working… really cheaply as a consequence") —
produces candidate claims against the frozen claim-node schema
(`gm_schema_v2` in graph.model — text, dates, cutoff, status, scope,
source_type, evidence). Everything
after that call is deterministic: normalization, dedup (simhash/entropy),
entity matching, and conflict detection never invoke an LLM (Chalef: "far
cheaper, far faster, far more deterministic"). The extractor proposes;
it never merges entities, applies trust policies, or mutates the graph.
Output is typed at the door (Coyle 209: validation before the loop
continues) and rejected rather than repaired. Extraction output is cached
per (episode id, extractor version) so re-ingest stays idempotent and the
graph remains rebuildable (`gm_embedded-store` semantics, in
graph.model); a version bump re-extracts as new work, never reusing a
cache entry from another version. An episode with zero valid candidates is
legitimately extracted and cached as empty — absence of claims is data,
not failure. A parked episode — one that exhausted its retry budget on
repeated call failure (bajan-42y) — holds no cache entry either, so a
later extraction pass re-attempts it with a fresh retry budget: the park
is one run's honest stopping (the same honesty as budget-exhaustion in
query.tools), never a permanent state, and re-ingest neither grants nor
blocks the retry — eligibility follows cache absence.

Pipeline seam: the three specs' lifecycles hand off as follows — an
episode leaves `ingestion.contract` as `persisted` and enters this spec's
lifecycle as `pending`; a claim leaves this spec's lifecycle as `staged`,
which is the same state graph.model names `proposed` (from there,
`adopt`/`discard`/`invalidate` apply). `staged` and `proposed` are one
state viewed from two files. How hedging survives extraction is governed
by `gm_hedge_anchor` in graph.model; reflection flags violations rather
than introducing claims (see `ex_reflection`). Supersession on version
bumps, per-extraction-call run records, and evidence-span containment
follow fpa's kb-extract/kb-store pipeline
(`openspec/changes/update-extraction-provenance/design.md` D1, D3, D4);
span-absent episodes persist a typed absent marker — same convention as
the ingestion contract's locator/cutoff absent marker — never a string
that could collide with a real span.

## Constraints

| id | kind | expr | traces_to |
|----|------|------|-----------|
| ex_single_call | invariant | each persisted episode id receives exactly one successful LLM extraction call producing candidate claims and entities; failed calls retry with backoff and park the episode in `rejected` after repeated failure; re-ingest of a successfully extracted episode reuses the (episode id, extractor version)-keyed cached output and starts no new call | [[extraction.claims]] |
| ex_park_requeue | invariant | an episode parked in `rejected` after repeated call failure holds no extraction-cache entry at the failed extractor version, so a later extraction pass re-attempts it with a fresh retry budget — the park is one run's honest stopping, never a permanent state; every re-attempt writes its own run rows and prior parked run rows persist with their reasons; re-ingest is orthogonal — an unchanged re-submission of a parked episode is an ingest-side no-op (`already_persisted`) that neither grants nor blocks the fresh budget, because eligibility follows cache absence, never re-ingest | [[extraction.claims]] |
| ex_typed_gate | invariant | a candidate claim persists only if it validates against the published claim schema, carries at least one episode lineage edge, and carries an evidence span that passes `ex_evidence_containment`; invalid candidates are rejected, never repaired; an episode with zero valid candidates is legitimately extracted and cached as empty | [[extraction.claims]] |
| ex_supersession | invariant | re-extracting an episode at a new extractor version supersedes only that episode's `staged` claims derived from prior extractor versions — they become `rejected` with reason `superseded-by-reextraction`, lineage and evidence intact (a tombstone, not a delete) — while `active` and `rejected` claims from any version are never mutated; new output that conflicts with an `active` claim stages an invalidation proposal per `ex_mutation_proposal`; a superseded claim re-enters `staged` only through an explicit re-stage action, never an automated path | [[extraction.claims]] |
| ex_run_record | invariant | every extraction call writes one run row — episode id, extractor version, model id when the extractor uses an LLM, started and finished timestamps, finish status — parallel to, and without changing, the `(episode id, extractor version)` cache economics; every failure outcome (an episode parked in `rejected` after repeated call failure, every candidate rejection at the validation gate) carries a machine-readable reason stored on the run or rejection record, never on a claim node | [[extraction.claims]] |
| ex_evidence_containment | invariant | every candidate claim carries an evidence span — a verbatim span of the supporting episode text plus its episode locator, or the typed absent marker when sentence alignment failed — validated by containment after whitespace collapse (all whitespace runs become a single space) of both span and episode text; a span failing containment is rejected with reason `evidence-not-contained`, never repaired; a typed-absent span persists but is flagged by the deterministic pass (`ex_reflection` extended), not treated as a violation | [[extraction.claims]] |
| ex_no_llm_post | invariant | normalization, dedup, entity matching, and conflict detection after the extraction call are deterministic; normalization rules appear both as prompt instructions and in a deterministic post-pass, because prompts are not bulletproof | [[extraction.claims]] |
| ex_mutation_proposal | invariant | a candidate claim that conflicts with an existing active claim stages an invalidation proposal carrying its causing-episode lineage; the existing claim is not mutated by the extractor | [[extraction.claims]] |
| ex_reflection | advisory | the single extraction call includes a self-check that verifies candidate claims against the episode text and enriches change lineage, rendered as flags by a deterministic pass; it flags unsupported candidates and never introduces new ones, and it is not a second LLM call | [[extraction.claims]] |
| ex_tag_inheritance | invariant | workspace tags and source metadata on an episode are inherited by every claim derived from it as a projection — the union over its lineage edges, resolved by walking `derived_from` at query time — and are never stored on the claim node | [[extraction.claims]] |
| ex_deterministic_structure | invariant | structure the converter already supplied (heading anchors, section boundaries, links) is consumed deterministically and never re-extracted by the LLM | [[extraction.claims]] |
| ex_section_filter | invariant | the deterministic post-pass rejects every candidate of an episode whose tags include a non-knowledge section-kind tag — `section-kind:praise`, `section-kind:copyright`, `section-kind:acknowledgments` — with machine-readable reason `section-filtered` on the run record (never on a claim node, per `ex_run_record`); the deny set is fixed in code, never an LLM judgment (`ex_no_llm_post` holds); untagged episodes stage unchanged, and a fully filtered episode still caches as extracted-empty per the `ex_single_call` cache economics | [[extraction.claims]] |
| ex_output_schema | extension_point | the candidate-claim
...[truncated]...
ime::now_utc()
        .format(&ts_format())
        .map_err(|e| WhisperError::new(format!("formatting timestamp: {e}")))
}

/// Full sha2 hex of `s` — the id alphabet for entries, revisions, bundles.
pub fn sha256_hex(s: &str) -> String {
    let mut h = Sha256::new();
    h.update(s.as_bytes());
    let d = h.finalize();
    let mut out = String::with_capacity(d.len() * 2);
    for b in d {
        out.push_str(&format!("{b:02x}"));
    }
    out
}

/// Deterministic entry id: sha2 of `scope_key + timestamp + content`.
///
/// Identical text within the same second in the same scope yields the same
/// id (the idempotency guarantee); a later re-statement is a new entry.
pub fn entry_id(scope_key: &str, ts: &str, text: &str) -> String {
    sha256_hex(&format!("{scope_key}\n{ts}\n{text}"))
}

/// A parsed structured entry.
#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
pub struct Entry {
    pub ts: String,
    pub id: String,
    pub topic: Option<String>,
    pub text: String,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub supersedes: Option<String>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub superseded_by: Option<String>,
}

impl Entry {
    /// Render as one ledger line (multi-line text becomes two-space
    /// continuation lines); suffix markers go after the final text line.
    pub fn render(&self) -> String {
        let mut line = format!("- {} [id:{}]", self.ts, self.id);
        if let Some(t) = &self.topic {
            line.push_str(&format!(" (#{t})"));
        }
        line.push(' ');
        let mut lines = self.text.split('\n');
        line.push_str(lines.next().unwrap_or(""));
        for cont in lines {
            line.push_str("\n  ");
            line.push_str(cont);
        }
        if let Some(s) = &self.supersedes {
            line.push_str(&format!(" (supersedes {s})"));
        }
        if let Some(s) = &self.superseded_by {
            line.push_str(&format!(" (superseded by {s})"));
        }
        line
    }
}

/// One item of a scope file, in file order.
#[derive(Debug, Clone, PartialEq)]
pub enum Item {
    Entry(Entry),
    /// Unmanaged text (including blank lines) — passed through verbatim.
    Line(String),
}

/// Parse a line that starts an entry (continuation lines handled by the
/// caller). Returns `None` for any non-entry line.
/// Strip a trailing " (<marker> value)" annotation; returns the trimmed
/// text and the extracted value (None when the marker is absent/malformed).
fn strip_marker(text: &str, marker: &str) -> (String, Option<String>) {
    let Some(idx) = text.rfind(marker) else {
        return (text.to_string(), None);
    };
    let suffix = &text[idx..];
    if !suffix.ends_with(')') {
        return (text.to_string(), None);
    }
    let value = suffix[marker.len()..suffix.len() - 1].to_string();
    (text[..idx].to_string(), Some(value))
}

/// Parse one entry line (ts, id, topic, text, supersede markers).
pub fn parse_entry_line(line: &str) -> Option<Entry> {
    let rest = line.strip_prefix("- ")?;
    let (ts, after) = rest.split_once(' ')?;
    // Timestamp must be canonical RFC-3339 seconds — malformed or
    // non-canonical lines degrade to unmanaged freeform instead of
    // corrupting recency ordering.
    match OffsetDateTime::parse(ts, &time::format_description::well_known::Rfc3339) {
        Ok(dt) if dt.format(&ts_format()).is_ok_and(|f| f == ts) => {}
        _ => return None,
    }
    let id_tok = after.strip_prefix("[id:")?;
    let (id, after) = id_tok.split_once(']')?;
    let (topic, after) = if let Some(stripped) = after.strip_prefix(" (#") {
        let (t, tail) = stripped.split_once(')')?;
        (Some(t.to_string()), tail.strip_prefix(' ').unwrap_or(tail))
    } else {
        (None, after.strip_prefix(' ').unwrap_or(after))
    };
    let (text, superseded_by) = strip_marker(after, " (superseded by ");
    let (text, supersedes) = strip_marker(&text, " (supersedes ");
    Some(Entry {
        ts: ts.to_string(),
        id: id.to_string(),
        topic,
        text,
        supersedes,
        superseded_by,
    })
}

/// Parse a whole scope file into ordered items. Continuation lines
/// (starting with exactly two spaces) fold into the preceding entry's text.
pub fn parse_file(raw: &str) -> Vec<Item> {
    let mut items = Vec::new();
    let mut lines = raw.lines().peekable();
    while let Some(line) = lines.next() {
        match parse_entry_line(line) {
            Some(mut entry) => {
                // Continuation lines start with EXACTLY two spaces (the
                // renderer's convention) — deeper indents (e.g. markdown
                // code blocks) stay unmanaged freeform.
                while lines.peek().is_some_and(|l| {
                    l.starts_with("  ") && !l.starts_with("   ") && !l.trim().is_empty()
                }) {
                    let cont = lines.next().unwrap();
                    entry.text.push('\n');
                    entry.text.push_str(cont.trim_start());
                }
                items.push(Item::Entry(entry));
            }
            None => items.push(Item::Line(line.to_string())),
        }
    }
    items
}

/// Render items back to file content (entries canonically, lines verbatim).
pub fn render_file(items: &[Item]) -> String {
    let mut out = String::new();
    for item in items {
        match item {
            Item::Entry(e) => {
                out.push_str(&e.render());
                out.push('\n');
            }
            Item::Line(l) => {
                out.push_str(l);
                out.push('\n');
            }
        }
    }
    out
}

/// All entry ids in a file's items.
pub fn entry_ids(items: &[Item]) -> Vec<&str> {
    items
        .iter()
        .filter_map(|i| match i {
            Item::Entry(e) => Some(e.id.as_str()),
            Item::Line(_) => None,
        })
        .collect()
}

/// Advisory incident-log lint (whisper-4xl): count date-like, id-like, and
/// chat-narration tokens in entry text; ≥3 per 500 chars (divisor floored
/// at 500 so short texts still need 3 tokens) suggests the text records an
/// incident instead of a generalizable lesson. Detection that warns can be
/// loose — this never blocks a write. Returns the advisory message.
/// Ro5-quantified lint thresholds (ticket whisper-4xl): ≥3 date/id-like
/// tokens per 500 chars ⇒ advisory. Divisor floored at 500 so short texts
/// still need 3 tokens. Tunable; detection that warns can be loose.
const LINT_TOKENS: f64 = 3.0;
const LINT_WINDOW: usize = 500;
const LINT_ID_MAX: usize = 64;

pub fn incident_log_density(text: &str) -> Option<String> {
    let tokens = text
        .split_whitespace()
        .filter(|t| is_date_like(t) || is_id_like(t) || is_issue_ref(t))
        .count();
    let units = (text.len() / LINT_WINDOW).max(1) as f64;
    if tokens as f64 / units < LINT_TOKENS {
        return None;
    }
    Some(format!(
        "this entry reads like an incident log ({tokens} date/id-like tokens in {} chars) — lessons, not logs: state the generalizable rule, keep one clause of why",
        text.len()
    ))
}

/// ISO-ish dates and timestamps: `2026-09-28`, `2026-09-28T10:00:00Z`,
/// `09/28/2026`. Bare times (`10:00`) stay quiet — 2–4 digits is not a date.
fn is_date_like(tok: &str) -> bool {
    let t = tok.trim_matches(|c: char| !c.is_ascii_alphanumeric());
    let digits = t.chars().filter(|c| c.is_ascii_digit()).count();
    let seps = t
        .chars()
        .filter(|c| *c == '-' || *c == '/' || *c == ':')
        .count();
    let has_year = t.len() >= 4 && t.chars().take(4).all(|c| c.is_ascii_digit());
    digits >= 6 && seps >= 1 && t.len() <= 20 && (seps >= 2 || has_year)
}

/// Hex-ish id: ≥8 hex chars INCLUDING at least one digit (so normal hex
/// words like `deadbeef`/`cafe` don't trip it), bounded length.
fn is_id_like(tok: &str) -> bool {
    let t = tok.trim_matches(|c: char| !c.is_ascii_alphanumeric());
    t.len() >= 8
        && t.len() <= LINT_ID_MAX
        && t.chars().all(|c| c.is_ascii_hexdigit())
        && t.chars().any(|c| c.is_ascii_digit())
}

## Assistant

bash -lc sed -n '1,240p' /tmp/review/whisper-main/src/distill.rs; printf '\n===== WHISPER QUICKSTART FULL =====\n'; sed -n '1,180p' /tmp/review/whisper-main/docs/src/getting-started.md; printf '\n===== WHISPER SUMMARY =====\n'; sed -n '1,150p' /tmp/review/whisper-main/docs/src/index.md; printf '\n===== BAJAN QUERY SEARCH RESULT STRUCT =====\n'; sed -n '90,230p' /tmp/review/bajan-main/src/query.rs; printf '\n===== BAJAN QUERY SEARCH =====\n'; sed -n '231,410p' /tmp/review/bajan-main/src/query.rs

## Tool

//! The distill contract: turu owns the mechanics (snapshot, revision,
//! conflict detection, install, audit); the calling agent owns the semantic
//! rewrite. Revisions are immutable and never pruned.

use serde::Serialize;
use serde_json::json;
use std::fs;

use crate::entry;
use crate::workspace::{self, Target};
use crate::{Result, WhisperError};

/// Snapshot + working paths for one revision.
#[derive(Debug, Serialize)]
pub struct Revision {
    pub id: String,
    pub snapshot_path: std::path::PathBuf,
    pub working_path: std::path::PathBuf,
    pub target_path: std::path::PathBuf,
    pub sha256: String,
    /// Per-entry usage stats (entry id → use_count/last_recalled) so the
    /// rewrite pass can prune dead entries. Omitted when the sidecar is
    /// absent (no telemetry yet).
    #[serde(skip_serializing_if = "Option::is_none")]
    pub recency: Option<std::collections::BTreeMap<String, crate::usage::Stats>>,
}

#[derive(Debug, Serialize)]
pub struct CommitReport {
    pub revision: String,
    pub replaced: std::path::PathBuf,
    pub snapshot_path: std::path::PathBuf,
    /// True when the revision was already committed with identical content.
    pub noop: bool,
}

/// `turu distill <scope> --begin`: snapshot the scope's current state into
/// an immutable revision dir and return the working paths.
pub fn begin(target: &Target, ts: &str) -> Result<Revision> {
    if !target.path.exists() {
        return Err(WhisperError::new(format!(
            "scope file does not exist: {}",
            target.path.display()
        ))
        .with_suggestion("turu init to create the layout (an empty file needs no distill)"));
    }
    let raw = std::fs::read_to_string(&target.path).map_err(WhisperError::from)?;
    let sha = entry::sha256_hex(&raw);
    let id = format!("{}-{}", ts.replace([':', '-'], ""), &sha[..8]);
    let rev_dir = revision_dir(target, &id)?;
    let snapshot_path = rev_dir.join("snapshot.md");
    let working_path = rev_dir.join("working.md");
    fs::write(&snapshot_path, &raw).map_err(WhisperError::from)?;
    write_revision_meta(&rev_dir, &id, target, &sha, &snapshot_path, &working_path)?;
    // Recency signal for the rewrite pass (empty map → omitted).
    let items = entry::parse_file(&raw);
    let recency = crate::usage::recency_for(&items, &target.path);
    let recency = (!recency.is_empty()).then_some(recency);
    Ok(Revision {
        id,
        snapshot_path,
        working_path,
        target_path: target.path.clone(),
        sha256: sha,
        recency,
    })
}

/// Create (or refuse to re-create) the immutable revision directory.
fn revision_dir(target: &Target, id: &str) -> Result<std::path::PathBuf> {
    let rev_dir = target.path.parent().unwrap().join("revisions").join(id);
    if rev_dir.exists() {
        return Err(
            WhisperError::new(format!("revision already exists: {}", rev_dir.display()))
                .with_suggestion(
                    "a distill cycle already began at this second — pass TURU_NOW or retry",
                ),
        );
    }
    fs::create_dir_all(&rev_dir).map_err(WhisperError::from)?;
    Ok(rev_dir)
}

/// Write meta.json: the agent rewrites `working.md`; commit verifies the
/// live file did not drift since this snapshot.
fn write_revision_meta(
    rev_dir: &std::path::Path,
    id: &str,
    target: &Target,
    sha: &str,
    snapshot_path: &std::path::Path,
    working_path: &std::path::Path,
) -> Result<()> {
    fs::write(
        rev_dir.join("meta.json"),
        json!({
            "revision": id,
            "target_path": target.path,
            "target_sha256": sha,
            "snapshot_path": snapshot_path,
            "working_path": working_path,
        })
        .to_string(),
    )
    .map_err(WhisperError::from)
}

fn load_meta(
    rev_dir: &std::path::Path,
) -> Result<(String, String, std::path::PathBuf, std::path::PathBuf)> {
    let raw = std::fs::read_to_string(rev_dir.join("meta.json")).map_err(|_| {
        WhisperError::new(format!(
            "missing revision metadata in {}",
            rev_dir.display()
        ))
        .with_suggestion("re-run `turu distill <scope> --begin`")
    })?;
    let meta: serde_json::Value = serde_json::from_str(&raw)
        .map_err(|e| WhisperError::new(format!("corrupt revision metadata: {e}")))?;
    Ok((
        meta["revision"].as_str().unwrap_or_default().to_string(),
        meta["target_sha256"]
            .as_str()
            .unwrap_or_default()
            .to_string(),
        meta["working_path"]
            .as_str()
            .map(std::path::PathBuf::from)
            .unwrap_or_default(),
        meta["snapshot_path"]
            .as_str()
            .map(std::path::PathBuf::from)
            .unwrap_or_default(),
    ))
}

/// `turu distill <scope> --commit --revision <id>`: install the distilled
/// output only if the live files are unchanged since `--begin`.
pub fn commit(target: &Target, revision: &str) -> Result<CommitReport> {
    let rev_dir = revision_dir_for_commit(target, revision)?;
    let (id, begin_sha, working_path, snapshot_path) = load_meta(&rev_dir)?;
    let committed_marker = rev_dir.join(".committed");
    let live = fs::read_to_string(&target.path).map_err(WhisperError::from)?;

    if let Some(report) = replay_report(
        &committed_marker,
        &live,
        target,
        id.clone(),
        snapshot_path.clone(),
    )? {
        return Ok(report);
    }
    check_drift(&live, &begin_sha)?;
    install(target, &working_path, &committed_marker)?;

    Ok(CommitReport {
        revision: id,
        replaced: target.path.clone(),
        snapshot_path,
        noop: false,
    })
}

/// Resolve + validate the revision directory for a commit.
fn revision_dir_for_commit(target: &Target, revision: &str) -> Result<std::path::PathBuf> {
    if !valid_revision_id(revision) {
        return Err(WhisperError::new(format!(
            "invalid revision id: {revision}"
        ))
        .with_suggestion(
            "revision ids look like 20260105T000000Z-1a2b3c4d — take them from the --begin envelope",
        ));
    }
    let rev_dir = target
        .path
        .parent()
        .unwrap()
        .join("revisions")
        .join(revision);
    if !rev_dir.exists() {
        return Err(
            WhisperError::new(format!("unknown revision: {revision}")).with_suggestion(
                "turu distill <scope> --begin first; revision ids are listed in its envelope",
            ),
        );
    }
    Ok(rev_dir)
}

/// Replay: a committed revision with an undrifted target is a no-op; a
/// committed revision with drift is refused (immutability).
#[allow(clippy::type_complexity)]
fn replay_report(
    committed_marker: &std::path::Path,
    live: &str,
    target: &Target,
    id: String,
    snapshot_path: std::path::PathBuf,
) -> Result<Option<CommitReport>> {
    if !committed_marker.exists() {
        return Ok(None);
    }
    let committed_sha = fs::read_to_string(committed_marker)
        .map_err(WhisperError::from)?
        .trim()
        .to_string();
    if entry::sha256_hex(live) == committed_sha {
        return Ok(Some(CommitReport {
            revision: id,
            replaced: target.path.clone(),
            snapshot_path,
            noop: true,
        }));
    }
    Err(
        WhisperError::new("revision is already committed and the target drifted since")
            .with_suggestion("run a new `turu distill <scope> --begin` cycle"),
    )
}

/// Conflict detection: live file must be byte-identical to --begin.
fn check_drift(live: &str, begin_sha: &str) -> Result<()> {
    let live_sha = entry::sha256_hex(live);
    if live_sha != begin_sha {
        return Err(WhisperError::new(format!(
            "scope file changed since --begin (concurrent write?) — expected sha {}, live {}",
            &begin_sha[..12],
            &live_sha[..12]
        ))
        .with_suggestion("re-run `turu distill <scope> --begin` and redo the rewrite"));
    }
    Ok(())
}

/// Install the distilled working file: mark it committed, then atomically
/// rename it over the live scope file (same f
...[truncated]...
/ claim's persisted episodes, freshest (largest) data cutoff, and the
/// staleness flag against `STALENESS_WINDOW_DAYS`. A claim with no
/// persisted backing never reaches this function (lineage-invisible).
fn ranking_metadata(
    supported_episodes: &[&crate::ingest::EpisodeRecord],
    now_days: i64,
    staleness_window_days: i64,
) -> (u8, Option<i64>, bool) {
    let authority_tier = supported_episodes
        .iter()
        .map(|ep| ep.source.authority_tier)
        .min()
        .unwrap_or(u8::MAX);
    let cutoff_days = supported_episodes
        .iter()
        .filter_map(|ep| ep.source.data_cutoff.as_deref().and_then(days_from_iso))
        .max();
    let stale = cutoff_days.is_some_and(|d| d < now_days - staleness_window_days);
    (authority_tier, cutoff_days, stale)
}

/// Search the persisted claim graph: every claim whose text contains
/// `pattern` (case-insensitive) **and** whose lineage resolves, at query
/// time, to at least one persisted episode (`qt_lineage_traceable` —
/// lineage-broken claims are invisible). Unscoped — see [`search_scoped`]
/// for the scoped form.

===== BAJAN QUERY SEARCH =====
pub fn search(
    db: &SqliteStore,
    pattern: &str,
    budget: usize,
) -> Result<SearchResult, BajanQueryError> {
    search_inner(db, pattern, budget, None, STALENESS_WINDOW_DAYS)
}

/// Window-configured search (bajan-bku): the staleness demotion window
/// comes from bajan.toml (`staleness_window_days`) instead of the
/// built-in default. `scope` follows qt_scope_filtering (`None` =
/// unfiltered). Everything else — budget walk, honest stopping,
/// ranking order — is identical to [`search`].
pub fn search_with_window(
    db: &SqliteStore,
    pattern: &str,
    budget: usize,
    staleness_window_days: i64,
    scope: Option<&[String]>,
) -> Result<SearchResult, BajanQueryError> {
    search_inner(db, pattern, budget, scope, staleness_window_days)
}

/// Scoped search (`qt_scope_filtering`, WR-SCOPE.1): restrict the answer
/// to claims whose **resolved tag projection** — the union of the
/// supporting episodes' tag sets via the lineage walk
/// (`ex_tag_inheritance`; tags are never stored on the claim) —
/// intersects the requested scope set. Out-of-scope claims are excluded
/// from the hits — never silently blended in. The predicate is pure set
/// intersection: an empty `scope` intersects no projection, so a scoped
/// answer under an empty scope is honestly empty; the unfiltered read is
/// the separate [`search`] entry point. The budget walk and
/// honest stopping are unchanged: out-of-scope claims are walked (they
/// consume budget like any non-matching claim) but never surface as
/// hits. The requested scope is echoed on the result (`qt_query-schema`
/// scope field). Reads never write (`qt_readonly`).
pub fn search_scoped(
    db: &SqliteStore,
    pattern: &str,
    budget: usize,
    scope: &[String],
) -> Result<SearchResult, BajanQueryError> {
    search_inner(db, pattern, budget, Some(scope), STALENESS_WINDOW_DAYS)
}

/// The shared traversal behind both entry points: `None` scope is the
/// unfiltered read; `Some(scope)` applies `qt_scope_filtering`.
fn search_inner(
    db: &SqliteStore,
    pattern: &str,
    budget: usize,
    scope: Option<&[String]>,
    staleness_window_days: i64,
) -> Result<SearchResult, BajanQueryError> {
    let episodes: Vec<crate::ingest::EpisodeRecord> =
        db.episodes().map_err(|e| BajanQueryError(e.to_string()))?;
    let persisted: Vec<String> = {
        let mut ids: Vec<String> = episodes.iter().map(|e| e.id.clone()).collect();
        ids.sort();
        ids
    };
    let needle = pattern.to_lowercase();
    let now_days = today_days_utc();
    let mut hits = Vec::new();
    let mut truncated = false;

    for (walked, (claim_key, node, lineage)) in db
        .claims_with_lineage()
        .map_err(|e| BajanQueryError(e.to_string()))?
        .into_iter()
        .enumerate()
    {
        if walked >= budget {
            truncated = true;
            break;
        }
        // qt_lineage_traceable: at least one lineage edge must resolve to
        // a persisted episode at query time.
        let supported: Vec<&crate::ingest::EpisodeRecord> = lineage
            .iter()
            .filter(|edge| persisted.binary_search(&edge.episode_id).is_ok())
            .filter_map(|edge| episodes.iter().find(|e| e.id == edge.episode_id))
            .collect();
        if supported.is_empty() {
            continue;
        }
        if node.text.to_lowercase().contains(&needle) {
            // qt_scope_filtering: the resolved tag projection is the
            // union of the supporting episodes' tags; the scope
            // predicate is pure intersection (a scoped read under an
            // empty scope intersects nothing). `None` = unfiltered.
            let in_scope = match scope {
                None => true,
                Some(scope) => supported
                    .iter()
                    .any(|ep| ep.source.tags.iter().any(|tag| scope.contains(tag))),
            };
            if !in_scope {
                continue;
            }
            let (authority_tier, cutoff_days, stale) =
                ranking_metadata(&supported, now_days, staleness_window_days);
            // Surface the freshest well-formed cutoff verbatim; a
            // well-formed-but-absent set stays absent.
            let data_cutoff = cutoff_days.map(iso_from_days).or_else(|| {
                supported
                    .iter()
                    .filter(|ep| ep.source.data_cutoff.is_some())
                    .for_each(|_| {});
                supported
                    .iter()
                    .find_map(|ep| ep.source.data_cutoff.clone())
            });
            let episodes: Vec<String> = supported.iter().map(|ep| ep.id.clone()).collect();
            hits.push(Hit {
                claim_key,
                text: node.text.clone(),
                status: node.status,
                scope: node.scope.clone(),
                source_type: node.source_type.clone(),
                data_cutoff,
                episodes,
                authority_tier,
                cutoff_days,
                stale,
            });
        }
    }

    // qt_ranking (WR-RANK.2): the ranking key is (authority rank if not
    // stale else demoted, recency) — a stale hit demotes below every
    // fresh hit regardless of tier; among stale hits authority still
    // orders. Then freshest cutoff (absent least fresh), claim key on
    // ties — a total, deterministic order.
    hits.sort_by(|a, b| {
        a.stale
            .cmp(&b.stale)
            .then(a.authority_tier.cmp(&b.authority_tier))
            .then(b.cutoff_days.cmp(&a.cutoff_days))
            .then(a.claim_key.cmp(&b.claim_key))
    });

    // WR-TIME.3: the best-scoring hit carries the staleness warning when
    // its cutoff is stale.
    let staleness_warning = hits
        .first()
        .filter(|hit| hit.stale)
        .map(|hit| StalenessWarning {
            claim_key: hit.claim_key,
            data_cutoff: hit.data_cutoff.clone().unwrap_or_default(),
        });

    let status = if truncated {
        BudgetStatus::BudgetExhausted
    } else {
        BudgetStatus::Complete
    };
    // Coverage surfacing (bajan-913): corpus metadata, independent of
    // the walk — a note is present exactly when the corpus has gaps.
    let coverage = coverage_note(db)?;
    Ok(SearchResult {
        status,
        scope: scope.unwrap_or(&[]).to_vec(),
        hits,
        staleness_warning,
        coverage,
    })
}

/// Query-surface error: the search itself is deterministic, so the only
/// failure is a broken store. Kept as a distinct type so the read path
/// cannot be confused with write-path errors.
#[derive(Debug, thiserror::Error)]
#[error("query failed: {0}")]
pub struct BajanQueryError(pub String);

/// One side of a contradiction pair (`qt_contradiction_query`): the
/// claim, its stored status verbatim, and the persisted episodes its
/// lineage resolves to (`qt_lineage_traceable`).
#[derive(Debug, Clone, PartialEq, Eq, Serialize)]

## Assistant

bash -lc sed -n '160,225p' /tmp/review/bajan-main/src/llm.rs; sed -n '330,620p' /tmp/review/bajan-main/src/llm.rs; sed -n '740,980p' /tmp/review/bajan-main/src/extract.rs; sed -n '1,180p' /tmp/review/bajan-main/src/review.rs; sed -n '1,170p' /tmp/review/bajan-main/src/resolve.rs; sed -n '1,200p' /tmp/review/bajan-main/src/cli.rs

## Tool

}

/// The published candidate-claim output schema (`ex_output_schema`):
/// strict — unknown fields are refused so schema drift is caught, not
/// silently tolerated; `text` and `evidence` are required, temporal
/// bounds are optional and must be null when the document states none.
#[derive(Debug, Clone, PartialEq, Eq, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct LlmOutput {
    pub claims: Vec<LlmClaim>,
}

#[derive(Debug, Clone, PartialEq, Eq, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct LlmClaim {
    /// Atomic, self-contained claim text.
    pub text: String,
    /// Verbatim substring of the episode text supporting the claim.
    pub evidence: String,
    /// Civil date (YYYY-MM-DD) when the document states one, else null.
    #[serde(default)]
    pub valid_at: Option<String>,
    #[serde(default)]
    pub invalid_at: Option<String>,
}

/// System prompt: extraction instructions only — no normalization, dedup,
/// or scoring work is asked of the model (`ex_no_llm_post` keeps the
/// post-pass deterministic in code, not in the prompt).
pub const LLM_SYSTEM_PROMPT: &str = "\
You extract atomic, self-contained claims from a source document. \
Return ONLY a JSON object with exactly this shape and no other text: \
{\"claims\":[{\"text\":\"...\",\"evidence\":\"...\",\"valid_at\":null,\"invalid_at\":null}]}. \
Each claim's text must be a single atomic claim in the document's language. \
The evidence must be an exact verbatim substring of the document supporting the claim. \
Set valid_at or invalid_at to a YYYY-MM-DD date only when the document states one; \
otherwise null. Never invent dates, evidence, or claims not supported by the document.";

/// Build the single user prompt from the chunk assembly (CORR-001: one
/// multi-part prompt, one call). Pure function of the chunks.
pub fn build_user_prompt(chunks: &[String]) -> String {
    let mut prompt = String::from("Extract claims from the following source document.\n\n");
    if chunks.len() == 1 {
        prompt.push_str(&chunks[0]);
        return prompt;
    }
    for (i, chunk) in chunks.iter().enumerate() {
        prompt.push_str(&format!("[chunk {}/{}]\n", i + 1, chunks.len()));
        prompt.push_str(chunk);
        prompt.push('\n');
    }
    prompt
}

/// Transport seam: one OpenAI-compatible chat-completions POST. Ok
/// carries the raw response body; Err is a retryable infrastructure
/// failure. Injectable so tests run fully scripted.
pub trait LlmTransport: std::fmt::Debug + Send + Sync {
    fn post(&self, base_url: &str, api_key: &str, body_json: &str) -> Result<String, String>;
}

/// The real transport: blocking HTTP via ureq (rustls), global timeout.
#[derive(Debug)]
pub struct UreqTransport {
    agent: ureq::Agent,
}
/// The real LLM claim extractor (bajan-vg6 default llm): proposes
/// candidate claims via ONE chat-completions call per episode per pass
/// (`ex_single_call`), retrying with backoff inside the call and
/// surfacing `Exhausted` after the retry budget — the pipeline parks the
/// episode. Deterministic inputs: the prompt is a pure function of the
/// episode text and configuration; the API key is read at call time from
/// the configured env-var NAME (never stored, never logged).
pub struct LlmExtractor {
    version: String,
    model_id: String,
    base_url: String,
    api_key_env: String,
    context_tokens: usize,
    max_attempts: u32,
    /// Spend cap in micro-USD (bajan-8cc). 0 = unbounded — only the
    /// direct constructor path (tests, custom plumbing); the config
    /// selection REQUIRES a cap for llm.
    spend_cap_micros: u64,
    /// Accumulated KNOWN spend this extractor instance (one pass),
    /// micro-USD. Calls whose response lacks `usage.cost` are counted in
    /// `unaccounted_calls` instead and fail the next call closed.
    spent_micros: Cell<u64>,
    /// Calls this instance made whose cost could not be accounted.
    unaccounted_calls: Cell<u32>,
    sleep: Box<dyn Fn(Duration) + Send + Sync>,
    transport: Box<dyn LlmTransport>,
    /// Per-call cost log (bajan-3w4): one line per successful call,
    /// emitted as soon as the cost is known — a burn-in's direct spend
    /// measurement. Default sink is stderr; injected in tests.
    call_log: Box<dyn Fn(String) + Send + Sync>,
    /// Global timeout for the built-in ureq transport (bajan-noj).
    /// Default 120s (the burn-in-verified default); overridden via
    /// BAJAN_EXTRACTOR_TIMEOUT_SECS at selection. A custom transport
    /// (with_transport) owns its own timeout policy.
    transport_timeout: Duration,
    key_lookup: KeyLookup,
}

impl std::fmt::Debug for LlmExtractor {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        // The API key never appears here: only the env-var NAME is held.
        f.debug_struct("LlmExtractor")
            .field("version", &self.version)
            .field("model_id", &self.model_id)
            .field("base_url", &self.base_url)
            .field("api_key_env", &self.api_key_env)
            .field("context_tokens", &self.context_tokens)
            .field("max_attempts", &self.max_attempts)
            .finish_non_exhaustive()
    }
}

impl LlmExtractor {
    /// Build with the real transport, real sleeps, and the process
    /// environment as the key source — override via the `with_*` builders
    /// in tests (scripted transport, no-op sleep, injected lookup).
    pub fn new(
        model_id: impl Into<String>,
        base_url: impl Into<String>,
        api_key_env: impl Into<String>,
        context_tokens: usize,
        max_attempts: u32,
    ) -> Self {
        let model_id = model_id.into();
        let transport_timeout = Duration::from_secs(120);
        Self {
            version: llm_version(&model_id),
            model_id,
            base_url: base_url.into(),
            api_key_env: api_key_env.into(),
            context_tokens,
            max_attempts,
            spend_cap_micros: 0,
            spent_micros: Cell::new(0),
            unaccounted_calls: Cell::new(0),
            sleep: Box::new(std::thread::sleep),
            transport: Box::new(UreqTransport::with_timeout(transport_timeout)),
            call_log: Box::new(|line| eprintln!("{line}")),
            transport_timeout,
            key_lookup: Box::new(|key| std::env::var(key).ok()),
        }
    }

    /// Set the built-in transport's global HTTP timeout in seconds
    /// (bajan-noj): carries BAJAN_EXTRACTOR_TIMEOUT_SECS from
    /// `ExtractorConfig::select`. Rebuilds the built-in ureq transport;
    /// a custom transport installed via with_transport owns its own
    /// timeout policy and should not be combined with this builder.
    pub fn with_timeout_secs(mut self, secs: u64) -> Self {
        self.transport_timeout = Duration::from_secs(secs);
        self.transport = Box::new(UreqTransport::with_timeout(self.transport_timeout));
        self
    }

    /// The transport timeout actually in force (bajan-noj).
    pub fn transport_timeout(&self) -> Duration {
        self.transport_timeout
    }

    /// Replace the transport (scripted fake in tests, custom endpoint
    /// plumbing elsewhere).
    pub fn with_transport(mut self, transport: impl LlmTransport + 'static) -> Self {
        self.transport = Box::new(transport);
        self
    }

    /// Set the spend cap in micro-USD (bajan-8cc): the pre-call gate
    /// refuses further calls once accumulated known spend has reached it,
    /// and any unaccounted call (response without `usage.cost`) fails the
    /// next call closed — a cap that cannot see spend must not keep
    /// spending.
    pub fn with_spend_cap_micros(mut self, micros: u64) -> Self {
        self.spend_cap_micros = micros;
        self
    }

    /// Replace the per-call cost log (captured in tests; default is
    /// stderr): one line per successful call carrying episode id,
    /// attempt number, the response's exact `usage.cost`, and the
    /// running spend against the cap (bajan-3w4).
    pub fn with_call_log(mut self, log: Box<dyn Fn(String) + Send + Sync>) -> Self {
        self.call_log = log;
        self
    }
...[truncated]...
eck `ok` first); Invariant 3.2.5 forbids emitting an error
//! without non-empty remediation, so every error path carries a fix hint.

use clap::{Parser, Subcommand};
use genesis::envelope::{Envelope, EnvelopeKind, ErrorResult, RemediationEntry};
use serde::Serialize;

use crate::contradict;
use crate::extract;
use crate::ingest;
use crate::query;
use crate::resolve;
use crate::review;
use crate::store::StoreError;

/// Top-level CLI: `bajan [--json] <subcommand>`.
#[derive(Debug, Parser)]
#[command(
    name = "bajan",
    version,
    about = "Spec-driven knowledge-graph pipeline CLI"
)]
pub struct Cli {
    /// Emit the machine-readable suite envelope instead of a text rendering.
    #[arg(long, global = true)]
    pub json: bool,

    /// Embedded SQLite database path (gm_embedded_store: one file, plain
    /// rows). Defaults to `bajan.db` in the working directory.
    #[arg(long, global = true, default_value = "bajan.db")]
    pub db: String,

    #[command(subcommand)]
    pub command: Command,
}

#[derive(Debug, Subcommand)]
pub enum Command {
    /// Print tool identity as a suite envelope.
    Version,
    /// Persist a normalized episode stream verbatim (the stream is read
    /// from stdin as a JSON array of episode records).
    Ingest,
    /// Propose candidate claims from persisted episodes (deterministic
    /// single-call pass over pending episodes).
    Extract,
    /// Resolve claim identity across versions (bajan-7q8): report every
    /// persisted claim's lineage, status, supersession tombstones, and
    /// staged invalidation proposals — or, with `--restage`, perform the
    /// explicit human-only re-stage of one superseded claim back to
    /// `staged` (`ex_supersession`: the only path back, never automated).
    Resolve {
        /// Re-stage this superseded claim (explicit human action).
        #[arg(long)]
        restage: Option<usize>,
        /// Operator identity for --restage; defaults to $USER.
        #[arg(long)]
        actor: Option<String>,
    },
    /// Search the persisted claim graph (first read command).
    Query {
        /// Text to search for (case-insensitive substring match).
        pattern: String,
        /// Bounded-traversal budget: maximum walked claim nodes
        /// (falls back to bajan.toml default_budget, then 256).
        #[arg(long)]
        budget: Option<usize>,
        /// Restrict the answer to claims whose resolved tag projection
        /// (union of supporting episodes' tags via lineage,
        /// qt_scope_filtering) intersects the given tags — repeat the
        /// flag or comma-separate. Omit for the unfiltered read.
        #[arg(long = "scope", value_delimiter = ',')]
        scope: Vec<String>,
    },
    /// Report contradict pairs and staged invalidation proposals over the
    /// given claims (graph structure only, never adjudicated).
    Contradict {
        /// Claim keys to run the contradiction traversal over (at least
        /// one — a no-op read must not report success).
        #[arg(num_args = 1.., required = true)]
        claims: Vec<usize>,
        /// Bounded-traversal budget: maximum walked edges
        /// (falls back to bajan.toml default_budget, then 256).
        #[arg(long)]
        budget: Option<usize>,
    },
    /// Human accept action: move staged claims to active (one audit record
    /// per claim).
    Adopt {
        /// Claim keys to accept (batch permitted, per-claim audited; at
        /// least one — a no-op accept must not report success).
        #[arg(num_args = 1.., required = true)]
        claims: Vec<usize>,
        /// Operator identity; defaults to $USER.
        #[arg(long)]
        actor: Option<String>,
    },
    /// Operator deletion surface (ic_deleted_tombstone): remove one
    /// claim-free persisted episode and record a deletion tombstone for
    /// its stable id — every later submission of the id, unchanged or
    /// mutated, is rejected with the machine-readable deleted-id reason
    /// until an explicit revive. Deletion is refused while any claim
    /// supports the episode (gm_lineage_survives).
    Delete {
        /// Stable id of the episode to delete.
        episode_id: String,
        /// Operator identity; defaults to $USER.
        #[arg(long)]
        actor: Option<String>,
    },
    /// Operator revive surface (ic_deleted_recreate): the only path that
    /// clears a deletion tombstone — revive alone changes nothing; the
    /// next submission of the id persists through the normal acceptance
    /// path exactly once.
    Revive {
        /// Stable id whose deletion tombstone to clear.
        episode_id: String,
        /// Operator identity; defaults to $USER.
        #[arg(long)]
        actor: Option<String>,
    },
    /// Deterministic entity-resolution pass (er_queue_entry): propose
    /// possible-duplicate merge candidates into the review queue from
    /// ranked claims — normalization equivalence/containment only, no LLM,
    /// no embedding. The queue drains, it never grows by human invention.
    Er {
        /// Bounded-candidate budget: maximum pair comparisons examined.
        #[arg(long)]
        budget: Option<usize>,
    },
    /// Deterministic contradiction-scan pass (gm_contradicts_provenance):
    /// the only in-pipeline producer of `contradicts` edges — closed edit
    /// classes over normalized texts (negation-marker present/absent, or a
    /// single differing numeral token), no fuzzy subject detection, no
    /// LLM. Every written edge carries the pass identity and rule as
    /// provenance; re-runs refuse duplicate edges honestly.
    Scan {
        /// Bounded-candidate budget: maximum pair comparisons examined.
        #[arg(long)]
        budget: Option<usize>,
    },
    /// The human-in-the-loop review surface (er_human_resolution): the
    /// only HITL commands in an otherwise AFK pipeline — inspect the open
    /// queue, or resolve one candidate with actor identity. Review
    /// commands never create candidates; they only resolve them.
    Review {
        #[command(subcommand)]
        action: ReviewAction,
    },
    /// LLM-assisted contradiction-proposal pass (cr_proposal_entry):
    /// proposes candidate contradicts pairs the closed rule set cannot
    /// see, staging them into the human-owned proposal queue — never
    /// writing edges. Config comes from the extractor env surface
    /// (BAJAN_EXTRACTOR_MODEL/_BASE_URL/_API_KEY_ENV).
    Propose {
        /// Bounded-candidate budget: maximum ranked claims walked.
        #[arg(long)]
        budget: Option<usize>,
    },
    /// The contradiction-proposal HITL surface (cr_human_resolution):
    /// inspect the open LLM-proposal queue, or resolve one proposal with
    /// actor identity — approve writes the contradicts edge with
    /// `llm:<model_id>` producer provenance, reject drops the proposal.
    Proposal {
        #[command(subcommand)]
        action: ProposalAction,
    },
    /// Score a model extraction run against a golden corpus
    /// (eval.claims, bajan-2k4): deterministic precision/recall with raw
    /// counts, per-case judgments in the closed reason vocabulary,
    /// hedge-fidelity as a first-class number, and missing metrics
    /// reported as explicit unknowns — never invented. Read-only: the
    /// harness never opens a store (ev_readonly).
    Eval {
        #[command(subcommand)]
        action: EvalAction,
    },
}

/// Review actions (`er_human_resolution`): list is a read; approve and
/// reject are human-only resolutions carrying actor identity.
#[derive(Debug, Subcommand)]
pub enum ReviewAction {
    /// Every open candidate with evidence, episode counts, and queue age
    /// (er_queue_transparency), oldest-first.
    List,
    /// Approve (merge): both sides' lineage survives onto the merged
    /// entity (er_merge_preserves); one audit record is written.
    Approve {
        /// One side of the candidate pair (as listed by `review list`).
        from: usize,
        /// The other side of the candidate pair.
        to: usize,
        /// Operator identity; defaults to $USER.
        #[arg(long)]

## Assistant

bash -lc sed -n '1,220p' /tmp/review/bajan-main/src/review.rs; printf '\n===== STORE PUBLIC METHODS =====\n'; rg -n '^    pub fn ' /tmp/review/bajan-main/src/store/sqlite.rs; printf '\n===== STORE CLAIM / EDGE METHODS =====\n'; rg -n -C 3 'insert_claim|insert_episode|claims_with_lineage|insert_edge|possible_duplicate|merge|entity|review' /tmp/review/bajan-main/src/store/sqlite.rs | head -260; printf '\n===== Bajan README KNOWN LIMITATIONS =====\n'; sed -n '230,285p' /tmp/review/bajan-main/README.md;

## Tool

//! Purpose: the deterministic entity-resolution pass feeding the HITL
//! review queue (bajan-6j1) — the only producer of merge candidates.
//! Responsibilities: ranked-candidate walk over the persisted claim graph,
//! normalization-based duplicate detection (whitespace-collapse +
//! case-fold equality or containment — deterministic scoring, no LLM, no
//! embedding), and honest enqueue reporting through the store's
//! `enqueue_candidate` guards.
//! Rationale: governed by specs/entity-review.md — `er_queue_entry` makes
//! this pass the only writer of candidate pairs (the queue drains, it
//! never grows by human invention); `gm_deterministic_er` keeps ER
//! deterministic (normalization plus curated alias lists). The walk is
//! budget-bounded with honest exhaustion, mirroring the `qt_bounded_traversal`
//! discipline of the read queries.

use crate::query::{self, BajanQueryError};
use crate::store::sqlite::SqliteStore;

pub use crate::store::EnqueueOutcome;

/// Whitespace-collapsed, case-folded form of a claim text — the
/// deterministic normalization duplicate detection operates on (the same
/// normalization family as `ex_evidence_containment`'s `collapse`).
pub fn normalize(text: &str) -> String {
    text.split_whitespace()
        .collect::<Vec<_>>()
        .join(" ")
        .to_lowercase()
}

/// Report of one deterministic ER pass over the persisted claim graph:
/// the honest traversal status, the pairs proposed into the review queue,
/// and the count of candidate pairs refused by the store's queue guards
/// (already open / rejected without new evidence).
#[derive(Debug, Clone, PartialEq, Eq, serde::Serialize)]
pub struct ErReport {
    /// Typed traversal outcome (`qt_bounded_traversal` discipline).
    pub status: query::BudgetStatus,
    /// Candidate pairs proposed (edge + queue row written).
    pub proposed: usize,
    /// Candidate pairs the store refused (already open, or rejected
    /// without new evidence) — refused honestly, never silently.
    pub refused: usize,
    /// The proposed pairs, as (from_claim, to_claim), in proposal order.
    pub pairs: Vec<(usize, usize)>,
}

/// Run the deterministic ER pass over ranked candidates
/// (`er_queue_entry`): every pair of ranked hits whose normalized texts
/// are content-equivalent (equal) or containment-related proposes a
/// `possible_duplicate_of` edge into the review queue. The walk is
/// budget-bounded — the budget bounds CANDIDATE comparisons (bajan-9pm):
/// pairs excluded by the sound pre-filters below are proven non-matches,
/// never examining them loses no information, so honest exhaustion means
/// "candidates remained unseen", not "all raw pairs visited".
///
/// Candidate pre-filters (both sound — they never exclude a true match):
///
/// 1. Normalization-equal pairs come from exact grouping on the
///    normalized text (computed once per hit, O(n)) — every pair inside
///    a group matches by construction.
/// 2. Containment candidates: for a hit `s`, a container `L` must
///    contain every character run of `s`, in particular every 4-gram of
///    `s`. The candidates for `s` are therefore the posting of `s`'s
///    rarest 4-gram (smallest posting; ties broken lexicographically),
///    filtered to strictly longer texts (equal-length containment
///    implies equality, already covered). For texts too short to have a
///    4-gram the filter falls back to all strictly longer hits.
///
/// `from`/`to` orientation: the contained (strictly shorter) text is the
/// suspected duplicate; on exact equality the lower claim key is `from`.
/// Evidence fingerprints order texts by ranked hit position — identical
/// to the pre-9pm walk, so a rejected pair's repropose guard compares
/// like for like across the change.
pub fn run_er_pass(db: &SqliteStore, budget: usize, now: u64) -> Result<ErReport, BajanQueryError> {
    // Ranked candidates (`qt_ranking`): the pass walks hits in ranked
    // order — an empty pattern matches every lineage-resolved claim.
    let result = query::search(db, "", budget)?;
    let hits = result.hits;
    // Normalization computed ONCE per hit (bajan-9pm): the old walk
    // re-normalized both sides inside the inner loop — quadratic recompute
    // on top of the quadratic pair walk.
    let norms: Vec<String> = hits.iter().map(|h| normalize(&h.text)).collect();

    let mut proposed = Vec::new();
    let mut refused = 0usize;
    let mut examined = 0usize;
    let mut exhausted = false;

    // One enqueue for a candidate pair {i, j} (i < j in ranked order):
    // orientation and fingerprint exactly as the pre-9pm walk computed
    // them, so queue order and repropose fingerprints are unchanged.
    let enqueue_pair = |i: usize,
                        j: usize,
                        from: usize,
                        to: usize,
                        evidence: &str,
                        proposed: &mut Vec<(usize, usize)>,
                        refused: &mut usize|
     -> Result<(), BajanQueryError> {
        let mut episodes: Vec<String> = hits[i].episodes.clone();
        episodes.extend(hits[j].episodes.clone());
        episodes.sort();
        episodes.dedup();
        let fingerprint = serde_json::json!({
            "texts": [hits[i].text, hits[j].text],
            "episodes": episodes,
        })
        .to_string();
        match db
            .enqueue_candidate(from, to, evidence, &fingerprint, now)
            .map_err(|e| BajanQueryError(e.to_string()))?
        {
            crate::store::EnqueueOutcome::Queued => proposed.push((from, to)),
            _ => *refused += 1,
        }
        Ok(())
    };

    // --- equality candidates: exact groups on the normalized text ---
    // Groups ordered by first member (ranked order); pairs within a
    // group by ranked position — the same order the old walk emitted
    // equal pairs in.
    let groups: Vec<(usize, Vec<usize>)> = {
        let mut by_text: std::collections::HashMap<&str, Vec<usize>> =
            std::collections::HashMap::new();
        for (idx, norm) in norms.iter().enumerate() {
            by_text.entry(norm.as_str()).or_default().push(idx);
        }
        let mut groups: Vec<(usize, Vec<usize>)> = by_text
            .into_values()
            .filter(|g| g.len() > 1)
            .map(|g| (*g.first().expect("non-empty"), g))
            .collect();
        groups.sort_by_key(|(first, _)| *first);
        groups
    };
    'equality: for (_, members) in &groups {
        for a in 0..members.len() {
            for b in (a + 1)..members.len() {
                if examined >= budget {
                    exhausted = true;
                    break 'equality;
                }
                examined += 1;
                let (i, j) = (members[a], members[b]);
                let (from, to) = if hits[i].claim_key <= hits[j].claim_key {
                    (hits[i].claim_key, hits[j].claim_key)
                } else {
                    (hits[j].claim_key, hits[i].claim_key)
                };
                enqueue_pair(
                    i,
                    j,
                    from,
                    to,
                    "normalization-equal",
                    &mut proposed,
                    &mut refused,
                )?;
            }
        }
    }

    // --- containment candidates: rarest-4-gram postings ---
    // Postings: 4-gram (within normalized tokens) -> ranked hit indices,
    // sorted. Soundness: if norm_s is a substring of norm_L, every
    // within-token 4-gram of s is a substring of L (a space-free gram
    // contained in L can never span L's token boundaries), so L is in
    // EVERY posting of s's grams — in particular the rarest one.
    let mut postings: std::collections::HashMap<String, Vec<u32>> =
        std::collections::HashMap::new();
    let mut grams_of: Vec<Vec<String>> = Vec::with_capacity(norms.len());
    for norm in &norms {
        // Distinct within-token 4-grams of the normalized text (chars,
        // not bytes — gram slices must not split UTF-8 code points).
        let mut seen: std::collections::HashSet<String>
...[truncated]...
lineage(&self) -> Result<Vec<(usize, ClaimNode, Vec<Lineage>)>, StoreError> {
802-        let mut stmt = self
803-            .conn
804-            .prepare(
--
924-    /// lineage plus the extraction-cache markers.
925-    pub fn dump_extraction_output(&self) -> Result<ExtractionDump, StoreError> {
926-        let claims = self
927:            .claims_with_lineage()?
928-            .into_iter()
929-            .map(|(claim_key, node, lineage)| DumpedClaim {
930-                claim_key,
--
936-        let edges = self.edges_with_provenance()?;
937-        let invalidations = self.invalidations()?;
938-        let supersessions = self.supersessions()?;
939:        let reviews = self.reviews()?;
940:        let review_audits = self.review_audits()?;
941-        let contradiction_proposals = self.contradiction_proposals()?;
942-        let contradiction_audits = self.contradiction_audits()?;
943-        let er_aliases = self.er_aliases()?;
--
956-                .collect(),
957-            invalidations,
958-            supersessions,
959:            reviews,
960:            review_audits,
961-            er_aliases,
962-            contradiction_proposals,
963-            contradiction_audits,
--
1003-        };
1004-        let mut pairs: Vec<(ClaimNode, Lineage)> = Vec::new();
1005-        if let Some(selected) = &selected {
1006:            for (_claim_key, node, lineages) in self.claims_with_lineage()? {
1007-                if !matches!(node.status, ClaimStatus::Staged | ClaimStatus::Active) {
1008-                    continue;
1009-                }
--
1091-        for record in &dump.supersessions {
1092-            self.insert_supersession_row(record.claim_key, &record.reason, record.superseded_at)?;
1093-        }
1094:        for record in &dump.reviews {
1095:            self.insert_review_row(record)?;
1096-        }
1097:        for record in &dump.review_audits {
1098:            self.insert_review_audit_row(record)?;
1099-        }
1100-        for record in &dump.contradiction_proposals {
1101-            self.insert_contradiction_proposal_row(record)?;
--
1141-    /// (`InvalidAliasPair`); a duplicate entry is an idempotent skip —
1142-    /// returns true when a row was inserted.
1143-    pub fn insert_er_alias(&self, a: &str, b: &str) -> Result<bool, StoreError> {
1144:        let (na, nb) = (crate::review::normalize(a), crate::review::normalize(b));
1145-        if na.is_empty() || nb.is_empty() || na == nb {
1146-            return Err(StoreError::InvalidAliasPair { spec: SPEC });
1147-        }
--
1191-    /// claims. Edges are a set relation: an identical (from, label, to)
1192-    /// triple is refused (`DuplicateEdge`) — a doubled contradicts edge
1193-    /// would double the reported pairs, a doubled
1194:    /// possible_duplicate_of entry would double er_queue rows (bajan-2hp).
1195-    /// Row order is preserved for dump-recreate.
1196:    pub fn insert_edge(
1197-        &self,
1198-        from_claim: usize,
1199-        label: EdgeLabel,
1200-        to_claim: usize,
1201-    ) -> Result<(), StoreError> {
1202:        self.insert_edge_provenanced(from_claim, label, to_claim, None)
1203-    }
1204-
1205-    /// Persist a typed claim-relation edge WITH producer provenance
1206-    /// (`gm_contradicts_provenance`): the contradiction-scan pass records
1207:    /// its pass identity and detection rule on every `contradicts` edge
1208:    /// it writes; the bare-triple `insert_edge` is the None-provenance
1209-    /// path. Same set-relation uniqueness and endpoint guards.
1210:    pub fn insert_edge_provenanced(
1211-        &self,
1212-        from_claim: usize,
1213-        label: EdgeLabel,
--
1227-            EdgeLabel::Contradicts => "contradicts",
1228-            EdgeLabel::Supports => "supports",
1229-            EdgeLabel::DerivedFrom => "derived_from",
1230:            EdgeLabel::PossibleDuplicateOf => "possible_duplicate_of",
1231-        };
1232-        // Uniqueness per relation (bajan-2hp): edges are a set relation —
1233-        // an identical (from, label, to) triple carries no new
--
1290-
1291-    /// Persisted typed edges WITH producer provenance, row order
1292-    /// preserved: `provenance` is `Some` only for edges written with a
1293:    /// pass identity + rule (`gm_contradicts_provenance`); legacy
1294-    /// bare-triple rows read back as `None` — absent is honest absent,
1295-    /// never a fabricated producer.
1296-    pub fn edges_with_provenance(&self) -> Result<Vec<EdgeWithProvenance>, StoreError> {
--
1419-        superseded_at: u64,
1420-    ) -> Result<Vec<usize>, StoreError> {
1421-        let mut superseded = Vec::new();
1422:        for (claim_key, node, lineage) in self.claims_with_lineage()? {
1423-            let on_episode = lineage.iter().any(|l| l.episode_id == episode_id);
1424-            if !on_episode
1425-                || lineage
--
1502-    /// it is `rejected` AND carries a supersession tombstone. Staged,
1503-    /// active, and gate-refused (tombstone-less rejected) claims are
1504-    /// refused; unknown keys are refused. One restage record per action
1505:    /// carries actor identity and timestamp.
1506-    pub fn restage(
1507-        &self,
1508-        claim_key: usize,
--
1569-        Ok(found.is_some())
1570-    }
1571-
1572:    // ---- entity review (specs/entity-review.md, bajan-6j1) ----
1573-
1574:    /// Queue a merge candidate for human review (`er_queue_entry`): the
1575-    /// only way a queue row is born is this call, and the only caller is
1576-    /// the deterministic ER pass — a candidate pair enters the queue only
1577:    /// as a `possible_duplicate_of` edge written by that pass. Refused
1578-    /// honestly (never silently) when the pair is already open
1579-    /// (`AlreadyProposed`) or a prior rejection covered identical evidence
1580-    /// (`er_repropose_guard`). Returns the outcome; row order preserved.
--
1609-            return Ok(EnqueueOutcome::RejectedWithoutNewEvidence);
1610-        }
1611-        // The queue row traces to an edge: write both.

===== Bajan README KNOWN LIMITATIONS =====
exact-pinned so a rebuild reproduces the same store; LLM passes only propose —
humans approve. Specifications under `specs/` are linted by
[specodelic](https://crates.io/crates/specodelic) and gate every commit.

## Known limitations

- **Parked episodes are visible but passive.** When the LLM extractor
  hits transient provider overload it parks 10–24% of episodes per
  pass; the extract report now names each parked episode with its
  failure class (timeout / http-N / transport / schema) and attempt
  count (bajan-gso). Retries back off 2s·2^(n−1) with jitter, capped at
  60s (bajan-266); a rerun recovers parked episodes (cache intact;
  burn-in reruns recovered 2/12).
- **Spend cap needs `usage.cost`.** The LLM extractor requires
  `BAJAN_MAX_SPEND_USD` and stops the pass when known spend reaches the
  cap (bajan-8cc) — but providers that do not report per-call cost in
  `usage.cost` (e.g. plain OpenAI) cannot be accounted: one
  unaccountable call fails the next call closed (never silently
  unbounded). Bound spend at the provider as well.
- **Extraction precision/recall numbers are not published yet.** The eval
  harness is built (`bajan eval claims`, bajan-2k4) but no golden corpus
  has been adjudicated yet — gold labels are human sign-off; until a
  corpus lands and a run is scored, adopt with judgment.
- **Per-call costs are logged, not reported.** The extractor logs one
  stderr line per successful LLM call carrying the response's exact
  `usage.cost` and the running spend against the cap (bajan-3w4);
  aggregate spend surfaces on the extract report only when a cap stops
  the pass (bajan-8cc).
- Burn-in findings and failure profile:
  [`docs/burnin-deepseek-v4-flash-profit-first.org`](docs/burnin-deepseek-v4-flash-profit-first.org).

## Development

```sh
just ci        # full gate: fmt, clippy, tests, spec lint, hooks parity
just --list    # all recipes
```

Issue tracking and burn-in history live in `.beads/`; the spec corpus is
under `specs/` with change proposals under `openspec/`.

## Assistant

bash -lc grep -RIn 'CREATE TABLE.*entit\|entity node\|entities' /tmp/review/bajan-main/src /tmp/review/bajan-main/specs | head -100; printf '\n===== BAJAN MODEL DOC SUMMARY =====\n'; sed -n '1,100p' /tmp/review/bajan-main/knowledge-graphs-report.md; printf '\n===== WHISPER DISTILL REMAINDER =====\n'; sed -n '180,300p' /tmp/review/whisper-main/src/distill.rs; printf '\n===== WHISPER SCOPES =====\n'; sed -n '1,240p' /tmp/review/whisper-main/src/workspace/scope.rs; printf '\n===== WHISPER LAYOUT FILES =====\n'; sed -n '1,260p' /tmp/review/whisper-main/src/workspace/layout.rs

## Tool

/tmp/review/bajan-main/src/eval.rs:60:/// the run and extractor identities stamped on the results record
/tmp/review/bajan-main/specs/graph-model.md:4:statement: "THE bajan knowledge graph SHALL represent every material claim as a reified claim node linked by lineage edges to verbatim episode nodes and entity nodes"
/tmp/review/bajan-main/specs/graph-model.md:12:Claims are reified as nodes — never typed triples between entities — so
/tmp/review/bajan-main/specs/graph-model.md:36:| gm_deterministic_er | invariant | entity resolution is deterministic (normalization plus curated alias lists); unmatched mentions create new entity nodes; merge candidates are proposed as `possible_duplicate_of` edges into a review queue; no silent or automatic merge | [[graph.model]] |
/tmp/review/bajan-main/specs/graph-model.md:68:| p_deterministic_er | unit | [[graph.model.gm_deterministic_er]] | mention streams mixing known aliases, unmatched names, and near-duplicates | entity node count changes only via explicit new-node creation or reviewed merges; queue contents equal candidate pairs |
/tmp/review/bajan-main/specs/entity-review.md:32:| er_merge_preserves | invariant | an approved merge preserves the union of both entities' lineage edges (every `derived_from` edge from both sides survives onto the merged entity) and writes one audit record per resolution — actor, timestamp, both entity ids, decision — per `gm_merge_keeps` | [[entity.review]] | |
/tmp/review/bajan-main/specs/entity-review.md:33:| er_reject_drops_edge | invariant | a rejected candidate loses only its `possible_duplicate_of` edge — both entities, their lineage, and their claims are untouched; the rejection is recorded in the audit trail with actor and timestamp | [[entity.review]] | |
/tmp/review/bajan-main/specs/entity-review.md:35:| er_queue_transparency | invariant | the queue is inspectable: a list command returns every open candidate with both entities' ids, alias/normalization evidence that produced the proposal, claim counts, and queue age, ordered oldest-first — a human can see what they are deciding and what they are leaving undecided | [[entity.review]] | |
/tmp/review/bajan-main/specs/entity-review.md:61:| p_reject_drops_edge | unit | [[entity.review.er_reject_drops_edge]] | rejections over pairs with claims and lineage on both sides | after rejection the `possible_duplicate_of` edge is gone and everything else — entities, lineage, claims, statuses — is unchanged; the audit trail gains one rejection record |
/tmp/review/bajan-main/specs/extraction-claims.md:19:it never merges entities, applies trust policies, or mutates the graph.
/tmp/review/bajan-main/specs/extraction-claims.md:53:| ex_single_call | invariant | each persisted episode id receives exactly one successful LLM extraction call producing candidate claims and entities; failed calls retry with backoff and park the episode in `rejected` after repeated failure; re-ingest of a successfully extracted episode reuses the (episode id, extractor version)-keyed cached output and starts no new call | [[extraction.claims]] |

===== BAJAN MODEL DOC SUMMARY =====
# Thematic Report — Building Knowledge Graphs from LLM/Agent Content

**Generated:** 2026-09-28

**TL;DR:** The corpus shows a full spectrum of KG construction — from deterministic,
structure-derived document graphs (no extraction LLM at all) to fully LLM-extracted
entity/relation graphs with provenance baked in. The consensus that emerges: **schema-first beats
schema-less**, **entity resolution is the underrated hard part**, **provenance must be
engineered into the data structure (a graph), not logged afterwards**, and **most teams
over-build** — several credible speakers argue you shouldn't reach for a graph DB (or a
KG at all) until multi-hop traversal is a proven need, measured by evals.

**Purpose:** a self-contained synthesis of how the corpus builds knowledge graphs from
unstructured content (talks, docs, agent activity), what works, what fails, and where the
practice disagreements are. Passes the amnesia test: readable with zero prior context.

**Sources:** all from the corpus in this repo; full transcripts in `transcripts*/txt/`,
metadata in `analysis/data/talks.json`. Method note: claims are speaker attributions from
stage, mostly transcribed from auto-captions; single-speaker accounts, not verified facts.
Vendor stakes are flagged where they exist (Neo4j and Zep both sell graph infrastructure).

---

## Glossary

| Term | Meaning as used in the corpus |
|---|---|
| **Triple** | subject–predicate–object; the atomic unit of a knowledge graph |
| **Episode** | (Graphiti/Zep) a verbatim source artifact stored as a graph node — the provenance anchor |
| **Entity resolution** | deciding that "J. Smith" and "John Smith" are one node; the merge step |
| **Provenance / lineage** | traceable links from every derived fact back to its source(s) |
| **Business ontology** | domain concepts named the way humans talk (customer, account — not `f_name`) |
| **Technical ontology** | metadata of every data source: where it sits, its schema, mappings |
| **Execution traces** | recorded agent runs: what was tried, whether it worked — a self-learning signal |
| **Decision trace** | (Context Graphs) the captured why behind one operational decision |
| **Community detection** | clustering densely interlinked nodes (Leiden/Louvain) to surface themes |
| **GraphRAG** | Microsoft-paper retrieval pattern: LLM-extracted entity graph + community summaries |
| **Schema-first extraction** | the LLM extractor is given a target node/edge schema to fill, rather than free-form triples |
| **Event-sourced graph** | (Nakajima/ActiveGraph) an immutable event log is the ground truth; the graph is a projection of it, queried at read time |

---

## 1. The two anchor talks

### 1.1 [Citation Needed: Provenance for LLM-Built Knowledge Graphs — Daniel Chalef, Zep AI](https://youtu.be/H7puB0RwJMM) (`transcripts_aieng/txt/206 - …[H7puB0RwJMM].txt`)

The problem: LLM synthesis is non-deterministic and **destroys the paper trail**. His failure
mode: an agent hands a doctor "patient has penicillin allergy," synthesized from three sources
(EHR record, PDF lab report, patient-typed intake chatbot). Without lineage you can't know the
critical fact came from the *patient*, not a verified clinical source.

**Why a source ID on the fact doesn't work** (the naive fix he explicitly rebuts): in
deterministic pipelines one value has one source; in LLM pipelines (a) facts are synthesized
from *multiple* sources, (b) entities get merged ("J. Smith" + "John Smith"), so John's facts
come from many places, (c) new data invalidates old facts, so "the store keeps changing
underneath your pointer." Lineage must be **an evolving set that survives mutation**.

**How they do it (Graphiti, the OSS framework behind Zep)** — pipeline details below are
from the talk and its Q&A; wording normalized from captions:**

- Sources are stored **verbatim as nodes** ("episodes"); every derived artifact is also a
  node; a fact is a hydrated triple (two entity nodes + an edge). Tracing a fact to its
  origin is **just a graph walk**.
- **Lineage survives mutation:** when two entities merge, the merged entity keeps all source
  links from both (otherwise lineage is silently dropped). When a fact is invalidated, an
  `invalid` date goes on the mutated edge and the source episodes that caused the mutation
  are recorded against the fact.
- **Metadata projection:** tag episodes once at ingestion (e.g., `EHR`); all entities and
  facts derived from them inherit the tag. Filtering "facts from verified clinical sources"
  is then a tag check during the walk — one tagging action supports veracity evaluation.
- **Mixed-trust parents are a policy problem, not a graph problem.** Two facts, both with
  three parents, one unverified: for an allergy flag, *any* verified parent suffices (missing
  it is deadly); for consent-on-file, *every* parent must be verified. The graph exposes
  which parents carry the tag; **your agent applies the business rule** — deliberately not
  baked into the store.
- **Deletion/G
...[truncated]...
itespace, parens, or `#`.
fn validate_topic(topic: Option<&str>) -> Result<()> {
    if let Some(t) = topic {
        let invalid = t.is_empty()
            || t.chars()
                .any(|c| c.is_whitespace() || c == '(' || c == ')' || c == '#');
        if invalid {
            return Err(
                WhisperError::new(format!("invalid topic '{t}'")).with_suggestion(
                    "topics are bare keys like 'infra' — no whitespace, parens, or '#'",
                ),
            );
        }
    }
    Ok(())
}

/// Normalize: no trailing whitespace overall, and no line may start with
/// whitespace — continuation lines start with exactly two spaces, so
/// leading whitespace would break the ledger round-trip.
fn normalize_text(text: &str) -> String {
    text.trim_end()
        .lines()
        .map(|l| l.trim_start())
        .collect::<Vec<_>>()
        .join("\n")
}

/// Duplicate guard: an entry with the same id is already in the file.
fn already_present(raw: &str, id: &str) -> bool {
    entry::parse_file(raw)
        .iter()
        .any(|i| matches!(i, Item::Entry(e) if e.id == id))
}

/// Supersede path: mark the target entry superseded and rewrite the file.
#[allow(clippy::too_many_arguments)]
fn rewrite_with_supersede(
    target: &Target,
    raw: &str,
    mut new: Entry,
    id: String,
    sup: &str,
) -> Result<AppendReport> {
    let mut items = entry::parse_file(raw);
    mark_superseded(&mut items, sup, &id)?;
    new.supersedes = Some(sup.to_string());
    items.push(Item::Entry(new));
    target.ensure().map_err(WhisperError::from)?;
    // Rewrite path (rare): concurrent appends during this window can be
    // lost — see design.md; the fast path below is the safe default.
    let rendered = entry::render_file(&items);
    std::fs::write(&target.path, &rendered).map_err(WhisperError::from)?;
    Ok(AppendReport {
        id,
        duplicate: false,
        superseded: Some(sup.to_string()),
        bytes: rendered.len(),
    })
}

/// Fast path: single O_APPEND write — concurrent agents appending in the
/// same window cannot lose each other's entries.
fn fast_path_append(target: &Target, raw: &str, new: Entry, id: String) -> Result<AppendReport> {
    target.ensure().map_err(WhisperError::from)?;
    use std::io::Write;
    let mut f = std::fs::OpenOptions::new()
        .append(true)
        .open(&target.path)
        .map_err(WhisperError::from)?;
    let rendered = entry::render_file(&[Item::Entry(new)]);
    let line = if !raw.is_empty() && !raw.ends_with('\n') {
        format!("\n{rendered}")
    } else {
        rendered
    };
    f.write_all(line.as_bytes()).map_err(WhisperError::from)?;
    Ok(AppendReport {
        id,
        duplicate: false,
        superseded: None,
        bytes: line.len(),
    })
}

/// Mark the supersedes-target entry superseded (error when it is not in
/// this scope file).
fn mark_superseded(items: &mut [Item], sup: &str, id: &str) -> Result<()> {
    match items
        .iter_mut()
        .find(|i| matches!(i, Item::Entry(e) if e.id == sup))
    {
        Some(Item::Entry(e)) => {
            e.superseded_by = Some(id.to_string());
            Ok(())
        }

===== WHISPER LAYOUT FILES =====
//! Layout tests: legacy-key consolidation and multi-layer init.

use crate::config::{Resolved, Routing};

use super::uw::Uw;
use super::*;

#[test]
fn consolidate_merges_nested_files_into_existing_dirs() {
    let (_tmp, canon, legacy, resolved) = nested_merge_fixture();
    consolidate(&uw::ws_facts("github.com/u/whisper"), &resolved).uw();
    t_merge_asserts(&canon, &legacy);
}

/// Nested canonical + legacy dirs with overlapping and novel notes.
type Fix = (
    tempfile::TempDir,
    std::path::PathBuf,
    std::path::PathBuf,
    Resolved,
);

fn nested_merge_fixture() -> Fix {
    let tmp = tempfile::tempdir().uw();
    let repos = tmp.path().join("repos");
    let canon = repos.join("github.com/u/whisper");
    let legacy = repos.join("whisper");
    std::fs::create_dir_all(canon.join("branches/main")).uw();
    std::fs::create_dir_all(legacy.join("branches/main")).uw();
    std::fs::create_dir_all(legacy.join("branches/feature--x")).uw();
    std::fs::write(canon.join("branches/main/notes.md"), "shared note\n").uw();
    std::fs::write(
        legacy.join("branches/main/notes.md"),
        "shared note\nlegacy note\n",
    )
    .uw();
    std::fs::write(
        legacy.join("branches/feature--x/notes.md"),
        "feature note\n",
    )
    .uw();
    let resolved = Resolved {
        workspace_root: tmp.path().to_path_buf(),
        group: None,
        shadowed_global_root: None,
        routing: Routing::RepoLocal,
    };
    (tmp, canon, legacy, resolved)
}

/// Post-merge expectations: extended note, new branch note, legacy gone.
fn t_merge_asserts(canon: &std::path::Path, legacy: &std::path::Path) {
    assert_eq!(
        std::fs::read_to_string(canon.join("branches/main/notes.md")).uw(),
        "shared note\nlegacy note\n"
    );
    assert_eq!(
        std::fs::read_to_string(canon.join("branches/feature--x/notes.md")).uw(),
        "feature note\n"
    );
    assert!(!legacy.exists());
}

#[test]
fn consolidate_noop_without_variants() {
    let tmp = tempfile::tempdir().uw();
    let resolved = Resolved {
        workspace_root: tmp.path().to_path_buf(),
        group: None,
        shadowed_global_root: None,
        routing: Routing::RepoLocal,
    };

    let report = consolidate(&uw::ws_facts("github.com/u/r"), &resolved).uw();

    assert!(report.variants.is_empty());
    assert!(report.moved.is_empty());
    assert!(report.merged.is_empty());
    assert!(!tmp.path().join("repos").exists());
}

#[test]
fn append_creates_then_extends() {
    let tmp = tempfile::tempdir().uw();
    let checkout = tempfile::tempdir().uw();
    let facts = Facts {
        repo_key: "github.com/u/r".into(),
        branch_slug: "main".into(),
        worktree_slot: "r".into(),
        repo_local_root: Some(checkout.path().join(".whisper")),
    };
    let resolved = Resolved {
        workspace_root: tmp.path().to_path_buf(),
        group: None,
        shadowed_global_root: None,
        routing: Routing::RepoLocal,
    };
    let t = resolve(Scope::Repo, &facts, &resolved).uw();
    // Decision A: repo knowledge lands in the checkout, not the store.
    assert_eq!(t.path, checkout.path().join(".whisper/env.md"));
    assert!(t.ensure().uw());
    t.append("first fact").uw();
    t.append("second fact\n\n").uw();
    let content = std::fs::read_to_string(&t.path).uw();
    assert_eq!(content, "first fact\nsecond fact\n");
    assert!(!t.ensure().uw());
}

#[test]
fn init_provisions_both_layers_when_in_a_checkout() {
    let (tmp, checkout, facts, resolved) = uw::checkout_fixture();
    init(&facts, &resolved).uw();
    assert_layers_provisioned(&tmp, &checkout);

    // Outside a checkout only the store layer exists — the scope files
    // are already there (no re-creation); only the branch-slot extras
    // (context.md/plan.md) are new, since the first init's branch slot
    // lived in the checkout layer.
    let bare = Facts {
        repo_local_root: None,
        ..facts
    };
    let report = init(&bare, &resolved).uw();
    assert_only_branch_extras(&report);
}

/// Both layers carry the scope files after init in a checkout.
fn assert_layers_provisioned(tmp: &tempfile::TempDir, checkout: &tempfile::TempDir) {
    assert!(checkout.path().join(".whisper/env.md").exists());
    assert!(
        checkout
            .path()
            .join(".whisper/branches/main/notes.md")
            .exists()
    );
    assert!(tmp.path().join("repos/github.com/u/r/env.md").exists());
    assert!(
        tmp.path()
            .join("repos/github.com/u/r/branches/main/notes.md")
            .exists()
    );
}

/// A bare (store-only) init may only add context.md/plan.md extras.
fn assert_only_branch_extras(report: &InitReport) {
    for p in &report.created {
        let name = p.file_name().uw().to_string_lossy();
        assert!(
            name == "context.md" || name == "plan.md",
            "unexpected creation: {p:?}"
        );
    }
}

## Assistant

bash -lc cat /tmp/review/bajan-main/converters/README.md; printf '\n===== CONVERTER CRATE =====\n'; cat /tmp/review/bajan-main/converters/Cargo.toml; printf '\n===== CONVERTER IMPLEMENTATIONS =====\n'; for f in /tmp/review/bajan-main/converters/src/bin/*.rs; do echo ---$(basename "$f"); rg -n '^fn |^pub fn|^struct |^pub struct|^enum |^pub enum|^const |^pub const|fn main' "$f"; done; printf '\n===== Bajan Cargo =====\n'; cat /tmp/review/bajan-main/Cargo.toml; printf '\n===== Whisper Cargo =====\n'; cat /tmp/review/whisper-main/Cargo.toml

## Tool

# bajan-converters

Standalone upstream converters (bajan-quq): turn source documents into the
bajan **episode-stream** JSON schema so they can be piped straight into
`bajan ingest`.

These tools are **never bajan dependencies** — bajan's `Cargo.toml` carries
no format parsers (`ic_no_format_parsing`): the ingest pipeline consumes
only the normalized episode stream and derives no structure from file
syntax. All format parsing happens here, upstream. This crate is
deliberately not a workspace member of bajan and keeps its own lockfile.

## Tools

| Bin | Input | Output |
|-----|-------|--------|
| `md2bajan` | CommonMark on stdin | episode-stream JSON on stdout |
| `html2bajan` | HTML (html5ever) on stdin | episode-stream JSON on stdout |
| `epub2bajan` | EPUB file (binary — file argument) | episode-stream JSON on stdout |
| `pdf2bajan` | PDF file (binary — file argument) | episode-stream JSON on stdout |

```sh
md2bajan < doc.md    | bajan --db graph.db ingest
html2bajan < page.html | bajan --db graph.db ingest
epub2bajan book.epub   | bajan --db graph.db ingest
pdf2bajan doc.pdf      | bajan --db graph.db ingest
```

## Mapping rules

- Each heading (`#`–`######` / `h1`–`h6`) closes the current episode and
  opens a new one with locator `{"kind": "span", "value": "heading:<text>"}`.
- Text before the first heading (or a document with no headings at all)
  becomes an episode with the typed absent locator `{"kind": "absent"}`
  (ic_verbatim: absent is a distinct marker, never a colliding string).
- Paragraph boundaries are preserved as `\n\n` joins; runs of whitespace
  collapse.
- Deterministic ids: a slug of the heading text (`untitled` when absent),
  repeated anchors disambiguated as `slug-2`, `slug-3`, … — same input
  always yields the same ids, which is what bajan's resubmission policy
  (ic_idempotent / ic_mutated_resubmit) keys on.
- Excluded as code, not prose: fenced code blocks (markdown),
  `<script>`, `<style>`, `<pre>` (HTML).
- Source metadata defaults: `source_type` `markdown`/`html`,
  `data_cutoff` **absent** (ic_date_fidelity: never invent a date),
  `authority_tier` 3 (lowest), no tags. Override downstream if the source
  has real authority/cutoff facts.

Schema conformance is enforced structurally: the emitted records are
bajan's own `EpisodeRecord` type via a path dependency, and the test suite
round-trips converter output through the real `bajan::ingest::persist_stream`
(persist → re-ingest `already_persisted`).

## EPUB mapping rules (`epub2bajan`)

- Each **spine chapter document** becomes ONE episode (chapter-level
  granularity — page numbers do not exist in reflowable EPUB, so there
  are no page locators).
- Chapter text reuses the HTML rules above per spine document (head,
  script/style/pre excluded; block containers as paragraph boundaries).
- Chapter anchor: the toc label wins (toc.ncx via the `epub` crate; the
  EPUB3 nav document is parsed separately — the crate leaves it out),
  else the chapter's first heading text. Locator is
  `{"kind": "span", "value": "heading:<chapter title>"}`.
- Chapters with no toc entry and no heading get the position-based
  fallback id slug `chapter-NNN` (NNN = spine position) and keep the
  typed absent locator — never an invented heading anchor.
- Episode ids: `slug(book title)-slug(chapter title)`, deterministic and
  stream-unique with the same `-N` disambiguation discipline.
- Navigation documents (`properties="nav"`, ncx) listed on a spine are
  skipped — they are metadata, not prose.
- Metadata: `source_type` `epub`; `data_cutoff` from `dc:date` ONLY when
  it is a clean civil date `YYYY-MM-DD` (anything else — "May 2023",
  year-only, ISO datetimes — stays absent, ic_date_fidelity); tier 3; no
  tags.

**EPUB container caveats** (the extra failure mode the flat-text
converters don't have — an EPUB is a ZIP): corrupt containers, valid
zips that are not EPUBs, and DRM-encumbered files fail honestly with a
nonzero exit and a diagnostic — never a partial or garbage stream.
Obfuscated/encrypted fonts are ignored; text extraction is unaffected.

## PDF mapping rules (`pdf2bajan`) — THE CAVEAT, front and center

**PDF text extraction is lossy by design.** Reading order is a heuristic;
columns, tables, and multi-column layouts scramble; hyphenation and
ligatures vary; and extractor-version changes change the extracted text.
That directly threatens verbatim fidelity (ic_verbatim) — the episode text
is only ever a best-effort extraction of the page, not a guaranteed
faithful copy.

Consequences implemented, not just documented:

- Every episode carries a tags entry `pdf-extractor:pdf-extract-<version>`
  naming the exact extractor crate and version, so a version change is
  visible on the record itself. The version constant co-evolves with the
  Cargo.toml pin (enforced by a test).
- Re-converting the same PDF under a different extractor version can
  yield different text → bajan rejects the resubmission with `conflict`
  (ic_mutated_resubmit). **That rejection is CORRECT behavior**: it
  protects claims whose lineage text would otherwise mutate. Do not
  "fix" it by mutating persisted episodes; treat version changes as new
  evidence, deliberately adopted.
- Same-version determinism holds: the same bytes always yield the same
  stream.
- Episode ids are `page-NNN` (page position), NOT document-scoped: two
  different PDFs both emit `page-001`. Ingesting a second, different PDF
  collides on ids and is rejected `conflict` — the same correct
  protection. Scope ids downstream if you need multi-document streams.
- One episode per PAGE, locator `{"kind": "span", "value": "page:N"}`
  (1-based); pages are the only honest anchor — no paragraph locators
  exist for extracted PDF text. Empty pages emit nothing but keep their
  page number (later pages are never renumbered).
- Document metadata (/Info title/author) never becomes episodes.
- `data_cutoff` is always absent: PDF file dates are file-management
  facts, not data cutoffs (ic_date_fidelity).
- **Known extractor limitation (bajan-98x)**: pdf-extract 0.12.1 silently
  returns empty/whitespace text for some Type0 CID fonts with Identity-H
  encoding (observed on a real text-rich PDF that `pdftotext` reads fine).
  pdf2bajan therefore refuses to emit a silent empty stream: a document
  with N>0 pages where EVERY page yields no text after collapse is an
  error (exit 1) naming the page count — a probable encoding failure,
  not an empty document. A 0-page document stays an honest empty stream
  (exit 0). If you hit that error, try `pdftotext` to confirm the PDF is
  text-rich, then treat the PDF as unsupported by pdf-extract for now —
  no silent garbage, no silent nothing.

## Formats not covered (yet) — and their caveats

Per the bajan-15i converter table:

===== CONVERTER CRATE =====
[package]
name = "bajan-converters"
version = "0.1.0"
edition = "2024"
description = "Standalone upstream converters: markdown/HTML → bajan episode-stream JSON (bajan-quq)"
license = "Apache-2.0"
publish = false

# NEVER a workspace member and NEVER a bajan dependency — these tools sit
# upstream of bajan and convert source formats into the published
# episode-stream schema (ic_no_format_parsing: bajan itself stays
# format-free; the converters do the parsing). The path dep below is the
# conformance mechanism: EpisodeRecord is bajan's published type, so the
# emitted JSON cannot drift from the schema bajan actually accepts.
[dependencies]
bajan = { path = ".." }
clap = { version = "4", features = ["derive"] }
serde_json = "1"

# Format parsers (converter-only crates per the bajan-15i table).
pulldown-cmark = "0.13.4"   # markdown: headings/links → locators + structure markers
scraper = "0.27.0"          # HTML: html5ever-backed DOM with CSS selectors
epub = "2.1.5"              # EPUB container: spine/toc/metadata (live-verified: EpubDoc::from_reader, mdata, spine navigation)
pdf-extract = "0.12.1"      # PDF text: extract_text_from_mem_by_pages (live-verified); version co-pinned with PDF_EXTRACTOR_VERSION tag

[[bin]]
name = "md2bajan"
path = "src/bin/md2bajan.rs"

[[bin]]
name = "html2bajan"
path = "src/bin/html2bajan.rs"

[[bin]]
name = "epub2bajan"
path = "src/bin/epub2bajan.rs"

[[bin]]
name = "pdf2bajan"
path = "src/bin/pdf2bajan.rs"

[dev-dependencies]
proptest = "1"

===== CONVERTER IMPLEMENTATIONS =====
---epub2bajan.rs
12:fn main() {
---html2bajan.rs
10:fn main() {
---md2bajan.rs
10:fn main() {
---pdf2bajan.rs
14:fn main() {

===== Bajan Cargo =====
[package]
name = "bajan"
version = "0.2.0"
edition = "2024"
description = "Spec-driven knowledge-graph pipeline CLI — ingest sources, extract claims, query the graph"
license = "Apache-2.0"
repository = "https://github.com/charly-vibes/bajan"
readme = "README.md"
keywords = ["cli", "knowledge-graph", "claims", "extraction", "charly-vibes"]
categories = ["command-line-utilities", "text-processing"]
include = ["src/**/*", "/Cargo.toml", "/Cargo.lock", "/LICENSE", "/README.md"]

[dependencies]
# Suite envelope output — genesis is the shared charly-vibes infrastructure
# crate. Registry dep (NOT git): cargo publish requires all deps to resolve
# on crates.io.
genesis = { package = "genesis-vibes", version = "0.8" }
clap = { version = "4", features = ["derive"] }
serde = { version = "1", features = ["derive"] }
serde_json = "1"
thiserror = "2"
# bajan-15i — pinned deterministic NLP/IR crates (exact `=` pins: a
# rebuild must reproduce the same store). Source: the deterministic-first
# pipeline grounding (Chalef/Blumenfeld/Ainge, `tv` corpus) — no LLM where
# traditional IR/NLP works; format parsers stay upstream-converter-only.
unicode-normalization = "=0.1.25"   # NFC id canonicalization (ic_id_canon)
unicode-segmentation = "=1.13.3"    # UAX #29 sentence boundaries (alignment aid only)
text-splitter = { version = "=0.33.0", features = ["tiktoken-rs"] }           # chunk assembly — input for ONE extraction call (ex_single_call)
tiktoken-rs = "=0.12.1"             # token budget counting
simhash = "=0.3.0"                  # simhash dedup (length-guarded: exact match below threshold)
aho-corasick = "=1.1.5"             # whitespace-collapsed containment search (pure string ops)
ureq = "=3.4.2"

[dev-dependencies]
proptest = "1"

[profile.release]
lto = true
[dependencies.rusqlite]
version = "0.32"
features = ["bundled"]

===== Whisper Cargo =====
[package]
name = "whisper-vibes"
version = "0.11.0"
default-run = "turu"
edition = "2024"
description = "Deterministic knowledge workspace management for AI agents — the mechanical half of the whisper skill as a CLI"
license = "MIT"
repository = "https://github.com/charly-vibes/whisper"
keywords = ["llm", "agents", "knowledge", "workspace", "cli"]
categories = ["command-line-utilities", "development-tools"]

[lib]
name = "whisper"

# The main command follows the song's turututu riff. `whisper` stays as a
# legacy alias so existing scripts and the incitaciones skill keep working.
[[bin]]
name = "turu"
path = "src/main.rs"

[[bin]]
name = "turututu"
path = "src/main.rs"

[[bin]]
name = "whisper"
path = "src/main.rs"

[dependencies]
clap = { version = "4.6.1", features = ["derive"] }
clap_complete = "4"
serde = { version = "1.0.228", features = ["derive"] }
serde_json = "1.0.149"
sha2 = "0.10"
time = { version = "0.3", features = ["formatting", "macros", "parsing"] }
toml = "0.8"
genesis-vibes = "0.13.1"

[dev-dependencies]
assert_cmd = "2"
predicates = "3"
serde_json = "1"
tempfile = "3"

## Assistant

{"path":"/files/search","args":{"search_query":[{"q":"Bajan README spec-driven knowledge graph pipeline ingest episodes extract atomic claims provenance evidence spans human adoption query contradiction"},{"q":"Bajan graph model claim node lineage verbatim episode evidence human adoption deterministic extraction no LLM post processing"},{"q":"Whisper turu append recall distill snapshot agent semantic rewrite commit drift guard structured entries scopes"},{"q":"Whisper knowledge workspace deterministic routing append recall budget newest first supersede"},{"q":"Bajan converters Markdown HTML EPUB PDF episode stream source structure limitations PDF extraction"}],"top_k":10}}

## Tool

{"api_tool_source":"files/search","results":[{"name":"slides(1).md","mime_type":"text/markdown","size_bytes":28901,"library_file_id":"libfile_bce36a5929d8819197ed458119091c56","file_id":"file_0000000098d8820ea4b5a5f2b6159a0c"},{"name":"slides(1).md","mime_type":"text/markdown","size_bytes":28901,"library_file_id":"libfile_bce36a5929d8819197ed458119091c56","file_id":"file_0000000098d8820ea4b5a5f2b6159a0c"},{"name":"slides(1).md","mime_type":"text/markdown","size_bytes":28901,"library_file_id":"libfile_bce36a5929d8819197ed458119091c56","file_id":"file_0000000098d8820ea4b5a5f2b6159a0c"},{"name":"slides(1).md","mime_type":"text/markdown","size_bytes":28901,"library_file_id":"libfile_bce36a5929d8819197ed458119091c56","file_id":"file_0000000098d8820ea4b5a5f2b6159a0c"},{"name":"slides(1).md","mime_type":"text/markdown","size_bytes":28901,"library_file_id":"libfile_bce36a5929d8819197ed458119091c56","file_id":"file_0000000098d8820ea4b5a5f2b6159a0c"},{"name":"slides(1).md","mime_type":"text/markdown","size_bytes":28901,"library_file_id":"libfile_bce36a5929d8819197ed458119091c56","file_id":"file_0000000098d8820ea4b5a5f2b6159a0c"},{"name":"slides(1).md","mime_type":"text/markdown","size_bytes":28901,"library_file_id":"libfile_bce36a5929d8819197ed458119091c56","file_id":"file_0000000098d8820ea4b5a5f2b6159a0c"},{"name":"pyday_hurlingham_2026.md.txt","mime_type":"text/plain","size_bytes":4852,"library_file_id":"libfile_d8ab667413888191b76bfd026984f9a8","file_id":"file_0000000066cc820eaa05650cb3c4fa5d"},{"name":"slides(1).md","mime_type":"text/markdown","size_bytes":28901,"library_file_id":"libfile_bce36a5929d8819197ed458119091c56","file_id":"file_0000000098d8820ea4b5a5f2b6159a0c"},{"name":"slides(1).md","mime_type":"text/markdown","size_bytes":28901,"library_file_id":"libfile_bce36a5929d8819197ed458119091c56","file_id":"file_0000000098d8820ea4b5a5f2b6159a0c"}]}

## Assistant

{"path":"/files/search","args":{"search_query":[{"q":"Bajan knowledge graph README ingest episode claim lineage evidence extraction query human adoption"},{"q":"Whisper turu append recall distill snapshot working file semantic rewrite agent commit drift"}],"scope":{"file_refs":[{"file_id":"file_00000000bd9c820eb23a54d266393334"},{"file_id":"file_00000000db74820e8523648512893a3f"}]},"top_k":10}}

## Tool

{"api_tool_source":"files/search","results":[]}

## Assistant

Sí. Creo que encontramos una idea bastante más propia y, sobre todo, más conectada con el argumento de *After Chatbon*.

La demo no debería ser «construyamos una aplicación con IA», sino **construyamos un instrumento para pensar: algo que nos ayude a entender qué tenemos, qué sabemos, qué no sabemos y qué podríamos hacer con eso**.

Eso cambia también el papel de la IA. No le pedimos que nos entregue una respuesta terminada: la usamos para externalizar el pensamiento, organizar material, formular preguntas, descubrir relaciones y hacer explícitas nuestras incertidumbres. El programa nos ayuda a mantener ese proceso visible, acumulativo y verificable.

Quiero mirar Bajan y Whisper desde esa perspectiva, sin asumir que sus arquitecturas actuales ya son la solución. También voy a contrastar la idea con el artículo sobre *writing as a thinking tool*.

Revisando los dos proyectos, veo una división de responsabilidades bastante interesante. Y también una oportunidad: **ninguno de los dos, por sí solo, implementa todavía la metodología completa que estamos buscando**.

## 1. Qué podemos aprender de Bajan y Whisper

No los pensaría como dos herramientas que hacen lo mismo, sino como dos partes diferentes de un proceso de pensamiento.

| | Bajan | Whisper / Turu |
|---|---|---|
| Problema | Entender qué dicen las fuentes y de dónde sale cada afirmación | No perder lo que vamos aprendiendo entre sesiones |
| Unidad principal | Episodios, afirmaciones y relaciones | Notas y entradas de conocimiento |
| Operación | Ingestar, extraer, relacionar, consultar, revisar | Escribir, recuperar, reemplazar y destilar |
| Rol de la IA | Proponer afirmaciones a partir de evidencia | Participar en la reescritura semántica |
| Garantía principal | Trazabilidad hasta la fuente | Persistencia, historial y recuperación determinista |

### Bajan: construir una representación de lo que sabemos

En el código actual hay una idea muy buena:

1. Las fuentes se convierten en *episodes*: fragmentos de texto que se conservan literalmente, con sus localizadores y metadatos.
2. La IA propone afirmaciones atómicas.
3. Cada afirmación debe incluir un fragmento literal que la respalde.
4. Un proceso determinista valida el esquema y la correspondencia de la evidencia.
5. Las afirmaciones quedan pendientes de adopción humana.
6. Las consultas recorren las relaciones de procedencia para poder volver a las fuentes.

Esto es importante: **no almacenamos solamente una respuesta generada por IA; conservamos cómo llegamos a ella**.

También hay límites que tenemos que reconocer:

- `bajan query` actualmente busca coincidencias literales de texto, no realiza búsqueda semántica.
- La extracción LLM todavía no tiene métricas de precisión y recall publicadas: el README indica que falta adjudicar el corpus de evaluación.
- La adopción humana es una decisión explícita para incorporar una afirmación al grafo, no una demostración de que sea objetivamente verdadera.
- Hay una diferencia entre la especificación y la implementación actual: `graph-model.md` habla de nodos de entidades, pero el esquema SQLite de este snapshot tiene tablas para episodios, afirmaciones, linaje y relaciones, no una tabla de entidades. El proceso de entity resolution implementado compara textos normalizados de afirmaciones. Es un buen ejemplo de algo que nuestro programa debería poder descubrir y mostrar.

Bajan es, entonces, un buen sustrato para **construir conocimiento verificable a partir de material existente**, pero todavía no es una herramienta de exploración conceptual completa.

### Whisper: convertir la experiencia en memoria de trabajo

Whisper (el proyecto cuyo ejecutable es `turu`, no el sistema de transcripción de audio) resuelve otra parte:

- `append`: registrar lo aprendido sin sobrescribir lo anterior.
- `recall`: recuperar una selección acotada de notas, por tema y recencia.
- `supersedes`: indicar cuándo un conocimiento nuevo reemplaza uno anterior.
- `distill`: crear una revisión, trabajar sobre una copia y confirmar el resultado solo si el original no cambió.

Hay un detalle arquitectónico especialmente interesante en `src/distill.rs`: Turu se ocupa de la mecánica —snapshot, revisión, detección de cambios y commit—, pero **el agente que lo invoca es quien realiza la reescritura semántica**.

Es una separación muy sana: el programa no pretende decidir qué significa una nota. Proporciona un proceso seguro para que nosotros y la IA podamos revisarla.

Whisper tampoco es un buscador semántico ni un motor de razonamiento. Es infraestructura determinista para la memoria de trabajo.

## 2. La conexión con «Writing as a thinking tool»

El artículo de Murat Demirbas aporta el principio que une ambos proyectos.

Su argumento central es que escribir no sirve solamente para conservar información: sirve para procesarla. Externalizar pensamientos permite trabajar con problemas más grandes que los que podemos mantener en nuestra memoria inmediata. <Cite ref="turn846435view0"/>

Me interesan especialmente cuatro ideas del artículo:

1. **Escribir antes de abrir el chat.** La IA conoce mucha información pública, pero no conoce nuestras intuiciones todavía incompletas. Si le pedimos una explicación inmediatamente, puede imponer un marco antes de que hayamos formulado el nuestro.
2. **Producir primero sin juzgar.** Hay que tener algo sobre lo que pensar. Las primeras notas pueden ser desordenadas, contradictorias o incompletas.
3. **Editar como una operación de pensamiento.** Revisar, eliminar, reorganizar y simplificar es parte del proceso de entender.
4. **Escribir para uno mismo.** El objetivo inicial no es producir un documento presentable, sino entender algo que antes no entendíamos.

La advertencia más importante es que la IA puede producir un documento muy bien escrito sin que haya ocurrido ningún proceso equivalente de comprensión humana. <Cite ref="turn846435view0"/>

Esto nos da una hipótesis para el programa:

> **Una herramienta para pensar con IA no debería limitarse a producir texto. Debería ayudarnos a construir, revisar y mejorar nuestra propia representación de un problema.**

## 3. El programa que necesitamos

Yo lo pensaría como un *workbench* de comprensión, no como un chatbot sobre documentos.

<box border radius="lg" padding={3} gap={3}>
  <title size="xl">Una mesa de trabajo para entender lo que tenemos</title>
  <text color="secondary" size="sm">El usuario y la IA construyen una representación progresiva del material.</text>
  <box background="surface-secondary" padding={3} radius="md" gap={1}>
    **1. Material**
    <text color="secondary" size="sm">Repositorios, documentos, notas, datos, especificaciones, experimentos.</text>
  </box>
  <box align="center">
    <icon name="arrow-down" color="secondary"/>
  </box>
  <box background="surface-secondary" padding={3} radius="md" gap={1}>
    **2. Inventario y estructura**
    <text color="secondary" size="sm">Qué existe, cómo está organizado, qué relaciones explícitas tiene y qué partes no pudimos procesar.</text>
  </box>
  <box align="center">
    <icon name="arrow-down" color="secondary"/>
  </box>
  <box border padding={3} radius="md" gap={1}>
    **3. Escritura propia**
    <text color="secondary" size="sm">Qué creo que tengo, qué entiendo, qué no entiendo y qué me llama la atención.</text>
    <badge color="success">Primero nosotros</badge>
  </box>
  <box align="center">
    <icon name="arrow-down" color="secondary"/>
  </box>
  <box background="surface-secondary" padding={3} radius="md" gap={1}>
    **4. Exploración con IA**
    <text color="secondary" size="sm">Proponer conceptos, afirmaciones, relaciones, explicaciones alternativas, contradicciones y preguntas.</text>
  </box>
  <box align="center">
    <icon name="arrow-down" color="secondary"/>
  </box>
  <box background="surface-secondary" padding={3} radius="md" gap={1}>
    **5. Revisión y comprensión**
    <text color="secondary" size="sm">Examinar evidencia, corregir interpretaciones, descubrir huecos y formular nuevas preguntas.</text>
  </box>
  <box align="center">
    <icon name="arrow-down" color="secondary"/>
  </box>
  <box border padding={3} radius="md" gap={1}>
    **6. Destilación**
    <text color="secondary" size="sm">Una representación más simple y útil de lo que entendimos, con historial y cuestiones pendientes.</text>
    <badge color="success">Bajan + Whisper</badge>
  </box>
</box>

La salida no debería ser solamente un resumen. Debería producir varios artefactos relacionados:

- **Mapa:** qué componentes, conceptos y temas existen.
- **Glosario:** qué significan las cosas en este contexto.
- **Afirmaciones:** qué sabemos y dónde está la evidencia.
- **Interpretaciones:** qué creemos que significa el material.
- **Contradicciones:** qué cosas no encajan entre sí.
- **Preguntas abiertas:** qué todavía no entendemos.
- **Próximos experimentos:** qué podemos investigar para resolver las incertidumbres.

Una distinción que considero fundamental: no mezclar afirmaciones observadas, interpretaciones, hipótesis y preguntas. La IA puede proponer todas ellas, pero el programa debe mostrar qué clase de objeto estamos mirando y qué evidencia tiene.

## 4. La primera aplicación: entender Bajan y Whisper

Creo que tenemos un ejemplo conductor excelente y no hace falta inventar otro.

**Vamos a construir un programa que nos ayude a entender los propios proyectos Bajan y Whisper.**

Esto tiene una ventaja narrativa enorme: usamos la herramienta para entender las herramientas que estamos construyendo.

<AsyncImage query="minimalist software architecture knowledge map nodes edges source documents visualization dark background" aspectRatio="16:9" width="100%"/>

Un recorrido concreto podría ser:

**Pregunta inicial:** ¿Qué tenemos realmente en estos dos repositorios y cómo se complementan?

1. Importamos los repositorios.
2. El programa inventaría archivos, módulos, documentación, especificaciones, tests y dependencias.
3. Antes de consultar a la IA, escribimos nuestra interpretación inicial.
4. Le pedimos a la IA que construya un mapa de responsabilidades y relaciones, con referencias a los archivos y líneas.
5. Exploramos preguntas concretas:
   - ¿Qué promete Bajan y qué implementa realmente?
   - ¿Qué significa una afirmación activa en Bajan?
   - ¿Qué operaciones de Whisper son mecánicas y cuáles dependen del agente?
   - ¿Qué información se pierde cuando pasamos de una fuente a una nota destilada?
   - ¿Qué falta para que ambos formen una metodología completa?
6. Revisamos las respuestas y producimos una explicación más clara que la que teníamos al principio.

El ejemplo de la diferencia entre los nodos de entidades declarados en Bajan y su implementación actual sería especialmente bueno: no es una respuesta genérica de un chatbot, sino un descubrimiento respaldado por la inspección del material.

## 5. Qué construiría primero

No empezaría implementando un nuevo grafo de conocimiento ni integrando todos los comandos de ambos proyectos.

Haría un prototipo pequeño con cinco capacidades:

| Capacidad | Comportamiento mínimo |
|---|---|
| Importar | Abrir un repositorio y sus documentos |
| Inventariar | Mostrar estructura, archivos y cobertura |
| Explorar | Hacer preguntas y recibir propuestas con evidencia |
| Anotar | Escribir, corregir y relacionar nuestras propias ideas |
| Destilar | Generar una representación revisada y conservar las anteriores |

Para el primer corpus usaría Markdown, TOML, JSON y código Rust. Los archivos de código necesitan un tratamiento estructural propio: módulos, funciones, tipos, tests y referencias con líneas. No conviene pasarlos simplemente como texto plano. Los conversores actuales de Bajan cubren Markdown, HTML, EPUB y PDF, pero todavía no un repositorio de código como unidad de análisis.

La implementación inicial podría reutilizar los contratos de Bajan y las ideas de persistencia de Whisper. No asumiría que sus binarios Rust pueden ejecutarse directamente dentro de Pyodide: son herramientas nativas con dependencias de SQLite y filesystem. Pyodide podría servir más adelante para ejecutar análisis Python, estadísticas y visualizaciones sobre los datos recopilados.

---

## 6. El argumento que esto le da a After Chatbon

Me parece que encontramos una tesis mucho más interesante que «la IA nos permite programar más rápido»:

> Antes necesitábamos herramientas para producir cosas. Ahora también necesitamos herramientas para entender las cosas que podemos producir.

Y una segunda frase, que puede ser el corazón de la demo:

> No quiero que la IA me explique lo que tengo. Quiero construir algo que me ayude a descubrir qué entiendo, qué no entiendo y qué vale la pena investigar.

Esto conecta directamente con el artículo, Bajan y Whisper, y con la idea de que aprender a trabajar con IA implica aprender a pensar mejor, no simplemente delegar más.

**Una decisión para seguir:** ¿Tomamos Bajan y Whisper como el primer corpus que el programa tiene que ayudarnos a comprender, y después generalizamos el instrumento para cualquier repositorio, documentos o conjunto de datos?

## User

Como podemos enfocar esto en una manera de probar software, experimentar, descartar y ver que sovrevive, cómo tiene que estar estructurado el software para poder ser re-escrito muchas veces. Esa metodologia nos va a permitir aprender que es lo queremos resolver y como construir cosas más cokplejas

## Assistant

bash -lc ls -lh /mnt/data && unzip -l '/mnt/data/bajan-main(2).zip' | head -60 && printf '\n--- WHISPER ---\n' && unzip -l '/mnt/data/whisper-main.zip' | head -80

## Tool

total 900K
-rw-r--r-- 1 root oai_shared 586K Nov 11 02:30 bajan-main(2).zip
-rw-r--r-- 1 root oai_shared 4.8K Nov 11 02:30 pyday_hurlingham_2026.md.txt
-rw-r--r-- 1 root oai_shared  29K Nov 11 02:30 slides(1).md
-rw-r--r-- 1 root oai_shared 272K Nov 11 02:30 whisper-main.zip
Archive:  /mnt/data/bajan-main(2).zip
990adce7960050a2864339c3dff488974126a103
  Length      Date    Time    Name
---------  ---------- -----   ----
        0  2026-11-10 21:52   bajan-main/
        0  2026-11-10 21:52   bajan-main/.beads.gate.lock
        0  2026-11-10 21:52   bajan-main/.beads/
     2334  2026-11-10 21:52   bajan-main/.beads/config.yaml
   165957  2026-11-10 21:52   bajan-main/.beads/issues.jsonl
        0  2026-11-10 21:52   bajan-main/.cargo/
      370  2026-11-10 21:52   bajan-main/.cargo/config.toml
        0  2026-11-10 21:52   bajan-main/.claude/
      389  2026-11-10 21:52   bajan-main/.claude/settings.json
        0  2026-11-10 21:52   bajan-main/.espectacular/
      745  2026-11-10 21:52   bajan-main/.espectacular/AGENTS.md
      123  2026-11-10 21:52   bajan-main/.espectacular/config.toml
        0  2026-11-10 21:52   bajan-main/.espectacular/contradiction-review/
      370  2026-11-10 21:52   bajan-main/.espectacular/contradiction-review/p-human-resolution.toml
      521  2026-11-10 21:52   bajan-main/.espectacular/contradiction-review/p-proposal-entry.toml
      349  2026-11-10 21:52   bajan-main/.espectacular/contradiction-review/p-queue-transparency.toml
      214  2026-11-10 21:52   bajan-main/.espectacular/contradiction-review/p-repropose-guard.toml
      280  2026-11-10 21:52   bajan-main/.espectacular/contradiction-review/p-scan-untouched.toml
        0  2026-11-10 21:52   bajan-main/.espectacular/entity-review/
      360  2026-11-10 21:52   bajan-main/.espectacular/entity-review/p-human-resolution.toml
      278  2026-11-10 21:52   bajan-main/.espectacular/entity-review/p-merge-preserves.toml
      550  2026-11-10 21:52   bajan-main/.espectacular/entity-review/p-queue-entry.toml
      311  2026-11-10 21:52   bajan-main/.espectacular/entity-review/p-queue-transparency.toml
      286  2026-11-10 21:52   bajan-main/.espectacular/entity-review/p-reject-drops-edge.toml
      222  2026-11-10 21:52   bajan-main/.espectacular/entity-review/p-repropose-guard.toml
      213  2026-11-10 21:52   bajan-main/.espectacular/entity-review/p-review-schema.toml
        0  2026-11-10 21:52   bajan-main/.espectacular/eval-claims/
      522  2026-11-10 21:52   bajan-main/.espectacular/eval-claims/p-deterministic-scoring.toml
      313  2026-11-10 21:52   bajan-main/.espectacular/eval-claims/p-golden-corpus.toml
      559  2026-11-10 21:52   bajan-main/.espectacular/eval-claims/p-hedge-scoring.toml
      313  2026-11-10 21:52   bajan-main/.espectacular/eval-claims/p-precision-recall.toml
      202  2026-11-10 21:52   bajan-main/.espectacular/eval-claims/p-readonly.toml
      232  2026-11-10 21:52   bajan-main/.espectacular/eval-claims/p-results-checked-in.toml
      315  2026-11-10 21:52   bajan-main/.espectacular/eval-claims/p-results-schema.toml
        0  2026-11-10 21:52   bajan-main/.espectacular/extraction-claims/
      440  2026-11-10 21:52   bajan-main/.espectacular/extraction-claims/p-deterministic-structure.toml
      536  2026-11-10 21:52   bajan-main/.espectacular/extraction-claims/p-evidence-containment.toml
      492  2026-11-10 21:52   bajan-main/.espectacular/extraction-claims/p-mutation-proposal.toml
      213  2026-11-10 21:52   bajan-main/.espectacular/extraction-claims/p-no-llm-post.toml
      457  2026-11-10 21:52   bajan-main/.espectacular/extraction-claims/p-output-schema.toml
      400  2026-11-10 21:52   bajan-main/.espectacular/extraction-claims/p-park-requeue.toml
      211  2026-11-10 21:52   bajan-main/.espectacular/extraction-claims/p-reflection.toml
      610  2026-11-10 21:52   bajan-main/.espectacular/extraction-claims/p-run-record.toml
      240  2026-11-10 21:52   bajan-main/.espectacular/extraction-claims/p-section-filter.toml
      471  2026-11-10 21:52   bajan-main/.espectacular/extraction-claims/p-single-call.toml
      704  2026-11-10 21:52   bajan-main/.espectacular/extraction-claims/p-supersession.toml
      419  2026-11-10 21:52   bajan-main/.espectacular/extraction-claims/p-tag-inheritance.toml
      513  2026-11-10 21:52   bajan-main/.espectacular/extraction-claims/p-typed-gate.toml
        0  2026-11-10 21:52   bajan-main/.espectacular/graph-model/
      470  2026-11-10 21:52   bajan-main/.espectacular/graph-model/p-contradicts-provenance.toml
      385  2026-11-10 21:52   bajan-main/.espectacular/graph-model/p-deterministic-er.toml
      556  2026-11-10 21:52   bajan-main/.espectacular/graph-model/p-embedded-store.toml
      424  2026-11-10 21:52   bajan-main/.espectacular/graph-model/p-hedge-anchor.toml
      547  2026-11-10 21:52   bajan-main/.espectacular/graph-model/p-human-adopt.toml
      400  2026-11-10 21:52   bajan-main/.espectacular/graph-model/p-lineage-survives.toml
      336  2026-11-10 21:52   bajan-main/.espectacular/graph-model/p-merge-keeps.toml

--- WHISPER ---
Archive:  /mnt/data/whisper-main.zip
cf0e410606de137ed4bcfd6e23cf732c9e0b7e66
  Length      Date    Time    Name
---------  ---------- -----   ----
        0  2026-11-05 13:44   whisper-main/
        0  2026-11-05 13:44   whisper-main/.beads/
     1615  2026-11-05 13:44   whisper-main/.beads/.gitignore
     2253  2026-11-05 13:44   whisper-main/.beads/README.md
     2267  2026-11-05 13:44   whisper-main/.beads/config.yaml
     4251  2026-11-05 13:44   whisper-main/.beads/interactions.jsonl
    41957  2026-11-05 13:44   whisper-main/.beads/issues.jsonl
      158  2026-11-05 13:44   whisper-main/.beads/metadata.json
        0  2026-11-05 13:44   whisper-main/.claude/
      389  2026-11-05 13:44   whisper-main/.claude/settings.json
        0  2026-11-05 13:44   whisper-main/.ddl/
       75  2026-11-05 13:44   whisper-main/.ddl/config.toml
     2189  2026-11-05 13:44   whisper-main/.ddl/manifest.json
        0  2026-11-05 13:44   whisper-main/.espectacular/
      745  2026-11-05 13:44   whisper-main/.espectacular/AGENTS.md
        0  2026-11-05 13:44   whisper-main/.espectacular/config-precedence/
      189  2026-11-05 13:44   whisper-main/.espectacular/config-precedence/config-found-in-a-parent.toml
      187  2026-11-05 13:44   whisper-main/.espectacular/config-precedence/fresh-machine.toml
      202  2026-11-05 13:44   whisper-main/.espectacular/config-precedence/nested-config-shadows-the-repo-root.toml
      181  2026-11-05 13:44   whisper-main/.espectacular/config-precedence/repo-joins-a-group.toml
      196  2026-11-05 13:44   whisper-main/.espectacular/config-precedence/repo-overrides-the-workspace-root.toml
      124  2026-11-05 13:44   whisper-main/.espectacular/config.toml
        0  2026-11-05 13:44   whisper-main/.espectacular/knowledge-append/
      189  2026-11-05 13:44   whisper-main/.espectacular/knowledge-append/empty-input-rejected.toml
      199  2026-11-05 13:44   whisper-main/.espectacular/knowledge-append/first-append-creates-the-file.toml
      186  2026-11-05 13:44   whisper-main/.espectacular/knowledge-append/piped-input.toml
      184  2026-11-05 13:44   whisper-main/.espectacular/knowledge-append/subsequent-appends-extend.toml
      187  2026-11-05 13:44   whisper-main/.espectacular/knowledge-append/trailing-whitespace-collapse.toml
        0  2026-11-05 13:44   whisper-main/.espectacular/managed-block/
      188  2026-11-05 13:44   whisper-main/.espectacular/managed-block/content-matches-resolve.toml
      186  2026-11-05 13:44   whisper-main/.espectacular/managed-block/file-override.toml
      201  2026-11-05 13:44   whisper-main/.espectacular/managed-block/first-sync-creates-the-block.toml
      186  2026-11-05 13:44   whisper-main/.espectacular/managed-block/re-sync-updates-in-place.toml
      192  2026-11-05 13:44   whisper-main/.espectacular/managed-block/target-file-missing.toml
        0  2026-11-05 13:44   whisper-main/.espectacular/shared-store/
      207  2026-11-05 13:44   whisper-main/.espectacular/shared-store/bundle-carries-no-transport-state.toml
      183  2026-11-05 13:44   whisper-main/.espectacular/shared-store/deterministic-pack.toml
      229  2026-11-05 13:44   whisper-main/.espectacular/shared-store/legacy-bundle-unpacks-into-current-resolution.toml
      213  2026-11-05 13:44   whisper-main/.espectacular/shared-store/merge-into-an-existing-workspace.toml
      213  2026-11-05 13:44   whisper-main/.espectacular/shared-store/pack-group-scope-with-no-active-group.toml
      220  2026-11-05 13:44   whisper-main/.espectacular/shared-store/pack-refuses-private-resolved-scopes.toml
      209  2026-11-05 13:44   whisper-main/.espectacular/shared-store/pack-with-private-content.toml
      214  2026-11-05 13:44   whisper-main/.espectacular/shared-store/round-trip-into-a-fresh-workspace.toml
      230  2026-11-05 13:44   whisper-main/.espectacular/shared-store/unpack-never-writes-into-the-private-zone.toml
        0  2026-11-05 13:44   whisper-main/.espectacular/workspace-maintenance/
      202  2026-11-05 13:44   whisper-main/.espectacular/workspace-maintenance/canonical-dir-absent.toml
      186  2026-11-05 13:44   whisper-main/.espectacular/workspace-maintenance/check-flags-legacy-variants.toml
      200  2026-11-05 13:44   whisper-main/.espectacular/workspace-maintenance/fresh-init-adds-the-rule.toml
      180  2026-11-05 13:44   whisper-main/.espectacular/workspace-maintenance/fresh-init.toml
      184  2026-11-05 13:44   whisper-main/.espectacular/workspace-maintenance/idempotent-ignore-rule.toml
      171  2026-11-05 13:44   whisper-main/.espectacular/workspace-maintenance/idempotent-re-init.toml
      221  2026-11-05 13:44   whisper-main/.espectacular/workspace-maintenance/leak-shaped-content-in-public-files.toml
      211  2026-11-05 13:44   whisper-main/.espectacular/workspace-maintenance/merge-extends-without-duplicating.toml
      225  2026-11-05 13:44   whisper-main/.espectacular/workspace-maintenance/private-zone-not-effectively-ignored.toml
      184  2026-11-05 13:44   whisper-main/.espectacular/workspace-maintenance/status-is-side-effect-free.toml
      227  2026-11-05 13:44   whisper-main/.espectacular/workspace-maintenance/tracked-file-under-the-private-zone.toml
      217  2026-11-05 13:44   whisper-main/.espectacular/workspace-maintenance/unrelated-colon-dirs-are-safe.toml
        0  2026-11-05 13:44   whisper-main/.espectacular/workspace-routing/
      176  2026-11-05 13:44   whisper-main/.espectacular/workspace-routing/bare-repo.toml
      207  2026-11-05 13:44   whisper-main/.espectacular/workspace-routing/branch-scope-resolves-into-the-checkout.toml
      227  2026-11-05 13:44   whisper-main/.espectacular/workspace-routing/consolidate-cannot-reach-the-private-zone.toml
      251  2026-11-05 13:44   whisper-main/.espectacular/workspace-routing/doctor-flags-stale-checkout-layer-content-under-machine-local.toml
      182  2026-11-05 13:44   whisper-main/.espectacular/workspace-routing/feature-branch.toml
      202  2026-11-05 13:44   whisper-main/.espectacular/workspace-routing/global-escape-hatch.toml
      214  2026-11-05 13:44   whisper-main/.espectacular/workspace-routing/group-scope-without-an-active-group.toml
      173  2026-11-05 13:44   whisper-main/.espectacular/workspace-routing/https-remote.toml
      246  2026-11-05 13:44   whisper-main/.espectacular/workspace-routing/init-under-machine-local-routing-provisions-only-the-store.toml
      194  2026-11-05 13:44   whisper-main/.espectacular/workspace-routing/linked-worktree-shares-the-slot.toml
      222  2026-11-05 13:44   whisper-main/.espectacular/workspace-routing/machine-local-routing-is-the-persistent-default.toml
      174  2026-11-05 13:44   whisper-main/.espectacular/workspace-routing/no-remote.toml
      224  2026-11-05 13:44   whisper-main/.espectacular/workspace-routing/pre-existing-global-store-knowledge-stays-servable.toml
      206  2026-11-05 13:44   whisper-main/.espectacular/workspace-routing/private-routing-flag.toml
      213  2026-11-05 13:44   whisper-main/.espectacular/workspace-routing/recall-serves-private-knowledge-locally.toml
      222  2026-11-05 13:44   whisper-main/.espectacular/workspace-routing/repo-local-remains-the-default-without-a-routing-key.toml
      176  2026-11-05 13:44   whisper-main/.espectacular/workspace-routing/ssh-remote.toml
      199  2026-11-05 13:44   whisper-main/.espectacular/workspace-routing/store-major-composition-order.toml

## Assistant

bash -lc rm -rf /tmp/after-chatbon && mkdir -p /tmp/after-chatbon && unzip -q '/mnt/data/bajan-main(2).zip' -d /tmp/after-chatbon && unzip -q '/mnt/data/whisper-main.zip' -d /tmp/after-chatbon && printf '\n--- BAJAN TOP LEVEL ---\n' && find /tmp/after-chatbon/bajan-main -maxdepth 2 -type f | sed 's#^.*/bajan-main/##' | sort | head -160 && printf '\n--- WHISPER TOP LEVEL ---\n' && find /tmp/after-chatbon/whisper-main -maxdepth 3 -type f | sed 's#^.*/whisper-main/##' | sort | head -160

## Tool

--- BAJAN TOP LEVEL ---
.beads.gate.lock
.beads/config.yaml
.beads/issues.jsonl
.cargo/config.toml
.claude/settings.json
.espectacular/AGENTS.md
.espectacular/config.toml
.genesis/tools.toml
.gitignore
.wai/.gitignore
.wai/.pipeline-run
.wai/AGENTS.md
.wai/PLUGINS.md
.wai/config.toml
AGENTS.md
CHANGELOG.md
CLAUDE.md
Cargo.lock
Cargo.toml
LICENSE
README.md
converters/Cargo.lock
converters/Cargo.toml
converters/README.md
docs/burnin-deepseek-v4-flash-profit-first.org
docs/knowledge-assistant-ears-spec.md
evals/results.md
justfile
knowledge-graphs-report.md
lefthook.yml
openspec/AGENTS.md
openspec/project.md
pretender.toml
proptest-regressions/store.txt
scripts/update-homebrew.py
scripts/update-scoop.py
site/index.html
specodelic/contradiction-review.tla
specodelic/contradiction-review.toml
specodelic/contradiction-review_props.rs
specodelic/entity-review.tla
specodelic/entity-review.toml
specodelic/entity-review_props.rs
specodelic/eval-claims.tla
specodelic/eval-claims.toml
specodelic/eval-claims_props.rs
specodelic/extraction-claims.tla
specodelic/extraction-claims.toml
specodelic/extraction-claims_props.rs
specodelic/graph-model.tla
specodelic/graph-model.toml
specodelic/graph-model_props.rs
specodelic/ingestion-contract.tla
specodelic/ingestion-contract.toml
specodelic/ingestion-contract_props.rs
specodelic/query-tools.tla
specodelic/query-tools.toml
specodelic/query-tools_props.rs
specs/contradiction-review.md
specs/entity-review.md
specs/eval-claims.md
specs/extraction-claims.md
specs/graph-model.md
specs/ingestion-contract.md
specs/query-tools.md
src/cli.rs
src/config.rs
src/contradict.rs
src/eval.rs
src/extract.rs
src/ingest.rs
src/lib.rs
src/llm.rs
src/main.rs
src/propose.rs
src/query.rs
src/resolve.rs
src/review.rs
testaruda.toml
tests/atomic_atomizer.proptest-regressions
tests/atomic_atomizer.rs
tests/cli.rs
tests/config.rs
tests/contradiction_proposals.rs
tests/contradiction_scan.proptest-regressions
tests/contradiction_scan.rs
tests/deps_pinned.rs
tests/entity_review.proptest-regressions
tests/entity_review.rs
tests/episode_tombstones.rs
tests/eval_harness.proptest-regressions
tests/eval_harness.rs
tests/extractor_config.rs
tests/extractor_seam.rs
tests/llm_extractor.rs
tests/mutation_proposal.rs
tests/query_contradiction.rs
tests/query_coverage.proptest-regressions
tests/query_coverage.rs
tests/query_ranking.proptest-regressions
tests/query_ranking.rs
tests/query_scope.rs
tests/resolve.rs
tests/scenarios.rs
tests/vertical_slice.proptest-regressions
tests/vertical_slice.rs
tests/write_path_discipline.rs
tools/deploy_specs.py
tools/spec_drift_gate.sh

--- WHISPER TOP LEVEL ---
.beads/.gitignore
.beads/README.md
.beads/config.yaml
.beads/interactions.jsonl
.beads/issues.jsonl
.beads/metadata.json
.claude/settings.json
.ddl/config.toml
.ddl/manifest.json
.espectacular/AGENTS.md
.espectacular/config-precedence/config-found-in-a-parent.toml
.espectacular/config-precedence/fresh-machine.toml
.espectacular/config-precedence/nested-config-shadows-the-repo-root.toml
.espectacular/config-precedence/repo-joins-a-group.toml
.espectacular/config-precedence/repo-overrides-the-workspace-root.toml
.espectacular/config.toml
.espectacular/knowledge-append/empty-input-rejected.toml
.espectacular/knowledge-append/first-append-creates-the-file.toml
.espectacular/knowledge-append/piped-input.toml
.espectacular/knowledge-append/subsequent-appends-extend.toml
.espectacular/knowledge-append/trailing-whitespace-collapse.toml
.espectacular/managed-block/content-matches-resolve.toml
.espectacular/managed-block/file-override.toml
.espectacular/managed-block/first-sync-creates-the-block.toml
.espectacular/managed-block/re-sync-updates-in-place.toml
.espectacular/managed-block/target-file-missing.toml
.espectacular/shared-store/bundle-carries-no-transport-state.toml
.espectacular/shared-store/deterministic-pack.toml
.espectacular/shared-store/legacy-bundle-unpacks-into-current-resolution.toml
.espectacular/shared-store/merge-into-an-existing-workspace.toml
.espectacular/shared-store/pack-group-scope-with-no-active-group.toml
.espectacular/shared-store/pack-refuses-private-resolved-scopes.toml
.espectacular/shared-store/pack-with-private-content.toml
.espectacular/shared-store/round-trip-into-a-fresh-workspace.toml
.espectacular/shared-store/unpack-never-writes-into-the-private-zone.toml
.espectacular/workspace-maintenance/canonical-dir-absent.toml
.espectacular/workspace-maintenance/check-flags-legacy-variants.toml
.espectacular/workspace-maintenance/fresh-init-adds-the-rule.toml
.espectacular/workspace-maintenance/fresh-init.toml
.espectacular/workspace-maintenance/idempotent-ignore-rule.toml
.espectacular/workspace-maintenance/idempotent-re-init.toml
.espectacular/workspace-maintenance/leak-shaped-content-in-public-files.toml
.espectacular/workspace-maintenance/merge-extends-without-duplicating.toml
.espectacular/workspace-maintenance/private-zone-not-effectively-ignored.toml
.espectacular/workspace-maintenance/status-is-side-effect-free.toml
.espectacular/workspace-maintenance/tracked-file-under-the-private-zone.toml
.espectacular/workspace-maintenance/unrelated-colon-dirs-are-safe.toml
.espectacular/workspace-routing/bare-repo.toml
.espectacular/workspace-routing/branch-scope-resolves-into-the-checkout.toml
.espectacular/workspace-routing/consolidate-cannot-reach-the-private-zone.toml
.espectacular/workspace-routing/doctor-flags-stale-checkout-layer-content-under-machine-local.toml
.espectacular/workspace-routing/feature-branch.toml
.espectacular/workspace-routing/global-escape-hatch.toml
.espectacular/workspace-routing/group-scope-without-an-active-group.toml
.espectacular/workspace-routing/https-remote.toml
.espectacular/workspace-routing/init-under-machine-local-routing-provisions-only-the-store.toml
.espectacular/workspace-routing/linked-worktree-shares-the-slot.toml
.espectacular/workspace-routing/machine-local-routing-is-the-persistent-default.toml
.espectacular/workspace-routing/no-remote.toml
.espectacular/workspace-routing/pre-existing-global-store-knowledge-stays-servable.toml
.espectacular/workspace-routing/private-routing-flag.toml
.espectacular/workspace-routing/recall-serves-private-knowledge-locally.toml
.espectacular/workspace-routing/repo-local-remains-the-default-without-a-routing-key.toml
.espectacular/workspace-routing/ssh-remote.toml
.espectacular/workspace-routing/store-major-composition-order.toml
.espectacular/workspace-routing/the-private-zone-override-composes-over-the-declared-mode.toml
.espectacular/workspace-routing/unknown-routing-mode-is-rejected-with-the-valid-values.toml
.espectacular/workspace-routing/unknown-scope-rejected.toml
.genesis/tools.toml
.github/workflows/ci.yml
.github/workflows/docs.yml
.github/workflows/release.yml
.gitignore
.wai/.gitignore
.wai/AGENTS.md
.wai/PLUGINS.md
.wai/config.toml
.whisper/env.md
.whisper/env.usage.jsonl
AGENTS.md
CHANGELOG.md
CLAUDE.md
Cargo.lock
Cargo.toml
LICENSE
README.md
book.toml
docs/src/SUMMARY.md
docs/src/cli.md
docs/src/configuration.md
docs/src/getting-started.md
docs/src/index.md
docs/src/status.md
justfile
lefthook.yml
llm.txt
llms.txt
openspec/AGENTS.md
openspec/project.md
pretender-baseline.json
pretender.toml
scripts/update-homebrew.py
scripts/update-scoop.py
src/bundle.rs
src/cmds/admin.rs
src/cmds/knowledge.rs
src/cmds/mod.rs
src/cmds/support.rs
src/config.rs
src/distill.rs
src/doctor/checks.rs
src/doctor/content.rs
src/doctor/leaks.rs
src/doctor/managed.rs
src/doctor/mod.rs
src/doctor/routing.rs
src/doctor/tests.rs
src/entry.rs
src/lib.rs
src/main.rs
src/recall.rs
src/serving.rs
src/skill_pack.rs
src/usage.rs
src/workspace/block.rs
src/workspace/init.rs
src/workspace/layout.rs
src/workspace/mod.rs
src/workspace/resolve.rs
src/workspace/scope.rs
src/workspace/tests.rs
testaruda.toml
tests/bundle.rs
tests/cli/append.rs
tests/cli/common.rs
tests/cli/doctor.rs
tests/cli/feedback.rs
tests/cli/groups.rs
tests/cli/key.rs
tests/cli/layout_sync.rs
tests/cli/main.rs
tests/cli/resolve_routing.rs
tests/cli/zone.rs
tests/config.rs
tests/entry.rs
tests/genesis_compatibility.rs
tests/lifecycle/append.rs
tests/lifecycle/bundle.rs
tests/lifecycle/common.rs
tests/lifecycle/distill.rs
tests/lifecycle/distill_commit.rs
tests/lifecycle/main.rs
tests/lifecycle/recall.rs
tests/lifecycle/usage_doctor.rs
theme/charly.css
versions.ddl.toml

## Assistant

bash -lc printf '\n===== BAJAN README =====\n'; sed -n '1,240p' /tmp/after-chatbon/bajan-main/README.md; printf '\n===== BAJAN GRAPH MODEL SPEC =====\n'; sed -n '1,260p' /tmp/after-chatbon/bajan-main/specs/graph-model.md; printf '\n===== BAJAN INGESTION SPEC =====\n'; sed -n '1,240p' /tmp/after-chatbon/bajan-main/specs/ingestion-contract.md; printf '\n===== BAJAN QUERY SPEC =====\n'; sed -n '1,260p' /tmp/after-chatbon/bajan-main/specs/query-tools.md; printf '\n===== WHISPER README =====\n'; sed -n '1,260p' /tmp/after-chatbon/whisper-main/README.md; printf '\n===== WHISPER DISTILL =====\n'; sed -n '1,280p' /tmp/after-chatbon/whisper-main/src/distill.rs

## Tool

===== BAJAN README =====
# bajan

A spec-driven knowledge-graph pipeline CLI — ingest sources, extract claims,
query the graph. Rust, SQLite-backed triple store, provenance as graph
structure.

Encodes the best practices from
[`knowledge-graphs-report.md`](knowledge-graphs-report.md) as enforced,
lint-checked specifications (`specs/`, `openspec/`).

Part of the charly-vibes suite; emits suite-envelope JSON on every command.

## Status

**v0.1.0 — early release.** The deterministic pipeline is spec-complete and
CI-gated (specodelic lint, contract tests, property tests). The LLM
extraction path is smoke-tested against real providers at book scale but
young — see [Known limitations](#known-limitations) before relying on it.

## Install

```sh
cargo install --path .          # from a checkout — the bajan CLI only
cargo install bajan             # once published
```

Requires Rust 1.85+ (edition 2024). The source converters live in the
separate `converters/` crate and are built separately:

```sh
cargo build --release --manifest-path converters/Cargo.toml
# binaries land in converters/target/release/{epub,html,md,pdf}2bajan
```

## Data & state

Your whole graph is one SQLite file — **`bajan.db` in the current directory**
by default. Point every command at the same file (or a different one) with
the global `--db` flag: `bajan --db corpus.db extract`. Claims are referenced
by numeric **claim keys**, which appear in extract/query output — text mode
shows them as `#N` in the hit list.

## Workspace config (`bajan.toml`)

An optional strict settings file in the current directory tunes a workspace
without touching code. Flat `key = <integer>` lines and `#` comments only —
unknown keys, table headers, quotes, and non-integers are refused at startup
with a `config_parse` envelope and exit 1. Resolution order is **CLI flag >
file > built-in default**; no file is byte-identical default behavior.

```toml
# bajan.toml — workspace tuning (bajan-bku)
staleness_window_days = 90   # qt_ranking demotion window (default 365)
default_budget = 64          # bounded-traversal budget when --budget is absent (default 256)
max_attempts = 5             # LLM retry budget per episode per pass (default 3)
```

API keys never go in this file — the strict key set refuses anything but
these three keys; keys stay env-var-NAME based (`BAJAN_EXTRACTOR_*`). Config
is not store state: dump-recreate is unaffected.

## Quickstart

Every command writes a JSON suite envelope to stdout; add `--json` after the
subcommand for machine consumption (text mode renders the same envelope in a
short human form — same content, never a second format).

```sh
# 1. Convert a source into a normalized episode stream (JSON array)
converters/target/release/epub2bajan book.epub > episodes.json

# 2. Ingest — episodes persist verbatim, each gets an outcome record
bajan ingest < episodes.json

# 3. Extract claims (default: deterministic `atomic` extractor)
bajan extract

# or the LLM extractor (OpenAI-compatible endpoint):
# BAJAN_MAX_SPEND_USD is REQUIRED — without it the extractor refuses to
# run; when a call would push known spend past the cap, the pass stops
# (later episodes stay pending; rerun with a raised cap to resume).
# BAJAN_EXTRACTOR_TIMEOUT_SECS raises the per-call HTTP timeout from the
# 120s default — reasoning models under load exceed it (must be a
# positive integer; misconfiguration refuses at selection).
BAJAN_EXTRACTOR=llm \
BAJAN_EXTRACTOR_MODEL=deepseek/deepseek-v4-flash \
BAJAN_EXTRACTOR_BASE_URL=https://openrouter.ai/api/v1 \
BAJAN_EXTRACTOR_API_KEY_ENV=OPENROUTER_API_KEY \
BAJAN_MAX_SPEND_USD=0.50 \
BAJAN_EXTRACTOR_TIMEOUT_SECS=600 \
bajan extract

# 4. Human-in-the-loop adoption of staged claims
#    (claim keys come from the extract output / `bajan query` hit list)
bajan adopt 1 2 3

# 5. Episode deletion / revival — operator maintenance (ic_deleted_tombstone)
bajan delete <episode_id> --actor you   # refused while a claim supports the episode
bajan revive <episode_id> --actor you   # the only path that clears a tombstone
# A deleted id is retired: every later submission is rejected with the
# machine-readable deleted_id reason until revive — re-ingest never
# resurrects, and dump-recreate carries the tombstone across rebuilds.

# 6. Entity-review queue — the only human-only resolutions in the pipeline
bajan review list
bajan review approve <from> <to> --actor you   # merge a duplicate pair
bajan review reject <from> <to> --actor you    # drop the merge candidate

# 7. Query — ranked hits with lineage-traceable provenance
bajan query "profit" --scope workspace:dev
bajan query "profit" --json | jq '.data.hits'

# 8. Contradictions — closed rule set over specific claims, plus an
#    optional LLM proposal pass
bajan contradict 1 2
bajan scan                                     # deterministic contradicts pass
bajan propose            # LLM-assisted: stages proposals, never writes edges
bajan proposal list
bajan proposal approve <from> <to> --actor you  # writes the contradicts edge

# 9. Score an extraction run against a golden corpus (see
#    "Evaluating extraction quality" below; the adjudicated corpus
#    lives in evals/fixtures/gold-fi4e-v1.json)
bajan eval claims --corpus evals/fixtures/gold-fi4e-v1.json --run run.json
```

Concepts:

- **Episode** — a normalized span of source text with a locator and
  authority metadata; persisted verbatim, never rewritten.
- **Claim** — a claim node derived from episodes, staged until adopted;
  lineage edges make provenance part of the graph structure.
- **Envelope** — every command answers `{ok, envelope_version, envelope_kind,
  data}`; exit status mirrors `ok`.

## Evaluating extraction quality

`bajan eval claims` scores an extraction run against a **golden corpus** —
a versioned fixture of episodes whose true claim sets a human adjudicated
(`specs/eval-claims.md`). It publishes precision, recall, and hedge
preservation with raw counts, one per-case judgment per candidate. Scoring
is deterministic: no embeddings, no LLM judgment, no store access, no wall
clock — identical inputs reproduce byte-identical results, and an eval run
can never touch a real graph.

The golden corpus is a JSON file; every episode carries the claims the
text **should** yield. Constraints: the corpus `version` is required,
episode ids and claim texts/spans must be non-empty and unique, `source_count`
must be ≥ 1, and `hedges` may only use the anchored vocabulary `may, might,
could, possibly, appears, seems, signals, estimates, reportedly, tentative,
uncertain` (anything else is rejected):

```json
{
  "id": "gold-fi4e", "version": "1",
  "episodes": [{
    "id": "ep-1", "text": "Profits may vary by run.",
    "golden_claims": [{
      "text": "Profits may vary by run.", "source_count": 1,
      "evidence_span": "Profits may vary by run.", "hedges": ["may"]
    }]
  }]
}
```

The run manifest is the extraction output to score — candidates with their
evidence spans, stamped with the run and extractor identities. Export a real
manifest from a store with `bajan eval manifest` (bajan-t6z): it carries the
store's live candidates (staged and active claims) for the extractor version
you name, skipping unknown-evidence candidates and reporting the skip count.
With one extraction run in the store the version is picked automatically;
with several, `--extractor-version` selects one (the export refuses to mix
runs into one manifest). Text mode prints the bare manifest JSON so the
round trip is two commands, and `--out <file>` writes it directly:

```console
$ bajan eval manifest --db book.db --out run.json
$ bajan eval claims --corpus gold.json --run run.json
```

(The extract envelope itself still carries counts, not claims — the store is
the run record.) Candidate `episode_id`s must match corpus episode ids: the
published record counts candidates naming unknown episodes in
`unknown_episode_ids`, and scoring hard-refuses (`ok:false`, non-zero exit)
when **every** candidate references an unknown episode — a run scored
against the wrong corpus fails loudly instead of yielding plausible-looking
low num
...[truncated]...
 no distill)"));
    }
    let raw = std::fs::read_to_string(&target.path).map_err(WhisperError::from)?;
    let sha = entry::sha256_hex(&raw);
    let id = format!("{}-{}", ts.replace([':', '-'], ""), &sha[..8]);
    let rev_dir = revision_dir(target, &id)?;
    let snapshot_path = rev_dir.join("snapshot.md");
    let working_path = rev_dir.join("working.md");
    fs::write(&snapshot_path, &raw).map_err(WhisperError::from)?;
    write_revision_meta(&rev_dir, &id, target, &sha, &snapshot_path, &working_path)?;
    // Recency signal for the rewrite pass (empty map → omitted).
    let items = entry::parse_file(&raw);
    let recency = crate::usage::recency_for(&items, &target.path);
    let recency = (!recency.is_empty()).then_some(recency);
    Ok(Revision {
        id,
        snapshot_path,
        working_path,
        target_path: target.path.clone(),
        sha256: sha,
        recency,
    })
}

/// Create (or refuse to re-create) the immutable revision directory.
fn revision_dir(target: &Target, id: &str) -> Result<std::path::PathBuf> {
    let rev_dir = target.path.parent().unwrap().join("revisions").join(id);
    if rev_dir.exists() {
        return Err(
            WhisperError::new(format!("revision already exists: {}", rev_dir.display()))
                .with_suggestion(
                    "a distill cycle already began at this second — pass TURU_NOW or retry",
                ),
        );
    }
    fs::create_dir_all(&rev_dir).map_err(WhisperError::from)?;
    Ok(rev_dir)
}

/// Write meta.json: the agent rewrites `working.md`; commit verifies the
/// live file did not drift since this snapshot.
fn write_revision_meta(
    rev_dir: &std::path::Path,
    id: &str,
    target: &Target,
    sha: &str,
    snapshot_path: &std::path::Path,
    working_path: &std::path::Path,
) -> Result<()> {
    fs::write(
        rev_dir.join("meta.json"),
        json!({
            "revision": id,
            "target_path": target.path,
            "target_sha256": sha,
            "snapshot_path": snapshot_path,
            "working_path": working_path,
        })
        .to_string(),
    )
    .map_err(WhisperError::from)
}

fn load_meta(
    rev_dir: &std::path::Path,
) -> Result<(String, String, std::path::PathBuf, std::path::PathBuf)> {
    let raw = std::fs::read_to_string(rev_dir.join("meta.json")).map_err(|_| {
        WhisperError::new(format!(
            "missing revision metadata in {}",
            rev_dir.display()
        ))
        .with_suggestion("re-run `turu distill <scope> --begin`")
    })?;
    let meta: serde_json::Value = serde_json::from_str(&raw)
        .map_err(|e| WhisperError::new(format!("corrupt revision metadata: {e}")))?;
    Ok((
        meta["revision"].as_str().unwrap_or_default().to_string(),
        meta["target_sha256"]
            .as_str()
            .unwrap_or_default()
            .to_string(),
        meta["working_path"]
            .as_str()
            .map(std::path::PathBuf::from)
            .unwrap_or_default(),
        meta["snapshot_path"]
            .as_str()
            .map(std::path::PathBuf::from)
            .unwrap_or_default(),
    ))
}

/// `turu distill <scope> --commit --revision <id>`: install the distilled
/// output only if the live files are unchanged since `--begin`.
pub fn commit(target: &Target, revision: &str) -> Result<CommitReport> {
    let rev_dir = revision_dir_for_commit(target, revision)?;
    let (id, begin_sha, working_path, snapshot_path) = load_meta(&rev_dir)?;
    let committed_marker = rev_dir.join(".committed");
    let live = fs::read_to_string(&target.path).map_err(WhisperError::from)?;

    if let Some(report) = replay_report(
        &committed_marker,
        &live,
        target,
        id.clone(),
        snapshot_path.clone(),
    )? {
        return Ok(report);
    }
    check_drift(&live, &begin_sha)?;
    install(target, &working_path, &committed_marker)?;

    Ok(CommitReport {
        revision: id,
        replaced: target.path.clone(),
        snapshot_path,
        noop: false,
    })
}

/// Resolve + validate the revision directory for a commit.
fn revision_dir_for_commit(target: &Target, revision: &str) -> Result<std::path::PathBuf> {
    if !valid_revision_id(revision) {
        return Err(WhisperError::new(format!(
            "invalid revision id: {revision}"
        ))
        .with_suggestion(
            "revision ids look like 20260105T000000Z-1a2b3c4d — take them from the --begin envelope",
        ));
    }
    let rev_dir = target
        .path
        .parent()
        .unwrap()
        .join("revisions")
        .join(revision);
    if !rev_dir.exists() {
        return Err(
            WhisperError::new(format!("unknown revision: {revision}")).with_suggestion(
                "turu distill <scope> --begin first; revision ids are listed in its envelope",
            ),
        );
    }
    Ok(rev_dir)
}

/// Replay: a committed revision with an undrifted target is a no-op; a
/// committed revision with drift is refused (immutability).
#[allow(clippy::type_complexity)]
fn replay_report(
    committed_marker: &std::path::Path,
    live: &str,
    target: &Target,
    id: String,
    snapshot_path: std::path::PathBuf,
) -> Result<Option<CommitReport>> {
    if !committed_marker.exists() {
        return Ok(None);
    }
    let committed_sha = fs::read_to_string(committed_marker)
        .map_err(WhisperError::from)?
        .trim()
        .to_string();
    if entry::sha256_hex(live) == committed_sha {
        return Ok(Some(CommitReport {
            revision: id,
            replaced: target.path.clone(),
            snapshot_path,
            noop: true,
        }));
    }
    Err(
        WhisperError::new("revision is already committed and the target drifted since")
            .with_suggestion("run a new `turu distill <scope> --begin` cycle"),
    )
}

/// Conflict detection: live file must be byte-identical to --begin.
fn check_drift(live: &str, begin_sha: &str) -> Result<()> {
    let live_sha = entry::sha256_hex(live);
    if live_sha != begin_sha {
        return Err(WhisperError::new(format!(
            "scope file changed since --begin (concurrent write?) — expected sha {}, live {}",
            &begin_sha[..12],
            &live_sha[..12]
        ))
        .with_suggestion("re-run `turu distill <scope> --begin` and redo the rewrite"));
    }
    Ok(())
}

/// Install the distilled working file: mark it committed, then atomically
/// rename it over the live scope file (same filesystem).
fn install(
    target: &Target,
    working_path: &std::path::Path,
    committed_marker: &std::path::Path,
) -> Result<()> {
    let distilled = fs::read_to_string(working_path).map_err(|_| {
        WhisperError::new(format!(
            "working file not written: {}",
            working_path.display()
        ))
        .with_suggestion(format!(
            "write the distilled content to {} then re-run --commit",
            working_path.display()
        ))
    })?;
    let distilled_sha = entry::sha256_hex(&distilled);
    fs::write(committed_marker, &distilled_sha).map_err(WhisperError::from)?;
    // Atomic install: same filesystem, rename replaces the live file.
    fs::rename(working_path, &target.path).map_err(WhisperError::from)
}

/// Strict revision-id grammar: `<compact-timestamp>-<8 hex>` — also closes
/// path traversal via a crafted --revision.
fn valid_revision_id(rev: &str) -> bool {
    let Some((ts, hash)) = rev.split_once('-') else {
        return false;
    };
    !ts.is_empty()
        && ts.chars().all(|c| c.is_ascii_alphanumeric())
        && hash.len() == 8
        && hash.chars().all(|c| c.is_ascii_hexdigit())
}

/// Doctor helper: revisions begun but not committed (informational).
pub fn pending_revisions(target_dir: &std::path::Path) -> Vec<String> {
    let rev_root = target_dir.join("revisions");
    let Ok(entries) = fs::read_dir(&rev_root) else {
        return Vec::new();
    };
    let mut pending = Vec::new();
    for e in entries.flatten() {
        let dir = e.path();
        if dir.is_dir() && dir.join("meta.json").exists() && !dir.join(".committed").exists() {

## Assistant

bash -lc printf '\n===== WHISPER README (1-240) =====\n'; sed -n '1,240p' /tmp/after-chatbon/whisper-main/README.md; printf '\n===== BAJAN SPECS INDEX =====\n'; for f in /tmp/after-chatbon/bajan-main/specs/*.md; do echo "--- $(basename "$f")"; sed -n '1,170p' "$f"; done; printf '\n===== BAJAN MODULE HEADERS =====\n'; for f in /tmp/after-chatbon/bajan-main/src/*.rs; do echo "--- $(basename "$f")"; grep -nE '^(pub )?(async )?fn |^pub (struct|enum|trait|mod)|^struct |^enum |^trait ' "$f" | head -70; done; printf '\n===== WHISPER MODULE HEADERS =====\n'; for f in /tmp/after-chatbon/whisper-main/src/*.rs /tmp/after-chatbon/whisper-main/src/cmds/*.rs; do echo "--- ${f#/tmp/after-chatbon/whisper-main/}"; grep -nE '^(pub )?(async )?fn |^pub (struct|enum|trait|mod)|^struct |^enum |^trait ' "$f" | head -80; done

## Tool

===== WHISPER README (1-240) =====
> *"Time can never mend*
> *The careless whispers of a good friend*
> *To the heart and mind, ignorance is kind*
> *There's no comfort in the truth, pain is all you'll find"*
> — George Michael, *Careless Whisper*

# whisper

`whisper` is a Rust CLI that makes the [incitaciones](https://github.com/charly-vibes/incitaciones) `whisper` skill deterministic.

The whisper skill asks an agent to manage `~/.whisper/` — canonical repo keys, branch slugs, worktree slots, and scope-based knowledge routing — by hand-rolling shell pipelines. Every invocation is a fresh chance for the model to mis-derive a path. This tool turns that mechanical layer into a binary: the skill prompts call the CLI, and the same inputs always produce the same outputs.

**The command is `turu`** — following the song's *turututu* riff. `turututu` and `whisper` run as aliases, so existing scripts and skill prompts keep working.

Part of the [charly-vibes](https://github.com/charly-vibes) tool suite; built on [genesis-vibes](https://github.com/charly-vibes/genesis) for the JSON envelope, config, and CLI conventions shared across the family.

> **Why:** agents accumulate operational knowledge across sessions, but "where does
> this note go?" is a question models answer unreliably by hand-rolling shell
> pipelines over `~/.whisper/` — every invocation is a fresh chance to mis-derive
> a canonical repo key or scope path. `turu` turns that mechanical layer into a
> deterministic binary: same inputs, same outputs, every machine.
> **Status:** [beta](docs/src/status.md) · core key/resolve/append/recall/distill shipped and used by other ecosystem tools · [Motivation & design](docs/src/index.md) · [charly-vibes Tool Ecosystem](https://charly-vibes.github.io/dulce-de-leche/ecosystem-map.html)
## What it does

- `turu key` — canonical repo key, branch slug, and worktree slot for the current checkout (the pure determinism core)
- `turu resolve <scope>` — the exact destination path for a knowledge scope: `global`, `repo`, `branch`, `worktree`, or `group`
- `turu append <scope> --text "..." [--topic k] [--supersedes id]` — structured, idempotent entries (sha2 ids over scope + second-precision UTC + text) written into the right file; freeform content preserved verbatim
- `turu recall <scope> [--topic k] [--budget bytes] [--include-superseded]` — ranked, budget-bounded slice serving (`all` composes scopes in precedence order); the envelope reports the context-horizon boundary (`served_bytes`, `budget_unused`, `entries_skipped`)
- `turu distill <scope> --begin|--commit --revision id` — two-phase contract: turu snapshots into immutable revisions and guards the commit against concurrent drift; the calling agent does the semantic rewrite into the working file
- `turu bundle pack|unpack` — deterministic, transport-agnostic knowledge bundles keyed by repo key; unpack merges extend-without-duplicate and never overwrites
- `turu init` — create the workspace layout
- `turu status` — one envelope with every relevant path and existence flag
- `turu check` — detect legacy key variants, undefined groups, missing files
- `turu doctor` — deep diagnostics: layout integrity, group health, legacy keys, managed block, skill pack staleness
- `turu sync` — inject the deterministic routing map into `AGENTS.md` as a `<!-- TURU:START -->` managed block, so agents read paths from a file instead of re-deriving them
- `turu feedback <kind>` — file a well-contexted GitHub issue (`bug`, `feature`, `question`, `chore`): redacted context bundle, optional `--from-last-error` scratch recall, `--dry-run` preview (via `genesis::feedback`)
- `turu skill install` — ship the whisper skill from this repo: router + sub-skills (including manual fallbacks), content-hashed so `turu doctor` flags staleness. Targets `~/.claude/skills` or any dir; incitaciones keeps a thin pointer to it

## Install

### Binary (curl)

```bash
V=$(basename "$(curl -fsSLI -o /dev/null -w '%{url_effective}' \
  https://github.com/charly-vibes/whisper/releases/latest)" | sed 's/^v//')
TGT="$(uname -s | tr '[:upper:]' '[:lower:]')_$(uname -m | sed 's/^x86_64$/amd64/; s/^aarch64$/arm64/')"
curl -fsSL "https://github.com/charly-vibes/whisper/releases/download/v${V}/turu_${V}_${TGT}.tar.gz" | tar xz
chmod +x turu turututu whisper && sudo mv turu turututu whisper /usr/local/bin/
```

### Cargo

```bash
cargo install whisper-vibes
```

Or from source:

```bash
git clone git@cv:charly-vibes/whisper.git && cd whisper && just install
```

## Configuration

Where knowledge gets written is layered. Precedence: **repo > group > global**.

**Global** — `~/.config/whisper/config.toml`:

```toml
workspace_root = "~/.whisper"   # default

[groups.cv-tools]
root = "~/para/areas/dev/gh/charly/knowledge"
repos = ["cv/charly-vibes/whisper"]   # explicit membership (optional)
```

A **group** routes knowledge from a set of repos into one shared workspace directory instead of each repo's private slot.

**Repo (private)** — `<repo>/.whisper/config.toml` (gitignored — never committed):

```toml
group = "cv-tools"              # join a group defined in the global config
workspace_root = "/path/to/dir" # or fully override the workspace root
```

A repo can join a group two ways: privately, via its own `.whisper/config.toml`, or centrally, by listing its canonical key in the group's `repos` array.

> **Note:** a repo-private `workspace_root` overrides *everything* — including the global scope, so the repo's `rules.md` resolves inside the private root instead of the shared workspace. `turu doctor` reports this shadowing and warns when the two `rules.md` files diverge. A relative `workspace_root` is anchored to the directory containing the repo config (not the process cwd), so calls from any subdirectory resolve to the same root.

## Knowledge transport & the private zone

Where knowledge lives depends on the scope and where the command runs:

| Scope | In a checkout (default) | `--global` escape hatch |
|---|---|---|
| `repo` | `<repo>/.whisper/env.md` (committed) | `<workspace>/repos/<key>/env.md` |
| `branch` | `<repo>/.whisper/branches/<slug>/notes.md` (committed) | `<workspace>/repos/<key>/branches/<slug>/notes.md` |
| `--private` repo/branch | `<repo>/.whisper/private/…` — **gitignored, never pushed** | — |

Transport decision: the repo's own git carries the shared knowledge. Repo-local
publication assumes a pushable checkout — `--global` is the fallback for
read-only checkouts (CI, no-push contributors).

Machine-specific knowledge (local paths, hostnames, credentials) belongs in the
**private zone**: `turu append <scope> --private` routes into
`<repo>/.whisper/private/`, which `turu init`/`turu sync` keep effectively
ignored — the rule is appended to the root `.gitignore` only when
`git check-ignore` does not already report the path (text presence is not the
truth; a nested `.gitignore` or your global excludes file counts).

`turu doctor` enforces the privacy contract with three checks:

- `turu.private-ignore` — the zone is *effectively* ignored (warning + fix hint otherwise)
- `turu.private-tracked` — **fails prominently** if any file under `private/` is tracked
- `turu.private-leaks` — advisory lint for machine paths, hostnames, and token-shaped strings in public repo-local files (surfaces via `warnings[]`)

git history is forever — prevention only. No turu verb can retract committed
knowledge; that is exactly why the private zone exists and why the tracked-files
check fails instead of warning.

## Skill integration

The distilled whisper skill in incitantes replaces its shell-snippet procedures with:

```
turu key        # derive repo key / branch slug / worktree slot
turu resolve branch
turu append repo --text "deploy requires vault login"
turu recall repo --topic deploy --budget 400   # slice, newest first, boundary reported
```

Agents in any repo with a `TURU` managed block read the routing map straight from `AGENTS.md` — no prompt bookkeeping required. `turu sync` refreshes the block; `turu doctor` flags it when it drifts.

Determinism guarantee: canonical
...[truncated]...
_with_window(
267:pub fn search_scoped(
278:fn search_inner(
405:pub struct BajanQueryError(pub String);
411:pub struct ContradictionSide {
423:pub struct ContradictionPair {
434:pub struct StagedInvalidation {
448:pub struct ContradictionResult {
475:pub fn contradictions(
--- resolve.rs
29:pub struct IdentityRecord {
42:pub struct ResolutionReport {
50:pub fn resolve(db: &SqliteStore) -> Result<ResolutionReport, BajanError> {
84:pub fn restage(
--- review.rs
23:pub fn normalize(text: &str) -> String {
35:pub struct ErReport {
74:pub fn run_er_pass(db: &SqliteStore, budget: usize, now: u64) -> Result<ErReport, BajanQueryError> {

===== WHISPER MODULE HEADERS =====
--- src/bundle.rs
18:pub struct Bundle {
29:pub fn pack(
61:fn assemble_bundle(
76:fn read_scope_items(path: &std::path::Path) -> (Vec<Entry>, Vec<String>) {
91:fn pack_to_file(bundle: &Bundle, path: &str, private_excluded: usize) -> Result<serde_json::Value> {
112:fn pack_inline(bundle: &Bundle, private_excluded: usize) -> Result<serde_json::Value> {
128:pub fn unpack(input: &str, facts: &Facts, resolved: &Resolved) -> Result<serde_json::Value> {
148:fn private_skip_report(path: &std::path::Path, bundle: &Bundle) -> serde_json::Value {
161:fn merge_bundle(bundle: &Bundle, path: &std::path::Path) -> Result<serde_json::Value> {
188:fn bundle_items(bundle: &Bundle) -> impl Iterator<Item = Item> + '_ {
198:fn append_item(items: &mut Vec<Item>, item: Item) -> bool {
215:fn private_zone_item_count(scope: Scope, facts: &Facts, resolved: &Resolved) -> usize {
231:fn scope_name(scope: Scope) -> &'static str {
242:pub fn read_input(file: Option<&str>, stdin: bool) -> Result<String> {
--- src/config.rs
20:pub struct GlobalConfig {
31:pub struct GroupConfig {
42:pub struct RepoConfig {
60:pub enum Routing {
89:pub struct Resolved {
115:pub fn global_path() -> PathBuf {
123:fn home_dir() -> PathBuf {
130:pub fn expand_tilde(path: &str) -> PathBuf {
142:pub fn find_repo_config(start: &Path) -> Option<(PathBuf, RepoConfig)> {
162:pub fn load(cwd: &Path, repo_key: &str) -> Result<Resolved> {
191:fn load_global() -> Result<GlobalConfig> {
200:fn global_default_root() -> Result<PathBuf> {
213:fn routing_of(repo_cfg: &Option<RepoConfig>) -> Result<Routing> {
223:fn resolve_group(
258:fn private_root_override(
--- src/distill.rs
15:pub struct Revision {
29:pub struct CommitReport {
39:pub fn begin(target: &Target, ts: &str) -> Result<Revision> {
70:fn revision_dir(target: &Target, id: &str) -> Result<std::path::PathBuf> {
86:fn write_revision_meta(
108:fn load_meta(
139:pub fn commit(target: &Target, revision: &str) -> Result<CommitReport> {
166:fn revision_dir_for_commit(target: &Target, revision: &str) -> Result<std::path::PathBuf> {
194:fn replay_report(
223:fn check_drift(live: &str, begin_sha: &str) -> Result<()> {
238:fn install(
261:fn valid_revision_id(rev: &str) -> bool {
272:pub fn pending_revisions(target_dir: &std::path::Path) -> Vec<String> {
293:pub fn begin_for_scope(
303:pub fn commit_for_scope(
--- src/entry.rs
20:pub fn ts_format() -> format_description::FormatItem<'static> {
26:pub fn parse_or_now(override_ts: Option<&str>) -> Result<String> {
44:pub fn sha256_hex(s: &str) -> String {
59:pub fn entry_id(scope_key: &str, ts: &str, text: &str) -> String {
65:pub struct Entry {
103:pub enum Item {
113:fn strip_marker(text: &str, marker: &str) -> (String, Option<String>) {
126:pub fn parse_entry_line(line: &str) -> Option<Entry> {
158:pub fn parse_file(raw: &str) -> Vec<Item> {
183:pub fn render_file(items: &[Item]) -> String {
201:pub fn entry_ids(items: &[Item]) -> Vec<&str> {
223:pub fn incident_log_density(text: &str) -> Option<String> {
240:fn is_date_like(tok: &str) -> bool {
253:fn is_id_like(tok: &str) -> bool {
263:fn is_issue_ref(tok: &str) -> bool {
--- src/lib.rs
11:pub mod bundle;
12:pub mod config;
13:pub mod distill;
14:pub mod doctor;
15:pub mod entry;
16:pub mod recall;
17:pub mod serving;
18:pub mod skill_pack;
19:pub mod usage;
20:pub mod workspace;
30:pub struct WhisperError {
--- src/main.rs
32:struct Cli {
204:fn main() {
213:fn run(cli: Cli) -> i32 {
240:fn scratch_timestamp() -> String {
244:fn emit_ok<T: serde::Serialize + std::fmt::Debug>(output: &Output<T>) -> i32 {
248:fn emit_err(output: &Output<String>) -> i32 {
254:fn emit<T: serde::Serialize + std::fmt::Debug>(output: &Output<T>, success: bool) -> i32 {
--- src/recall.rs
23:pub enum RecallScope {
28:pub fn parse_recall_scope(s: &str) -> Result<RecallScope> {
38:pub struct Served {
46:pub struct ServedLine {
59:struct Store {
73:fn stores_for(recall: &RecallScope, facts: &Facts, resolved: &Resolved) -> Result<Vec<Store>> {
103:fn store_path(scope: Scope, facts: &Facts, resolved: &Resolved) -> Result<std::path::PathBuf> {
111:fn all_scope_stores(
141:fn repo_file(scope: Scope, facts: &Facts) -> std::path::PathBuf {
155:fn private_file(scope: Scope, facts: &Facts) -> std::path::PathBuf {
170:fn checkout_stores(scope: Scope, facts: &Facts) -> Vec<Store> {
187:pub struct RecallQuery {
205:fn serve_stores(
220:fn serve_one_store(
251:fn rank_store(raw: &str, query: &RecallQuery) -> (Vec<entry::Entry>, Vec<String>) {
279:pub fn recall(
311:fn insert_payload(m: &mut serde_json::Map<String, Value>, query: &RecallQuery, acc: &Acc) {
322:fn scope_label(recall_scope: &RecallScope) -> String {
331:fn render(
--- src/serving.rs
--- src/skill_pack.rs
15:pub enum PackState {
32:pub struct PackHealth {
39:pub fn generate_pack(pack_name: &str) -> Result<PackFiles, String> {
47:pub fn pack_content_hash(files: &PackFiles) -> String {
58:pub fn disk_content_hash(dir: &Path) -> io::Result<String> {
63:fn read_dir_files(dir: &Path) -> io::Result<PackFiles> {
69:fn collect_files(base: &Path, current: &Path, out: &mut PackFiles) -> io::Result<()> {
91:fn generate_whisper() -> PackFiles {
171:fn sub(name: &str, description: &str, protocol: &str) -> String {
177:fn sub_fallback(name: &str, description: &str, protocol: &str) -> String {
181:fn router_skill() -> String {
--- src/usage.rs
22:pub struct Record {
29:pub struct Stats {
40:pub fn staleness(entry_ts: &str, stats: Option<&Stats>, now: &str) -> Staleness {
68:pub enum Staleness {
75:pub fn recency_for(items: &[entry::Item], scope_file: &std::path::Path) -> BTreeMap<String, Stats> {
85:pub fn sidecar_path(scope_file: &std::path::Path) -> std::path::PathBuf {
91:pub fn append(scope_file: &std::path::Path, ids: &[String], ts: &str) -> Result<usize> {
125:pub fn read_stats(scope_file: &std::path::Path) -> BTreeMap<String, Stats> {
--- src/cmds/admin.rs
66:fn render_feedback(result: genesis::feedback::gh::GhResult) -> Arm {
--- src/cmds/knowledge.rs
42:fn append_data(target: &workspace::Target, report: &workspace::AppendReport) -> serde_json::Value {
54:fn append_warnings(text: &str) -> Vec<String> {
59:fn append_hint(report: &workspace::AppendReport) -> Option<String> {
116:fn distill_begin(ctx: &Ctx, scope: workspace::Scope) -> whisper::Result<Arm> {
141:fn distill_commit(
176:fn append_recall_arm(cli: &Cli, ctx: &Ctx) -> whisper::Result<Option<Arm>> {
184:fn append_arm(cli: &Cli, ctx: &Ctx) -> whisper::Result<Option<Arm>> {
211:fn recall_arm(cli: &Cli, ctx: &Ctx) -> whisper::Result<Option<Arm>> {
234:fn distill_arm(cli: &Cli, ctx: &Ctx) -> whisper::Result<Option<Arm>> {
254:fn empty_scope_warnings(data: &serde_json::Value) -> Vec<String> {
264:fn snapshot_lint(snapshot_path: &std::path::Path) -> Vec<String> {
278:fn reject_empty(text: &str) -> whisper::Result<()> {
--- src/cmds/mod.rs
55:fn pick(cli: &Cli, ctx: &Ctx) -> whisper::Result<Arm> {
76:fn init_arm(cli: &Cli, ctx: &Ctx) -> whisper::Result<Option<Arm>> {
87:fn admin_arm(cli: &Cli, ctx: &Ctx) -> whisper::Result<Arm> {
103:fn key(ctx: &Ctx) -> whisper::Result<Arm> {
117:fn resolve(
138:fn bundle_cmd(ctx: &Ctx, command: &BundleCommand) -> whisper::Result<Arm> {
161:fn init(ctx: &Ctx) -> whisper::Result<Arm> {
176:fn status(ctx: &Ctx) -> whisper::Result<Arm> {
192:fn check(ctx: &Ctx) -> whisper::Result<Arm> {
222:fn check_warnings(ctx: &Ctx) -> Vec<String> {
246:fn consolidate(ctx: &Ctx) -> whisper::Result<Arm> {
--- src/cmds/support.rs
48:fn global_target(
157:fn read_stdin() -> whisper::Result<String> {

## Assistant

bash -lc printf '\n===== BAJAN EXTRACT =====\n'; sed -n '1,320p' /tmp/after-chatbon/bajan-main/src/extract.rs; printf '\n===== BAJAN INGEST =====\n'; sed -n '1,300p' /tmp/after-chatbon/bajan-main/src/ingest.rs; printf '\n===== BAJAN STORE STRUCTURES =====\n'; grep -nE 'CREATE TABLE|pub struct SqliteStore|pub fn |fn ' /tmp/after-chatbon/bajan-main/src/store.rs | head -180; printf '\n===== BAJAN EXTRACTION TESTS =====\n'; sed -n '1,260p' /tmp/after-chatbon/bajan-main/tests/extractor_seam.rs; printf '\n===== BAJAN GOLDEN EVAL TESTS =====\n'; sed -n '1,240p' /tmp/after-chatbon/bajan-main/specs/eval-claims.md; printf '\n===== WHISPER DISTILL CONTRACT DOC =====\n'; grep -RniE 'distill|snapshot|revision|drift|rewrite' /tmp/after-chatbon/whisper-main/docs/src /tmp/after-chatbon/whisper-main/AGENTS.md | head -100;

## Tool

===== BAJAN EXTRACT =====
//! Purpose: extraction module — propose candidate claims typed against the
//! published claim schema, with lineage edges to their source episode.
//! Responsibilities: boundary between persisted episodes and proposed
//! claims; claim-schema conformance at the typed gate.
//! Rationale: governed by specs/extraction-claims.md; this scaffold ships
//! the module seam only (bajan-2xv), behavior arrives with the gated
//! implementation tickets.

use crate::cli::BajanError;
use crate::ingest::EpisodeRecord;
use crate::store::{ClaimNode, Evidence, Lineage};
use serde::{Deserialize, Serialize};
use unicode_segmentation::UnicodeSegmentation;

#[cfg(test)]
use proptest::prelude::*;

pub const SPEC: &str = "specs/extraction-claims.md";

/// The class of an extractor failure (bajan-gso): timeout vs HTTP
/// status vs generic transport vs schema-decode — diagnosable from the
/// report without reproducing the call. Carried on park reasons and
/// `Exhausted` failures; never on claim nodes.
#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
#[serde(tag = "kind", rename_all = "snake_case")]
pub enum FailureClass {
    /// The configured transport timeout elapsed.
    Timeout,
    /// The provider returned an HTTP error status.
    HttpStatus { code: u16 },
    /// Any other transport-level error (connection refused, DNS, auth
    /// plumbing).
    Transport,
    /// The response body did not decode against the published schema.
    Schema,
}

impl FailureClass {
    /// Stable machine-readable code for the text render (gso).
    pub fn code(&self) -> String {
        match self {
            FailureClass::Timeout => "timeout".into(),
            FailureClass::HttpStatus { code } => format!("http-{code}"),
            FailureClass::Transport => "transport".into(),
            FailureClass::Schema => "schema".into(),
        }
    }
}

impl std::fmt::Display for FailureClass {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        f.write_str(&self.code())
    }
}

/// Machine-readable reason for a failure outcome (`ex_run_record`).
///
/// Reasons are stable snake_case codes stored on the run or rejection
/// record — never on a claim node (`gm_schema_v2` field list stays
/// closed). Each variant names the invariant that produces it.
#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
#[serde(tag = "code", rename_all = "snake_case")]
pub enum Reason {
    /// Episode parked in `rejected` after repeated call failure
    /// (`ex_single_call`). Carries the attempt count and the failure
    /// class of the last error (bajan-gso).
    RepeatedCallFailure { attempts: u32, class: FailureClass },
    /// Candidate rejected at the validation gate because its evidence span
    /// fails whitespace-collapsed containment (`ex_evidence_containment`,
    /// enforced from bajan-0hs.7).
    EvidenceNotContained,
    /// Candidate rejected because persisting it would drop hedge marker(s)
    /// present in the supporting episode text (`gm_hedge_anchor`).
    HedgeMarkerDropped,
    /// Prior-version `staged` claim tombstoned by a version-bump
    /// re-extraction (`ex_supersession`). Carried on the supersession
    /// record in the claim store — never on the claim node.
    SupersededByReextraction,
    /// Every candidate refused by the deterministic section-kind filter
    /// (`ex_section_filter`): the episode's tags include a non-knowledge
    /// section kind. Carries the offending tag.
    SectionFiltered { tag: String },
}

impl Reason {
    /// Stable machine-readable snake_case code.
    pub fn code(&self) -> &'static str {
        match self {
            Reason::RepeatedCallFailure { .. } => "repeated_call_failure",
            Reason::EvidenceNotContained => "evidence_not_contained",
            Reason::HedgeMarkerDropped => "hedge_marker_dropped",
            Reason::SupersededByReextraction => "superseded_by_reextraction",
            Reason::SectionFiltered { .. } => "section_filtered",
        }
    }
}

/// Finish status of an extraction call (`ex_run_record`).
///
/// Failure outcomes carry their machine-readable reason structurally — a
/// parked or gate-rejected run cannot exist without one.
#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
#[serde(tag = "status", rename_all = "snake_case")]
pub enum Finish {
    /// Call succeeded; candidates reached the gate outcome.
    Succeeded,
    /// Episode parked in `rejected` after repeated call failure
    /// (`ex_single_call` abort path).
    Parked { reason: Reason },
    /// Call succeeded but candidates were refused at the gate
    /// (`ex_typed_gate` refuse path).
    GateRejected { reason: Reason },
}

/// One run row per extraction call (`ex_run_record`): episode id,
/// extractor version, model id when the extractor uses an LLM, started
/// and finished timestamps (epoch millis), and finish status. Parallel
/// to — and without changing — the `(episode id, extractor version)`
/// cache economics: rows are additive telemetry, never cache entries.
#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct ExtractionRun {
    pub episode_id: String,
    pub extractor_version: String,
    pub model_id: Option<String>,
    pub started_at: u64,
    pub finished_at: u64,
    pub finish: Finish,
}

/// The run-record store: append-only, one row per extraction call
/// (`ex_run_record`). Parallel to the `(episode id, extractor version)`
/// cache — recording a run never creates, invalidates, or reuses a cache
/// entry.
#[derive(Debug, Default, Clone)]
pub struct ExtractionRunStore {
    rows: Vec<ExtractionRun>,
}

impl ExtractionRunStore {
    /// Record exactly one run row for one extraction call.
    pub fn record(&mut self, run: ExtractionRun) {
        self.rows.push(run);
    }

    pub fn rows(&self) -> std::slice::Iter<'_, ExtractionRun> {
        self.rows.iter()
    }
}

/// One park outcome on the report (`ex_single_call` abort path): the
/// parked episode and its machine-readable reason — repeated call
/// failure after the extractor's retry budget was exhausted.
#[derive(Debug, Clone, PartialEq, Eq, Serialize)]
pub struct ParkedEpisode {
    pub episode_id: String,
    pub reason: Reason,
}

/// One gate refusal on the report (`ex_typed_gate` refuse path): the
/// refused episode and its machine-readable reason (`ex_run_record` —
/// reasons live on rejection records, never on claim nodes).
#[derive(Debug, Clone, PartialEq, Eq, Serialize)]
pub struct GateRejection {
    pub episode_id: String,
    pub reason: Reason,
}

/// One candidate claim proposed by an extractor — exactly the fields an
/// extractor may set: claim text, temporal bounds, and typed evidence.
/// Status, scope, source type, data cutoff, and lineage are NOT the
/// extractor's business — the pipeline projects them from the episode
/// record and its configuration (`gm_schema_v2` stays closed; extractors
/// never fabricate metadata they cannot know).
#[derive(Debug, Clone, PartialEq, Eq)]
pub struct CandidateClaim {
    pub text: String,
    pub valid_at: Option<String>,
    pub invalid_at: Option<String>,
    pub evidence: Evidence,
}

/// Why an extractor failed to propose for one episode.
/// Infrastructure failures (network, auth, malformed provider response)
/// are NOT gate rejections — they fail the run honestly (`ex_run_record`
/// class separation, bajan-r1h discipline).
#[derive(Debug, Clone, PartialEq, thiserror::Error)]
pub enum ExtractionFailure {
    /// The extractor could not complete its call. Propagates — the run
    /// fails; the episode stays pending and retryable.
    #[error("extraction infrastructure failure: {0}")]
    Infrastructure(String),
    /// The extractor exhausted its retry budget (`ex_single_call`
    /// repeated-failure abort). The PIPELINE parks the episode: run row
    /// `Parked` with reason `repeated_call_failure`, report entry, no
    /// cache entry — the next pass re-attempts with a fresh budget
    /// (`ex_park_requeue`).
    #[error("extraction retry budget exhausted after {attempts} attempt
...[truncated]...
4.6). So bajan publishes its own numbers.

Discipline: golden-file corpora carry known source counts N (the
`p_reified` generator contract from `graph.model`), so recall is
computable without judging prose. Scoring is deterministic — a candidate
matches a golden claim only on content equivalence (normalized text
overlap) plus evidence-span containment into the corpus episode, never
on embedding similarity or LLM judgment. Hedge preservation is scored
explicitly: a candidate that drops a hedge marker present in its
supporting episode is a precision failure even when the content matches
(`gm_hedge_anchor` made checkable). Eval results are checked into the
repo (`evals/results.md`) as the decision artifact for storage-stack
choices — the record that decides "keep SQLite vs earn a graph DB" is a
table of numbers with the corpus, extractor version, and date that
produced them, reproducible by command. A eval run is read-only over
the store: it seeds its own corpus fixture and never mutates a real
graph — evaluation runs the same pipeline stages (ingest → extract →
gate) but into a scratch store, so evals can never contaminate adopted
knowledge (adoption stays human-only per `gm_human_adopt`).

## Constraints

| id | kind | expr | traces_to | satisfies |
|----|------|------|-----------|-----------|
| ev_golden_corpus | invariant | a golden corpus is a versioned fixture of episodes where every episode carries a known claim set — each golden claim listing its source count N (the `p_reified` contract), its evidence span within the episode text, and its hedge markers; the corpus version is stamped on every eval run record | [[eval.claims]] | |
| ev_deterministic_scoring | invariant | scoring maps a candidate claim to a golden claim only when normalized text content matches and the candidate's evidence span passes the same whitespace-collapsed containment check as `ex_evidence_containment`; identical inputs (corpus version, extractor version, seed) produce byte-identical scores — no embedding similarity and no LLM judgment anywhere in scoring | [[eval.claims]] | [[extraction.claims.ex_output_schema]] |
| ev_precision_recall | invariant | every eval run publishes precision (matched candidates / emitted candidates), recall (matched golden claims / total golden claims), and the hedge-preservation rate, computed per corpus and per extractor version, plus raw match counts so the ratios are recomputable; an eval run emits exactly one results record per (corpus version, extractor version) pair | [[eval.claims]] | |
| ev_hedge_scoring | invariant | a candidate whose evidence span or text drops a hedge marker present in the supporting golden episode within the span's coverage scores as a precision failure with reason `hedge-dropped`, distinct from a content miss, so hedge fidelity is a first-class reported number per `gm_hedge_anchor` | [[eval.claims]] | |
| ev_readonly | invariant | an eval run writes only to its own scratch store and results record — it never mutates episodes, claims, or audit records of a real store, and it never moves any claim toward `active`; the only automated state the harness can produce is the pipeline's own `staged`/`rejected` outcomes inside the scratch store, adoption remains human-only per `gm_human_adopt` | [[eval.claims]] | |
| ev_results_checked_in | invariant | eval results persist as a checked-in `evals/results.md` table — corpus version, extractor version, date, precision, recall, hedge-preservation rate, raw counts — and regenerating from the same inputs reproduces the same row values, making the storage-stack decision (keep SQLite vs earn a graph DB) auditable to its numbers | [[eval.claims]] | |
| ev_results-schema | extension_point | the eval results record schema (fields, types, requiredness, including the match-record and reason vocabulary `matched`, `content-miss`, `spurious`, `hedge-dropped`) is published for reporting specs to conform to | [[eval.claims]] | |

## Model

### States

- `ready`
- `ran`
- `published`

### Transitions

| id | from | to | guard |
|----|------|----|-------|
| execute | ready | ran | [[eval.claims.ev_golden_corpus]] |
| score | ran | published | [[eval.claims.ev_deterministic_scoring]] |

## Properties

| id | kind | derives_from | generator | predicate |
|----|------|--------------|-----------|-----------|
| p_golden_corpus | unit | [[eval.claims.ev_golden_corpus]] | golden corpora with episodes carrying zero to many golden claims, varied source counts N in 1..4, and mixed hedge markers | every episode in a loaded corpus exposes its full golden claim set with source counts, evidence spans, and hedge markers; a corpus without a version is rejected |
| p_deterministic_scoring | unit | [[eval.claims.ev_deterministic_scoring]] | candidate sets replayed twice against the same corpus version, containing matches, near-miss paraphrases, span-violating candidates, and duplicates | replayed runs produce identical match assignments; paraphrases without content equivalence score as misses; span-violating candidates never match; no scoring call depends on wall-clock, randomness, or network |
| p_precision_recall | unit | [[eval.claims.ev_precision_recall]] | candidate sets with known true-positive, false-positive, and false-negative counts over a seeded corpus | published precision equals matched/emitted and recall equals matched/golden exactly for the seeded counts; raw counts accompany every ratio; one results record per (corpus version, extractor version) |
| p_hedge_scoring | unit | [[eval.claims.ev_hedge_scoring]] | candidates matching golden content with dropped, preserved, and added hedge markers | hedge-dropping candidates are precision failures with reason `hedge-dropped`, never plain matches; hedge preservation rate equals preserved-hedge matches over hedge-bearing golden claims |
| p_readonly | unit | [[eval.claims.ev_readonly]] | eval runs executed against stores pre-seeded with adopted claims and audit records | after any eval run the real store's claims, statuses, and audit records are unchanged; no claim reaches `active` from an automated path; the scratch store is the only mutated store |
| p_results_checked_in | unit | [[eval.claims.ev_results_checked_in]] | repeated eval runs at fixed corpus and extractor versions, and runs at bumped versions | reruns at identical versions reproduce identical row values in `evals/results.md`; version bumps append new rows without mutating prior ones |
| p_results-schema | unit | [[eval.claims.ev_results-schema]] | results records sampled from the published schema | every published results record validates against the published schema with the closed reason vocabulary |

===== WHISPER DISTILL CONTRACT DOC =====
/tmp/after-chatbon/whisper-main/docs/src/cli.md:41:## `turu distill <scope>`
/tmp/after-chatbon/whisper-main/docs/src/cli.md:43:Two-phase distill contract: snapshot, agent rewrites, guarded commit.
/tmp/after-chatbon/whisper-main/docs/src/cli.md:45:- `--begin` — snapshot the current state and return the working paths
/tmp/after-chatbon/whisper-main/docs/src/cli.md:46:- `--commit --revision <id>` — install the distilled working file for this revision
/tmp/after-chatbon/whisper-main/docs/src/cli.md:47:- Guards the commit against concurrent drift between snapshot and commit
/tmp/after-chatbon/whisper-main/docs/src/status.md:3:`whisper` **[current release](./release.md)** — Status: **beta**. Core (key/resolve/append/recall/distill)
/tmp/after-chatbon/whisper-main/docs/src/status.md:15:| `turu distill` | stable | two-phase begin/commit with drift guard |
/tmp/after-chatbon/whisper-main/docs/src/status.md:38:- **incitaciones** — the distilled `whisper` skill is a thin pointer to this
/tmp/after-chatbon/whisper-main/AGENTS.md:26:- `ah signals` — emit dont drift signals
/tmp/after-chatbon/whisper-main/AGENTS.md:184:- Commands: `turu resolve <scope>` · `turu append <scope> [--global] --text ... [--topic k] [--supersedes id]` · `turu recall <scope> [--topic k] [--budget bytes]` · `turu distill <scope> --begin|--commit` · `turu bundle pack|unpack` · `turu status` · `turu doctor` · `turu feedback <kind>`

## Assistant

bash -lc sed -n '220,500p' /tmp/after-chatbon/bajan-main/src/extract.rs; printf '\n===== EXTRACTOR SEAM TEST (FULL) =====\n'; sed -n '1,320p' /tmp/after-chatbon/bajan-main/tests/extractor_seam.rs; printf '\n===== INGESTION SPEC =====\n'; cat /tmp/after-chatbon/bajan-main/specs/ingestion-contract.md; printf '\n===== EXTRACTION SPEC =====\n'; sed -n '1,280p' /tmp/after-chatbon/bajan-main/specs/extraction-claims.md; printf '\n===== WHISPER DISTILL TESTS =====\n'; sed -n '1,300p' /tmp/after-chatbon/whisper-main/tests/lifecycle/distill_commit.rs; printf '\n===== WHISPER DISTILL DOC =====\n'; sed -n '35,65p' /tmp/after-chatbon/whisper-main/docs/src/cli.md

## Tool

///
/// Implementors propose candidates for ONE episode per `propose` call;
/// the pipeline (not the extractor) owns the gate, the cache, the
/// run-row telemetry, supersession, and scope/lineage projection.
/// A version bump (any change to `version()`) re-extracts every episode
/// under the new key — the version is the cache identity.
pub trait Extractor: std::fmt::Debug {
    /// Cache-identity version of this extractor (`ex_single_call`:
    /// the (episode id, extractor version) pair keys the cache).
    fn version(&self) -> &str;
    /// Model id when this extractor uses an LLM — lands verbatim on the
    /// run rows (`ex_run_record`); `None` for deterministic extractors.
    fn model_id(&self) -> Option<&str> {
        None
    }
    /// Propose candidate claims for one episode. Batch semantics: the
    /// returned set is staged all-or-nothing — one gate failure in the
    /// batch refuses the whole episode's candidates (no partial
    /// staging, per-episode gate outcome).
    fn propose(&self, episode: &EpisodeRecord) -> Result<Vec<CandidateClaim>, ExtractionFailure>;

    /// The network timeout actually in force for this extractor's
    /// transport (bajan-noj); `None` for extractors with no transport.
    /// Selection-testable: BAJAN_EXTRACTOR_TIMEOUT_SECS must yield a
    /// transport carrying exactly that timeout.
    fn transport_timeout(&self) -> Option<std::time::Duration> {
        None
    }
}

/// The vertical-slice extractor report: one deterministic single-call
/// pass over pending episodes (`ex_single_call`), one candidate per
/// episode, typed at the door by the gate (`ex_typed_gate`), cached per
/// (episode id, extractor version).
///
/// Outcome classes are separated (bajan-r1h): a persisted candidate
/// counts in `candidates_proposed`; a gate refusal is recorded per
/// episode in `gate_rejections` with its machine-readable reason. A
/// zero-candidate episode is yet another class — legitimately extracted
/// and cached as empty (`ex_typed_gate`) — and cannot arise in this
/// slice: the deterministic proposer always proposes exactly one
/// candidate. A version-bump re-extraction additionally tombstones the
/// episode's prior-version `staged` claims (`ex_supersession`), counted
/// in `superseded` — `staged` claims take the supersession path; an
/// `active` claim is never mutated (`ex_supersession`): instead, a new
/// output that CONFLICTS with it stages an invalidation proposal citing
/// the causing episode (`ex_mutation_proposal`), counted in
/// `proposals_staged`.
#[derive(Debug, Clone, PartialEq, Serialize)]
pub struct ExtractReport {
    pub episodes_processed: usize,
    pub candidates_proposed: usize,
    pub superseded: usize,
    /// Invalidation proposals staged this pass against ACTIVE claims
    /// whose evidence position the new output conflicts with
    /// (`ex_mutation_proposal`). Duplicates (same claim + causing
    /// episode) are idempotent skips, never re-counted.
    pub proposals_staged: usize,
    pub gate_rejections: Vec<GateRejection>,
    /// Episodes parked this pass after retry-budget exhaustion
    /// (`ex_single_call` abort; `ex_park_requeue`: no cache entry — the
    /// next pass re-attempts with a fresh budget).
    pub parked: Vec<ParkedEpisode>,
    /// The spend-cap stop (bajan-8cc): Some when the pass ended early
    /// because the configured cost cap refused further calls. The
    /// stopped episode and everything after it stay PENDING (never
    /// parked) — a raised cap re-attempts them with the cache intact.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub spend_cap: Option<SpendCapStop>,
}

/// The machine-readable spend-cap stop (bajan-8cc): known spend at the
/// stop, the cap, calls whose cost could not be accounted (responses
/// without `usage.cost` — enforcement failed closed), and how many
/// episodes were never attempted because of the stop.
#[derive(Debug, Clone, PartialEq, Serialize)]
pub struct SpendCapStop {
    pub spent_usd: f64,
    pub cap_usd: f64,
    pub unaccounted_calls: u32,
    pub episodes_left_pending: usize,
}

/// Classify a store refusal at the wired gate (bajan-r1h): a gate-level
/// refusal maps to its machine-readable reason; an infrastructure
/// failure (SQL) is never a gate rejection — it propagates and the run
/// fails honestly instead of being swallowed into the report. The wired
/// path pre-validates batches (see run_extract_with); this classifier
/// survives for run-row/test parity of the refusal taxonomy.
#[allow(dead_code)]
fn classify_refusal(err: &crate::store::StoreError) -> Result<Reason, BajanError> {
    match err {
        crate::store::StoreError::HedgeMarkerDropped { .. } => Ok(Reason::HedgeMarkerDropped),
        other => Err(BajanError::Store(other.to_string())),
    }
}

/// Epoch milliseconds for run-row timestamps (`ex_run_record`).
fn epoch_millis() -> u64 {
    std::time::SystemTime::now()
        .duration_since(std::time::UNIX_EPOCH)
        .map(|d| d.as_millis() as u64)
        .unwrap_or(0)
}

/// Minimum claim-sized unit length in chars (bajan-5zy): sentences (or
/// accumulated fragments) below this merge into the next unit — no
/// orphan fragments like a bare `Dr.` abbreviation sentence.
pub const ATOMIZER_MIN_UNIT_CHARS: usize = 20;

/// Maximum claim-sized unit length in chars (bajan-5zy): units above
/// this split at semicolon connectors (`; `) — never mid-word. A run-on
/// with no semicolons stays whole: splitting is best-effort, documented,
/// never a hard cut (an honest oversized unit beats a mangled one).
pub const ATOMIZER_MAX_UNIT_CHARS: usize = 300;

/// Cache-identity version of the default atomizer: namespaced under
/// `atomic-` so stores extracted by the legacy whole-episode proposer
/// (plain package version) re-extract — with supersession — when the
/// default switched (bajan-5zy): the upgrade must not silently reuse
/// legacy whole-episode output.
pub fn atomic_default_version() -> String {
    format!("atomic-{}", env!("CARGO_PKG_VERSION"))
}

/// Segment episode text into atomic claim-sized units (bajan-5zy):
/// UAX #29 sentence boundaries (unicode-segmentation, `=`-pinned), then
/// (1) merge fragments below `ATOMIZER_MIN_UNIT_CHARS` — forward while
/// accumulating, and the trailing short fragment merges back into the
/// previous unit; (2) split units above `ATOMIZER_MAX_UNIT_CHARS` at
/// semicolon connectors, the semicolon staying with the left part and
/// the following whitespace dropped.
///
/// Deterministic pure function: same text → same units. Every unit is a
/// verbatim substring of the text (byte-slice of the original), and the
/// units re-concatenate to the text modulo whitespace — `ic_verbatim`
/// holds by construction, so the typed gate's whitespace-collapsed
/// containment and hedge-marker survival pass without repair.
pub fn atomic_claim_units(text: &str) -> Vec<String> {
    // 1. UAX #29 sentence spans (byte offsets), trimmed, non-empty.
    let mut spans: Vec<(usize, usize)> = Vec::new();
    let mut offset = 0usize;
    for sentence in text.split_sentence_bounds() {
        let start = offset;
        offset += sentence.len();
        let lead = sentence.len() - sentence.trim_start().len();
        let s = start + lead;
        let end = s + sentence.trim().len();
        if end > s {
            spans.push((s, end));
        }
    }
    if spans.is_empty() {
        return Vec::new();
    }

    // 2. Merge below the minimum: accumulate forward — a unit still under
    // the minimum absorbs the next sentence; a trailing short fragment
    // merges back into the previous unit.
    let mut units: Vec<(usize, usize)> = Vec::new();
    for (s, e) in spans {
        match units.last_mut() {
            Some(last) if char_len(text, last.0, last.1) < ATOMIZER_MIN_UNIT_CHARS => {
                last.1 = e;
            }
            _ => units.push((s, e)),
        }
    }
    if units.len() > 1 {
        let last = *units.last().expect("len > 1 checked");
        if char_len(text, last.0, last.1) < ATOMIZER_MIN_UNIT_CHARS {
            units.pop();
            let prev 
...[truncated]...
tic_structure | unit | [[extraction.claims.ex_deterministic_structure]] | episodes with converter-supplied structure markers | structural relations derive from markers alone, independent of extraction output |
| p_output_schema | unit | [[extraction.claims.ex_output_schema]] | candidate-claim records sampled from the published schema | the published schema validates every emitted candidate record |

===== WHISPER DISTILL TESTS =====
//! `distill --commit` semantics: install, drift refusal, replay noop,
//! revision id validation, immutable revisions.

use crate::common::{Uw, at, begin_distill, repo_env, resolve_repo_path};
use predicates::str::contains;

#[test]
pub(crate) fn distill_commit_installs_distilled_output_and_keeps_snapshot() {
    let tmp = tempfile::tempdir().uw();
    let (home, repo) = repo_env(&tmp);
    at(&home, &repo, "2026-01-01T00:00:00Z")
        .args(["append", "repo", "--text", "stale fact"])
        .assert()
        .success();
    let target = resolve_repo_path(&home, &repo);
    let pre = std::fs::read_to_string(&target).uw();

    let (working, revision) = begin_distill(&home, &repo, "2026-01-05T00:00:00Z");

    // Agent rewrites: keep the entry, drop nothing, add a fresh fact.
    std::fs::write(&working, "distilled content\n").uw();
    at(&home, &repo, "2026-01-05T00:00:00Z")
        .args([
            "distill",
            "repo",
            "--commit",
            "--revision",
            &revision,
            "--json",
        ])
        .assert()
        .success()
        .stdout(contains("\"phase\":\"commit\""))
        .stdout(contains("\"noop\":false"));

    let after = std::fs::read_to_string(&target).uw();
    assert_eq!(after, "distilled content\n");

    // Snapshot immutable and retained, equal to the pre-distill content.
    let rev_dir = target.parent().uw().join("revisions").join(&revision);
    assert_eq!(
        std::fs::read_to_string(rev_dir.join("snapshot.md")).uw(),
        pre
    );
}

#[test]
pub(crate) fn distill_commit_refuses_on_drift() {
    let tmp = tempfile::tempdir().uw();
    let (home, repo) = repo_env(&tmp);
    at(&home, &repo, "2026-01-01T00:00:00Z")
        .args(["append", "repo", "--text", "fact one"])
        .assert()
        .success();

    let (working, revision) = begin_distill(&home, &repo, "2026-01-05T00:00:00Z");

    // Concurrent append after --begin → drift.
    at(&home, &repo, "2026-01-06T00:00:00Z")
        .args(["append", "repo", "--text", "concurrent fact"])
        .assert()
        .success();
    std::fs::write(&working, "distilled content\n").uw();

    let before = std::fs::read_to_string(resolve_repo_path(&home, &repo)).uw();
    at(&home, &repo, "2026-01-06T00:00:00Z")
        .args(["distill", "repo", "--commit", "--revision", &revision])
        .assert()
        .failure()
        .stderr(contains("changed since --begin"));
    let after = std::fs::read_to_string(resolve_repo_path(&home, &repo)).uw();
    assert_eq!(before, after, "live file must be untouched on drift");
}

#[test]
pub(crate) fn distill_commit_rejects_crafted_revision_ids() {
    let tmp = tempfile::tempdir().uw();
    let (home, repo) = repo_env(&tmp);
    at(&home, &repo, "2026-01-01T00:00:00Z")
        .args(["append", "repo", "--text", "fact"])
        .assert()
        .success();
    at(&home, &repo, "2026-01-01T00:00:00Z")
        .args([
            "distill",
            "repo",
            "--commit",
            "--revision",
            "../../evil-12345678",
        ])
        .assert()
        .failure()
        .stderr(contains("invalid revision id"));

    // Refusal must be side-effect free: target untouched, no revisions dir.
    let target = resolve_repo_path(&home, &repo);
    let content = std::fs::read_to_string(&target).uw();
    assert!(content.ends_with(" fact\n"), "entry altered: {content:?}");
    assert!(!content.contains("evil"));
    assert!(!target.parent().uw().join("revisions").exists());
}

#[test]
pub(crate) fn distill_commit_replay_is_a_noop() {
    let tmp = tempfile::tempdir().uw();
    let (home, repo) = repo_env(&tmp);
    at(&home, &repo, "2026-01-01T00:00:00Z")
        .args(["append", "repo", "--text", "fact"])
        .assert()
        .success();

    let (working, revision) = begin_distill(&home, &repo, "2026-01-05T00:00:00Z");
    std::fs::write(&working, "distilled\n").uw();
    at(&home, &repo, "2026-01-05T00:00:00Z")
        .args(["distill", "repo", "--commit", "--revision", &revision])
        .assert()
        .success();

    let out = String::from_utf8(
        at(&home, &repo, "2026-01-05T00:00:00Z")
            .args([
                "distill",
                "repo",
                "--commit",
                "--revision",
                &revision,
                "--json",
            ])
            .output()
            .uw()
            .stdout,
    )
    .uw();
    assert!(out.contains("\"noop\":true"), "{out}");
    assert_eq!(
        std::fs::read_to_string(resolve_repo_path(&home, &repo)).uw(),
        "distilled\n",
        "replay must not rewrite the live file"
    );
}

#[test]
pub(crate) fn distill_commit_without_working_file_fails() {
    let tmp = tempfile::tempdir().uw();
    let (home, repo) = repo_env(&tmp);
    at(&home, &repo, "2026-01-01T00:00:00Z")
        .args(["append", "repo", "--text", "fact"])
        .assert()
        .success();

    let (_working, revision) = begin_distill(&home, &repo, "2026-01-05T00:00:00Z");

    at(&home, &repo, "2026-01-05T00:00:00Z")
        .args(["distill", "repo", "--commit", "--revision", &revision])
        .assert()
        .failure()
        .stderr(contains("working file not written"));
    // live file untouched
    assert!(
        std::fs::read_to_string(resolve_repo_path(&home, &repo))
            .uw()
            .contains("fact")
    );
}

#[test]
pub(crate) fn distill_two_cycles_produce_two_distinct_immutable_revisions() {
    let tmp = tempfile::tempdir().uw();
    let (home, repo) = repo_env(&tmp);
    at(&home, &repo, "2026-01-01T00:00:00Z")
        .args(["append", "repo", "--text", "v1"])
        .assert()
        .success();
    let target = resolve_repo_path(&home, &repo);
    let pre = std::fs::read_to_string(&target).uw();

    let run_cycle = |now: &str, text: &str| -> String {
        let (working, revision) = begin_distill(&home, &repo, now);
        std::fs::write(&working, text).uw();
        at(&home, &repo, now)
            .args(["distill", "repo", "--commit", "--revision", &revision])
            .assert()
            .success();
        revision
    };

    let rev1 = run_cycle("2026-01-05T00:00:00Z", "first distill\n");
    let rev2 = run_cycle("2026-01-06T00:00:00Z", "second distill\n");
    assert_ne!(rev1, rev2);
    let rev_dir = target.parent().uw().join("revisions");
    assert!(rev_dir.join(&rev1).join("snapshot.md").exists());
    assert!(rev_dir.join(&rev2).join("snapshot.md").exists());
    assert_eq!(
        std::fs::read_to_string(rev_dir.join(&rev1).join("snapshot.md")).uw(),
        pre
    );
    assert_eq!(std::fs::read_to_string(&target).uw(), "second distill\n");
}

===== WHISPER DISTILL DOC =====
- scope may be `all` — composes scopes in precedence order
- `--topic <k>` — only entries with this topic key
- `--budget <bytes>` — byte budget
- `--include-superseded` — include superseded entries
- `--read-only` — skip usage telemetry (sidecar untouched)

## `turu distill <scope>`

Two-phase distill contract: snapshot, agent rewrites, guarded commit.

- `--begin` — snapshot the current state and return the working paths
- `--commit --revision <id>` — install the distilled working file for this revision
- Guards the commit against concurrent drift between snapshot and commit

## `turu bundle pack|unpack`

Deterministic, transport-agnostic knowledge bundles keyed by repo key.
Unpack merges extend-without-duplicate and never overwrites.

## `turu init`

Create the workspace layout for this checkout (never overwrites).

## `turu status`

One envelope with every relevant path and existence flag.

## `turu check`

Detect legacy key variants, undefined groups, and missing files.

## Assistant

bash -lc grep -n '^fn\|^#\[test\]' /tmp/after-chatbon/bajan-main/tests/extractor_seam.rs | head -100; sed -n '1,220p' /tmp/after-chatbon/bajan-main/tests/extractor_seam.rs; grep -n '^## Constraints\|^## Model\|^## Properties\|^###' /tmp/after-chatbon/bajan-main/specs/extraction-claims.md | head -80; sed -n '1,180p' /tmp/after-chatbon/bajan-main/specs/extraction-claims.md

## Tool

21:fn episode(id: &str, text: &str) -> EpisodeRecord {
35:fn seed_two_episodes(db: &SqliteStore) {
71:fn scripted_claim(text: &str) -> CandidateClaim {
84:fn staged_texts(db: &SqliteStore) -> Vec<String> {
101:#[test]
102:fn section_kind_tag_refuses_candidates_and_caches_extracted() {
151:#[test]
152:fn scripted_extractor_dispatches_through_run_extract() {
184:#[test]
185:fn default_extractor_is_the_sentence_atomizer() {
209:#[test]
210:fn legacy_config_keeps_whole_episode_proposer() {
224:#[test]
225:fn model_id_lands_on_run_rows() {
247:#[test]
248:fn one_gate_failure_in_batch_stages_nothing() {
277:#[test]
278:fn infrastructure_failure_fails_the_run() {
296:#[test]
297:fn same_version_reuses_cache_extractor_agnostically() {
315:#[test]
316:fn version_bump_reextracts_across_extractors() {
//! Purpose: red-first tests for the extractor seam (bajan-9av) — the
//! `Extractor` trait boundary between persisted episodes and candidate
//! proposals. Responsibilities: trait dispatch through `run_extract` with
//! a scripted fake extractor; all-or-nothing candidate persistence (a
//! partial batch is refused, nothing staged — the gate is per-episode);
//! the default extractor is the deterministic sentence atomizer
//! (bajan-5zy; the byte-stable whole-episode proposer stays behind
//! config as `legacy`); model id reaches the run
//! rows when an extractor carries one; deterministic extractors cache
//! identically (one call per episode per version).
//! Rationale: `ex_single_call`/`ex_run_record` name the extractor's
//! contract but not its implementation — the seam makes "proposer
//! differs, contract does not" structural instead of incidental.

use bajan::extract::{self, CandidateClaim, ExtractionFailure, Extractor};
use bajan::ingest::{EpisodeRecord, Locator, SourceMeta};
use bajan::store::sqlite::SqliteStore;
use bajan::store::{ClaimStatus, Evidence};
use proptest::prelude::*;

fn episode(id: &str, text: &str) -> EpisodeRecord {
    EpisodeRecord {
        id: id.into(),
        text: text.into(),
        locator: Locator::Span("heading:H".into()),
        source: SourceMeta {
            source_type: "markdown".into(),
            data_cutoff: Some("2026-01-01".into()),
            authority_tier: 2,
            tags: vec!["workspace:dev".into()],
        },
    }
}

fn seed_two_episodes(db: &SqliteStore) {
    ingest::persist(db, &episode("ep-1", "First episode text. Second sentence.")).expect("persist");
    ingest::persist(db, &episode("ep-2", "Other episode text.")).expect("persist");
}
use bajan::ingest;

/// A scripted extractor: fixed output per episode id, optional model id.
/// Fails for ids in `fail_for` (infrastructure failure class).
#[derive(Debug)]
struct FakeExtractor {
    version: &'static str,
    model_id: Option<&'static str>,
    /// Output per episode id; missing id = infrastructure failure.
    outputs:
        std::collections::HashMap<&'static str, Result<Vec<CandidateClaim>, ExtractionFailure>>,
}

impl Extractor for FakeExtractor {
    fn version(&self) -> &str {
        self.version
    }
    fn model_id(&self) -> Option<&str> {
        self.model_id
    }
    fn propose(&self, episode: &EpisodeRecord) -> Result<Vec<CandidateClaim>, ExtractionFailure> {
        self.outputs
            .get(episode.id.as_str())
            .cloned()
            .unwrap_or_else(|| {
                Err(ExtractionFailure::Infrastructure(
                    "no script for this episode".into(),
                ))
            })
    }
}

fn scripted_claim(text: &str) -> CandidateClaim {
    CandidateClaim {
        text: text.into(),
        valid_at: None,
        invalid_at: None,
        evidence: Evidence::Span {
            text: text.into(),
            locator: "heading:H".into(),
        },
    }
}

/// Staged claim texts after a run (via the full read-back).
fn staged_texts(db: &SqliteStore) -> Vec<String> {
    db.claims_with_lineage()
        .expect("claims read back")
        .into_iter()
        .filter(|(_, node, _)| node.status == ClaimStatus::Staged)
        .map(|(_, node, _)| node.text)
        .collect()
}

// --- section-kind filter (ex_section_filter, bajan-162) ------------------

/// An episode tagged with a non-knowledge section kind has every candidate
/// refused at the deterministic post-pass: zero staged claims, a gate
/// rejection entry with the machine-readable `section_filtered` reason, a
/// run row carrying the same reason (`ex_run_record`), and the episode
/// CACHED as extracted — re-extraction would deterministically re-produce
/// filterable junk, so cache economics say one call, never a retry.
#[test]
fn section_kind_tag_refuses_candidates_and_caches_extracted() {
    let db = SqliteStore::open(":memory:").expect("store");
    let mut tagged = episode("ep-praise", "Praise text one. Praise text two.");
    tagged.source.tags.push("section-kind:praise".into());
    ingest::persist(&db, &tagged).expect("persist");
    ingest::persist(&db, &episode("ep-plain", "Plain text one. Plain text two.")).expect("persist");
    let outputs = [
        ("ep-praise", Ok(vec![scripted_claim("Praise text one.")])),
        ("ep-plain", Ok(vec![scripted_claim("Plain text one.")])),
    ]
    .into_iter()
    .collect();
    let extractor = FakeExtractor {
        version: "9.9.9",
        model_id: None,
        outputs,
    };
    let mut runs = extract::ExtractionRunStore::default();
    let report = extract::run_extract_with(&db, &extractor, &mut runs).expect("pass runs");

    assert_eq!(staged_texts(&db), vec!["Plain text one.".to_string()]);
    let rejection = report
        .gate_rejections
        .iter()
        .find(|r| r.episode_id == "ep-praise")
        .expect("praise refusal reported");
    assert_eq!(rejection.reason.code(), "section_filtered");
    let row = runs
        .rows()
        .find(|r| r.episode_id == "ep-praise")
        .expect("run row for the filtered episode");
    match &row.finish {
        extract::Finish::GateRejected { reason } => {
            assert_eq!(reason.code(), "section_filtered")
        }
        other => panic!("expected gate-rejected finish, got {other:?}"),
    }

    // Cached as extracted-empty: a second pass has nothing pending.
    let second = extract::run_extract_with(&db, &extractor, &mut Default::default())
        .expect("second pass runs");
    assert_eq!(second.episodes_processed, 0);
}

// --- dispatch ------------------------------------------------------------

/// A scripted extractor's candidates reach the store through run_extract:
/// two atomic claims per episode, staged, with the extractor's version on
/// their lineage rows.
#[test]
fn scripted_extractor_dispatches_through_run_extract() {
    let db = SqliteStore::open(":memory:").expect("store");
    seed_two_episodes(&db);
    let extractor = FakeExtractor {
        version: "2.0.0",
        model_id: Some("test-model"),
        outputs: [
            (
                "ep-1",
                Ok(vec![
                    scripted_claim("First episode text."),
                    scripted_claim("Second sentence."),
                ]),
            ),
            ("ep-2", Ok(vec![scripted_claim("Other episode text.")])),
        ]
        .into_iter()
        .collect(),
    };
    let report = extract::run_extract_with(&db, &extractor, &mut Default::default())
        .expect("extract succeeds");
    assert_eq!(report.episodes_processed, 2);
    assert_eq!(report.candidates_proposed, 3);
    let texts = staged_texts(&db);
    assert!(texts.contains(&"First episode text.".to_string()));
    assert!(texts.contains(&"Second sentence.".to_string()));
    assert!(texts.contains(&"Other episode text.".to_string()));
}

/// The default extractor is the deterministic sentence atomizer
/// (bajan-5zy): atomic claim-sized candidates per pending episode,
/// `model_id: None` — the no-LLM path produces real atomic claims.
#[test]
fn default_extractor_is_the_sentence_atomizer() {
    let db = SqliteStore::open(":memory:").expect("store");
    ingest::persist(
        &db,
        &episode("ep-1", "The first claim is here. The second claim lives."),
    )
    .expect("persist")
...[truncated]...
ure, every candidate rejection at the validation gate) carries a machine-readable reason stored on the run or rejection record, never on a claim node | [[extraction.claims]] |
| ex_evidence_containment | invariant | every candidate claim carries an evidence span — a verbatim span of the supporting episode text plus its episode locator, or the typed absent marker when sentence alignment failed — validated by containment after whitespace collapse (all whitespace runs become a single space) of both span and episode text; a span failing containment is rejected with reason `evidence-not-contained`, never repaired; a typed-absent span persists but is flagged by the deterministic pass (`ex_reflection` extended), not treated as a violation | [[extraction.claims]] |
| ex_no_llm_post | invariant | normalization, dedup, entity matching, and conflict detection after the extraction call are deterministic; normalization rules appear both as prompt instructions and in a deterministic post-pass, because prompts are not bulletproof | [[extraction.claims]] |
| ex_mutation_proposal | invariant | a candidate claim that conflicts with an existing active claim stages an invalidation proposal carrying its causing-episode lineage; the existing claim is not mutated by the extractor | [[extraction.claims]] |
| ex_reflection | advisory | the single extraction call includes a self-check that verifies candidate claims against the episode text and enriches change lineage, rendered as flags by a deterministic pass; it flags unsupported candidates and never introduces new ones, and it is not a second LLM call | [[extraction.claims]] |
| ex_tag_inheritance | invariant | workspace tags and source metadata on an episode are inherited by every claim derived from it as a projection — the union over its lineage edges, resolved by walking `derived_from` at query time — and are never stored on the claim node | [[extraction.claims]] |
| ex_deterministic_structure | invariant | structure the converter already supplied (heading anchors, section boundaries, links) is consumed deterministically and never re-extracted by the LLM | [[extraction.claims]] |
| ex_section_filter | invariant | the deterministic post-pass rejects every candidate of an episode whose tags include a non-knowledge section-kind tag — `section-kind:praise`, `section-kind:copyright`, `section-kind:acknowledgments` — with machine-readable reason `section-filtered` on the run record (never on a claim node, per `ex_run_record`); the deny set is fixed in code, never an LLM judgment (`ex_no_llm_post` holds); untagged episodes stage unchanged, and a fully filtered episode still caches as extracted-empty per the `ex_single_call` cache economics | [[extraction.claims]] |
| ex_output_schema | extension_point | the candidate-claim record schema (field names, types, requiredness) is published for eval-harness specs to conform to | [[extraction.claims]] |

## Model

### States

- `pending`
- `extracted`
- `validated`
- `staged`
- `rejected`

### Transitions

| id | from | to | guard |
|----|------|----|-------|
| run | pending | extracted | [[extraction.claims.ex_single_call]] |
| gate | extracted | validated | [[extraction.claims.ex_typed_gate]] |
| abort | pending | rejected | [[extraction.claims.ex_single_call]] |
| requeue | rejected | pending | [[extraction.claims.ex_park_requeue]] |
| refuse | extracted | rejected | [[extraction.claims.ex_typed_gate]] |
| supersede | staged | rejected | [[extraction.claims.ex_supersession]] |
| stage | validated | staged | [[extraction.claims.ex_no_llm_post]] |
| refuse_section | extracted | rejected | [[extraction.claims.ex_section_filter]] |

## Properties

| id | kind | derives_from | generator | predicate |
|----|------|--------------|-----------|-----------|
| p_single_call | unit | [[extraction.claims.ex_single_call]] | episode corpora ingested, re-ingested unchanged, and re-ingested with a bumped extractor version | exactly one successful call per (episode id, extractor version); re-ingest at the same version produces no new call and reuses cached output; a version bump re-extracts |
| p_park_requeue | unit | [[extraction.claims.ex_park_requeue]] | episodes parked after retry-budget exhaustion, re-submitted unchanged, then re-run through extraction passes that fail again and succeed | the re-attempt pass starts a fresh retry budget and writes new run rows while prior parked rows persist with their reasons; success caches the output and ends the requeue cycle; renewed exhaustion parks again with a recorded reason; the unchanged re-submission itself emits `already_persisted` and changes neither graph nor run state |
| p_section_filter | unit | [[extraction.claims.ex_section_filter]] | candidate batches from episodes tagged with each deny-set section kind and from untagged episodes | tagged episodes stage zero claims and their run rows carry the `section-filtered` reason; untagged episodes stage unchanged; a fully filtered episode is cached as extracted so the pass never re-calls it |
| p_typed_gate | unit | [[extraction.claims.ex_typed_gate]] | candidate records mixing schema-valid, schema-violating, lineage-less, evidence-less, and zero-candidate episodes | only schema-valid lineage-bearing candidates with a passing evidence span reach `validated`; every violation lands in `rejected` unmodified; a zero-candidate episode caches as legitimately empty |
| p_supersession | unit | [[extraction.claims.ex_supersession]] | episode corpora re-extracted at bumped extractor versions with prior output in `staged`, `active`, and `rejected` states | only prior-version `staged` claims become `rejected` with reason `superseded-by-reextraction`, lineage and evidence remaining queryable; `active` and `rejected` claims from any version never change status; active conflicts stage invalidation proposals; superseded claims re-enter `staged` only via explicit re-stage |
| p_run_record | unit | [[extraction.claims.ex_run_record]] | extraction calls with success, repeated-failure, and gate-rejection outcomes | every call writes exactly one run row with episode id, extractor version, model id when present, timestamps, and finish status; every parked episode and gate rejection carries a machine-readable reason; claim nodes expose no reason field |
| p_evidence_containment | unit | [[extraction.claims.ex_evidence_containment]] | candidate spans that are contained, non-contained after whitespace collapse, and typed-absent | contained spans persist verbatim; non-contained spans reject with reason `evidence-not-contained` and are never repaired; typed-absent spans persist flagged by the reflection pass and are never reported as violations |
| p_no_llm_post | unit | [[extraction.claims.ex_no_llm_post]] | candidate sets containing near-duplicates (simhash distance) and unnormalized fields | identical post-pass inputs produce identical outputs and no LLM call occurs after the extraction step |
| p_mutation_proposal | unit | [[extraction.claims.ex_mutation_proposal]] | candidate claims conflicting with seeded active claims | every conflict stages an invalidation proposal citing its causing episode; seeded claims are unchanged until the proposal is applied |
| p_reflection | unit | [[extraction.claims.ex_reflection]] | extracted candidates containing unsupported statements and dropped hedges | reflection flags each unsupported candidate; the post-reflection candidate set introduces no new claims |
| p_tag_inheritance | unit | [[extraction.claims.ex_tag_inheritance]] | episodes with varying tag sets, derived claim sets, and multi-source claims | every derived claim resolves to exactly the union of its supporting episodes' tag sets via lineage walk; no tag is stored on the claim node |
| p_deterministic_structure | unit | [[extraction.claims.ex_deterministic_structure]] | episodes with converter-supplied structure markers | structural relations derive from markers alone, independent of extraction output |
| p_output_schema | unit | [[extraction.claims.ex_output_schema]] | candidate-claim records sampled from the published schema | the published schema validates every emitted candidate record |

## Assistant

bash -lc printf '\n===== BAJAN EVAL RESULTS =====\n'; cat /tmp/after-chatbon/bajan-main/evals/results.md 2>/dev/null || true; printf '\n===== BAJAN FIXTURES =====\n'; find /tmp/after-chatbon/bajan-main/evals -maxdepth 3 -type f -print 2>/dev/null; printf '\n===== BAJAN EXTRACTOR CONFIG/SELECT =====\n'; grep -nE 'impl Extractor|struct .*Extractor|fn select|atomic_default_version|run_extract_with|run_extract\(' /tmp/after-chatbon/bajan-main/src/extract.rs | head -120; printf '\n===== BAJAN PIPELINE / STORE TESTS =====\n'; grep -nE 'gold|precision|recall|hedge|run_extract_with|Extractor' /tmp/after-chatbon/bajan-main/tests/eval_harness.rs | head -100

## Tool

===== BAJAN EVAL RESULTS =====
# Eval results

Per `ev_results_checked_in` (specs/eval-claims.md): checked-in decision
artifact. One row per (corpus, extractor) run. The eval harness is
implemented (bajan-2k4: `bajan eval claims`). Gold labels are human
sign-off and land in a reviewed commit before any metrics run; the first
adjudicated corpus is `gold-fi4e-v1` (2026-11-04). Raw counts and
observed noise rates are the measured columns.
**No fabricated numbers.**

The pre-harness table below records burn-in observations. Scored runs
append to the eval-claims table (columns match `data.results_row` from
`bajan eval claims`; fill the date cell):

| date | corpus | extractor | precision | recall | hedge preservation | raw counts |
|------|--------|-----------|-----------|--------|--------------------|------------|
| 2026-11-04 | gold-fi4e@v1 | det-0.1.0 | 0.752 | 0.884 | 0.929 | emitted=101 matched=76 golden=86 content-miss=0 spurious=25 hedge-dropped=0 |

First scored run (bajan-2k4 MUST gate): the deterministic extractor's 25
spurious candidates are exactly the questions/headings/navigation lines
adjudication crossed out — on real prose, sentence segmentation alone is
the precision bottleneck (all 76 kept proposals matched; the 10 golden
unmatched are authored/recovered claims the extractor missed, e.g.
heading-contaminated definitions). Hedge preservation 13/14: the one
miss is an unmatched golden claim, not a dropped marker.

| date | corpus | extractor | episodes | extracted | claims staged | junk claims (praise/testimonial/copyright/CTA) | notes |
|------|--------|-----------|----------|-----------|---------------|------------------------------------------------|-------|
| 2026-10-01 | Profit First (2017 EPUB, 50 episodes, v1 stream, untagged) | llm-deepseek/deepseek-v4-flash-0.1.0 (pre-filter) | 50 | 40 (2 passes) | 344 | 41 (11.9%) | burn-in run, docs/burnin-deepseek-v4-flash-profit-first.org; 10 parked stochastically |
| 2026-10-01 | Profit First (2017 EPUB, 50 episodes, v2 stream, section-kind tags) | llm-deepseek/deepseek-v4-flash-0.1.0 (post-filter) | 50 | 42 (1 pass) | 246 | 4 (1.6%) | bajan-9uy fix measured; all 4 residual are ProfitCON CTA mentions inside genuine chapter prose — content-level, not section-level, out of reach of section tags (curation surface's job) |

## Section-filter delta (bajan-9uy → bajan-0yg/ie0/pbd/162)

- Converter tags: exactly 4 episodes tagged (`section-kind:praise` ×2,
  `section-kind:copyright`, `section-kind:acknowledgments`).
- The 4 tagged episodes extracted-and-cached empty (ex_section_filter);
  38 untagged episodes extracted normally.
- Junk claims: **41 → 4 (−90%)**; claim volume 344 → 246 across fewer
  knowledge episodes (the removed volume was noise, per the sample).
- Unknown-evidence spans: 74 (v1) / 68 (v2) — ~20% either way; deepseek-v4-flash
  omitting verbatim spans is provider behavior, honestly flagged by
  reflection (`ex_evidence_containment` typed-absent path), unchanged by
  the filter.
- Stochastic parking persists at book scale (8/50 pending in one pass;
  v1 recovered 2 on rerun) — tracked in bajan-266, not a filter effect.

## Storage-stack decision status

Insufficient: precision/recall do not exist yet (eval harness unimplemented).
SQLite carries the load fine so far (50-episode corpus, sub-second reads);
the decision waits for the harness and a multi-book corpus.
===== BAJAN FIXTURES =====
/tmp/after-chatbon/bajan-main/evals/fixtures/gold-fi4e-v1.json
/tmp/after-chatbon/bajan-main/evals/fixtures/gold-fi4e-v1-run.json
/tmp/after-chatbon/bajan-main/evals/fixtures/gold-fi4e-v1-worksheet.md
/tmp/after-chatbon/bajan-main/evals/results.md

===== BAJAN EXTRACTOR CONFIG/SELECT =====
307:/// path pre-validates batches (see run_extract_with); this classifier
341:pub fn atomic_default_version() -> String {
446:/// cache identity (`atomic_default_version` for the default build).
460:impl Extractor for SentenceAtomizer {
499:impl Extractor for LegacyProposer {
526:pub struct ExtractorConfig {
580:impl ExtractorConfig {
602:    pub fn select(&self) -> Result<Box<dyn Extractor>, ExtractorConfigError> {
604:            "atomic" => Ok(Box::new(SentenceAtomizer::new(atomic_default_version()))),
689:pub fn run_extract(
693:    run_extract_with(db, &SentenceAtomizer::new(atomic_default_version()), runs)
706:    run_extract_with(
756:pub fn run_extract_with(

===== BAJAN PIPELINE / STORE TESTS =====
3://! golden corpus.
5://! versioned corpus loading (`ev_golden_corpus`), deterministic
7://! (`ev_deterministic_scoring`), exact precision/recall with raw counts
8://! and one record per (corpus, extractor) pair (`ev_precision_recall`),
9://! hedge-dropped as a distinct precision failure (`ev_hedge_scoring`),
27:    json!({"id": "gold", "version": version, "episodes": episodes}).to_string()
30:fn golden_claim(text: &str, span: &str, hedges: &[&str]) -> serde_json::Value {
32:    if !hedges.is_empty() {
33:        v["hedges"] = json!(hedges);
46:// ---------- ev_golden_corpus ----------
50:    let no_version = json!({"id": "gold", "episodes": []}).to_string();
57:fn golden_corpus_exposes_claims_with_counts_spans_hedges() {
60:         "golden_claims": [
61:            golden_claim("Costs are real.", "Costs are real.", &[]),
62:            golden_claim("Profits vary", "profits may vary", &["may"]),
64:        {"id": "ep-2", "text": "no claims here", "golden_claims": []},
70:    assert_eq!(ep1.golden_claims.len(), 2);
71:    assert_eq!(ep1.golden_claims[0].source_count, 1);
72:    assert_eq!(ep1.golden_claims[1].hedges, vec!["may".to_string()]);
73:    assert!(ep1.golden_claims[0].hedges.is_empty());
74:    assert!(corpus.episodes[1].golden_claims.is_empty());
83:         "golden_claims": [golden_claim("Costs are real.", "Costs are real.", &[])]},
99:         "golden_claims": [golden_claim("Costs are real.", "Costs are real.", &[])]},
115:    // Candidate text equals the golden claim but its evidence span does
119:         "golden_claims": [golden_claim("Costs are real.", "Costs are real.", &[])]},
132:    // The first candidate consumes the golden claim; the duplicate can
133:    // only score spurious — precision punishes the double emission.
136:         "golden_claims": [golden_claim("Costs are real.", "Costs are real.", &[])]},
151:// ---------- ev_precision_recall ----------
154:fn precision_recall_exact_with_raw_counts() {
155:    // Seeded: 2 emitted, 1 matched (1 spurious), 2 golden → P=1/2, R=1/2.
158:         "golden_claims": [
159:            golden_claim("Costs are real.", "Costs are real.", &[]),
160:            golden_claim("Time is money.", "Time is money.", &[]),
172:    assert_eq!(outcome.counts.golden, 2);
174:    assert_eq!(outcome.counts.golden_unmatched, 1);
175:    assert_eq!(outcome.precision, Some(0.5));
176:    assert_eq!(outcome.recall, Some(0.5));
184:// ---------- ev_hedge_scoring ----------
187:fn hedge_drop_is_precision_failure_not_match() {
189:    // matches but the hedge fidelity fails, distinct from a content miss.
192:         "golden_claims": [golden_claim("Profits may vary by run.", "Profits may vary by run.", &["may"])]},
205:        "a hedge drop is never a plain match"
207:    assert_eq!(outcome.counts.hedge_dropped, 1);
208:    assert_eq!(outcome.precision, Some(0.0), "precision failure");
209:    assert_eq!(outcome.hedge_preservation, Some(0.0));
213:fn hedge_preserved_matches_and_added_hedges_are_plain_matches() {
214:    // Preserving the hedge scores as a match and feeds the preservation
215:    // rate; ADDING a hedge marker the golden lacks is not scored as a
216:    // failure — content equivalence ignores hedge tokens on both sides.
219:         "golden_claims": [
220:            golden_claim("Profits may vary by run.", "Profits may vary by run.", &["may"]),
221:            golden_claim("Costs high.", "Costs seems high.", &[]),
236:    assert_eq!(outcome.counts.hedge_bearing_golden, 1);
237:    assert_eq!(outcome.counts.preserved_hedge_matches, 1);
238:    assert_eq!(outcome.hedge_preservation, Some(1.0));
242:        "added hedge is not scored"
247:fn hedge_dropped_golden_stays_available_for_clean_candidate() {
248:    // A hedge-dropping candidate never consumes the golden claim; a later
252:         "golden_claims": [golden_claim("Profits may vary by run.", "Profits may vary by run.", &["may"])]},
267:    assert_eq!(outcome.counts.preserved_hedge_matches, 1);
275:        {"id": "ep-1", "text": "plain text only", "golden_claims": []},
278:    // Empty run: no emitted candidates → precision unknown.
282:        outcome.precision, None,
283:        "precision must be unknown, never invented"
285:    assert_eq!(outcome.recall, None, "no golden claims → recall unknown");
286:    assert!(outcome.unknown_metrics.contains(&"precision".to_string()));
287:    assert!(outcome.unknown_metrics.contains(&"recall".to_string()));
291:            .contains(&"hedge_preservation".to_string())
294:    // Hedge-free corpus: recall computable, hedge rate unknown.
295:    let hedge_free = json!([
297:         "golden_claims": [golden_claim("Costs are real.", "Costs are real.", &[])]},
299:    let corpus = eval::load_corpus(&corpus_json("1", hedge_free)).expect("valid corpus");
303:    assert_eq!(outcome.precision, Some(1.0));
304:    assert_eq!(outcome.recall, Some(1.0));
305:    assert_eq!(outcome.hedge_preservation, None);
308:        vec!["hedge_preservation".to_string()]
318:         "golden_claims": [golden_claim("Costs are real.", "Costs are real.", &[])]},
348:         "golden_claims": [
349:            golden_claim("Profits may vary.", "Profits may vary.", &["may"]),
350:            golden_claim("Costs are real.", "Costs are real.", &[]),
355:        candidate("ep-1", "Profits vary.", "Profits may vary."), // hedge-dropped
369:        vec!["hedge-dropped", "content-miss", "matched", "spurious"],
372:    assert_eq!(outcome.counts.hedge_dropped, 1);
379:fn hedge_detection_at_text_boundaries() {
380:    // Regression: a hedge marker at the very start or end of a text is a
385:         "golden_claims": [
386:            golden_claim("may vary.", "may vary.", &["may"]),
387:            golden_claim("Costs could rise.", "Costs could rise.", &["could"]),
403:    assert_eq!(outcome.counts.preserved_hedge_matches, 2);
411:        golden_text in "[a-z]{3,6}( [a-z]{3,6}){1,6}",
416:            {"id": "ep-1", "text": golden_text,
417:             "golden_claims": [golden_claim(&golden_text, &golden_text, &[])]},
420:        let claims = json!([candidate("ep-1", &cand_text, &golden_text)]);
429:        let gold_tokens: Vec<&str> = golden_text.split_whitespace().collect();
430:        if cand_tokens != gold_tokens {
434:            prop_assert_eq!(a.precision, Some(1.0));
435:            prop_assert_eq!(a.recall, Some(1.0));
440:    fn p_hedge_scoring(
442:        // the dropped-vs-preserved delta is exactly the generated hedge;

## Assistant

Creo que ahora estamos llegando al argumento central de *After Chatbon*. Lo formularía así:

**No tenemos que aprender a construir software que no cambie. Tenemos que aprender a construir software que podamos cambiar, poner a prueba, descartar y volver a escribir sin perder lo que aprendimos.**

La IA hace que producir una implementación sea barato. Pero eso no significa que sepamos qué implementación necesitamos. Muchas veces tampoco sabemos formular correctamente el problema hasta que probamos algo, vemos cómo se comporta y descubrimos qué estaba mal en nuestra comprensión.

Por eso la unidad de progreso no debería ser el código producido, ni siquiera la funcionalidad terminada. Debería ser **la incertidumbre que logramos eliminar y el conocimiento que sobrevive a cada experimento**.

Esto une tres actividades que solemos tratar por separado:

- Pensar y escribir para entender el problema.
- Construir prototipos para poner nuestras ideas en contacto con la realidad.
- Diseñar el software para poder reemplazar sus implementaciones sin perder las decisiones, los contratos y las pruebas que ya aprendimos.

## 1. Cambiar la unidad de progreso: de funcionalidades a experimentos

Una funcionalidad terminada nos dice que conseguimos implementar algo. Un experimento bien diseñado nos dice algo más importante: **si nuestra idea sobre el problema era correcta**.

Propongo distinguir:

| Desarrollo convencional | Desarrollo experimental |
|---|---|
| ¿Qué funcionalidad implementamos? | ¿Qué queremos averiguar? |
| ¿Cómo hacemos que funcione? | ¿Qué hipótesis estamos poniendo a prueba? |
| ¿Pasaron los tests? | ¿Los tests miden lo que realmente nos importa? |
| ¿Qué código conservamos? | ¿Qué conocimiento merece sobrevivir? |
| ¿Cómo agregamos funcionalidades? | ¿Qué nueva complejidad podemos justificar con evidencia? |

El código es una implementación candidata. No es todavía la solución, ni necesariamente la arquitectura definitiva.

Una implementación puede durar diez minutos y haber sido valiosa si nos permitió descubrir que una hipótesis era falsa. Otra puede durar años sin que hayamos comprobado que resuelve el problema correcto.

Esto se conecta directamente con el artículo de Murat Buffalo: escribir es una forma de externalizar el pensamiento, producir un primer borrador sin juzgarlo y después editarlo críticamente. La IA puede ayudarnos en esas operaciones, pero generar una explicación convincente no demuestra que hayamos comprendido el problema. <Cite ref="turn232215search0"/>

## 2. El ciclo: formular, construir, medir, descartar

No lo presentaría como una metodología para seguir una vez y llegar a una solución. Es un ciclo que repetimos hasta que nuestra comprensión y el sistema maduran.

<box border radius="lg" padding={3} gap={2}>
  <title size="lg">El ciclo experimental</title>
  <list connector="solid" marker="number" gap={3}>
    <list-item>
      **Observar**

      ¿Qué tenemos? ¿Qué hace hoy el sistema? ¿Qué dicen las fuentes, los datos, los usuarios y los tests?
    </list-item>
    <list-item>
      **Escribir**

      ¿Qué creemos que está pasando? ¿Qué queremos resolver? ¿Qué no entendemos todavía? Primero nuestra interpretación, después la IA.
    </list-item>
    <list-item>
      **Formular una hipótesis**

      Si hacemos X, esperamos observar Y, porque creemos Z. ¿Qué resultado nos demostraría que estamos equivocados?
    </list-item>
    <list-item>
      **Construir un experimento**

      La implementación más pequeña que permita distinguir entre explicaciones o alternativas.
    </list-item>
    <list-item>
      **Medir y contrastar**

      Ejecutar con datos conocidos, casos límite y criterios independientes de la implementación.
    </list-item>
    <list-item>
      **Descartar o conservar**

      ¿Qué funcionó? ¿Qué falló? ¿Qué fue inesperado? ¿Qué alternativa merece otro intento?
    </list-item>
    <list-item>
      **Destilar lo aprendido**

      Actualizar el modelo del problema, los contratos, los ejemplos y las preguntas pendientes. Volver a empezar.
    </list-item>
  </list>
</box>

Hay una distinción esencial: el resultado de un experimento puede ser positivo, negativo o inconcluso. Un resultado negativo no es trabajo perdido si nos permitió eliminar una posibilidad.

Y tampoco tenemos que conservar cada implementación que funcionó. Tenemos que conservar las razones por las que creemos que funciona.

## 3. Qué tiene que sobrevivir a una reescritura

Esta es, para mí, la pregunta arquitectónica central.

Si reescribimos el sistema desde cero mañana, ¿qué deberíamos poder recuperar sin tener que volver a descubrirlo todo?

| Debe sobrevivir | Puede descartarse |
|---|---|
| El problema y su contexto | La primera implementación |
| Ejemplos reales y datos de referencia | La estructura interna de los módulos |
| Contratos de comportamiento | El framework utilizado |
| Propiedades e invariantes verificadas | El algoritmo que no dio resultado |
| Casos límite descubiertos | Los prototipos intermedios |
| Resultados y métricas de experimentos | Las abstracciones que no demostraron utilidad |
| Decisiones y motivos para tomarlas | La interfaz inicial |

La idea no es congelar el diseño. Es separar el conocimiento acumulado de la forma accidental en que lo implementamos.

**El experimento es el artefacto durable. El código es reemplazable.**

## 4. Cómo estructurar el software para que pueda cambiar

No intentaría predecir todas las futuras versiones del sistema. Diseñaría cada parte para que podamos sustituirla cuando descubramos que nuestra hipótesis era incorrecta.

Hay cuatro principios que ayudan.

### A. Contratos estables, implementaciones intercambiables

Definir qué entra, qué sale y qué garantías tiene un componente, sin exigir que todos utilicen la misma implementación.

<box border radius="lg" padding={3} gap={2}>
  <box background="surface-secondary" radius="md" padding={3} align="center">
    **Contrato**
    <text color="secondary" size="sm">Input serializable → Output serializable</text>
  </box>
  <box align="center">
    <icon name="arrow-down" color="secondary"/>
  </box>
  <grid columns={3} gap={2}>
    <grid-item>
      <box border radius="md" padding={2} align="center" gap={1}>
        **A**
        <text size="xs" color="secondary" textAlign="center">Algoritmo simple</text>
      </box>
    </grid-item>
    <grid-item>
      <box border radius="md" padding={2} align="center" gap={1}>
        **B**
        <text size="xs" color="secondary" textAlign="center">Algoritmo alternativo</text>
      </box>
    </grid-item>
    <grid-item>
      <box border radius="md" padding={2} align="center" gap={1}>
        **C**
        <text size="xs" color="secondary" textAlign="center">Implementación con IA</text>
      </box>
    </grid-item>
  </grid>
  <box align="center">
    <icon name="arrow-down" color="secondary"/>
  </box>
  <box background="surface-secondary" radius="md" padding={3} align="center">
    **Mismo banco de experimentos**
    <text color="secondary" size="sm">Mismos datos, propiedades, métricas y criterios</text>
  </box>
</box>

El contrato debe describir comportamiento, no detalles internos. Si dos implementaciones cumplen el mismo contrato, podemos compararlas sin cambiar el resto del sistema.

### B. Separar el núcleo de los efectos externos

- Núcleo: transformaciones, reglas y decisiones que podamos probar con entradas y salidas explícitas.
- Adaptadores: archivos, bases de datos, APIs, modelos de IA, interfaces y otros servicios.
- Orquestación: cómo se conectan las operaciones.

Esto reduce el costo de cambiar una tecnología sin tener que reescribir todo el sistema.

### C. Registrar los experimentos

Cada ejecución debería poder reconstruirse:

- Pregunta e hipótesis.
- Versión de la implementación y commit.
- Datos y parámetros de entrada.
- Entorno y dependencias.
- Resultados y métricas.
- Veredicto y explicación.
- Próxima pregunta.

No alcanza con decir «esta versión funcionó». Necesitamos saber con qué datos, bajo qué condiciones y respecto de qué criterio.

### D. No generalizar antes de observar variación

Una advertencia: hacer todo intercambiable desde el principio puede convertirse en sobreingeniería.

Primero construimos una solución concreta. Cuando aparece una segunda implementación o un segundo caso que revela una variación real, buscamos el contrato común. **Abstraemos diferencias observadas, no diferencias imaginadas.**

## 5. Los tests tienen que servir para aprender

No todos los tests cumplen la misma función. Si los tratamos como una única categoría, podemos terminar conservando comportamientos que en realidad queríamos cambiar.

| Tipo de prueba | Qué nos permite descubrir | ¿Sobrevive a una reescritura? |
|---|---|---|
| Caracterización | Qué hace hoy el sistema, incluso si es accidental | No necesariamente |
| Contrato | Qué comportamiento queremos garantizar | Sí |
| Propiedades / invariantes | Qué debe ser cierto para una familia de entradas | Sí, mientras siga siendo válido el modelo |
| Corpus de evaluación | Qué calidad tiene una implementación frente a ejemplos adjudicados | Sí, si sigue representando el problema |
| Integración | Si los componentes funcionan juntos | Se adapta a las nuevas implementaciones |
| Exploratoria | Qué ocurre cuando probamos algo que todavía no entendemos | Se conserva el resultado, no necesariamente el test |

Una precaución importante: **un test que pasa no demuestra que nuestra idea sea correcta**. Demuestra que la implementación cumple una condición que nosotros escribimos. Todavía tenemos que preguntarnos si esa condición representa el problema real.

Por eso necesitamos oráculos independientes: resultados conocidos, datos reales, propiedades matemáticas, criterios humanos o comportamientos observables.

## 6. Tenemos un ejemplo concreto en Bajan

Creo que acá está la mejor demostración para *After Chatbon*: no necesitamos inventar un sistema ficticio. Bajan ya contiene una experiencia de este tipo.

Su problema es extraer afirmaciones de documentos conservando evidencia y procedencia.

En el código actual existe un contrato `Extractor`:

```rust
pub trait Extractor {
    fn version(&self) -> &str;

    fn propose(
        &self,
        episode: &EpisodeRecord
    ) -> Result<Vec<CandidateClaim>, ExtractionFailure>;
}
```

El pipeline se encarga de la validación, caché, registro de ejecuciones, supersession y procedencia. El extractor solamente propone candidatos.

Eso permite probar diferentes implementaciones sin reescribir el pipeline:

- Un atomizador determinista de oraciones.
- Una implementación alternativa basada en estructura documental.
- Un extractor basado en LLM.

Y hay algo todavía mejor: Bajan tiene un corpus adjudicado para evaluar la extracción.

<box border radius="lg" padding={3} gap={3}>
  **Un experimento que ya tenemos parcialmente realizado**

  <text color="secondary" size="xs" weight="medium">BASELINE · DETERMINISTIC EXTRACTOR · gold-fi4e@v1</text>
  <grid columns={3} gap={2}>
    <grid-item>
      <title size="2xl" tabularNums>75,2%</title>
      <text color="secondary" size="xs">Precisión</text>
    </grid-item>
    <grid-item>
      <title size="2xl" tabularNums>88,4%</title>
      <text color="secondary" size="xs">Recall</text>
    </grid-item>
    <grid-item>
      <title size="2xl" tabularNums>92,9%</title>
      <text color="secondary" size="xs">Preservación de hedges</text>
    </grid-item>
  </grid>
  <divider color="subtle"/>
  | Resultado | Cantidad |
  |---|---:|
  | Candidatos emitidos | 101 |
  | Coincidencias | 76 |
  | Afirmaciones esperadas | 86 |
  | Candidatos espurios | 25 |

  <text color="secondary" size="xs">Fuente: evals/results.md del snapshot de Bajan compartido. Un corpus y una versión; no representa una estimación general de calidad.</text>
</box>

El resultado es interesante porque nos enseña algo que no sabíamos antes de medir: la segmentación de oraciones encuentra afirmaciones reales, pero también extrae encabezados, preguntas y elementos de navegación como si fueran conocimiento.

Eso nos permite formular una nueva hipótesis:

> Si utilizamos la estructura del documento, además del texto, podemos mejorar la precisión sin perder recall ni evidencia.

Ahora podemos construir una segunda implementación y ejecutarla sobre exactamente el mismo corpus.

Si mejora, tenemos evidencia para conservarla. Si no, la descartamos. En ambos casos conservamos el corpus, el contrato, las métricas y lo aprendido.

**Esta es una reescritura que no empieza de cero.**

## 7. Whisper completa el otro lado del método

Whisper aporta un mecanismo distinto que me parece importante para la charla.

Su operación `distill` implementa un proceso de dos fases:

1. Crear un snapshot inmutable.
2. Entregar una copia de trabajo para que el agente la reescriba.
3. Comprobar que el original no cambió durante la revisión.
4. Instalar el resultado atómicamente si no hubo conflictos.
5. Conservar la revisión anterior.

Esto no es un mecanismo para reescribir código, sino para reescribir conocimiento sin perder el estado previo.

Pero la misma idea se puede aplicar al desarrollo:

- Crear una versión de referencia.
- Experimentar en una rama o worktree aislado.
- Ejecutar el banco de pruebas.
- Comparar resultados.
- Aceptar o descartar el cambio.
- Registrar qué aprendimos.

Bajan nos ayuda a conservar evidencia y evaluar propuestas. Whisper nos ayuda a conservar conocimiento y revisar su evolución de manera segura.

## 8. El programa que construiría para demostrarlo

Ya no lo llamaría simplemente un programa para entender repositorios. Lo llamaría provisionalmente **Software Lab**: una mesa de trabajo para explorar y evolucionar sistemas mediante experimentos.

No intentaría construir una plataforma genérica. Haría una primera versión con un caso de uso real: comparar extractores de Bajan.

<box border radius="lg" padding={3} gap={3}>
  <title size="xl">Software Lab</title>
  <text color="secondary" size="sm">Una interfaz para pasar de una pregunta a una decisión respaldada por evidencia.</text>
  <box background="surface-secondary" radius="md" padding={3} gap={1}>
    **1. Entender**
    <text size="sm" color="secondary">Explorar el repositorio, su estructura, sus contratos y sus pruebas existentes.</text>
    <badge>Qué tenemos</badge>
  </box>
  <box background="surface-secondary" radius="md" padding={3} gap={1}>
    **2. Formular**
    <text size="sm" color="secondary">Escribir una pregunta, una hipótesis y el resultado que esperamos observar.</text>
    <badge>Qué queremos averiguar</badge>
  </box>
  <box background="surface-secondary" radius="md" padding={3} gap={1}>
    **3. Experimentar**
    <text size="sm" color="secondary">Crear una variante aislada, con ayuda de IA, y ejecutar la misma batería de pruebas.</text>
    <badge>Qué podemos probar</badge>
  </box>
  <box background="surface-secondary" radius="md" padding={3} gap={1}>
    **4. Comparar**
    <text size="sm" color="secondary">Ver diferencias, métricas, fallos, regresiones y resultados inesperados.</text>
    <badge>Qué observamos</badge>
  </box>
  <box background="surface-secondary" radius="md" padding={3} gap={1}>
    **5. Destilar**
    <text size="sm" color="secondary">Conservar las conclusiones, los contratos y las nuevas preguntas. Descartar lo que no sobrevivió.</text>
    <badge>Qué aprendimos</badge>
  </box>
</box>

La IA participa en todo el recorrido, pero no decide automáticamente qué sobrevive. Puede proponer hipótesis, escribir variantes, generar casos de prueba y explicar diferencias. La evaluación y la decisión tienen que tener criterios explícitos.

## 9. Cómo lo convertiría en el argumento de la charla

Veo una narrativa mucho más clara ahora:

1. **La IA hace barato producir implementaciones.** Pero no hace que sepamos qué problema resolver.
2. **Escribir nos ayuda a pensar.** Primero externalizamos nuestra propia comprensión; después usamos IA para desafiarla y ampliarla.
3. **El software es una hipótesis ejecutable.** Construimos para descubrir qué entendimos mal.
4. **Experimentar requiere poder descartar.** Una arquitectura rígida convierte cada descubrimiento en una reescritura costosa.
5. **Los contratos y los tests preservan lo aprendido.** Podemos cambiar las implementaciones sin perder las garantías.
6. **La complejidad se construye gradualmente.** Cada experimento exitoso nos permite incorporar nuevas capacidades sobre una comprensión más sólida.

<box border radius="lg" padding={3} gap={2}>
  <title size="2xl">La idea central</title>
  **No construimos software para demostrar que teníamos razón. Lo construimos para descubrir dónde estábamos equivocados.**

  <divider color="subtle"/>
  <title size="xl" textAlign="center">El código puede morir. Lo que aprendimos no.</title>
</box>

Y esto tiene una consecuencia importante: podemos construir sistemas más complejos sin tener que diseñarlos enteros por adelantado. La complejidad se vuelve manejable cuando cada nueva parte tiene un contrato, evidencia, pruebas y una razón para existir.

Para mí, esta es la diferencia entre *vibe coding* como generación de código y una verdadera práctica de exploración asistida por IA: **no buscamos generar más; buscamos aprender más por cada cosa que intentamos**.

No diseñaría la charla alrededor de una arquitectura ideal. La diseñaría alrededor de una reescritura real de Bajan: mostrar una hipótesis, medir la implementación actual, construir una alternativa, observar qué sobrevive y enseñar qué conocimiento pudimos conservar. Esa experiencia puede hacer visible toda la metodología.

## User

como el software ejecutable puede ser la expresión de nuestras ideas y como poder ejecutarlo nos desafia las ideas

## Assistant

Creo que esta es la conexión filosófica más importante de la charla: **el software ejecutable es una forma de expresar ideas que nos permite enfrentarlas con sus propias consecuencias.**

Normalmente pensamos que primero entendemos un problema, después diseñamos una solución y finalmente escribimos el programa.

Pero muchas veces ocurre al revés: no sabemos realmente qué pensamos hasta que intentamos convertirlo en algo que funcione.

Un programa nos obliga a comprometernos con una interpretación del mundo. Y cuando lo ejecutamos, podemos descubrir que esa interpretación era incompleta, contradictoria o directamente equivocada.

## 1. Del pensamiento a algo que podemos poner a prueba

Hay distintos grados de formalización de una idea:

<box border radius="lg" padding={3} gap={3}>
  <box gap={1}>
    <badge>01 · Intención</badge>
    **«Quiero entender qué dicen estos documentos».**

    <text color="secondary" size="sm">Tenemos una intuición, un problema, una necesidad. Pero todavía hay mucha ambigüedad.</text>
  </box>
  <box align="center">
    <icon name="arrow-down" color="secondary"/>
  </box>
  <box gap={1}>
    <badge>02 · Modelo</badge>
    **«Un documento contiene episodios, que pueden expresar afirmaciones respaldadas por evidencia».**

    <text color="secondary" size="sm">Elegimos conceptos, relaciones y distinciones. Estamos expresando cómo creemos que funciona el problema.</text>
  </box>
  <box align="center">
    <icon name="arrow-down" color="secondary"/>
  </box>
  <box gap={1}>
    <badge>03 · Contrato</badge>
    **«Toda afirmación extraída debe poder vincularse con un fragmento de su fuente».**

    <text color="secondary" size="sm">Convertimos una parte de nuestro modelo en un compromiso observable.</text>
  </box>
  <box align="center">
    <icon name="arrow-down" color="secondary"/>
  </box>
  <box gap={1}>
    <badge>04 · Programa</badge>
    **`document → episodes → claims → evidence validation`**

    <text color="secondary" size="sm">La idea adquiere una forma ejecutable. Ahora podemos alimentarla con datos.</text>
  </box>
  <box align="center">
    <icon name="arrow-down" color="secondary"/>
  </box>
  <box gap={1}>
    <badge color="success">05 · Ejecución</badge>
    **¿Qué sucede cuando lo ponemos en contacto con la realidad?**

    <text color="secondary" size="sm">Aparecen resultados, casos inesperados, contradicciones y preguntas que no habíamos formulado.</text>
  </box>
</box>

El programa es una representación operacional de nuestro pensamiento. No expresa todo lo que pensamos, pero hace explícitas algunas de nuestras decisiones.

Y eso es extraordinariamente valioso.

## 2. Ejecutar es una manera de desafiar nuestras ideas

La ejecución tiene una propiedad que la escritura y la conversación no tienen: nos obliga a confrontar nuestras abstracciones con casos concretos.

Por ejemplo, en Bajan decimos:

> Queremos extraer afirmaciones atómicas de documentos y conservar su evidencia.

Suena razonable. Pero intentemos implementarlo.

- ¿Qué es exactamente una afirmación?
- ¿Una oración puede contener varias afirmaciones?
- ¿Un encabezado puede ser una afirmación?
- ¿Una cita demuestra lo que dice la afirmación o solamente que alguien lo dijo?
- ¿Cómo representamos una excepción?
- ¿Qué hacemos cuando dos documentos se contradicen?

No necesariamente sabíamos que teníamos todas estas preguntas.

**El intento de construir el programa las hizo visibles.**

Y cuando ejecutamos el extractor aparecen todavía más:

- Produce afirmaciones que no esperábamos.
- Omite información que considerábamos importante.
- Confunde navegación con contenido.
- Encuentra relaciones que no habíamos previsto.

Cada comportamiento es una oportunidad para revisar nuestro modelo.

<box border radius="lg" padding={3} gap={2}>
  <title size="xl">El programa nos devuelve una crítica</title>
  <title size="lg" color="secondary" weight="medium">Lo que pensamos</title>
  <title size="lg">Lo que implementamos</title>
  <title size="lg" color="secondary" weight="medium">Lo que realmente ocurre</title>
  <divider color="subtle"/>
  <title size="xl" textAlign="center">¿Qué estaba mal en nuestra comprensión?</title>
</box>

La computadora no entiende nuestra intención. Ejecuta nuestras decisiones, incluidas las que no sabíamos que habíamos tomado.

Por eso ejecutar una idea puede ser mucho más revelador que discutirla.

## 3. El software es una hipótesis ejecutable

Me gusta pensar en esta analogía con la ciencia:

| Investigación científica | Desarrollo experimental |
|---|---|
| Modelo del fenómeno | Modelo del problema |
| Hipótesis | Comportamiento esperado |
| Experimento | Programa ejecutable |
| Instrumento de medición | Tests, métricas, observaciones |
| Resultado experimental | Comportamiento observado |
| Revisión de la teoría | Revisión del modelo y del software |

No es una equivalencia perfecta: un programa puede tener bugs, y un test puede estar mal planteado. Pero la analogía ayuda a cambiar nuestra relación con el código.

No escribimos código solamente para conseguir que algo funcione.

Lo escribimos para descubrir qué ocurre cuando nuestras ideas se enfrentan a situaciones concretas.

Y hay una condición importante: no podemos usar únicamente nuestros propios tests como prueba de que teníamos razón. Necesitamos datos reales, ejemplos independientes, propiedades matemáticas, observaciones externas y criterios humanos. De lo contrario, podemos construir un programa que confirme perfectamente nuestras propias equivocaciones.

## 4. Por eso necesitamos poder reescribir

Si el software es una expresión de nuestras ideas, cuando nuestras ideas cambian, el software también debería poder cambiar.

El problema es que muchas veces construimos sistemas donde las decisiones iniciales quedan profundamente entrelazadas con su implementación.

Entonces, descubrir que una idea era incorrecta tiene un costo enorme.

Necesitamos invertir esa relación:

<grid columns={2} gap={2}>
  <grid-item>
    <box border radius="lg" padding={3} gap={2} height="100%">
      <badge color="danger">Sistema rígido</badge>
      **La implementación es el centro.**

      <text color="secondary" size="sm">Las ideas, los datos, las pruebas y las decisiones quedan atrapados en el código.</text>
      <text color="secondary" size="sm">Cambiar de idea significa reconstruir demasiado.</text>
    </box>
  </grid-item>
  <grid-item>
    <box border radius="lg" padding={3} gap={2} height="100%">
      <badge color="success">Sistema experimental</badge>
      **El conocimiento es el centro.**

      <text color="secondary" size="sm">Contratos, ejemplos, propiedades, datos y resultados pueden sobrevivir a una implementación.</text>
      <text color="secondary" size="sm">Podemos reemplazar el código y volver a experimentar.</text>
    </box>
  </grid-item>
</grid>

Esto sugiere una arquitectura particular:

- Las ideas y los modelos deben poder escribirse y revisarse.
- Los contratos deben poder ejecutarse independientemente de la implementación.
- Los datos y los experimentos deben poder reproducirse.
- Las implementaciones deben ser sustituibles.
- Las decisiones deben conservar sus motivos y evidencia.
- Las abstracciones deben aparecer cuando descubrimos variaciones reales, no antes.

Así podemos probar cinco implementaciones diferentes sin perder el conocimiento que obtuvimos con las cuatro anteriores.

## 5. La complejidad aparece como resultado del aprendizaje

Hay otra consecuencia que me parece todavía más interesante.

No necesitamos saber desde el principio cómo construir un sistema complejo.

Podemos empezar con una idea pequeña, expresarla en un programa, ejecutarla, encontrar sus límites y extenderla.

<box border radius="lg" padding={3} gap={3}>
  <title size="lg">Complejidad por acumulación de comprensión</title>
  <list connector="solid" marker="number" gap={3}>
    <list-item>
      **Una primera idea**

      Construimos algo pequeño que representa una parte del problema.
    </list-item>
    <list-item>
      **Descubrimos una limitación**

      La ejecución revela una situación que nuestro modelo no contempla.
    </list-item>
    <list-item>
      **Ampliamos nuestra comprensión**

      Incorporamos una nueva distinción, regla o propiedad.
    </list-item>
    <list-item>
      **Extendemos el sistema**

      Agregamos capacidad sin perder los comportamientos que ya sabemos garantizar.
    </list-item>
    <list-item>
      **Repetimos**

      El sistema crece porque sabemos más, no porque imaginamos de antemano todas las posibilidades.
    </list-item>
  </list>
</box>

Esto es muy diferente de diseñar una arquitectura enorme para un futuro que todavía no conocemos.

La complejidad deja de ser algo que intentamos anticipar y pasa a ser algo que podemos incorporar a medida que aprendemos a manejarla.

---

## 6. La IA cambia el costo de este proceso

Acá aparece el verdadero significado de *After Chatbon*.

Antes, convertir una idea en algo ejecutable podía requerir mucho tiempo, conocimientos especializados y esfuerzo de implementación.

Ahora podemos pedirle a la IA que nos ayude a:

- Expresar un modelo.
- Crear una primera implementación.
- Generar datos y casos de prueba.
- Construir implementaciones alternativas.
- Comparar comportamientos.
- Buscar contraejemplos.
- Documentar lo que descubrimos.
- Reescribir lo que ya no representa nuestras ideas.

Pero hay una inversión importante:

**Cuando producir código se vuelve barato, entender qué código vale la pena producir se vuelve más importante.**

La IA no elimina la necesidad de pensar. Hace posible que probemos más de nuestros pensamientos.

Y eso requiere una metodología para no confundir la velocidad de producción con el progreso del conocimiento.

## 7. La tesis que llevaría a la charla

Creo que podemos condensar todo esto en cuatro frases:

<box gap={3}>
  <box padding={3} background="surface-secondary" radius="lg">
    **1. Pensar es construir modelos del mundo.**
  </box>
  <box padding={3} background="surface-secondary" radius="lg">
    **2. Programar es convertir algunos de esos modelos en algo ejecutable.**
  </box>
  <box padding={3} background="surface-secondary" radius="lg">
    **3. Ejecutar es descubrir las consecuencias de nuestras ideas.**
  </box>
  <box padding={3} background="surface-secondary" radius="lg">
    **4. Reescribir es incorporar lo que aprendimos.**
  </box>
</box>

Y la frase que podría convertirse en el eje de la presentación:

# No programamos solamente para hacer cosas.
# Programamos para descubrir qué cosas podemos hacer.

El software no es necesariamente el resultado final de nuestro pensamiento. Puede ser uno de sus instrumentos.

Es una manera de darle forma a una idea, hacerla funcionar, observar sus consecuencias, discutirla, descartarla o mejorarla.

**Una idea que podemos ejecutar es una idea que podemos poner a prueba.**

Y una idea que podemos poner a prueba es una idea que podemos mejorar.

Esta sería la conexión que uniría la escritura como herramienta de pensamiento, Bajan, Whisper, la experimentación y la posibilidad de construir sistemas cada vez más complejos sin tener que conocer de antemano su forma definitiva.

## User

Recapitulemos, tenemos las 12 diapositivas, los dos lados, el ejemplo de como procesar u ordenar conocimiento, la guia de tener un ambiente donde sea facil experimeetar y probar y la manera de istructurar el software para crear/recrear. El software como un sebstrato de nuestras ideas

## Assistant

Sí. Creo que ya tenemos la columna vertebral de **After Chatbon**. Y lo importante es que no son cuatro temas independientes —IA, conocimiento, experimentación y arquitectura—: son distintas partes de un mismo argumento.

La tesis que los une es:

# El software como sustrato de nuestras ideas.

Un medio en el que podemos expresar lo que pensamos, hacerlo ejecutable, confrontarlo con la realidad, descubrir qué no entendíamos y modificarlo sin perder lo aprendido.

## 1. El argumento central

Lo podemos resumir en este ciclo:

<box border radius="lg" padding={3} gap={2}>
  <box background="surface-secondary" radius="md" padding={3} align="center">
    **IDEAS**

    <text color="secondary" size="sm">Qué creemos, qué queremos entender, qué problema vemos.</text>
  </box>
  <box align="center">
    <icon name="arrow-down" color="secondary" size="lg"/>
  </box>
  <box background="surface-secondary" radius="md" padding={3} align="center">
    **MODELOS Y SOFTWARE**

    <text color="secondary" size="sm">Damos forma a esas ideas mediante conceptos, reglas, contratos y programas.</text>
  </box>
  <box align="center">
    <icon name="arrow-down" color="secondary" size="lg"/>
  </box>
  <box background="surface-secondary" radius="md" padding={3} align="center">
    **EJECUCIÓN Y EXPERIMENTACIÓN**

    <text color="secondary" size="sm">Ponemos las ideas en contacto con datos y situaciones concretas.</text>
  </box>
  <box align="center">
    <icon name="arrow-down" color="secondary" size="lg"/>
  </box>
  <box background="surface-secondary" radius="md" padding={3} align="center">
    **OBSERVACIÓN Y APRENDIZAJE**

    <text color="secondary" size="sm">Encontramos contradicciones, límites, excepciones y nuevas preguntas.</text>
  </box>
  <box align="center">
    <icon name="arrow-down" color="secondary" size="lg"/>
  </box>
  <box background="surface" border={{size:1,color:"#16A34A"}} radius="md" padding={3} align="center">
    **REVISIÓN Y RECREACIÓN**

    <text color="secondary" size="sm">Reescribimos los modelos y las implementaciones con lo que aprendimos.</text>
  </box>
  <box align="center">
    <icon name="repeat" color="success" size="xl"/>
    <text color="secondary" size="xs">El ciclo vuelve a empezar, pero no desde cero.</text>
  </box>
</box>

La IA hace que algunas transiciones de este ciclo sean mucho más baratas. Pero el valor está en el ciclo completo, no en producir código más rápido.

## 2. Los dos lados

Los dos lados del disco pueden darle a la charla su estructura narrativa. No son simplemente dos mitades de contenido: representan dos movimientos.

<grid columns={2} gap={3}>
  <grid-item>
    <AsyncImage query="Sumo After Chabon album cover original" aspectRatio="1:1" width="100%" maxHeight={160} fit="contain"/>
    **Lado A — Descubrir**

    <text color="secondary" size="sm">Pasar de las ideas a algo ejecutable. Descubrir posibilidades y confrontar lo que creemos con lo que ocurre.</text>
  </grid-item>
  <grid-item>
    <AsyncImage query="Sumo After Chabon vinyl album back cover" aspectRatio="1:1" width="100%" maxHeight={160} fit="contain"/>
    **Lado B — Construir**

    <text color="secondary" size="sm">Aprender a experimentar deliberadamente, conservar lo aprendido y construir sistemas que podamos recrear.</text>
  </grid-item>
</grid>

La transición entre los lados es el momento en que dejamos de preguntarnos solamente qué podemos hacer con estas herramientas y empezamos a preguntarnos cómo queremos trabajar y pensar con ellas.

## 3. Las cuatro piezas que sostienen el argumento

| Pieza | Qué queremos mostrar | Pregunta que responde |
|---|---|---|
| **El conocimiento** | Cómo procesamos, organizamos y hacemos verificable lo que sabemos. | ¿Qué entendemos realmente? |
| **El ambiente experimental** | Cómo hacemos barato crear variantes, ejecutarlas, medirlas y descartarlas. | ¿Cómo descubrimos si nuestras ideas funcionan? |
| **La estructura del software** | Cómo separamos contratos, implementaciones, datos y evaluaciones. | ¿Cómo podemos cambiar de idea sin empezar de cero? |
| **El software como sustrato** | Cómo usamos programas para expresar, ejecutar y revisar nuestros modelos mentales. | ¿Qué papel cumple el software en nuestro pensamiento? |

Estas piezas se necesitan mutuamente.

- Sin conocimiento organizado, olvidamos por qué tomamos decisiones.
- Sin un ambiente experimental, nuestras ideas quedan en especulaciones.
- Sin una estructura reemplazable, cada aprendizaje se vuelve una reescritura costosa.
- Sin una idea de fondo sobre el software como instrumento de pensamiento, todo se reduce a técnicas de programación.

## 4. El ejemplo conductor: procesar conocimiento

Bajan puede ser el caso concreto que permite recorrer todo el argumento sin convertir la charla en una presentación de un proyecto.

<AsyncImage query="knowledge graph document information extraction provenance graph visualization" aspectRatio="16:9" width="100%"/>

Partimos de una idea:

> Queremos convertir documentos en conocimiento estructurado, conservando la evidencia que respalda cada afirmación.

Después la hacemos ejecutable:

1. Los documentos se convierten en episodios.
2. Un extractor propone afirmaciones.
3. Las afirmaciones se validan y vinculan con evidencia.
4. Un corpus de referencia permite evaluar los resultados.
5. Probamos otros extractores sin cambiar el criterio de evaluación.

Tenemos incluso un resultado real para mostrar: en una evaluación de referencia de Bajan, el extractor determinista obtuvo 75,2 % de precisión, 88,4 % de recall y 92,9 % de preservación de matices. Aparecieron falsos positivos concretos que nos permiten formular una hipótesis nueva: ¿podemos aprovechar la estructura del documento para mejorar la extracción? Es una medición de un corpus acotado, no una afirmación general sobre la calidad del sistema. 

Ahí aparece la charla entera en miniatura:

- Una idea se transforma en un modelo.
- El modelo se convierte en un programa.
- El programa produce resultados.
- Los resultados desafían el modelo.
- Construimos otra implementación.
- Conservamos el corpus, los contratos y lo aprendido.

Whisper puede complementar este ejemplo con otra idea: cómo conservar revisiones y conocimiento mediante snapshots, cambios controlados y commits verificados. <MemoryCite />

## 5. Qué significa estructurar el software para crear y recrear

Esta es la parte más técnica y también una de las más importantes.

No queremos una arquitectura que proteja una implementación para siempre. Queremos una arquitectura que permita reemplazar implementaciones sin perder las cosas que ya sabemos.

Lo que debería sobrevivir:

- Los ejemplos reales.
- Los contratos de comportamiento.
- Las propiedades e invariantes verificadas.
- Los corpus de evaluación.
- Los resultados de los experimentos.
- Las decisiones y sus motivos.
- Los contraejemplos y resultados negativos.

Lo que debería poder desaparecer:

- El primer algoritmo.
- Una implementación particular.
- Un prompt.
- Una biblioteca.
- Una estructura interna.
- Una abstracción que dejó de ser útil.

La distinción fundamental:

**No necesitamos que el código sea permanente. Necesitamos que el conocimiento sea acumulativo.**

## 6. Las doce diapositivas como recorrido

Una posible organización conceptual de las doce, manteniendo los dos lados:

| Diapositiva | Lado A — Descubrir | Diapositiva | Lado B — Construir |
|---:|---|---:|---|
| 1 | After Chatbon: cambia el costo de producir software | 7 | Necesitamos un ambiente para experimentar |
| 2 | Escribir para pensar antes de pedir respuestas | 8 | Las ideas como hipótesis ejecutables |
| 3 | Del pensamiento al modelo y del modelo al programa | 9 | Medir, comparar, encontrar contraejemplos |
| 4 | Ejecutar desafía nuestras ideas | 10 | Estructurar para poder reemplazar implementaciones |
| 5 | El ejemplo: transformar documentos en conocimiento | 11 | Preservar lo aprendido al recrear el software |
| 6 | Lo que el primer intento nos revela | 12 | El software como sustrato de nuestras ideas |

No tomaría esta tabla como un cambio obligatorio de las doce diapositivas existentes, sino como el mapa para verificar que cada una cumple una función en la historia.

---

## 7. Lo que realmente estamos proponiendo

Hay una distinción que me parece esencial para el cierre.

No estamos proponiendo simplemente una metodología para escribir mejor software. Estamos proponiendo otra relación con el software:

- No verlo solamente como un producto terminado.
- No verlo solamente como una herramienta que automatiza tareas.
- No verlo solamente como código que hay que mantener.
- Verlo como un medio para desarrollar, expresar y poner a prueba nuestro conocimiento.

Eso cambia también cómo pensamos la arquitectura, los tests, la documentación y el rol de la IA.

La frase que reúne todo:

# El software puede ser el lugar donde nuestras ideas se vuelven ejecutables, donde la realidad las desafía y donde lo que aprendemos toma forma.

Y dejaría como frase final, quizá incluso más memorable:

**El código puede morir. Las ideas pueden cambiar. Pero lo que aprendimos debería sobrevivir.**

Ese es, para mí, el verdadero argumento de *After Chatbon*.

## User

el lado A debería ser una demo de como usar uv para crear un proyecto de python y el lado b como usar vanillajs para crear una SPA que me ayude a visulaizar e interactuar con lo que construi

## Assistant

¡Ahora sí! Esto cambia bastante la interpretación de los dos lados y hace que la estructura sea mucho más concreta. **Cada lado del disco es una experiencia de construcción, con una herramienta y un propósito diferente.** Y ambos producen partes de un mismo sistema.

No son dos demos independientes: construimos algo en el lado A y, en el lado B, construimos el instrumento que nos permite verlo, explorarlo y cuestionarlo.

# After Chatbon: dos lados, un mismo experimento

<grid columns={2} gap={3}>
  <grid-item>
    <AsyncImage query="Python programming language logo yellow blue" aspectRatio="5:3" fit="contain"/>
    **Lado A — Python + uv**

    <badge color="success">Construir</badge>
    <title size="xl">Crear un proyecto que procesa conocimiento.</title>
    <text color="secondary" size="sm">Pasar de documentos e información a estructuras, modelos y resultados ejecutables.</text>
  </grid-item>
  <grid-item>
    <AsyncImage query="JavaScript logo yellow black" aspectRatio="5:3" fit="contain"/>
    **Lado B — Vanilla JavaScript**

    <badge color="success">Explorar</badge>
    <title size="xl">Crear una SPA para interactuar con ese conocimiento.</title>
    <text color="secondary" size="sm">Hacer visible lo construido, recorrerlo, filtrarlo, inspeccionarlo y descubrir qué falta.</text>
  </grid-item>
</grid>

## 1. Lado A: Python y uv — expresar una idea como programa

<AsyncImage query="Python terminal code editor project files uv package manager" aspectRatio="16:9" width="100%"/>

La pregunta de partida:

**¿Cómo transformamos documentos en conocimiento que podamos consultar y verificar?**

La demo debería recorrer un ciclo pequeño, pero completo:

1. Crear el proyecto con `uv init`.
2. Definir dependencias y entorno con `uv`.
3. Organizar el código en módulos con responsabilidades claras.
4. Implementar un primer procesamiento de documentos.
5. Representar episodios, afirmaciones y evidencias.
6. Ejecutar sobre ejemplos reales.
7. Verificar resultados y generar una salida estructurada.

El resultado del lado A no es solamente un programa Python. Es un modelo de conocimiento que conseguimos hacer ejecutable.

<box border radius="lg" padding={3} gap={2}>
  **El artefacto que dejamos al terminar el lado A**

  <text color="secondary" size="xs">Ejemplo conceptual de salida</text>
  ```json
  {
    "document": "resolucion.pdf",
    "claims": [
      {
        "text": "La inscripción es obligatoria",
        "evidence": {
          "page": 3,
          "text": "..."
        }
      }
    ]
  }
  ```
  <badge color="success">Contrato de intercambio</badge>
  JSON define qué produce nuestro sistema, independientemente de cómo lo visualicemos.
</box>

La idea importante: no intentamos construir toda la aplicación. Construimos una primera interpretación ejecutable del problema.

## 2. El cambio de lado: lo que construimos también necesita ser observado

Acá está la transición narrativa.

Tenemos un programa que procesa documentos. Tenemos resultados estructurados. Pero leer JSON o mirar logs no es una buena manera de comprender sistemas de conocimiento.

Queremos poder explorar:

- ¿Qué afirmaciones encontramos?
- ¿De qué documentos vienen?
- ¿Qué evidencia las respalda?
- ¿Qué relaciones existen?
- ¿Qué información falta?
- ¿Qué resultados son sospechosos?

Y entonces aparece una segunda pregunta:

**¿Podemos construir una herramienta que nos permita pensar con los resultados de nuestro programa?**

## 3. Lado B: Vanilla JavaScript — construir un ambiente para explorar ideas

<AsyncImage query="minimal vanilla javascript web application knowledge graph interactive dashboard document explorer UI" aspectRatio="16:9" width="100%"/>

La demo parte de un HTML vacío y construye una SPA progresivamente:

1. Crear `index.html`, `app.js` y `style.css`.
2. Usar módulos nativos de JavaScript, sin framework ni build system.
3. Cargar el JSON generado por Python.
4. Renderizar documentos, afirmaciones y evidencias.
5. Agregar selección, filtros y navegación.
6. Permitir inspeccionar relaciones y fragmentos originales.
7. Interactuar con los resultados: marcar problemas, comparar variantes o explorar subconjuntos.

La SPA no es simplemente una interfaz bonita. Es un instrumento de observación.

Al visualizar las afirmaciones junto a sus fuentes, podemos descubrir errores que no habíamos detectado mirando la salida del extractor. Al filtrar y comparar, aparecen patrones. Al inspeccionar los casos problemáticos, surgen nuevas hipótesis.

Y esas hipótesis vuelven al lado A.

## 4. La arquitectura que conecta los dos lados

Esta es una de las diapositivas técnicas centrales.

<box border radius="lg" padding={3} gap={3}>
  <box align="center" gap={1}>
    <badge color="info">Lado A</badge>
    **Python / uv**
    <text color="secondary" size="sm">Ingesta · Procesamiento · Extracción · Validación</text>
    <box background="surface-secondary" radius="md" padding={2} width="100%" align="center">
      <icon name="file-json" size="xl"/>
      **Conocimiento estructurado**
      <text color="secondary" size="xs">JSON · contratos · evidencia · procedencia</text>
    </box>
  </box>
  <box align="center" gap={1}>
    <icon name="arrow-down-up" size="xl" color="success"/>
    <text color="secondary" size="xs">Intercambio mediante un contrato explícito</text>
  </box>
  <box align="center" gap={1}>
    <badge color="info">Lado B</badge>
    **Vanilla JavaScript**
    <text color="secondary" size="sm">Visualización · Navegación · Filtros · Interacción</text>
    <box background="surface-secondary" radius="md" padding={2} width="100%" align="center">
      <icon name="monitor" size="xl"/>
      **Ambiente de exploración**
      <text color="secondary" size="xs">Una vista interactiva del conocimiento construido</text>
    </box>
  </box>
  <divider color="subtle"/>
  <row align="center" justify="center">
    <icon name="repeat" color="success" size="lg"/>
    **Nuevas observaciones → nuevas hipótesis → Python**
  </row>
</box>

Hay una decisión deliberada acá: no necesitamos introducir un framework de frontend, una API compleja ni un sistema distribuido. Para la demo, Python puede generar un JSON y la SPA puede cargarlo desde un servidor estático local. Podemos persistir anotaciones exploratorias en el navegador si hace falta.

Esto permite mostrar una separación muy valiosa: **el modelo de conocimiento no depende de su interfaz, y la interfaz no necesita conocer los detalles internos del procesamiento.**

## 5. Las doce diapositivas, reorganizadas

Con esta interpretación, propondría distribuirlas así:

| N.º | Lado A — Python + uv | N.º | Lado B — Vanilla JS |
|---:|---|---:|---|
| 1 | After Chatbon: el nuevo costo de crear software | 7 | Cambiamos de lado: necesitamos ver lo que construimos |
| 2 | Una idea: transformar documentos en conocimiento | 8 | Una SPA sin framework |
| 3 | Crear el proyecto con uv | 9 | Cargar y visualizar los resultados de Python |
| 4 | Modelar documentos, afirmaciones y evidencia | 10 | Interactuar: explorar, filtrar e inspeccionar |
| 5 | Implementar y ejecutar el procesamiento | 11 | La interfaz como instrumento de experimentación |
| 6 | Evaluar resultados: lo que descubrimos | 12 | El software como sustrato de nuestras ideas |

El ritmo podría ser aproximadamente:

- Introducción y planteo: 3 minutos.
- Lado A: 8 minutos.
- Transición: 1 minuto.
- Lado B: 8 minutos.
- Síntesis y cierre: 5 minutos.

## 6. Lo que demuestra realmente la charla

Hay tres niveles de aprendizaje que se superponen:

**Nivel 1 — Herramientas:** sabemos iniciar un proyecto Python con uv y construir una SPA con JavaScript nativo.

**Nivel 2 — Ingeniería:** sabemos separar procesamiento, datos, contratos y visualización; crear componentes reemplazables y evaluar comportamientos.

**Nivel 3 — Pensamiento:** descubrimos que construir software es una manera de expresar ideas, ejecutarlas, observar sus consecuencias y revisar nuestra comprensión.

El tercer nivel es el que da sentido a los otros dos.

La SPA no es un añadido al programa Python. Es una segunda forma de expresar y explorar el mismo modelo. El procesamiento hace explícita nuestra interpretación; la interfaz nos permite interrogarla.

Y el ciclo completo queda así:

<box background="surface-secondary" radius="lg" padding={3} gap={2}>
  <title size="2xl" textAlign="center">Pensar → Construir → Ejecutar</title>
  <title size="2xl" textAlign="center">Visualizar → Interactuar → Aprender</title>
  <title size="2xl" textAlign="center">Recrear</title>
</box>

**La tesis final:** el software no es solamente algo que construimos para resolver problemas. Es un sustrato donde podemos dar forma a nuestras ideas, hacerlas ejecutables, interactuar con ellas y desarrollar nuevas ideas a partir de lo que descubrimos.

Una observación de diseño: mantendría el ejemplo de procesamiento de conocimiento en ambos lados. Así el público no ve dos tutoriales, sino cómo una misma idea adquiere dos expresiones complementarias: un programa que construye conocimiento y una aplicación que nos permite pensar con él.

## User

Ok en la charla tengo que incluis un par de preguntas generales para el publico lo mismo en el combio de lado y el final, y quizas preferible apuntar a la charla de 20min asi hay timpo para preguntas

## Assistant

Sí. Apuntaría a una charla de **18–19 minutos de contenido, con un máximo de 20**, y reservaría los últimos 8–10 minutos del bloque para preguntas. Eso también obliga a que las demos sean muy enfocadas: mostrar una idea completa, no enseñar exhaustivamente las herramientas.

Las preguntas al público deberían cumplir tres funciones: conectar con experiencias que ya tienen, hacerlos participar en el cambio de lado y dejarles una pregunta que puedan llevarse.

# Propuesta de ritmo: 20 minutos

## Apertura — 2 minutos

No empezaría explicando uv, Python o JavaScript. Primero plantearía el problema.

**Diapositiva 1 — After Chatbon**

Una idea para abrir:

> Hoy podemos producir software mucho más rápido. Pero ¿sabemos mejor qué software necesitamos construir?

**Diapositiva 2 — Preguntas al público**

Haría dos preguntas breves, levantando la mano. No pediría respuestas largas.

1. «¿Quién empezó alguna vez con un script de unas pocas líneas que terminó convirtiéndose en algo difícil de entender o modificar?»
2. «¿Quién usó IA para generar código que funcionaba, pero no estaba seguro de que realmente resolviera el problema correcto?»

Dejaría unos segundos para observar las manos.

La transición:

> Creo que el problema no es solamente cómo producimos código. Es cómo usamos el software para pensar, experimentar y aprender.

## Lado A — Python + uv: construir conocimiento (6–7 minutos)

<badge color="info">0:02–0:09</badge>

| Diapositiva | Contenido | Tiempo |
|---|---|---:|
| 3 | El problema: transformar documentos en conocimiento | 1:00 |
| 4 | Crear el proyecto con `uv` | 1:30 |
| 5 | Modelar documentos, afirmaciones y evidencia | 2:00 |
| 6 | Ejecutar, observar resultados y encontrar errores | 2:00 |

**Objetivo de la demo:** mostrar cómo una idea se convierte en un programa ejecutable.

No hace falta explicar todos los comandos de uv ni cada línea de Python. Lo interesante es que el público vea cómo pasamos de una intuición a un modelo, de un modelo a código y de código a resultados que podemos inspeccionar.

Al terminar, dejaría visible el resultado estructurado que produce Python.

## Cambio de lado — 1:30 minutos

<badge color="success">0:09–0:10:30</badge>

Este debería ser uno de los momentos más importantes de la charla. No lo trataría como una pausa entre demos, sino como una pregunta que justifica la segunda mitad.

Mostraría el JSON producido por Python.

Y preguntaría:

> Ahora tenemos un programa que procesa documentos y produce conocimiento estructurado. ¿Cómo sabemos si ese conocimiento realmente tiene sentido?

Después:

> ¿Alcanza con mirar el JSON? ¿Qué cosas podemos descubrir y cuáles quedan escondidas?

Dejaría que respondan una o dos personas, o simplemente observaría las reacciones durante unos segundos.

Entonces:

> Necesitamos algo más que producir resultados. Necesitamos poder explorarlos, interactuar con ellos y cuestionarlos. Cambiamos de lado.

## Lado B — Vanilla JavaScript: pensar con lo construido (7–8 minutos)

<badge color="info">0:10:30–0:18:30</badge>

| Diapositiva | Contenido | Tiempo |
|---|---|---:|
| 7 | Necesitamos visualizar lo que construimos | 1:00 |
| 8 | Crear la SPA con Vanilla JavaScript | 1:30 |
| 9 | Cargar y visualizar los resultados | 1:30 |
| 10 | Interactuar: filtros, selección y evidencia | 2:00 |
| 11 | Lo que descubrimos al explorar los resultados | 1:30 |

La idea es que la audiencia vea cómo una interfaz sencilla se convierte en un instrumento de investigación.

El momento más importante no es cuando aparece el dashboard. Es cuando interactuamos con él y encontramos algo que nos hace cuestionar el procesamiento original.

Por ejemplo:

- Una afirmación que no tiene evidencia suficiente.
- Varias afirmaciones casi duplicadas.
- Una sección del documento que no se procesó correctamente.
- Un resultado que parece correcto aisladamente, pero pierde sentido en su contexto.

La interfaz nos permite formular una nueva hipótesis que podemos llevar de vuelta a Python.

## Cierre — 1:30 minutos

<badge color="success">0:18:30–0:20</badge>

**Diapositiva 12 — El software como sustrato de nuestras ideas**

Volvería al ciclo:

<box border radius="lg" padding={3} gap={2}>
  <grid columns={3} gap={1}>
    <grid-item background="surface-secondary" radius="md" padding={2} align="center">
      **Pensar**
    </grid-item>
    <grid-item background="surface-secondary" radius="md" padding={2} align="center">
      **Construir**
    </grid-item>
    <grid-item background="surface-secondary" radius="md" padding={2} align="center">
      **Ejecutar**
    </grid-item>
    <grid-item background="surface-secondary" radius="md" padding={2} align="center">
      **Observar**
    </grid-item>
    <grid-item background="surface-secondary" radius="md" padding={2} align="center">
      **Aprender**
    </grid-item>
    <grid-item background="surface-secondary" radius="md" padding={2} align="center">
      **Recrear**
    </grid-item>
  </grid>
  <title size="lg" textAlign="center">Y volver a empezar, pero no desde cero.</title>
</box>

La última pregunta al público:

> ¿Qué idea que hoy tienen solamente en la cabeza podrían convertir en algo ejecutable para ponerla a prueba?

Una pausa. No hace falta que respondan todos.

Y cerraría:

> El software puede ser mucho más que algo que construimos para resolver problemas. Puede ser el lugar donde expresamos nuestras ideas, las ponemos a prueba y desarrollamos nuevas ideas a partir de lo que aprendemos.
>
> El código puede morir. Lo que aprendimos no debería.

Después, abriría las preguntas.

---

## Distribución de tiempo

<box border radius="lg" padding={3} gap={3}>
  <title size="lg">Presupuesto de la charla</title>
  {@body const segments = [{label:"Apertura",minutes:2,color:"#64748b"},{label:"Lado A · Python + uv",minutes:7,color:"#3776ab"},{label:"Cambio de lado",minutes:1.5,color:"#a78bfa"},{label:"Lado B · Vanilla JS",minutes:8,color:"#d6a629"},{label:"Cierre",minutes:1.5,color:"#16a34a"}]}
  <row height="16px" radius="full" clip gap="2px">
    {#each segments as s}
      <box flex={s.minutes} background={s.color}/>
    {/each}
  </row>
  {#each segments as s}
    <row align="center" justify="between">
      <row align="center" gap={2}>
        <box size="10px" radius="xs" background={s.color}/>
        <text size="sm">{s.label}</text>
      </row>
      <text tabularNums weight="medium" size="sm">{s.minutes} min</text>
    </row>
  {/each}
  <divider color="subtle"/>
  <row justify="between">
    **Charla**
    **20 minutos**
  </row>
  <row justify="between">
    **Preguntas**
    **8–10 minutos**
  </row>
</box>

## Tres recomendaciones para que funcione

1. **Las preguntas deben ser fáciles de contestar.** Levantar la mano o responder con una frase. No abrir debates de cinco minutos durante la charla.
2. **Las demos deben estar preparadas en puntos de control.** No gastar tiempo tipeando código que no aporta al argumento. Mostrar las transformaciones importantes y tener resultados preparados si falla una ejecución.
3. **El cambio de lado debe sentirse.** Podés cambiar la diapositiva, el color o incluso la disposición visual. Es el momento en que la audiencia entiende que ya no estamos construyendo el conocimiento, sino construyendo una manera de pensar con él.

Mi recomendación es ensayar para terminar en **18:30**, dejando 90 segundos de margen. En una charla con dos demos, ese margen vale muchísimo.

Y hay una decisión narrativa que conservaría: no anunciar al principio que vas a enseñar uv y Vanilla JS. Primero planteá el problema y hacé que la audiencia quiera ver cómo lo resolvés. Las herramientas aparecen como consecuencia de la idea, no como el tema de la charla.

## User

Ok en la temática del lado A se perdió la idea de necesitamos tener ambientes donde explorar, romper sin preocuparnos. Los dos mensales que quiero que se lleven de la charla son: lo que necesitan es experiencia y saber como obtenerla y el sofware es una sustrato para ayudarnos a pensar

## Assistant

Tenés razón. Habíamos convertido el lado A en una demostración de cómo construir un procesador de conocimiento, pero habíamos perdido algo más importante: **necesitamos crear las condiciones para adquirir experiencia**.

Creo que ahora los dos mensajes centrales quedan mucho más claros:

1. **Necesitamos experiencia, y necesitamos saber cómo obtenerla.** No alcanza con leer documentación, recibir respuestas o generar código. Tenemos que poder probar, equivocarnos, romper cosas, observar qué sucede y volver a intentar.
2. **El software es un sustrato para pensar.** Nos permite expresar ideas como modelos ejecutables, confrontarlas con la realidad, interactuar con ellas y modificarlas a partir de lo que aprendemos.

Los dos lados del disco deberían contar cómo llegamos a esos dos mensajes.

# La nueva narrativa de After Chatbon

<box border radius="lg" padding={3} gap={3}>
  <box gap={1}>
    <badge color="info">Lado A · Python + uv</badge>
    <title size="2xl">Construir un laboratorio</title>
    **Aprender a obtener experiencia.**

    Crear un ambiente aislado, reproducible y descartable donde podamos experimentar con ideas e implementaciones sin miedo a romper algo importante.
  </box>
  <divider color="subtle"/>
  <box gap={1}>
    <badge color="info">Lado B · Vanilla JavaScript</badge>
    <title size="2xl">Construir un instrumento para pensar</title>
    **Usar el software para explorar conocimiento.**

    Crear una aplicación que nos permita visualizar, recorrer, manipular y cuestionar lo que construimos.
  </box>
</box>

## 1. Lado A: construir un laboratorio de experimentación

La pregunta inicial no debería ser «¿cómo creo un proyecto Python?», sino:

> ¿Qué necesitamos para poder probar una idea sin miedo a romper lo que ya tenemos?

La demo con `uv` es una respuesta práctica a esa pregunta.

<AsyncImage query="Python uv terminal project development isolated virtual environment code editor" aspectRatio="16:9" width="100%"/>

El recorrido sería:

1. **Crear un espacio de trabajo:** `uv init`, proyecto propio y entorno virtual.
2. **Controlar el entorno:** dependencias declaradas y reproducibles, lockfile y ejecución consistente.
3. **Separar el experimento:** fixtures, datos de prueba, directorios temporales y resultados descartables.
4. **Construir una primera implementación:** procesar documentos y extraer afirmaciones.
5. **Ejecutar y romper:** cambiar una regla, probar casos difíciles, observar fallos.
6. **Comparar y volver atrás:** conservar resultados, descartar una variante y probar otra.

Una distinción técnica importante: `uv` nos ayuda a gestionar el entorno Python y las dependencias, pero no proporciona por sí solo aislamiento seguro de datos ni reversibilidad. Para eso necesitamos también fixtures, estado descartable, Git y, cuando corresponda, worktrees o contenedores.

**La idea que debe quedar:** no necesitamos ser capaces de predecir todo. Necesitamos tener un lugar donde descubrirlo.

### Preguntas al público para este lado

- ¿Cuántos tienen proyectos que no se animan a modificar porque no saben qué pueden romper?
- ¿Cuántas veces aprendieron más de un experimento que salió mal que de seguir un tutorial?

La segunda pregunta puede aparecer mientras la demo muestra un fallo deliberado.

## 2. El cambio de lado

Este momento tiene que conectar los dos mensajes.

Terminamos el lado A con un programa que procesa documentos y genera conocimiento estructurado.

Mostramos el JSON producido.

Y preguntamos:

> Ahora tenemos algo que funciona. ¿Cómo podemos explorar lo que construimos y descubrir cosas que todavía no entendemos?

O, más provocador:

> ¿Cuánto conocimiento podemos descubrir mirando un archivo JSON?

La respuesta es: probablemente no demasiado.

Entonces cambiamos de lado. Dejamos de construir el procesador y empezamos a construir un instrumento que nos permita pensar con sus resultados.

## 3. Lado B: construir una interfaz para pensar

<AsyncImage query="minimal interactive knowledge graph document explorer web app user interface evidence relationships" aspectRatio="16:9" width="100%"/>

La demo de Vanilla JS debería mostrar cómo:

1. Creamos una SPA sin framework ni build system.
2. Cargamos los resultados generados por Python.
3. Visualizamos documentos y afirmaciones.
4. Navegamos desde una afirmación hasta su evidencia.
5. Filtramos, seleccionamos y comparamos resultados.
6. Encontramos algo inesperado y formulamos una nueva hipótesis.

La interfaz es más que una presentación de resultados: es un nuevo ambiente experimental.

Python nos permite experimentar con cómo construimos el conocimiento. JavaScript nos permite experimentar con cómo lo observamos y lo entendemos.

Y ambos ambientes se retroalimentan.

# 4. Las doce diapositivas revisadas

Esta sería la estructura que conservaría:

| # | Diapositiva | Función |
|---:|---|---|
| 1 | After Chatbon | Introducir el cambio: producir código es más barato, pero adquirir experiencia sigue requiriendo trabajo. |
| 2 | ¿Cómo aprendemos? | Preguntas al público sobre proyectos que temen modificar y experiencias aprendidas al equivocarse. |
| 3 | Necesitamos un laboratorio | Presentar la experimentación como forma de adquirir experiencia. |
| 4 | Python + uv | Crear un entorno de trabajo reproducible. |
| 5 | Romper sin miedo | Separar datos, estado, fixtures e implementaciones. |
| 6 | Experimentar con conocimiento | Procesar documentos, ejecutar, observar errores y comparar variantes. |
| 7 | Cambiamos de lado | ¿Cómo pensamos con los resultados que construimos? |
| 8 | Vanilla JavaScript | Crear una SPA mínima. |
| 9 | Hacer visible el conocimiento | Cargar y visualizar resultados. |
| 10 | Interactuar y explorar | Navegar, filtrar e inspeccionar evidencias. |
| 11 | Descubrir algo que no sabíamos | La interacción revela un problema y genera una nueva hipótesis. |
| 12 | El software como sustrato de nuestras ideas | Integrar los dos mensajes y cerrar. |

## 5. Distribución de los 20 minutos

| Parte | Tiempo |
|---|---:|
| Apertura y preguntas | 2 min |
| Lado A: laboratorio y experimentación | 6,5 min |
| Cambio de lado | 1,5 min |
| Lado B: interfaz e interacción | 8 min |
| Cierre | 2 min |
| **Total** | **20 min** |

Después reservaría 8–10 minutos para preguntas.

## 6. Lo que quiero que se lleven

Creo que no deberíamos cerrar con una lista de herramientas o consejos. Deberíamos volver explícitamente a los dos mensajes.

<box gap={3}>
  <box border radius="lg" padding={3} gap={2}>
    <text color="secondary" weight="medium" size="xs">MENSAJE 1</text>
    <title size="2xl">La experiencia no se descarga. Se construye.</title>
    Necesitamos ambientes donde experimentar sea barato, seguro y reproducible. Necesitamos aprender a formular preguntas, probar ideas, observar resultados y equivocarnos.
  </box>
  <box border radius="lg" padding={3} gap={2}>
    <text color="secondary" weight="medium" size="xs">MENSAJE 2</text>
    <title size="2xl">El software es un sustrato para pensar.</title>
    Podemos expresar nuestras ideas como programas, ejecutarlas, interactuar con ellas y dejar que sus resultados desafíen nuestra comprensión.
  </box>
</box>

Y terminaría con una pregunta:

**¿Qué podrías aprender si tuvieras un lugar donde experimentar sin miedo a romper nada?**

Después, la frase final:

> No necesitamos que la IA piense por nosotros ni que produzca más código. Necesitamos usarla para experimentar más, aprender más y construir mejores formas de pensar.
>
> El código puede cambiar. Las implementaciones pueden desaparecer. Pero la experiencia y el conocimiento que construimos deberían acumularse.

Esta estructura también resuelve algo importante: **uv y Vanilla JS dejan de ser el tema de la charla y se convierten en dos herramientas para demostrar una forma de trabajar**. La audiencia se lleva herramientas concretas, pero sobre todo una manera de adquirir experiencia y pensar mediante software.
