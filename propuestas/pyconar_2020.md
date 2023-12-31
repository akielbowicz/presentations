# PyConAr2020 propuesta de charlas

Ideas de charlas que me gustaría preparar para la Pycon


## Bio

Sasha es un desarrollador de software amateur y autodidacta. Es aficionado por resolver problemas y obsesivo por encontrar soluciones sencillas. Hábitos que obtuvo durante su formación académica en la Facultad de Ciencias Exactas. Además tiene dejos de divulgador científico y cuando puede da charlas en meetups, colegios y otros eventos. Actualmente se desempeña como Quant Developer programando en C#.


## Prefacio a una apología

¿Qué aprendí durante mis primeros dos años trabajando como desarrollador?

Siempre me pasó que al empezar un nuevo trabajo tengo mas dudas de cómo va a ser la experiencia, cuáles van a ser todos los inconvenientes con los cuales me voy a encontrar y que cosas voy aprender. Casi siempre las cosas ocurren de manera muy distinta a lo que me imaginaba y mi perspectiva cambia a medida que van ocurriendo. Hace un poco más de dos años empecé a trabajar de programador no teniendo experiencia profesional ni una formación en el rubro, por lo que quiero compartir mis vivencias y opiniones a todes les que estén arrancando.


En la charla voy a hablar de los miedos, prejuicios y expectativas que tenía al iniciar mi trayecto profesional como programador. También voy hablar sobre cuales son las cosas que me parecen más importantes a tener en cuenta al momento de empezar a trabajar y a tener en cuenta en el ambiente de trabajo.

--------------------
*Miedos con los que empecé y los que siguen.*
Cosas importantes para el trabajo
Cómo aprendí cosas nuevas
Preconceptos de la profesión y realidad

*¿Cuáles son los miedos con los que empecé y cuales sobreviven?*
No poder solucionar los problemas
Escribir código que rompa producción
No mantener el ritmo del equipo
No entender los problemas que me asignaban
No llegar a tiempo con la solución

*¿Cuales son las cosas que ahora considero más importantes al tiempo de trabajar?*
Tener un ambiente en el cual pueda expresar las dudas
Tener una buenas habilidades de comunicación
Tener espacio para experimentar nuevas soluciones
Tener claridad para estimar el trabajo que conlleva el problema
Un espacio para poder documentar el avance

*¿De qué manera aprendí cosas nuevas?*
Interactuando con mis companieres
Tomando cursos especializados
Explorando muuuchas fuentes distintas para un tema
Exponiendo sobre temas que me interesaban
Ayudando a otres 

*¿Qué preconceptos tenía sobre la profesión y como son realmente?*

Los sistemas de producción eran sistemas estables y sin problemas
El desarrollo de nuevos features era directo y sin interrupciones
Las cosas se hacían de una única manera 
No existían tantas especializaciones ni tecnologías



## Kritik des reinen Codes


Métricas para medir la calidad de tu código

A medida que un programa crece, crece su complejidad. Además existen muchas formas de obtener una misma solución, cada una con distintas características y cualidades para que sean aptas para variadas situaciones. 
Pero algo característico del software es que es algo maleable y que cambia constantemente, de ahí viene el *soft*, y hay soluciones que hacen de nuestras soluciones más rígidas que otras lo cual trae complicaciones a futuro.

Para evitar esos problemas es necesario evaluar las soluciones y tener un control sobre el estado del código. Para eso existen distintas métricas para cuantificar las características del software y poder comparar las distintas soluciones.


La charla va a estar guiada por las siguiente preguntas

¿Qué mide realmente cada una de estas métricas?  
Y ¿cómo puedo utilizarlas para mejorar mi código?

Y voy a exponer las siguientes métricas divididas en dos grupos y  las herramientas disponibles en Python para evaluarlas

Métricas más usuales:
Numero de lineas
Complejidad ciclomática
Índice de mantenibilidad
Cobertura de tests

Métricas más complejas:
Indice ABC
Cognitive complexity




## Conozco un grupo de objetos que resuelven problemas

Los Decoradores:

Ep.1 El origen de una solución
Ep.2 El problema en la serpiente
Ep.3 Cuatro porciones para llevar
Ep.4 El recambio de yerba


En la charla voy a hablar sobre
¿Qué son los decoradores?
¿Cómo se implementan los decoradores en Python?
Exponer una distinción en los distintos usos/tipos de decoradores
Exponer mis opiniones sobre que tener en cuenta al utilizar decoradores


*¿Qué son los decoradores?*

Los decoradores como patrón de diseño, 

*¿Cómo se usan los decoradores en Python?*

Objeto que recibe un Callable y devuelve un callable

*Distinción de los distintos tipos de decoradores que se pueden implementar*

Tagging, Control flow, Descriptive, Executing

*Cosas importantes a tener en cuenta al utilizar decoradores*

Agregar características ortogonales a nuestros objetos de manera dinámica
Agrega complejidad en una sola línea de código
Implementación, función, parametrizable, clase



## Bug through the ./run and you're to blame
Scripting, you give code a bad name :dark_sunglasses:

¿Es posible utilizar JupyterLab como ambiente de desarrollo?

El ecosistema de herramientas asociadas a Jupyter es cada vez más extenso. Pero una de las mayores críticas para el desarrollo de soluciones es el  uso de Notebooks como principal ambiente de trabajo. En la charla vamos a explorar cuáles son las características ideales para el desarrollo de código y algunas de las soluciones existentes para utilizar en JupyterLab 


- ¿Qué es necesario para poder desarrollar código?

Editor de texto
Posibilidad de tener linting
Ejecución del código
Integración con el test runner
Debugger integrado

- ¿Qué herramientas están disponibles para facilitar el desarrollo dentro de jlab?

Julynter
Pytest nbval


## Tres tristes unit tests

“Una vez que le agarres la mano no va a haber vuelta atrás” debe ser una de las frases más dichas al enseñar sobre los test unitarios. Pero siempre queda corta para demostrar las bondades y problemas que acarrea su uso. Algo muy importante es que es necesario ejercitar mucho como implementar test unitarios para comprender su beneficio en situaciones más complejas. Además, al principio es extremadamente complicado entender qué es lo que hay que testear y cómo testearlo. 

Acá vamos a poner a prueba ( o testear ) la manera en la que pensamos sobre los test unitarios cuando no sabemos nada de test unitarios. ¿Hace sentido lo que digo? Quizás tengas que ver la charla para comprobarlo.


En la charla se va a hablar sobre:
- ¿Qué es un Test Unitario (TU)?
- ¿Para qué sirve un TU?
- ¿Por qué es tan complicado implementar un TU?

*¿Qué es un Test Unitario (TU)?*

Self testing code
Automatizar la evaluación de tu código 


*¿Para qué sirve un TU?*

Validar tu código
Documentar cómo se usa tu código
Presión sobre el código que demuestra fallas en el diseño del código
Red de contención para realizar cambios de manera segura

*¿Por qué es tan complicado escribir un TU?*

Testeamos implementación 
El diseño no es el adecuado 