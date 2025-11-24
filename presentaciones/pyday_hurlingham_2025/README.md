# PyDay Hurlingham - Noviembre 2025

## Nada es Algo: ¿Existe la Programación Orientada a Objetos sin if?

[evento](https://eventos.python.org.ar/events/pyday-hurlingham-2025/)
~[video]()~
[diapos/slides](https://slides.saxa.xyz/slides/pyday_hurlingham_2025/slides)
[fuente/source](https://github.com/akielbowicz/presentations/blob/master/presentaciones/pyday_hurlingham_2025/)

## Archivos

* `index.html` - Página HTML principal para visualizar la presentación
* `slides.md` - Contenido de la presentación en formato Markdown

## Cómo ver la presentación

### Opción 1: Servidor Local

```bash
# Con Python
python -m http.server 8000

# Con Node.js
npx http-server

# Luego abrir en el navegador:
# http://localhost:8000
```

### Opción 2: Abrir directamente

Si tu navegador lo permite, puedes abrir `index.html` directamente.

## Estructura de la Charla (25 minutos)

1. **Introducción** (2 min) - El problema del None
2. **Null Object Pattern** (6 min) - "Nada es siempre algo"
3. **Null Object en Data** (2 min) - Monoides y DataFrames vacíos
4. **Composición** (7 min) - Roles vs Herencia
5. **Cierre** (7 min) - Resumen y servicios

## Temas Clave

* Null Object Pattern
* Polimorfismo sobre condicionales
* Composición sobre herencia
* Dependency Injection
* Programación funcional (Monoides)

## Personalización

Antes de presentar, edita `slides.md` y reemplaza los siguientes placeholders:

* `[Tu Nombre]` - Tu nombre completo
* `[Tu Título y Especialidad]` - Tu título profesional
* `[Punto clave de tu experiencia]` - Tus puntos de experiencia (2 items)
* `[Tu Contacto Principal / Twitter]` - Tu usuario de Twitter/X o contacto principal
* `[Tu Email]` - Tu dirección de email
* `[Tu LinkedIn]` - Tu perfil de LinkedIn

## Navegación en la Presentación

Durante la presentación, usa estas teclas:

* `→` o `Espacio` - Siguiente slide
* `←` - Slide anterior
* `Esc` o `O` - Vista general (overview)
* `F` - Pantalla completa
* `S` - Modo presentador (speaker notes)
* `?` - Ayuda con todos los comandos

## Editar el Contenido

### Estructura del Markdown

Las slides están separadas por `---` (tres guiones). Para agregar o modificar slides:

1. Abre `slides.md` en tu editor favorito
2. Cada sección `---` representa una nueva slide
3. Usa `#` para títulos, `##` para subtítulos, etc.
4. Los bloques de código van entre triple backtick con lenguaje: ` ```python `

### Ejemplo de Slide

```markdown
## Título de la Slide

### Subtítulo

* Punto uno
* Punto dos

` ``python
def ejemplo():
    return "código"
` ``
```

## Cambiar el Tema

En `index.html`, línea 13, puedes cambiar el tema:

```html
<!-- Temas disponibles: black, white, league, beige, sky, night, serif, simple, solarized -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.0.4/dist/theme/black.css">
```

## Exportar a PDF

1. Abre la presentación en Chrome o Chromium
2. Agrega `?print-pdf` al final de la URL: `http://localhost:8000?print-pdf`
3. Usa Ctrl+P (o Cmd+P en Mac) y selecciona "Guardar como PDF"
4. Importante: Desmarca "Encabezados y pies de página" en las opciones de impresión

## Troubleshooting

### La presentación no carga

* Verifica que el servidor esté corriendo en el puerto correcto
* Asegúrate de tener conexión a internet (reveal.js se carga desde CDN)
* Revisa la consola del navegador (F12) para ver errores

### El código Python no se ve bien

* Verifica que los bloques de código tengan ` ```python ` correctamente
* Asegúrate de que el plugin de highlight esté cargando

### Los cambios no se reflejan

* Refresca el navegador (Ctrl+R o Cmd+R)
* Si usas cache, prueba con Ctrl+Shift+R (hard refresh)

## Recursos Adicionales

* [Documentación oficial de reveal.js](https://revealjs.com/)
* [Markdown Guide](https://www.markdownguide.org/)
* [Python Syntax Highlighting](https://highlightjs.org/)

## Timing de la Presentación

* **Total:** 25 minutos
* Practica con el modo presentador (`S`) para ver el tiempo
* Deja 1-2 minutos de buffer para preguntas durante la charla
