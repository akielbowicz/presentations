---
theme : "solarized"
highlightTheme : "monokai"
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

- Entes

--

- Entes

![entes](https://upload.wikimedia.org/wikipedia/commons/3/37/Wilson1900Fig2.jpg) {.fragment fade-in}

--

- Entes

![homunculo](https://github.com/akielbowicz/presentations/blob/pyar_codesmells/meetup/pyar-19-sep-2020/materiales/imagenes/humunculo_objeto.png?raw=true) {.fragment fade-in}

--

- Mensajes

<span class="fragment"> 🎁 </span>
![homunculo](https://github.com/akielbowicz/presentations/blob/pyar_codesmells/meetup/pyar-19-sep-2020/materiales/imagenes/humunculo_objeto.png?raw=true)
![homunculo](https://github.com/akielbowicz/presentations/blob/pyar_codesmells/meetup/pyar-19-sep-2020/materiales/imagenes/humunculo_objeto.png?raw=true) {.fragment fade-in}

--

```smalltalk
👾 ✉
```

--

```smalltalk
🤖 ✉
```

--

```smalltalk
👤 📦
```

--

```smalltalk
🦆 🔊
```

--

```smalltalk
ente mensaje
```

--

Necesitamos un sistema para *clasificar*{.fragment .highlight-blue} a los Entes

--

```smalltalk
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

```smalltalk
MiEnteCantor <: Ente

   cantar -> {} 

   cantar: partitura -> {} 
```

--

```smalltalk
> "Hola Mundo!" tamaño 
11
```

--

```smalltalk
> "Hola Mundo!" tamaño sumar: 31
```

--

## Condicionales

--

Dada una `[premisa]`

`[consecuente]` {.fragment fade-in}

**Control de la ejecución** {.fragment fade-in}

---

Ejercicio

--

Ejercicio

```c
Booleano <: Ente

  negar {}

  y: otro {}

  o: otro {}
```

--

Ejercicio

```c
Verdadero <: Booleano

  negar {}

  y: otro {}

  o: otro {}
```

--

Ejercicio

```c
Verdadero <: Booleano    Falso <: Booleano
                         
  negar {}                 negar {}
                         
  y: otro {}               y: otro {}
                         
  o: otro {}               o: otro {}
```

--

booleano y: otroBooleano {.fragment fade-in}

| `y` | Verdadero |Falso |
| --- | --- | --- |
|**Verdadero**| | |
|**Falso** | | |

--

booleano o: otroBooleano {.fragment fade-in}

| `o` | Verdadero |Falso |
| --- | --- | --- |
|**Verdadero**| | |
|**Falso** | | |

--

Ejemplo 🐍

--

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
        values = [ e.strip() for e in fila ]
        ed, id_, tipo= values
        escala = 1.0
        if ed == "casa":
            total += 1.0 
        elif ed == "departamento":
            total += 0.5 
        else:
            print(f"Desconocido:{values}")
```

--

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
        values = [ e.strip() for e in fila ]
        ed, id_, tipo= values
        escala = 1.0
        if ed == "casa":
            total += 1.0 * precios[tipo] 
        elif ed == "departamento":
            total += 0.5 * precios[tipo]
        else:
            print(f"Desconocido:{values}")
```

--

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
        values = [ e.strip() for e in fila ]
        ed, id_, tipo= values
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
            print(f"Desconocido:{values}")
```

--

ABC

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

--

[Referencia del Lenguaje Python](https://docs.python.org/es/3/reference/index.html)

---
