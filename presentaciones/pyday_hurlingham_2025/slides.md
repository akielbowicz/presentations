<!-- .slide: id="titulo" -->

# Nadie nada nunca

**PyDay Hurlingham**

**29 de Noviembre 2025**

---

<!-- .slide: data-transition="none" -->

### Sasha

Líder Técnico en Mercado Libre 

*IT Staff || Financial Planning & Analysis*

--

<!-- .slide: data-transition="none" -->

### Sasha

**TL** en **MELI**

*IT Staff || Financial Planning & Analysis*

--

- Estudié Física en la UBA
- Trabaje como Desarrollador de Software en JP Morgan
- Trabaje como Lead Quant Developer en **Qontigo/Simcorp**

NOTES:
Acá tengo que mencionar un par de cosas de que me interesa y que motiva esta charla

--

<img src="./images/george_nothing.gif" width="70%">

--

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/OMPfEXIlTVE?si=pqTo6xzKa1qfn5us" title="Nothing is Something" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe> 

[Nothing is Something](https://www.youtube.com/watch?v=OMPfEXIlTVE) de Sandi Metz


NOTES:
Hay demasiadas sutilezas en esta presentacion y muchas particularidades que me llevaron bastante tiempo entenderlas y más que entenderlas,internalizarlas y ver como podia utilizarlas en mi dia a dia.

---



<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%; gap: 20px;">

<div style="display: flex; flex-direction: column; width: 60%; gap: 5%;">

<div style="background-color: #4CAF50; height: 20%; border: 2px solid #000; display: flex; align-items: center; justify-content: center;">
<h3 style="margin: 0; color: #000; visibility: hidden;"><em>Buscando</em> la Abstracción</h3>
</div>

<div style="background-color: #4CAF50; height: 20%; border: 2px solid #000; display: flex; align-items: center; justify-content: center;">
<h3 style="margin: 0; color: #000; visibility: hidden;"><em>Centrado</em> en los Mensajes</h3>
</div>

<div style="background-color: #4CAF50; height: 20%; border: 2px solid #000; display: flex; align-items: center; justify-content: center;">
<h3 style="margin: 0; color: #000; visibility: hidden"><em>Reacio</em> a los Condicionales</h3>
</div>

<div style="background-color: #4CAF50; height: 20%; border: 2px solid #000; display: flex; align-items: center; justify-content: center; margin-top: 30px;">
<h3 style="margin: 0; color: #000;"><em>Infectado</em> por Smalltalk </h3>
</div>

</div>
</div>


NOTES: 
Hay una particularidad en como la gente que programa en Smalltalk piensa el código orientado a objetos.

--

<!-- .slide: id="poo" -->

### Programación Orientada a Objetos (POO)

<div class="fragment">
<iframe width="560" height="315" src="https://www.youtube.com/embed/ioeMeQNEgL8?si=DMdhg2cY7f_SQlry" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

[Programar (casi) sin condicionales](https://www.youtube.com/watch?v=ioeMeQNEgL8)

</div>

NOTES:

Voy a pasar rapido por un par de ideas que explico en mas detalle en esta charla pero que nos van a ayudar a sentar las bases para lo que sigue.

--

Definamos unas reglas para la Programación Orientada a Objetos.

1. Todo es un objeto 
<!-- .element: class="fragment" -->
2. Los objetos se comunican enviandose mensajes
<!-- .element: class="fragment" -->


NOTES:
La programacion orientada a objetos tiene dos simples ideas o reglas:
y con estas reglas podemos generar todo tipo de comportamientos complejos.

--

```python
objetoA = MiObjeto()
```

--

<!-- .slide: data-transition="none" -->
```python
objetoA = MiObjeto()
objetoB = MiOtroObjeto()
```
--

<!-- .slide: data-transition="none" -->
```python
objetoA = MiObjeto()
objetoB = MiOtroObjeto()

objetoA.mensaje(objetoB)
```

--

<!-- .slide: data-transition="none" -->
```python
objetoA = MiObjeto()
objetoB = MiOtroObjeto()

objetoA.mensaje(objetoB)

objetoB.otro_mensaje(1, "2", [True], None, objetoA)
```

NOTES:

Para que nos sirve esto? 
Para reducir el contexto de cada cosa que hacemos. Separar responsabilidades, etc

--

```python
class MiObjeto:
    def mensaje(self, otro_objeto):
        otro_objeto.otro_mensaje(42)
```

---

Analicemos una particularidad de Smalltalk para ver como conceptualizamos los objetos.

--

```python
str(1)
# => '1'
```

--

<!-- .slide: data-transition="none" -->

```python
(1).__str__()
# => '1'
```

--

```python
1 + 1
# => 2 
```

--

```python
(1).__add__(1)
# => 2 
```

--

```python
type(1)
# => int
```

--

```python
dir(int)
# => ['__abs__', '__add__', '__and__', '__bool__', 
# '__class__', ..., '__str__', '__sub__', ...]
``` 

NOTES:
Esto es lo que es real, esto es lo que esta detras de la sintaxis especial que tenemos en Python para trabajar con los objetos. Estamos mandando un mensaje a un objeto.

---

```python
1 == 1
# => True
```

--

```python
(1).__eq__(1)
# => True
```

--

```python
type(True)
# => bool
```

--

```python
dir(bool)
# => [ '__abs__', '__add__', '__and__', '__bool__', ...
#  '__ne__', '__neg__', '__new__', '__or__',
#  ... '__ror__',... '__rxor__',... '__xor__', ... ]
```

NOTES:

Lo extrano es que en Python exista una sintaxis especial para trabajar con los booleanos, pero lo tenemos tan naturalizado que no lo cuestionamos.

---

## A diferencia de Smalltalk, Python tiene una sentencia especial para trabajar con los booleanos

--

Las keywords de SmallTalk: 

> true, false, nil, self, super, thisContext

<div class="fragment">

Las keywords de Python:

```python [|5]
import keyword
print(keyword.kwlist)
# => ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 
# 'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
# 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 
# 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 
# 'raise', 'return', 'try', 'while', 'with', 'yield']
```
</div>

<small class="fragment">

[Wikipedia: SmallTalk Syntax](https://en.wikipedia.org/wiki/Smalltalk#Syntax) | 
[Python Keywords](https://docs.python.org/3/reference/lexical_analysis.html#keywords)
</small>

--

```python
if (1 == 1):
    print("Verdadero")
else:
    print("Falso")
```

NOTES: 
Esta es la manera en la que utilizamos esta sintaxis en Python y en muchos otros 
lenguajes de programacion.
Hay una expresion que se evalua y dependiendo de su valor se ejecuta un bloque de codigo u otro.

--

<!-- .slide: data-transition="none" -->

```python
if (True):
    print("Verdadero")
else:
    print("Falso")
```

--

<!-- .slide: data-transition="none" -->

```python
if ( truthy ):
    # Código a evaluar cuando es verdadero
else:
    # Código a evaluar cuando es falso
```

--

<!-- .slide: data-transition="none" -->

```python
if ( Objeto del cual conozco el tipo ):
    # Código que hace algo
else:
    # Código que hace otra cosa
```

NOTES:
Esto es un TypeCheck, y es algo que se no se hace en OO.

--

### Solo quiero pasarle un **mensaje** a los objetos.

NOTES:
No quiero tener que ver el tipo de objeto que estoy manejando. Y en 
base a eso decidir entre distintos comportamientos.

--

# El "if"

**es un facilitador**
<!-- .element: class="fragment" -->

NOTES:
Si venimos de lenguajes procedurales es parecería que es normal y razonable implementar largos condicionales (con if, switch, case, etc) 

Y la idea principal de Sandi es que la presencia de esta palabra hace facilita
que mantengamos nuestra manera de pensar de manera procedural. Y nos impide aprender y a aprovechar el poder de la Programación Orientada a Objetos.

---

### Sintaxis de "Envío de Mensajes" para True y False

--

```python
class Verdadero:
    @classmethod
    def si_verdadero(cls, bloque_de_codigo):
        bloque_de_codigo()

```

--

<!-- .slide: data-transition="none" -->

```python
class Verdadero:
    @classmethod
    def si_verdadero(cls, bloque_de_codigo):
        bloque_de_codigo()
        return cls
```

--

<!-- .slide: data-transition="none" -->

```python [7-9]
class Verdadero:
    @classmethod
    def si_verdadero(cls, bloque_de_codigo):
        bloque_de_codigo()
        return cls
    @classmethod
    def si_falso(cls, bloque_de_codigo):
        return cls
```

--

```python
class Verdadero:
    @classmethod
    def si_verdadero(cls, bloque_de_codigo):
        bloque_de_codigo()
        return cls

    @classmethod
    def si_falso(cls, bloque_de_codigo):
        return cls
```

```python
class Falso:
    @classmethod
    def si_verdadero(cls, bloque_de_codigo):
        return cls

    @classmethod
    def si_falso(cls, bloque_de_codigo):
        bloque_de_codigo()
        return cls
```
<!-- .element: class="fragment" -->

--

```python
Verdadero.si_verdadero(lambda: print("Evalua este bloque"))
# => Evalua este bloque
```

```python
Verdadero.si_falso(lambda: print("Evalua este bloque"))
# =>
```
<!-- .element: class="fragment" -->

```python
Falso.si_verdadero(lambda: print("Evalua este bloque"))
# =>
```
<!-- .element: class="fragment" -->

```python
Falso.si_falso(lambda: print("Evalua este bloque"))
# => Evalua este bloque
```
<!-- .element: class="fragment" -->

--

```python
if (1 == 1):
    print("Es verdadero")
else:
    print("Es falso")
# => Es verdadero
```    

```python
(1 == 1).si_verdadero(lambda: print("Es verdadero"))
        .si_falso(lambda: print("Es falso"))
# => Es verdadero
```    
<!-- .element: class="fragment" -->

--

```python
if (1 == 2):
    print("Es verdadero")
else:
    print("Es falso")
# => Es falso
```    

```python
(1 == 2).si_verdadero(lambda: print("Es verdadero"))
        .si_falso(lambda: print("Es falso"))
# => Es falso
```    
<!-- .element: class="fragment" -->

--

### No queremos cambiar Python

--

<!-- .slide: data-transition:"none" -->

### Quiero que cambiemos nuestra manera de pensar

NOTES:
Solo queremos cambiar nuestra manera de pensar.
Es una invitación a pensar en como se diseñamos nuestro código

---

<!-- .slide: id="no-existiese-el-if" -->

**¿Qué pasaría si no existiera la sentencia `"if"`?**

---


<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%; gap: 20px;">

<div style="display: flex; flex-direction: column; width: 60%; gap: 5%;">

<div style="background-color: #4CAF50; height: 20%; border: 2px solid #000; display: flex; align-items: center; justify-content: center;">
<h3 style="margin: 0; color: #000; visibility: hidden;"><em>Buscando</em> la Abstracción</h3>
</div>

<div style="background-color: #4CAF50; height: 20%; border: 2px solid #000; display: flex; align-items: center; justify-content: center;">
<h3 style="margin: 0; color: #000; visibility: hidden;"><em>Centrado</em> en los Mensajes</h3>
</div>

<div style="background-color: #4CAF50; height: 20%; border: 2px solid #000; display: flex; align-items: center; justify-content: center;">
<h3 style="margin: 0; color: #000; visibility: hidden"><em>Reacio</em> a los Condicionales</h3>
</div>

<div style="background-color: #4CAF50; height: 20%; border: 2px solid #000; display: flex; align-items: center; justify-content: center; margin-top: 30px;">
<h3 style="margin: 0; color: #000;"><em>Infectado</em> por Smalltalk </h3>
</div>

</div>
</div>

--

<!-- .slide: data-transition="none" -->

<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%; gap: 20px;">

<div style="display: flex; flex-direction: column; width: 60%; gap: 5%;">

<div style="background-color: #4CAF50; height: 20%; border: 2px solid #000; display: flex; align-items: center; justify-content: center;">
<h3 style="margin: 0; color: #000; visibility: hidden;"><em>Buscando</em> la Abstracción</h3>
</div>

<div style="background-color: #4CAF50; height: 20%; border: 2px solid #000; display: flex; align-items: center; justify-content: center;">
<h3 style="margin: 0; color: #000; visibility: hidden;"><em>Centrado</em> en los Mensajes</h3>
</div>

<div style="background-color: #4CAF50; height: 20%; border: 2px solid #000; display: flex; align-items: center; justify-content: center;">
<h3 style="margin: 0; color: #000;"><em>Reacio</em> a los Condicionales</h3>
</div>

<div style="background-color: #4CAF50; height: 20%; border: 2px solid #000; display: flex; align-items: center; justify-content: center; margin-top: 30px;">
<h3 style="margin: 0; color: #000;"><em>Infectado</em> por Smalltalk </h3>
</div>

</div>
</div>

--

```python
Biblioteca.buscar("Los Sorias")
# =>  <__main__.Libro at 0x7f0f49464d70>
```

```python
Biblioteca.buscar("")
# => None
```
<!-- .element: class="fragment" -->

NOTES:
Veamos un caso terrible

--

```python [1|1-3|3-6|5]
ids = ["Los Sorias", "", "El Fiord"]

libros = [ Biblioteca.buscar(id) for id in ids ]
# => [<__main__.Libro object at 0x7f0f4bf35940> id:Los Sorias,
# None,
# <__main__.Libro object at 0x7f0f48e10190> id:El Fiord]
```

```python
for libro in libros:
    print(libro.autor)

```
<!-- .element: class="fragment" -->

--

<!-- .slide: data-transition="none" -->

```python
ids = ["Los Sorias", "", "El Fiord"]

libros = [ Biblioteca.buscar(id) for id in ids ]
# => [<__main__.Libro object at 0x7f0f4bf35940> id:Los Sorias,
# None,
# <__main__.Libro object at 0x7f0f48e10190> id:El Fiord]
```

```python [|4]
for libro in libros:
    print(libro.autor)
# => Alberto Laiseca
# AttributeError: 'NoneType' object has no attribute 'autor'
```

--

Hay veces que **None** *"es nada"*.

--

```python [|2|5-6]
libros = [ libro for id in ids 
           if (libro := Biblioteca.buscar(id)) 
         ]
# => [
# <__main__.Libro object at 0x7f0f4bf35940> id:Los Sorias,
# <__main__.Libro object at 0x7f0f48e10190> id:El Fiord
#    ]
```

--

Pero si le pasamos un mensaje a **None**,

entonces *"es algo"*.
<!-- .element: class="fragment" -->

--

¿Y qué pasa si quiero manejar ese caso?

```python [9]
ids = ["Los Sorias", "", "El Fiord"]

libros = [ Biblioteca.buscar(id) for id in ids ]
# => [<__main__.Libro object at 0x7f0f4bf35940> id:Los Sorias,
# None,
# <__main__.Libro object at 0x7f0f48e10190> id:El Fiord]

for libro in libros:
    print("Libro desconocido" if libro is None else libro.autor)
```
<!-- .element: class="fragment" -->

--

<!-- .slide: data-transition="none" -->

```python [9]
ids = ["Los Sorias", "", "El Fiord"]

libros = [ Biblioteca.buscar(id) for id in ids ]
# => [<__main__.Libro object at 0x7f0f4bf35940> id:Los Sorias,
# None,
# <__main__.Libro object at 0x7f0f48e10190> id:El Fiord]

for libro in libros:
    print(libro and libro.autor)
```

--

```python
"Libro desconocido" if libro is None else libro.autor
```

```python
if libro is None:
    return "Libro desconocido"
else:
    return libro.autor
```
<!-- .element: class="fragment" -->

--

```python
if libro is None:
    return "Libro desconocido"
else:
    return libro.autor
```

```python [1|2|4]
if ( Objeto del cual conozco el tipo ):
    # Código que hace algo
else:
    # Código que hace otra cosa
```
<!-- .element: class="fragment" -->

--

<div style="display: flex; justify-content: space-around; overflow: hidden;">
<div style="flex: 1 1 auto; padding: 3px;">

```python
if libro is None:
    return "Libro desconocido"
else:
    return libro.autor
```

</div>
<div style="flex: 1 1 auto; padding: 3px;">

```python [|2]
if ( Objeto del cual conozco el tipo ):
    # Código que hace algo
else:
    # Código que hace otra cosa
```

</div>
</div>

--

<!-- .slide: data-transition="none" -->

<div style="display: flex; justify-content: space-around; overflow: hidden;">
<div style="flex: 1 1 auto; padding: 3px;">

```python
if libro is None:
    return "Libro desconocido"
else:
    return libro.autor
```

</div>
<div style="flex: 1 1 auto; padding: 3px;">

```python [2|4]
if ( Objeto del cual conozco el tipo ):
    # Yo proveo el comportamiento
else:
    # Código que hace otra cosa
```

</div>
</div>

--

<!-- .slide: data-transition="none" -->

<div style="display: flex; justify-content: space-around; overflow: hidden;">
<div style="flex: 1 1 auto; padding: 3px;">

```python
if libro is None:
    return "Libro desconocido"
else:
    return libro.autor
```

</div>
<div style="flex: 1 1 auto; padding: 3px;">

```python [4]
if ( Objeto del cual conozco el tipo ):
    # Yo proveo el comportamiento
else:
    # Le envío un mensaje al objeto
```

</div>
</div>

NOTES:
Esto es abosolutamente terrible y el problema central es que los condicionales 
se multiplican.

--

<!-- .slide: id="condicionales" -->

## LOS CONDICIONALES

<h1 style="font-size: 3em; color: #e74c3c;" class="fragment">SE MULTIPLICAN</h1>

--

<div style="position: relative; height: 600px; width: 100%;">

<!-- Snippet central - sin modificar -->
<div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">

```python
libro = Biblioteca.buscar(id)
"Libro desconocido" if libro is None else libro.autor
```

</div>

<!-- Primera transición - snippets en esquinas y parte superior -->
<div class="fragment">

<div style="position: absolute; top: 5%; left: 5%; transform: rotate(-15deg); opacity: 0.6; font-size: 0.7em;">

```python
libro = Biblioteca.buscar(id)
"Libro desconocido" if libro is None else libro.autor
```

</div>

<div style="position: absolute; top: 5%; right: 5%; transform: rotate(12deg); opacity: 0.6; font-size: 0.7em;">

```python
libro = Biblioteca.buscar(id)
"Libro desconocido" if libro is None else libro.autor
```

</div>

<div style="position: absolute; top: 30%; left: 2%; transform: rotate(-20deg); opacity: 0.6; font-size: 0.7em;">

```python
libro = Biblioteca.buscar(id)
"Libro desconocido" if libro is None else libro.autor
```

</div>

<div style="position: absolute; top: 30%; right: 2%; transform: rotate(18deg); opacity: 0.6; font-size: 0.7em;">

```python
libro = Biblioteca.buscar(id)
"Libro desconocido" if libro is None else libro.autor
```

</div>

</div>

<!-- Segunda transición - snippets en parte inferior y lados -->
<div class="fragment">

<div style="position: absolute; bottom: 5%; left: 5%; transform: rotate(10deg); opacity: 0.6; font-size: 0.7em;">

```python
libro = Biblioteca.buscar(id)
"Libro desconocido" if libro is None else libro.autor
```

</div>

<div style="position: absolute; bottom: 5%; right: 5%; transform: rotate(-15deg); opacity: 0.6; font-size: 0.7em;">

```python
libro = Biblioteca.buscar(id)
"Libro desconocido" if libro is None else libro.autor
```

</div>

<div style="position: absolute; bottom: 30%; left: 2%; transform: rotate(20deg); opacity: 0.6; font-size: 0.7em;">

```python
libro = Biblioteca.buscar(id)
"Libro desconocido" if libro is None else libro.autor
```

</div>

<div style="position: absolute; bottom: 30%; right: 2%; transform: rotate(-12deg); opacity: 0.6; font-size: 0.7em;">

```python
libro = Biblioteca.buscar(id)
"Libro desconocido" if libro is None else libro.autor
```

</div>

</div>

<!-- Mensaje "Libro desconocido" aproximándose en 3 transiciones -->
<div class="fragment" style="position: absolute; top: 20%; left: 20%; font-size: 1em; color: #e74c3c; font-weight: bold; opacity: 0.7; font-family: monospace; background: rgba(0, 0, 0, 0.7); padding: 10px; border-radius: 5px;">
"Libro desconocido"
</div>

<div class="fragment" style="position: absolute; top: 35%; left: 35%; font-size: 2em; color: #e74c3c; font-weight: bold; opacity: 0.85; font-family: monospace; background: rgba(0, 0, 0, 0.75); padding: 15px; border-radius: 8px;">
"Libro desconocido"
</div>

<div class="fragment" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 4em; color: #e74c3c; font-weight: bold; opacity: 1; text-shadow: 0 0 20px rgba(231, 76, 60, 0.8); font-family: monospace; background: rgba(0, 0, 0, 0.85); padding: 20px; border-radius: 10px;">
"Libro desconocido !!!"
</div>

</div>

--

<!-- .slide: id="shotgun-surgery" -->

## ¿Qué pasa si quiero cambiar ese valor?

--

<img alt="shotgun surgery" src="./images/shotgun_surgery.png" width="70%" >  

--

<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%; gap: 20px;">

<div style="display: flex; flex-direction: column; width: 60%; gap: 5%;">

<div style="background-color: #4CAF50; height: 20%; border: 2px solid #000; display: flex; align-items: center; justify-content: center;">
<h3 style="margin: 0; color: #000; visibility: hidden;"><em>Buscando</em> la Abstracción</h3>
</div>

<div style="background-color: #4CAF50; height: 20%; border: 2px solid #000; display: flex; align-items: center; justify-content: center;">
<h3 style="margin: 0; color: #000; visibility: hidden;"><em>Centrado</em> en los Mensajes</h3>
</div>

<div style="background-color: #4CAF50; height: 20%; border: 2px solid #000; display: flex; align-items: center; justify-content: center;">
<h3 style="margin: 0; color: #000;"><em>Reacio</em> a los Condicionales</h3>
</div>

<div style="background-color: #4CAF50; height: 20%; border: 2px solid #000; display: flex; align-items: center; justify-content: center; margin-top: 30px;">
<h3 style="margin: 0; color: #000;"><em>Infectado</em> por Smalltalk </h3>
</div>

</div>
</div>

--

<!-- .slide: data-transition="none" -->

<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%; gap: 20px;">

<div style="display: flex; flex-direction: column; width: 60%; gap: 5%;">

<div style="background-color: #4CAF50; height: 20%; border: 2px solid #000; display: flex; align-items: center; justify-content: center;">
<h3 style="margin: 0; color: #000; visibility: hidden;"><em>Buscando</em> la Abstracción</h3>
</div>

<div style="background-color: #4CAF50; height: 20%; border: 2px solid #000; display: flex; align-items: center; justify-content: center;">
<h3 style="margin: 0; color: #000;"><em>Centrado</em> en los Mensajes</h3>
</div>

<div style="background-color: #4CAF50; height: 20%; border: 2px solid #000; display: flex; align-items: center; justify-content: center;">
<h3 style="margin: 0; color: #000;"><em>Reacio</em> a los Condicionales</h3>
</div>

<div style="background-color: #4CAF50; height: 20%; border: 2px solid #000; display: flex; align-items: center; justify-content: center; margin-top: 30px;">
<h3 style="margin: 0; color: #000;"><em>Infectado</em> por Smalltalk </h3>
</div>

</div>
</div>

--


<div style="display: flex; justify-content: space-around; overflow: hidden;">
<div style="flex: 1 1 auto; padding: 10px;">

```python
if libro is None:
    return "Libro desconocido"
else:
    return libro.autor
```

</div>
<div style="flex: 1 1 auto; padding: 10px;">

```python
if ( Objeto del cual conozco el tipo ):
    # Yo proveo el comportamiento
else:
    # Le envío un mensaje al objeto
```

</div>
</div>

--

```python [|4]
if libro is None:
    return "Libro desconocido"
else:
    return libro.autor
```

NOTES:
No quiero saber todo el tiempo si el objeto es None o no, solo quiero 
mandarle un mensaje

--

```python
class Libro:
    @property
    def autor(self):
        ...
```

```python
class NoneType:
    # No entiende el mensaje "autor"
```
<!-- .element: class="fragment" -->

NOTES:
El problema está en que unas veces recibimos el objeto Libro y otras veces NoneType que no entiende el mensaje autor.

--

<!-- .slide: data-transition="none" -->

```python
class Libro:
    @property
    def autor(self):
        ...
```

```python
class ???:
    @property
    def autor(self):
        return "Libro desconocido"
```
<!-- .element: class="fragment" -->

--

<!-- .slide: data-transition="none" -->

```python
class Libro:
    @property
    def autor(self):
        ...
```

```python
class LibroDesconocido:
    @property
    def autor(self):
        return "Libro desconocido"
```

--

```python [4]
ids = ["Los Sorias", "", "El Fiord"]

libros = [ 
    Biblioteca.buscar(id)
    for id in ids ]
# => [
# <__main__.Libro object at 0x7f0f49464ec0> id:Los Sorias,
# None,
# <__main__.Libro object at 0x7f0f48e11a90> id:El Fiord
# ]

for libro in libros:
    if libro is None:
        print("Libro desconocido")
    else:
        print(libro.autor)
```

--

<!-- .slide: data-transition="none" -->

```python [4|4,8]
ids = ["Los Sorias", "", "El Fiord"]

libros = [ 
    Biblioteca.buscar(id) or LibroDesconocido() 
    for id in ids ]
# => [
# <__main__.Libro object at 0x7f0f49464ec0> id:Los Sorias,
# None,
# <__main__.Libro object at 0x7f0f48e11a90> id:El Fiord
# ]

for libro in libros:
    if libro is None:
        print("Libro desconocido")
    else:
        print(libro.autor)
```

--

<!-- .slide: data-transition="none" -->

```python [8|4,13|13-16|13-15]
ids = ["Los Sorias", "", "El Fiord"]

libros = [ 
    Biblioteca.buscar(id) or LibroDesconocido() 
    for id in ids ]
# => [
# <__main__.Libro object at 0x7f0f49464ec0> id:Los Sorias,
# <__main__.LibroDesconocido at 0x7f0f49464c20>,
# <__main__.Libro object at 0x7f0f48e11a90> id:El Fiord
# ]

for libro in libros:
    if libro is None:
        print("Libro desconocido")
    else:
        print(libro.autor)
```

NOTES:
¿Es mejor este codigo?
- tenemos una nueva dependencia
- todavía tenemos un condicional
- pero ya no somos responsables del comportamiento

--

<!-- .slide: data-transition="none" -->

```python [12-13]
ids = ["Los Sorias", "", "El Fiord"]

libros = [ 
    Biblioteca.buscar(id) or LibroDesconocido() 
    for id in ids ]
# => [
# <__main__.Libro object at 0x7f0f49464ec0> id:Los Sorias,
# <__main__.LibroDesconocido at 0x7f0f49464c20>,
# <__main__.Libro object at 0x7f0f48e11a90> id:El Fiord
# ]

for libro in libros:
        print(libro.autor)
```

--

<!-- .slide: data-transition="none" -->

```python [12-13]
ids = ["Los Sorias", "", "El Fiord"]

libros = [ 
    Biblioteca.buscar(id) or LibroDesconocido() 
    for id in ids ]
# => [
# <__main__.Libro object at 0x7f0f49464ec0> id:Los Sorias,
# <__main__.LibroDesconocido at 0x7f0f49464c20>,
# <__main__.Libro object at 0x7f0f48e11a90> id:El Fiord
# ]

for libro in libros:
    print(libro.autor)
```

--

```python [12-17]
ids = ["Los Sorias", "", "El Fiord"]

libros = [ 
    Biblioteca.buscar(id) or LibroDesconocido() 
    for id in ids ]
# => [
# <__main__.Libro object at 0x7f0f49464ec0> id:Los Sorias,
# <__main__.LibroDesconocido at 0x7f0f49464c20>,
# <__main__.Libro object at 0x7f0f48e11a90> id:El Fiord
# ]

for libro in libros:
    print(libro.autor)
# => 
# Alberto Laiseca
# Libro desconocido
# Osvaldo Lamborghini
```


--

```python
class Libro:
    @property
    def autor(self):
        ...
```

```python [1]
class LibroDesconocido:
    @property
    def autor(self):
        return "Libro desconocido"
```
<!-- .element: class="fragment" -->

--

### Patrón del Objeto Nulo

*Null Object Pattern*
<!-- .element: class="fragment fade-out" -->


**'La Nada Activa'** 
<!-- .element: class="fragment" -->

--


```python [4]
ids = ["Los Sorias", "", "El Fiord"]

libros = [ 
    Biblioteca.buscar(id) or LibroDesconocido() 
    for id in ids ]

for libro in libros:
    print(libro.autor)
# => 
# Alberto Laiseca
# Libro desconocido
# Osvaldo Lamborghini
```

--

Tenemos que preferir conocer un objeto que duplicar comportamiento.

--

Tenemos que preferir conocer **pocos** objetos.

--

<div style="position: relative; height: 600px; width: 100%;">

<!-- Snippet central - sin modificar -->
<div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">

```python
libro = Biblioteca.buscar(id) or LibroDesconocido()
libro.autor
```

</div>

<!-- Primera transición - snippets en esquinas y parte superior -->
<div class="fragment">

<div style="position: absolute; top: 5%; left: 5%; transform: rotate(-15deg); opacity: 0.6; font-size: 0.7em;">

```python
libro = Biblioteca.buscar(id) or LibroDesconocido()
libro.autor
```

</div>

<div style="position: absolute; top: 5%; right: 5%; transform: rotate(12deg); opacity: 0.6; font-size: 0.7em;">

```python
libro = Biblioteca.buscar(id) or LibroDesconocido()
libro.autor
```

</div>

<div style="position: absolute; top: 30%; left: 2%; transform: rotate(-20deg); opacity: 0.6; font-size: 0.7em;">

```python
libro = Biblioteca.buscar(id) or LibroDesconocido()
libro.autor
```

</div>

<div style="position: absolute; top: 30%; right: 2%; transform: rotate(18deg); opacity: 0.6; font-size: 0.7em;">

```python
libro = Biblioteca.buscar(id) or LibroDesconocido()
libro.autor
```

</div>

</div>

<!-- Segunda transición - snippets en parte inferior y lados -->
<div class="fragment">

<div style="position: absolute; bottom: 5%; left: 5%; transform: rotate(10deg); opacity: 0.6; font-size: 0.7em;">

```python
libro = Biblioteca.buscar(id) or LibroDesconocido()
libro.autor
```

</div>

<div style="position: absolute; bottom: 5%; right: 5%; transform: rotate(-15deg); opacity: 0.6; font-size: 0.7em;">

```python
libro = Biblioteca.buscar(id) or LibroDesconocido()
libro.autor
```

</div>

<div style="position: absolute; bottom: 30%; left: 2%; transform: rotate(20deg); opacity: 0.6; font-size: 0.7em;">

```python
libro = Biblioteca.buscar(id) or LibroDesconocido()
libro.autor
```

</div>

<div style="position: absolute; bottom: 30%; right: 2%; transform: rotate(-12deg); opacity: 0.6; font-size: 0.7em;">

```python
libro = Biblioteca.buscar(id) or LibroDesconocido()
libro.autor
```

</div>

</div>

<!-- Mensaje "Libro desconocido" aproximándose en 3 transiciones -->
<div class="fragment" style="position: absolute; top: 20%; left: 20%; font-size: 1em; color: #e74c3c; font-weight: bold; opacity: 0.7; font-family: monospace; background: rgba(0, 0, 0, 0.7); padding: 10px; border-radius: 5px;">
"LibroDesconocido"
</div>

<div class="fragment" style="position: absolute; top: 35%; left: 35%; font-size: 2em; color: #e74c3c; font-weight: bold; opacity: 0.85; font-family: monospace; background: rgba(0, 0, 0, 0.75); padding: 15px; border-radius: 8px;">
"LibroDesconocido"
</div>

<div class="fragment" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 4em; color: #e74c3c; font-weight: bold; opacity: 1; text-shadow: 0 0 20px rgba(231, 76, 60, 0.8); font-family: monospace; background: rgba(0, 0, 0, 0.85); padding: 20px; border-radius: 10px;">
"LibroDesconocido ???"
</div>

</div>

--

```python
class Biblioteca:

    @staticmethod
    def buscar(id):
        ...
```

--


```python
class BibliotecaSegura:

    @staticmethod
    def buscar(id):
        return Biblioteca.buscar(id) or LibroDesconocido()
```

--

```python [2]
libros = [ 
    Biblioteca.buscar(id) or LibroDesconocido() 
    for id in ids ]
```

--

<!-- .slide: data-transition="none" -->

```python [2]
libros = [ 
    BibliotecaSegura.buscar(id) 
    for id in ids ]
```

--


```python [2|]
libros = [ 
    BibliotecaSegura.buscar(id) 
    for id in ids ]
# => [
# <__main__.Libro object at 0x7f0f49464ec0> id:Los Sorias,
# <__main__.LibroDesconocido at 0x7f0f49464c20>,
# <__main__.Libro object at 0x7f0f48e11a90> id:El Fiord
# ]
```

```python
for libro in libros:
    print(libro.autor)
# => 
# Alberto Laiseca
# Libro desconocido
# Osvaldo Lamborghini
```
<!-- .element: class="fragment" -->


---


<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%; gap: 20px;">

<div style="display: flex; flex-direction: column; width: 60%; gap: 5%;">

<div style="background-color: #4CAF50; height: 20%; border: 2px solid #000; display: flex; align-items: center; justify-content: center;">
<h3 style="margin: 0; color: #000; visibility: hidden;"><em>Buscando</em> la Abstracción</h3>
</div>

<div style="background-color: #4CAF50; height: 20%; border: 2px solid #000; display: flex; align-items: center; justify-content: center;">
<h3 style="margin: 0; color: #000;"><em>Centrado</em> en los Mensajes</h3>
</div>

<div style="background-color: #4CAF50; height: 20%; border: 2px solid #000; display: flex; align-items: center; justify-content: center;">
<h3 style="margin: 0; color: #000;"><em>Reacio</em> a los Condicionales</h3>
</div>

<div style="background-color: #4CAF50; height: 20%; border: 2px solid #000; display: flex; align-items: center; justify-content: center; margin-top: 30px;">
<h3 style="margin: 0; color: #000;"><em>Infectado</em> por Smalltalk </h3>
</div>

</div>
</div>

--

<!-- .slide: data-transition="none" -->

<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%; gap: 20px;">

<div style="display: flex; flex-direction: column; width: 60%; gap: 5%;">

<div style="background-color: #4CAF50; height: 20%; border: 2px solid #000; display: flex; align-items: center; justify-content: center;">
<h3 style="margin: 0; color: #000;"><em>Buscando</em> la Abstracción</h3>
</div>

<div style="background-color: #4CAF50; height: 20%; border: 2px solid #000; display: flex; align-items: center; justify-content: center;">
<h3 style="margin: 0; color: #000;"><em>Centrado</em> en los Mensajes</h3>
</div>

<div style="background-color: #4CAF50; height: 20%; border: 2px solid #000; display: flex; align-items: center; justify-content: center;">
<h3 style="margin: 0; color: #000;"><em>Reacio</em> a los Condicionales</h3>
</div>

<div style="background-color: #4CAF50; height: 20%; border: 2px solid #000; display: flex; align-items: center; justify-content: center; margin-top: 30px;">
<h3 style="margin: 0; color: #000;"><em>Infectado</em> por Smalltalk </h3>
</div>

</div>
</div>

--

## Hasta acá seguimos la charla de Sandi Metz

NOTES:
Acá tengo que detallar que la charla de Sandi sigue con un ejemplo largo y que 
es ultra recomendable seguirlo

--

## Pensemos el Vacio

NOTES:
Pero vamos a detallar la Abstracción 

--

<img src="./images/taza.png" width="70%">

--

<!-- .slide: id="filosofia-nada" -->

### El Principio de la Utilidad del Vacío

**Tao Te Ching:**
> "Trabajamos con el ser, pero el no-ser es lo que usamos."
<!-- .element: class="fragment" -->

--

<img src="./images/zen-python.png" width="70%">

---

Lo que tenemos que entender es la función del vacío.

--

<!-- .slide: id="monoides" -->

- 10 + 0 = 10
<!-- .element: class="fragment" -->

- 4 * 1 = 4
<!-- .element: class="fragment" -->

- `"Hola" + "" = "Hola"`
<!-- .element: class="fragment" -->

- `[1, 2] + [] = [1, 2]`
<!-- .element: class="fragment" -->

- `pd.concat([df, pd.DataFrame()]) = df`
<!-- .element: class="fragment" -->

- `set.union(A, set()) = A`
<!-- .element: class="fragment" -->

- $\mathbb{M} * \mathbb{I} = \mathbb{M}$
<!-- .element: class="fragment" -->

<div>

- `lambda x: x`

- `def identidad(x): return x`
</div>
<!-- .element: class="fragment" -->

--

**Monoide:** Una estructura algebraica con una operación binaria y un elemento identidad

--

<!-- .slide: id="paralelizacion" -->

## Los Monoides y la Paralelización

NOTES:
La abstracción de monoide no es solo elegancia matemática, es la clave para algoritmos paralelizables.

--

### ¿Por qué importan los monoides?

Las operaciones asociativas se pueden **dividir**
<!-- .element: class="fragment" -->

--

```python
# Operación asociativa: (a + b) + c = a + (b + c)
total = sum([1, 2, 3, 4, 5, 6, 7, 8])
```

--

<!-- .slide: data-transition="none" -->

```python
# Podemos dividir el trabajo
chunk1 = sum([1, 2, 3, 4])  # = 10
chunk2 = sum([5, 6, 7, 8])  # = 26
total = chunk1 + chunk2     # = 36
```

--

### Propiedades Clave para Paralelización

1. **Asociatividad**: `(a ⊕ b) ⊕ c = a ⊕ (b ⊕ c)`
<!-- .element: class="fragment" -->

2. **Elemento Identidad**: `a ⊕ e = e ⊕ a = a`
<!-- .element: class="fragment" -->

3. **Sin efectos secundarios**: Funciones puras
<!-- .element: class="fragment" -->

--

### De los Objetos Nulos a la Alta Performance

- Los patrones que eliminan condicionales...
<!-- .element: class="fragment" -->

- ...facilitan el razonamiento sobre el código...
<!-- .element: class="fragment" -->

- ...y permiten optimizaciones automáticas
<!-- .element: class="fragment" -->

NOTES:
El código bien abstraído es más fácil de paralelizar y optimizar.

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

### Transformamos prototipos en sistemas de producción

- Refactorización guiada por principios
- Optimización de rendimiento (benchmarkeado)
- Arquitecturas desacopladas y mantenibles
- Stack: `Python` `Julia` `C#`

--

### Capacitación Técnica

**Para laboratorios de investigación y equipos de I+D**

<div style="font-size: 0.9em; margin-top: 2rem;">

- Fundamentos de Computación Numérica
- Rigor de Producción (TDD, CI/CD)
- Machine Learning Científico
- Programación con Julia para Software de Alto Rendimiento
- Diseño de Sistemas Arquitectónicos

</div>

<p style="margin-top: 2rem;">
<a href="https://phorma.sh/es/trainees" style="border-bottom: 2px solid;">phorma.sh/es/trainees</a>
</p>

--

> Y una técnica que te sirve para escribir te tiene que servir también para vivir. O sea que si yo lo único que te voy a dar es tecniquería (sic), no sirve para nada. 
— **Fabián Casas**

--

<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%;">

<h3>¿Listo para eliminar los condicionales de tu código?</h3>

<div style="margin-top: 2rem; font-size: 1.2em;">

**[info@phorma.sh](mailto:info@phorma.sh)**

**[sasha@phorma.sh](mailto:sasha@phorma.sh)**

</div>

<p style="margin-top: 2rem; font-family: monospace; color: #666;">
Estructura sobre el Caos
</p>

</div>

---

<!-- .slide: id="gracias" -->

## Gracias
