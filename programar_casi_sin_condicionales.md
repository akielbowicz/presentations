---
theme : "solarized"
highlightTheme : "base16/solarized-light"
transition: "slide"
---

# Programar <span class="fragment">**(casi)** </span> sin condicionales

---

![lapiz](https://big.assets.huffingtonpost.com/ToothpicksMade.gif)
![resortes](https://big.assets.huffingtonpost.com/SpringII.gif)

![cadena](https://big.assets.huffingtonpost.com/ChainLinkMade.gif)

--

![cramica](https://media4.giphy.com/media/Ri7oq0YpkoEu3mtdPn/giphy.gif?cid=ecf05e470xfccoyb1t5648q3cahtum8mqhb7933srlxk3o8t&rid=giphy.gif&ct=g)

--

![marqueteria](http://homofabercursos.com/wp-content/uploads/2018/05/IMGP2236.jpg)

--

![vidrio](https://dailynewshungary.com/wp-content/uploads/2018/09/1-1.jpg)

--

## Artesanía <span class="fragment">de Software</span>

---

## Programar

--

### Modelo simplificado de programación

--

### Entes

--

### Entes

![entes](https://upload.wikimedia.org/wikipedia/commons/3/37/Wilson1900Fig2.jpg) {.fragment fade-in}

--

### Entes

![homunculo](https://github.com/akielbowicz/presentations/blob/pyar_codesmells/meetup/pyar-19-sep-2020/materiales/imagenes/humunculo_objeto.png?raw=true) {.fragment fade-in}

--

### Mensajes

![homunculo](https://github.com/akielbowicz/presentations/blob/pyar_codesmells/meetup/pyar-19-sep-2020/materiales/imagenes/humunculo_objeto.png?raw=true)
<span class="fragment"> 🎁 </span>
![homunculo](https://github.com/akielbowicz/presentations/blob/pyar_codesmells/meetup/pyar-19-sep-2020/materiales/imagenes/humunculo_objeto.png?raw=true) {.fragment fade-in}

--

```py
👾 ✉ 
```

--

```py
🤖 ✉
```

--

```py
👤 📦
```

--

```py
🦆 🔊
```

--

```py
ente mensaje
```

--

Necesitamos un sistema para *clasificar*{.fragment .highlight-blue} a los Entes

--

```py
Ente

    nuevo -> { } 

    interactuar: x -> {
        x otroMensaje: yo
      }

    combinarCon: x e: y -> {
        [yo, x, y]
      }
```

--

```py
MiEnteCantor <: Ente

   cantar -> { ... } 

   cantar: partitura -> { ... } 
```

--

```py
> "Hola Mundo!" tamaño 
11
```

--

```py
> "Hola Mundo!" tamaño sumar: 31
```

---

## Condicionales

--

Dada una `[premisa]`

`[consecuente]` {.fragment fade-in}

**Control de la ejecución** {.fragment fade-in}

---

##### Ejercicio 🤔

--

##### Ejercicio 🤔

```py
Booleano <: Ente

  negar {}

  y: otro {}

  o: otro {}
```

--

##### Ejercicio 🤔

```py
Verdadero <: Booleano

  negar {}

  y: otro {}

  o: otro {}
```

--

##### Ejercicio 🤔

```py
Verdadero <: Booleano    Falso <: Booleano
                         
  negar {}                 negar {}
                         
  y: otro {}               y: otro {}
                         
  o: otro {}               o: otro {}
```

--

`booleano y: otroBooleano`{.fragment fade-in}

| `y` | Verdadero |Falso |
| --- | --- | --- |
|**Verdadero**| | |
|**Falso** | | |

--

`booleano o: otroBooleano`{.fragment fade-in}

| `o` | Verdadero |Falso |
| --- | --- | --- |
|**Verdadero**| | |
|**Falso** | | |

--

![reloj-arena](https://media1.giphy.com/media/xuUmRnrF6uGQM/giphy.gif?cid=ecf05e47tsdbjk6r3ydze87b331fdse5x4e4y90ecxvyqy2j&rid=giphy.gif&ct=g)

---

### Ejemplo 🐍

--

Tabla Empresa de Agua Potable 💧

```py
"""
Edificacion, Id, Tipo
casa,         0, domestico
departamento, 1, domestico
departamento, 2, comercial
departamento, 3, oficina
casa,         4, oficina
"""
```

--

```py
lineas = documento.splitlines()
headers = [ e.strip() for e in lineas[0].split(",") ]
total = 0
for linea in lineas[1:]:
    if len(linea.strip()) > 0:
        fila = linea.split(",")
        valores = [ e.strip() for e in fila ]
        ed, id_, tipo= valores
        escala = 1.0
        if ed == "casa":
            total += 1.0 
        elif ed == "departamento":
            total += 0.5 
        else:
            print(f"Desconocido:{valores}")
```

--

Tabla Empresa de Agua Potable 💧

```py
"""
Edificacion, Id, Tipo
casa,         0, domestico
departamento, 1, domestico
departamento, 2, comercial
departamento, 3, oficina
casa,         4, oficina
"""

"oficina": 0.8, 
"comercial": 5.0, 
"domestico": 1.0, 
```

--

```py
precios = {"oficina": 0.8, "comercial": 5.0, "domestico": 1.0}

for linea in lineas[1:]:
    if len(linea.strip()) > 0:
        fila = linea.split(",")
        valores = [ e.strip() for e in fila ]
        ed, id_, tipo= valores
        escala = 1.0
        if ed == "casa":
            total += 1.0 * precios[tipo] 
        elif ed == "departamento":
            total += 0.5 * precios[tipo]
        else:
            print(f"Desconocido:{valores}")
```

--

Tabla Empresa de Agua Potable 💧

```py
"""
Edificacion, Id,      Tipo, Consumo
casa,         0, domestico, 3.1
departamento, 1, domestico, 11.4
departamento, 2, comercial, 0.1
departamento, 3,   oficina, 10.0
casa,         4,   oficina, 1.0
"""
```

--

```py
for linea in lineas[1:]:
    if len(linea.strip()) > 0:
        fila = linea.split(",")
        valores = [ e.strip() for e in fila ]
        ed, id_, tipo= valores
        escala = 1.0
        if ed == "casa":
            if consumo > 1.0:
                escala = 5.0
            else:
                escala = 1.1

            total += 1.0 * escala * precios[tipo] * consumo
        elif ed == "departamento":
            if consumo > 1.0:
                escala = 3.0
            else:
                escala = 1.2

            total += 0.5 * escala * precios[tipo] * consumo
        else:
            print(f"Desconocido:{valores}")
```

--

Tabla Empresa de Energía Eléctrica ⚡

```py
"""
 Edificacion, Id,      Tipo, Consumo
        casa, A0, domestico, 6.1
departamento, A1, domestico, 22.4
departamento, A2, comercial, 0.2
departamento, A3,   oficina, 20.0
        casa, A4,   oficina, 2.0
    edificio, A5,   oficina, 123.0
"""
```

--

Empresa de Agua Potable 💧

Empresa de Energía Eléctrica ⚡ {.fragment fade-in}

Empresa de Gas Natural 🔥 {.fragment fade-in}

Empresa de Telefonía ☎ {.fragment fade-in}

Empresa de Internet 💻 {.fragment fade-in}

Empresa de ... {.fragment fade-in}

--

Casa 🏠 {.fragment fade-in}

Departamento 🏬 {.fragment fade-in}

Edificio 🏢 {.fragment fade-in}

PH 🏘 {.fragment fade-in}

Terreno 🏜 {.fragment fade-in}

... {.fragment fade-in}

--

![bruce](https://media0.giphy.com/media/O0AEyXviC1vtC/giphy.gif?cid=ecf05e47l7vi7a53r9pyfk2lmn4gvef63c1raqxkxkpar566&rid=giphy.gif&ct=g)

--

`servicio cobrar: edificacion`{.fragment fade-in} `???`{.fragment fade-in}

| `x` | Electricidad | Agua | Gas | ... |
| --- | --- | --- | --- | --- |
|**Casa**| | | | |
|**Departamento** | | | | |
|**Edificio** | | | | |
|**...** | | | | |

--

```py
Servicio <: Ente

   cobrar: edificacion -> {

   }
```

--

##### Ejercicio 💸

```py
edificacion monto: servicio
```

---

#################### 33

---

- Contexto de la charla
- Artesania de Software

---

- Modelo de programacion
- Objetos y mensajes
- Clasificacion de los objetos

---

- Porque necesitamos los condicionales
- Logica Binaria
- Generalizar la interaccion entre objetos

---

- Metricas

[Dogdge if statements](https://python-patterns.guide/gang-of-four/composition-over-inheritance/#dodge-if-statements)

[radon](https://radon.readthedocs.io/en/latest/intro.html#cyclomatic-complexity)

--

[Referencia del Lenguaje Python](https://docs.python.org/es/3/reference/index.html)

---
