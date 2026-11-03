<!-- .slide: id="titulo" -->

# Software científico e IA: cómo usar LLMs sin romper todo

**PyDay La Plata**

**7 de Noviembre 2026**

[saxa.xyz/charla-rs](https://saxa.xyz/charla-rs)

---

<!-- .slide: data-transition="none" -->

### Sasha

Consultor independiente

**[Phorma Scientific](https://phorma.sh)** 

--

- Estudié Física en la UBA
- Trabajé como Desarrollador de Software en **JP Morgan**
- Trabajé como Lead Quant Developer en **Qontigo/Simcorp** *(Quantitative Pricing and Risk Analytics)*
- Trabajé como Líder Técnico en **Mercado Libre** *(IT Staff, Financial Planning & Analysis)*
- Trabajé como Senior AI Engineer en **AstraZeneca** *(R&D Oncology)*

NOTES:
Acá tengo que mencionar un par de cosas de que me interesa y que motiva esta charla

--

No me gusta programar, 

me gusta resolver problemas.
<!-- .element: class="fragment" -->

--

Los generadores (probabilísticos) de texto^1 son una gran ayuda.

^1: Grandes Modelos de Lenguaje

---

<!-- 3	Presentación del problema	3 min -->

El Software Científico tiene características muy distintas a los de una aplicación
comercial.

- Experimental
- Dinámico
- Repetitivo

--

```py
#armar script de tiro parabólico
Y el plot
```

--

¿Cuáles son las prácticas de Ingeniería de Software que podemos re-utilizar para mejorar nuestras herramientas?

--

Artesanía de Software

> Prácticas y metodologías para producir artefactos de mejor calidad.
<!-- .element: class="fragment" -->

NOTES:
Importante mencionar la escala del software

---

<!-- 4	IA como herramienta	3 min -->

Lo que cambió es el sustrato sobre el que trabajamos:

Madera -> Melamina/MDF
<!-- .element: class="fragment" -->

Escribir código -> Generar código
<!-- .element: class="fragment" -->

NOTES:
Necesitamos mucho más control sobre lo que hacemos.

--


NOTES:
En esta charla no vamos a hablar de Regla y Escuadra y no de Serrucho y Martillo

--

Al poder producir de manera probabilística el código,
necesitamos establecer protocolos, procedimientos que nos ayuden a 
elegir, evaluar, verificar lo que se produce.


NOTES:

No se trata de producir más código, necesitamos producir cosas de mayor calidad.

--

El valor del código es despreciable, es como el plástico, es algo descartable. 

Lo que tiene valor es lo que produce.
<!-- .element: class="fragment" -->

En vez de crear un montón de cosas, tenemos que enfocarnos en mejorar la calidad.
<!-- .element: class="fragment" -->

--

<h2 style="color: #e53935;">WARNING</h2>

Los proveedores de tokens quieren que utilicemos sus herramientas lo más que se pueda, están diseñadas para ser adictivas.  <!-- .element: class="fragment" -->

Piensen en los Chats en los mismos términos que Facebook, Instagram, TikTok, X/Twitter.... <!-- .element: class="fragment" -->

- ¿Cuántas horas al día lo utilizan? <!-- .element: class="fragment" -->
- ¿Cuántas menos interacciones con otros seres humanos tienen? <!-- .element: class="fragment" -->
- ¿Qué información le están entregando? <!-- .element: class="fragment" -->

---

<!-- 5	Fricción: serialización	3 min -->

Lo más importante es lograr un código bien modularizado, que nos permita
abstraer componentes.

--

```py
from math import cos, radians, sin
import matplotlib.pyplot as plt

velocidad = 10  # m/s
angulo = radians(45)
gravedad = 10  # m/s²

vx = velocidad * cos(angulo)
vy = velocidad * sin(angulo)
duracion = 2 * vy / gravedad
t = [duracion * i / 100 for i in range(101)]
x = [vx * instante for instante in t]
y = [vy * instante - gravedad * instante**2 / 2 for instante in t]

plt.plot(x, y)
plt.savefig("trayectoria.png")
```

Necesitamos registrar los inputs y los outputs
<!-- .element: class="fragment" -->

--

```py
import json
from pathlib import Path

entrada = {"velocidad": 10, "angulo": 45, "gravedad": 10}
Path("entrada.json").write_text(json.dumps(entrada, indent=2), encoding="utf-8")
```

```py
# script de tiro parabólico
entrada = json.loads(Path("entrada.json").read_text(encoding="utf-8"))
velocidad = entrada["velocidad"]
angulo = radians(entrada["angulo"])
gravedad = entrada["gravedad"]

# ... las mismas ecuaciones de antes ...
```
<!-- .element: class="fragment" -->

--

```py
# script de tiro parabólico
from tiro_parabolico import simular

entrada = json.loads(Path("entrada.json").read_text(encoding="utf-8"))
salida = simular(**entrada)
```

```py
registro = {"entrada": entrada, "salida": salida}
Path("resultado.json").write_text(json.dumps(registro, indent=2), encoding="utf-8")
```
<!-- .element: class="fragment" -->

--

Este cambio en las restricciones que le imponemos a nuestro código nos permite pensar en nuestro sistema de manera modular y componible.

---

<!-- 6	Diseño / Implementación / Verificación	4 min -->

--

Lo que necesitamos es entender lo que un sistema hace, y poner restricciones.

Conversar, describir lo que queremos hacer, entender que tiene que pasar y cómo puede fallar.

Describirlo en lenguaje natural, o explicito como pruebas automáticas (tests) o propiedades. 

Intención, Restricciones, Propiedades/Invariantes

NOTES:

Tracer bullet

--


<iframe width="560" height="315" src="https://www.youtube.com/embed/c5QF2HjHLSE?si=96Hcss0gU9AApBwv&amp;controls=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

[Design In Practice](https://www.youtube.com/watch?v=c5QF2HjHLSE)


[WAI Decision Matrix](https://charly-vibes.github.io/wai/concepts/decision-matrix.html) <!-- .element: class="fragment" --> 

--

Pruebas Automáticas

NOTES:
Acá es donde el mayor valor del LLM aparece, en sintetizar el código para lo que queremos.
Pero las especificaciones en texto no son ejecutables, así que tenemos que construir la definición en algo ejecutable, que cada vez que cambiemos algo nos avise si rompimos algo.


--

```py
import pytest

from tiro_parabolico import simular


def test_lanzamiento_a_45_grados():
    salida = simular(velocidad=10, angulo=45, gravedad=10)

    # Calculado a mano: alcance = v²·sen(2θ)/g, duración = 2v·sen(θ)/g, h = v²·sen²(θ)/(2g)
    assert salida["alcance"] == pytest.approx(10)
    assert salida["duracion"] == pytest.approx(2**0.5)
    assert salida["altura_maxima"] == pytest.approx(2.5)
```

--

```py
@pytest.mark.parametrize("angulo, alcance", [
    (0, 0),
    (30, 5 * 3**0.5),
    (45, 10),
    (60, 5 * 3**0.5),
    (90, 0),
])
def test_alcances_conocidos(angulo, alcance):
    salida = simular(velocidad=10, angulo=angulo, gravedad=10)
    assert salida["alcance"] == pytest.approx(alcance, abs=1e-12)
```

--


```py
from hypothesis import given, strategies as st


@given(angulo=st.floats(min_value=1, max_value=89))
def test_angulos_complementarios_tienen_el_mismo_alcance(angulo):
    uno = simular(velocidad=10, angulo=angulo, gravedad=10)
    otro = simular(velocidad=10, angulo=90 - angulo, gravedad=10)
    assert uno["alcance"] == pytest.approx(otro["alcance"])
```


--

Implementación

--

Verificación y Validación

NOTES:

Para validar y verificar podemos pedir que nos cree herramientas
que nos permitan visualizar los resultados

--

<div style="display: grid; grid-template-columns: 1.2fr 1fr; gap: 1.5rem; align-items: start; font-size: 0.8em;">
<div>
<h4>Trayectoria — Python en el navegador</h4>
<div id="tray-editor">
<pre id="tray-highlight" aria-hidden="true"><code class="hljs language-python"></code></pre>
<textarea id="tray-codigo" spellcheck="false" wrap="off"></textarea>
</div>
<p>
<button id="tray-boton" onclick="ejecutarPyodide('tray')">▶ Ejecutar</button>
<button onclick="restablecerTrayectoria()">↺ Restablecer</button>
<span id="tray-estado" style="color: #999;"></span>
</p>
</div>
<div>
<img id="tray-imagen" style="display: none; max-height: 15rem;">
<pre id="tray-salida" style="text-align: left; font-size: 0.5em;"></pre>
</div>
</div>

--

<div style="font-size: 0.8em;">
<h4>Resultados de las simulaciones</h4>
<p>
<input type="file" id="res-archivo" accept=".json,application/json">
<button id="res-boton" onclick="graficarResultado()">Graficar</button>
<span id="res-estado" style="color: #999;"></span>
</p>
<img id="res-imagen" style="display: none; max-height: 12rem;">
</div>

---

<!-- 7	Extensión y evolución	3 min -->

--

```py
# computo de sensibilidades
```

--



--

<iframe width="560" height="315" src="https://www.youtube.com/embed/F8fBgDCf2Y4?si=KUeMyrdQTVIwb4Cf&amp;controls=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

[Kent Beck: Software Engineering in the Age of AI](https://www.youtube.com/watch?v=F8fBgDCf2Y4)

--

```py
import json
import random
from pathlib import Path
from tiro_parabolico import simular

random.seed(42)  # experimento reproducible
experimentos = {
    "velocidad": [
        simular(velocidad=random.gauss(10, 0.5), angulo=45)
        for _ in range(1000)
    ],
    "angulo": [
        simular(velocidad=10, angulo=random.gauss(45, 2))
        for _ in range(1000)
    ],
}
Path("montecarlo.json").write_text(json.dumps(experimentos), encoding="utf-8")
```

```py
experimentos = json.loads(Path("montecarlo.json").read_text(encoding="utf-8"))
for nombre, lanzamientos in experimentos.items():
    for lanzamiento in lanzamientos:
        plt.plot(lanzamiento["x"], lanzamiento["y"], alpha=0.1)
    plt.title(f"Monte Carlo variando {nombre}")
    plt.savefig(f"montecarlo-{nombre}.png")
    plt.close()
```
<!-- .element: class="fragment" -->

--

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; align-items: center;">
<img src="./images/montecarlo-velocidad.png" style="width: 100%; height: auto;">
<img src="./images/montecarlo-angulo.png" style="width: 100%; height: auto;">
</div>

<p class="fragment" style="font-size: 0.7em;">velocidad: 8.39 a 11.82 m — angulo: 9.91 a 10.00 m</p>

<p class="fragment" style="font-size: 0.7em;">cerca de 45 grados, controlar la velocidad importa mucho más que el angulo</p>

--

"Revisemos que esto no sea YAGNI"  <!-- .element: class="fragment" --> 

"No estamos haciendo sobre-ingenieria"  <!-- .element: class="fragment" --> 

--

<span class="fragment" data-fragment-index="1">A</span>
<span class="fragment" data-fragment-index="0">B</span>

---

<!-- 8	P.H.O.R.M.A.	2 min -->

- Probado (testado, validado) <!-- .element: class="fragment" --> 
- Habitable (legible, human-friendly) <!-- .element: class="fragment" -->
- Operable (ejecuta en cualquier lugar) <!-- .element: class="fragment" -->
- Robusto (maneja fallas de manera correcta) <!-- .element: class="fragment" -->
- Mantenible (construido para durar) <!-- .element: class="fragment" -->
- <!-- .element: class="fragment" --> Auditable (transparente, rastreable/traceable) 

--

<!-- .slide: data-transition="none" -->

- **P**robado (testado, validado) 
- **H**abitable (legible, human-friendly)
- **O**perable (ejecuta en cualquier lugar)
- **R**obusto (maneja fallas de manera correcta) 
- **M**antenible (construido para durar) 
- **A**uditable (transparente, rastreable/traceable)

--

**P.H.O.R.M.A**

---

<!-- .slide: id="servicios" -->

## De la Teoría a la Práctica

Llevamos estos principios a tu código de producción.
<!-- .element: class="fragment" -->

--

<img src="./images/logo.svg" class="light-theme-logo" width="50%" style="display: block; margin: 0 auto;">
<img src="./images/logo-invertido.svg" class="dark-theme-logo" width="50%" style="display: none; margin: 0 auto;">

### [Phorma Scientific](https://phorma.sh/es)

**Rigor. Rendimiento. Arquitectura.**

--

### [Phorma Scientific](https://phorma.sh/es)

**Rigor. Rendimiento. Arquitectura.**

<div style="font-size: 0.9em; margin-top: 2rem;">

— Auditoría de Sistema y Arquitectura

— Ingeniería de Software de Investigación (RSE)

— Machine Learning Científico (SciML)

— Síntesis de Rendimiento

</div>


--


### Capacitación Técnica

**Para laboratorios de investigación y equipos de I+D**

<div style="font-size: 0.9em; margin-top: 2rem;">

- Fundamentos de Computación Numérica
- Rigor de Producción (TDD, CI/CD)
- Machine Learning Científico
- Diseño de Sistemas Cuantitativos

</div>

<p style="margin-top: 2rem;">
<a href="https://phorma.sh/es/trainees" style="border-bottom: 2px solid;">phorma.sh/es/trainees</a>
</p>

--

> Una técnica que te sirve para escribir te tiene que servir también para vivir. O sea que si yo lo único que te voy a dar es tecniquería (sic), no sirve para nada. 
— **Fabián Casas**

--

<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%;">

<div style="margin-top: 2rem; font-size: 1.2em;">

**[info@phorma.sh](mailto:info@phorma.sh)**

</div>

<p style="margin-top: 2rem; font-family: monospace; color: #666;">
Estructura sobre el Caos
</p>

</div>

---

<!-- .slide: id="gracias" -->

## Gracias
