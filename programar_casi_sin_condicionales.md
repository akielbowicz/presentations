---
theme : "solarized"
# highlightTheme : "base16/solarized-light"
highlightTheme : "base16/windows-95"
transition: "slide"
---

## Programar <span class="fragment">**(casi)** </span> sin condicionales

10 de Noviembre de 2022, PyAr Meetup

@sashakile

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

### Programa de la charla

- ¿Qué significa programar? {.fragment .fade-in}
- Ejemplo práctico {.fragment .fade-in}

---

## Programar

--

### Modelo simplificado de programación

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

```ruby
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

```ruby
MiEnteCantor <: Ente

   contar -> { ... } 

   cantar: partitura -> { ... } 
```

--

`Caracteres` `<: Ente`{.fragment .fade-in}

`Cadenas de caracteres`{.fragment .fade-in} `<: Ente`{.fragment .fade-in}

`Números`{.fragment .fade-in} `<: Ente`{.fragment .fade-in}

`Fotos`{.fragment .fade-in}  `<: Ente`{.fragment .fade-in}

`Archivos`{.fragment .fade-in} `Matrices`{.fragment .fade-in}
`URLs`{.fragment .fade-in} `Patos`{.fragment .fade-in}
`Conexiones`{.fragment .fade-in} `Colecciones`{.fragment .fade-in}
`Bits`{.fragment .fade-in}

--

```py
> "Hola Mundo!" 
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

```ruby
Booleano <: Ente

  negar {}

  y: otro {}

  o: otro {}
```

--

##### Ejercicio 🤔

```ruby
Verdadero <: Booleano

  negar {}

  y: otro {}

  o: otro {}
```

--

##### Ejercicio 🤔

```ruby
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

Tabla: Empresa de Agua Potable 💧

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

Tabla: Empresa de Agua Potable 💧

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

Tabla: Empresa de Agua Potable 💧

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
        ed, id_, tipo, consumo = valores
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

Tabla: Empresa de Energía Eléctrica ⚡

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

¿Qué podemos hacer para controlar la complejidad?

![bruce](https://media0.giphy.com/media/O0AEyXviC1vtC/giphy.gif?cid=ecf05e47l7vi7a53r9pyfk2lmn4gvef63c1raqxkxkpar566&rid=giphy.gif&ct=g){.fragment .fade-in}

--

`ALGO`{.fragment .fade-in} `(servicio, edificacion)`

--

~~ALGO~~ `(servicio, edificacion)`

--

`(servicio, edificacion)`

`servicio cobrar: edificacion`{.fragment fade-in} `???`{.fragment fade-in}

--

```py
...
for servicio in servicios:
  total = 0
  for edificacion in edificaciones:
    total += servicio.cobrar(edificacion)
  ....
```

![cartas](https://img1.ibxk.com.br/2014/4/materias/5345510175955.gif){.fragment .fade-in}

--

`servicio cobrar: edificacion`

| `⨉` | Electricidad | Agua | Gas | ... |
| --- | --- | --- | --- | --- |
|**Casa**| | | | |
|**Departamento** | | | | |
|**Edificio** | | | | |
|**...** | | | | |

---

```ruby
Servicio <: Ente

  cobrar: edificacion -> {

  }
```

--

```ruby
Servicio <: Ente                       Edificacion <: Ente

  cobrar: edificacion -> {                                    
                                                                     
  }                                                          
```

--

```ruby
Servicio <: Ente                       Edificacion <: Ente

  cobrar: edificacion -> {               consumo: servicio -> {

  }                                      }
```

--

```ruby
Servicio <: Ente                       Edificacion <: Ente

  cobrar: edificacion -> {               consumo: servicio -> {
    edificacion consumo: yo                0.0
  }                                      }
```

--

```ruby
Servicio <: Ente                       Edificacion <: Ente

  cobrar: edificacion -> {               consumo: servicio -> {
    edificacion consumo: yo                0.0
  }                                      }                
```

```ruby
Agua <: Servicio                       Casa <: Edificacion 

  cobrar: edificacion -> {               consumoDeAgua: servicio -> {
    edificacion consumoDeAgua: yo
  }                                      }
```

--

```ruby
Servicio <: Ente                       Edificacion <: Ente

  cobrar: edificacion -> {               consumo: servicio -> {
    edificacion consumo: yo                0.0
  }                                      }                
```

```ruby
Agua <: Servicio                       Casa <: Edificacion 

  cobrar: edificacion -> {               consumoDeAgua: servicio -> {
    edificacion consumoDeAgua: yo
  }                                      }
                                         consumoDeGas: servicio -> {
Gas <: Servicio
                                         }
  cobrar: edificacion -> {
    edificacion consumoDeGas: yo
  }
```

--

```ruby
Servicio <: Ente                       Edificacion <: Ente

  cobrar: edificacion -> {               consumo: servicio -> {
    edificacion consumo: yo                0.0
  }                                      }
  montoParaCasa: ... -> {...}
```

```ruby
Agua <: Servicio                       Casa <: Edificacion 

  cobrar: edificacion -> {               consumoDeAgua: servicio -> {
    edificacion consumoDeAgua: yo          servicio montoParaCasa: ...
  }                                      }
                                         consumoDeGas: servicio -> {
Gas <: Servicio                            servicio montoParaCasa: ...
                                         }
  cobrar: edificacion -> {
    edificacion consumoDeGas: yo
  }
```

--

![servicios.py](https://github.com/akielbowicz/presentations/blob/pyar_sincondicionales/img/2022-11-09%2022_46_52-%E2%97%8F%20servicios.py%20-%20panela%20-%20Visual%20Studio%20Code.png?raw=true)
--

![edificacion.py](https://github.com/akielbowicz/presentations/blob/pyar_sincondicionales/img/2022-11-09%2022_48_21-%E2%97%8F%20edificacion.py%20-%20panela%20-%20Visual%20Studio%20Code.png?raw=true)

--

![test.py](https://github.com/akielbowicz/presentations/blob/pyar_sincondicionales/img/2022-11-09%2023_09_24-test_servicios_y_edificios.py%20-%20panela%20-%20Visual%20Studio%20Code.png?raw=true)

--

![debug](https://github.com/akielbowicz/presentations/blob/pyar_sincondicionales/img/debug.gif?raw=true)

--

###### Para pensar:

- ¿Qué código hay que modificar para agregar una nueva edificación? {.fragment .current-visible}
- ¿Qué código hay que modificar para agregar un nuevo servicio? {.fragment .current-visible}
- ¿Qué código hay que modificar para eliminar una edificación? {.fragment .current-visible}
- ¿Qué código hay que modificar para eliminar un servicio? {.fragment .current-visible}

--

##### Ejercicio 💸

```py
edificacion monto: servicio
```

---

#### Programar **(casi)**{.fragment .highlight-red} sin condicionales

---

Tabla: Empresa de Energía Eléctrica ⚡

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

---

```py
edificaciones = [
Casa(watts=6.1,tipo=Domestico()), 
Departamento(watts=6.1,tipo=Domestico()), 
Departamento(watts=6.1,tipo=Comercial()), 
Departamento(watts=6.1,tipo=Oficina()), 
Casa(watts=6.1,tipo=Oficina()), 
Edificio(watts=6.1,tipo=Oficina()), 
]
```

---

```py
linea = "departamento, A1, domestico, 22.4"
fila = linea.split(",")
valores = [ e.strip() for e in fila ]
ed, id_, tipo, consumo = valores
```

--

![pan](https://media0.giphy.com/media/gM5rrNKbkpTUsnS0Gz/giphy.gif)

--

```py
mapa_edificaciones = {
  "casa": Casa,
  "departamento": Departamento,
  "edificio": Edificio,
}

def obtener_edificacion(ed, id_, tipo, consumo, servicio):
  if tipo == 'oficina':
    t = Oficina()
  elif: tipo == 'domestico':
    t = Domestico()
  else:
    t = Comercial()
  
  c =  float(consumo)

  tipo_consumo = servicio.tipo_consumo()
  args = {"tipo":t, tipo_consumo:c}

  return mapa_edificaciones[ed](**args)
```

--

![clips](https://cdn.acidcow.com/pics/20150928/factory_gifs_15.gif)

> Las Factories son el lugar a donde los "IF"s van a morir.
Sandi Metz {.fragment .fade-in}

--

[Dogdge if statements](https://python-patterns.guide/gang-of-four/composition-over-inheritance/#dodge-if-statements)

1. Localidad (*Locality*) {.fragment .fade-in}
2. Borrabilidad (*Deletability*) {.fragment .fade-in}  
3. Codigo muerto (*Dead code analysis*) {.fragment .fade-in}
4. Testing {.fragment .fade-in}
5. Eficiencia (*Efficiency*) {.fragment .fade-in}

---

>A computer is like a violin. You can imagine a novice trying first a
phonograph and then a violin. The latter, he says, sounds terrible.
That is the argument we have heard from our humanists and most
of our computer scientists.

--

>Computer programs are good, they say,
for particular purposes, but they aren't flexible. Neither is a violin,
or a typewriter, until you learn how to use it.

>Marvin Minsky, “Why Programming Is a Good Medium for
Expressing Poorly-Understood and Sloppily-Formulated Ideas” in
Design and Planning, (1967){.fragment .fade-in}

---

### Gracias

![](https://64.media.tumblr.com/30bedeb563c8f8df76afbc4c4f61cbfb/55ed7abd84b43635-45/s400x600/be41a12e3e6d95978f089b0e5b1b2af1d3585cd7.gif)

---

- Metricas

[radon](https://radon.readthedocs.io/en/latest/intro.html#cyclomatic-complexity)

--

[Referencia del Lenguaje Python](https://docs.python.org/es/3/reference/index.html)
