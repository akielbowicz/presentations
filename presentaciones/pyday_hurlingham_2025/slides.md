# Nada es Algo

## ¿Existe la Programación Orientada a Objetos sin if?

**PyDay Hurlingham 2025**

---

## El Peor Enemigo del Desarrollador Python 💥

### Cuando la Búsqueda Falla...

---

## EL PROBLEMA EN VIVO

```python
# Un gestor busca un libro por ID
class GestorInventario:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def procesar_libro(self, libro_id):
        libro = self.repositorio.buscar(libro_id)

        # ¡Atención! Si no se encuentra, libro es None
        return libro.obtener_portada()
```

---

## EL RESULTADO

### ¡AttributeError!

```
'NoneType' object has no attribute 'obtener_portada'
```

---

## El Parche Universal

### La Solución Anti-OO de Todos los Días

```python
def procesar_libro(self, libro_id):
    libro = self.repositorio.buscar(libro_id)

    if libro is None:
        return "placeholder_default.jpg"
    else:
        return libro.obtener_portada()
```

**Pregunta: ¿Hay una mejor manera de diseñar esto?**

---

## La Tesis de Sandi Metz

### La Programación Orientada a Objetos Perfecta NO USA if.

---

## Quién Soy

**[Tu Nombre]**

* [Tu Título y Especialidad]
* [Punto clave de tu experiencia]
* [Punto clave de tu experiencia]

---

# TEMA 1: NULL OBJECT

## (6 minutos)

---

## La Gran Idea

### "Nada es Siempre Algo"

* **Costo del if:** Acoplamiento, Fragilidad, Pruebas complejas
* El buen diseño elimina la necesidad de preguntar

---

## Solución 1: Null Object Pattern

### La "Nada Activa"

* **LibroNoEncontrado** (Objeto Nulo)
* Conformidad de Interfaz

---

## Implementación

```python
# El objeto que representa la AUSENCIA de un Libro
class LibroNoEncontrado:
    def obtener_portada(self):
        # Implementación de comportamiento neutro
        return "placeholder_default.jpg"

    def registrar_prestamo(self):
        pass # No tiene side effects
```

---

## Código Cliente Limpio

### Reemplazamos la Condición por Polimorfismo

* El GestorInventario confía en el mensaje
* El cliente no tiene que saber si es `Libro` o `LibroNoEncontrado`

---

## Aislamiento

### ¿Dónde va el if?

* La condición solo vive en el **Repositorio** o en el código de inicialización
* El Repositorio devuelve siempre un objeto funcional

---

# TEMA 2: NULL OBJECT EN DATA

## (2 minutos)

---

## Paralelo Funcional: Monoides

### El Objeto Nulo en Data Processing

* En el procesamiento de datos, la **Identidad Monoidal** es el "Null Object"
* Ejemplo Clásico: Si queremos appendear resultados de múltiples procesos

---

## La Lista Vacía y el DataFrame Vacío

* Si un proceso no encuentra datos ("Nada"), debe devolver la **Identidad**
* **Identidad:** Una lista vacía `[]` o un DataFrame vacío `pd.DataFrame()`
* **Beneficio:** Permite que el paso siguiente (concatenación) se ejecute sin if y sin errores

> **Nota:** Crear un DataFrame vacío puede ser más costoso que un simple if en loops muy rápidos. Es una compensación entre legibilidad/robustez y velocidad.

---

# TEMA 3: COMPOSICIÓN

## (7 minutos)

---

## Solución 3: Composición

### Evitando la Trampa de la Herencia

---

## La Trampa de la Herencia

### "Es un" (is-a) vs. "Tiene un" (has-a)

* La herencia es solo para la **especialización**
* Usarla para reúso de código causa **Explosión Combinatoria**

---

## El Pensamiento Correcto

### De "¿Qué ES este objeto?" a "¿Qué ROL juega?"

* Debemos aislar la variación y nombrar la abstracción

---

## El Rol y la Inyección

### Composición con Dependency Injection (DI)

**Principio:** El objeto principal depende de (usa) Roles que se le entregan en el constructor

---

## Código con Roles

```python
class Notificador:
    def __init__(self, metodo_alerta):
        self.alerta = metodo_alerta

    def enviar(self):
        self.alerta.ejecutar()

# La variación vive en 'metodo_alerta'
# (Email, SMS, Slack), no en 'Notificador'.
```

---

## La Victoria de la Composición

### ¡Puedes combinar cualquier Rol con cualquier Entidad!

* El código es más flexible
* Más fácil de probar
* Más mantenible

---

# CIERRE Y CALL TO ACTION

## (7 minutos)

---

## La Filosofía de la Nada

### El Principio de la Utilidad del Vacío

**Tao Te Ching:**
> "Trabajamos con el ser, pero el no-ser es lo que usamos."

La abstracción se esconde en el espacio vacío (la ausencia de if)

---

## Resumen Final

### Tres Pasos para el Código Limpio

1. **Encuentra la Nada:** Identifica la lógica condicional
2. **Nómbrala:** Crea el Rol (la abstracción)
3. **Hazla un Objeto:** Implementa el Null Object o usa la Composición

---

## ¡Preguntas!

**[Tu Contacto Principal / Twitter]**

---

## Servicios de Consultoría

### ¿Tu código sufre de if y acoplamiento?

* **Refactorización Estratégica:** Transformación de monolitos
* **Diseño Orientado a Objetos:** Aplicación de patrones avanzados
* **Auditoría de Código:** Identificación y corrección de fragilidad

---

## Tutorías y Mentoring

### Invierte en tu futuro como desarrollador senior

* Clases personalizadas de Python avanzado
* Sesiones de TDD y Pruebas Unitarias
* Formación en Arquitectura de Software

---

## Gracias

### Contacto y Redes

* **Email:** [Tu Email]
* **LinkedIn:** [Tu LinkedIn]
* ¡Hablemos de código!
