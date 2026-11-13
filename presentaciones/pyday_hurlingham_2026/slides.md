<!-- .slide: id="titulo" -->

# After•Chatbon <!-- .element: class="fragment" -->

**PyDay Hurlingham**

**14 de Noviembre 2026**

[saxa.xyz/charla-after-chatbon](https://saxa.xyz/charla-after-chatbon/) <!-- .element: class="fragment" -->

--

- Física en la **UBA**
- Desarrollador de Software en **JP Morgan** *(Rates, CIB)*
- Lead Quant Developer en **Qontigo/Simcorp** *(Quantitative Pricing and Risk Analytics)*
- Líder Técnico en **Mercado Libre** *(IT Staff, Financial Planning & Analysis)*
- Senior AI Engineer en **AstraZeneca** *(R&D Oncology)*

NOTES:
0:25 — 3 hitos, sin leer línea por línea.

--

No me gusta programar,

me gusta resolver problemas.
<!-- .element: class="fragment" -->

--

#### A: Necesitamos ambientes donde podamos explorar y experimentar sin miedo a romper

#### B: Necesitamos entender de que manera los humanos tienen que validar/verificar los resultados

---

## WARNING

Los proveedores de tokens quieren que utilicemos sus herramientas lo más que se pueda,
 están diseñadas para ser adictivas.  <!-- .element: class="fragment" -->

Piensen en los Chats en los mismos términos que Facebook, Instagram, TikTok, X/Twitter.... <!-- .element: class="fragment" -->

- ¿Cuántas horas al día lo utilizan? <!-- .element: class="fragment" -->
- ¿Cuántas menos interacciones con otros seres humanos tienen? <!-- .element: class="fragment" -->
- ¿Qué información le están entregando? <!-- .element: class="fragment" -->

NOTES:
0:45 — UNA sola pregunta retórica (la de horas/día), no las tres. Si va tarde: una frase y seguir.
mejor no hablar de ciertas cosas

---

<!-- 01 Crua chan  · ~1:00 -->

## “Come on Hurlingham, here we come”

--

## [Charly Vibes](https://charly-vibes.github.io/)

[![](https://avatars.githubusercontent.com/u/245880461)](https://charly-vibes.github.io/)


NOTES:
No va a ser una charla fácil, necesito que presten atención. Es sencilla en apariencia pero crece de manera rizomática
y van a tener que regresar muchas veces.

--

<iframe src="https://charly-vibes.github.io/jams/sensor-log/" width="880" height="480" title="Sensor Log"></iframe>

https://charly-vibes.github.io/jams/sensor-log/

NOTES:
01 total 1:00 — narrar sobre el iframe, sin interactuar. Si el wifi falla: URL desnua + números de memoria (0,9 MB/min con los 6 a 60 Hz).

--

memoria a 60 Hz:
<!-- .element: style="text-align: center; margin: 0;" -->

| duración | 1 sensor | los 6 sensores |
|---|---|---|
| 1 min | 3.600 lecturas · 150 KB | 21.600 · 0,9 MB |
| 10 min | 36.000 · 1,5 MB | 216.000 · 8,8 MB |
| 30 min | 108.000 · 4,5 MB | 648.000 · 26 MB |
| 1 hora | 216.000 · 9,1 MB | 1.296.000 · 53 MB |
<!-- .element: style="font-size: 0.64em; width: fit-content; margin: 0 auto;" -->

---

<!-- 02 No tan distintos · ~1:00 -->

#### ¿Cómo aprendemos?

NOTES:
1:00 — pregunta que abre el bloque 02–06; la respuesta la construye la cadena de 03.

<!-- 03 Banderitas y globos · ~1:30 -->

[uv](https://docs.astral.sh/uv/) <!-- .element: class="fragment" -->
-> [Github Actions](https://github.com/charly-vibes/dulce-de-leche/actions/workflows/ci.yml) <!-- .element: class="fragment" -->
-> [docker](https://www.docker.com/) <!-- .element: class="fragment" -->
-> [devenv.sh](https://devenv.sh/) <!-- .element: class="fragment" -->

NOTES:
1:30 — nombrar la cadena sin abrir los links; si va tarde, solo uv+CI.
lo entendido es lo que no entiendo

--

<!-- 04 Mañana en el Abasto · ~1:00 -->

- ¿Cómo recrear el software, hacer que funcione 
y que los cambios que hagamos avancen y no retrocedan?


NOTES:
1:00 — la pregunta guía del resto; dejar que llegue sola, sin desarrollar.
“No tengas miedo, no”

--

<!-- 05 Hola Frank · ~1:15 -->

## Oh mama, what did you do? 

#### ¿Cómo registro<!-- .element: class="fragment" -->

- las decisiones, las investigaciones, las distintas opciones evaluadas, las [comparaciones de diseño](https://charly-vibes.github.io/wai)?<!-- .element: class="fragment" -->
- la [funcionalidad que realmente esperamos](https://charly-vibes.github.io/specodelic)?<!-- .element: class="fragment" -->
- lo que [aprendo](https://charly-vibes.github.io/bajan)?<!-- .element: class="fragment" -->
- lo que es puramente [operacional](https://charly-vibes.github.io/whisper)?<!-- .element: class="fragment" -->

NOTES:
1:15 — nombrar wai y bajan; specodelic y whisper quedan visuales.
--

<!-- 06 Ojos de terciopelo · Entender el sistema · ~1:30 -->

- ¿Cómo puedo subir los [estándares de calidad](https://charly-vibes.github.io/pretender) del código que se produce y restringir lo que se acepta?<!-- .element: class="fragment" -->
- ¿Cómo hago para que las verificaciones [corran más rápido](https://charly-vibes.github.io/testaruda)?<!-- .element: class="fragment" -->
- ¿Cómo verifico que el código [cumple con las especificaciones](https://charly-vibes.github.io/espectacular)?<!-- .element: class="fragment" -->
- ¿Cómo tengo que dividir las [tareas](https://charly-vibes.github.io/incitaciones/content/distilled/issue-review-unified.md)?<!-- .element: class="fragment" -->

NOTES:
1:30 — frags de a 2; sin leer cada bullet.
I showed her where to go
she showed me what to do
i’d do the same for me right now
that I’d do for you 

--

- ¿Cómo descomponemos nuestro software en partes más pequeñas en las que podemos **releas**ear?
- ¿Cómo construyo sistemas en los cuales pueda cambiar los componentes de manera segura?
- ¿Cómo se propagan las dependencias?
- ¿Cómo tiene que ser el [versionado](https://charly-vibes.github.io/wild)?<!-- .element: class="fragment" -->

--


[Github Pages](https://github.com/charly-vibes/dulce-de-leche/blob/main/.github/workflows/docs.yml)<!-- .element: class="fragment" -->

[Cloudflare (Pages, Worker, Tunnel, ...)](https://www.cloudflare.com/)<!-- .element: class="fragment" -->
[auth0](https://auth0.com/)<!-- .element: class="fragment" -->
[Tailscale](https://tailscale.com/)<!-- .element: class="fragment" -->


---

#### A: <span class="fragment">Necesitamos ambientes donde podamos explorar y experimentar sin miedo a romper</span>

---

<!-- 07 Lo quiero ya · ~0:45 -->

### No sé lo que quiero

#### pero lo quiero ya!<!-- .element: class="fragment" -->

--

- Tenemos que aprender a interpretar las intenciones <!-- .element: class="fragment" -->
<!-- - ¿Por qué seguimos recreando las interfaces de usuario como dashboards? -->

- Software especializado para que un humano pueda completar la validación <!-- .element: class="fragment" -->

- Qué es un proceso repetible <!-- .element: class="fragment" -->

NOTES:
0:45 sección — mostrar el JSON crudo 1 segundo; promesa: el visor lo hace visible.

--

<!-- 08 La gota en el ojo · Vanilla JS · ~1:30 -->

## Do it right man

**SPA** <!-- .element: class="fragment" -->

**PWA** <!-- .element: class="fragment" -->

**VanillaJS** <!-- .element: class="fragment" -->

--

<iframe src="./demo/visor/index.html" width="880" height="480" title="Sensor Log"></iframe>

[Dashboard](./demo/visor/index.html)

NOTES:
CHECKPOINT 10:00 — acá hay que estar entrando al visor. 1:30: titular + chips quieto/sacudón. El demo nunca extiende su budget.

--

<!-- 09 El cieguito volador · ~1:30 -->

## yo estoy al derecho / dado vuelta estás vos

- ¿Qué actividades se repiten y son directas? <!-- .element: class="fragment" -->
- ¿Qué se puede automatizar? <!-- .element: class="fragment" -->
- ¿Qué tiene que ser determinista? <!-- .element: class="fragment" -->
- ¿Cómo puedo simplificar la validación o interacción necesaria parte de un humano? <!-- .element: class="fragment" -->

NOTES:
1:30 — slider con deep-link ?tramo=8&tasa=15 ("existe pero miente") y volver a 40 Hz.
---

<!-- 10 No te pongas azul · ~0:45 -->

## We all know, we all know, we all know

- Vamos a necesitar expertos que puedan construir herramientas y procesos transparentes
- Entender cómo re-construir cajas negras

NOTES:
0:45 — dos frases y fluir hacia el sueño.

--

<!-- 11 Noche de paz · mensaje A · ~1:00 -->

## “Sueña un sueño imposible”

NOTES:
1:00 — beat A: IA para MEJOR calidad, no más código.

Utilizar las nuevas herramientas para producir software de mejor calidad

en vez de simplemente generar más código.<!-- .element: class="fragment" -->

--

<!-- 11 Noche de paz · mensaje B payoff · ~1:00 (sección 11: 2:00) -->

## “Sueña TU sueño imposible”

NOTES:
1:00 — payoff del mensaje B; NO recortar esta diapo.

Aprovechar las capacidades de la IA y simplificar sistemas y procesos complejos

Hacer tecnologías accesibles e inclusivas. <!-- .element: class="fragment" -->

---

#### B: <span class="fragment">Necesitamos entender de que manera los humanos tienen que validar/verificar los resultados </span>

NOTES:
1:15 con incitaciones — síntesis de los dos mensajes; incitaciones: destacar YAGNI, causa/enfermedad y Rule of 5 sin leer los prompts completos.

---

## [Pequeñas incitaciones para guiar a la IA](https://charly-vibes.github.io/incitaciones)


"Revisemos que esto no sea YAGNI"  <!-- .element: class="fragment" -->

"No estamos haciendo sobre-ingeniería?"  <!-- .element: class="fragment" -->

"Entendamos cuál es la causa y no la enfermedad"  <!-- .element: class="fragment" -->

--

## [Pequeñas incitaciones para guiar a la IA](https://charly-vibes.github.io/incitaciones)


"¿Por qué no detectamos esto antes? 
y ¿cómo podemos garantizar que no ocurra otra vez?"

"Revisa que el prompt no tenga sesgos (bias) y eliminalos" <!-- .element: class="fragment" -->

"Asegurate que el documento cumpla con el amnesia test (no more context) 
y funcione cold-read" <!-- .element: class="fragment" -->

--

## [Pequeñas incitaciones para guiar a la IA](https://charly-vibes.github.io/incitaciones)

"Revisa siguiendo el Rule of 5: Boceto, Correctitud, Claridad, Casos borde, Excelencia" <!-- .element: class="fragment" -->

---


--

    Escribir es como escuchar un cover
    Una sensación de algo conocido. Familiar.
    Algo de todos. Algo tuyo. Algo nuevo.
    Es organizar una fiesta y que nadie se quede afuera
    Pero principalmente: sos vos el que se tiene que divertir.
    El que la tiene que vivir.
    Bailar. Cantar.
    Emborracharte de la alegría. Bancártela si te pinta un pedo triste.
    No tenerle miedo al ridículo. 
    Evocar.
    Aquello que nos hizo tan felices. Como así también lo que nos hizo mal.
    Hacernos cargo de nuestros respectivos prontuarios.
    Mostrar de dónde venimos. Mostrar quiénes somos.
    Compartirlo. No ser mezquinos.
    Ponerle todas las ganas.
    Brillar y después explotar.
    Porque todo eso, ni más ni menos, es escribir.

[Leo Oyola: La canción que cada uno tiene adentro](https://www.youtube.com/watch?v=DC-OdcjzED0) <!-- .element: class="fragment" -->

NOTES:
1:15 — LEER LA CITA COMPLETA (decisión de Sasha). Es el cierre emocional: no resumir, no recortar.

---

<!-- .slide: data-transition="none" -->

# Sasha Kielbowicz

Consultor Independiente <!-- .element: class="fragment" --> 

--

<img src="./images/logo.svg" class="light-theme-logo" width="50%" style="display: block; margin: 0 auto;">
<img src="./images/logo-invertido.svg" class="dark-theme-logo" style="display: none; margin: 0 auto;" width="50%">

# [Phorma Scientific](https://phorma.sh/es) <!-- .element: class="fragment" --> 

--

### Dos días con tu equipo

NOTES:
0:30 — si va muy tarde: solo info@phorma.sh en pantalla.

[info@phorma.sh](mailto:info@phorma.sh)

[Capacitaciones y Consultorías](https://phorma.sh/es/trainees)

- Código de investigación reproducible · 2 días
- Prácticas de testing · 2 días
- Liderando la adopción de IA · 1 día
- Diagnósticos de sistemas cuantitativos · 2 días

---

<!-- .slide: id="gracias" -->

# Gracias

NOTES:
0:15 — QR en pantalla y cerrar.

[saxa.xyz/charla-after-chatbon](https://saxa.xyz/charla-after-chatbon)<!-- .element: class="fragment" -->

