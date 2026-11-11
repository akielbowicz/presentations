// Visor de conocimiento: el instrumento para pensar con lo que construyó Python.
// Vanilla JS, sin framework, sin build. Los datos vienen del Lado A.

const DATOS = [
  { archivo: "conocimiento.json", etiqueta: "atómico" },
  { archivo: "conocimiento-estructura.json", etiqueta: "estructura" },
];

const estado = {
  datos: null, // el documento cargado
  busqueda: "",
  seccion: "todas",
  seleccionada: null, // id de la afirmación mostrada como evidencia
};

const $ = (selector) => document.querySelector(selector);

function esc(texto) {
  const nodo = document.createElement("span");
  nodo.textContent = texto;
  return nodo.innerHTML;
}

async function cargar(archivo) {
  const respuesta = await fetch(`data/${archivo}`);
  estado.datos = await respuesta.json();
  estado.seccion = "todas";
  estado.busqueda = "";
  $("#busqueda").value = "";
  estado.seleccionada = null;
  render();
}

function afirmacionesFiltradas() {
  const { afirmaciones } = estado.datos;
  const q = estado.busqueda.trim().toLowerCase();
  return afirmaciones.filter((a) => {
    if (estado.seccion !== "todas" && a.seccion !== estado.seccion) return false;
    if (q && !a.texto.toLowerCase().includes(q)) return false;
    return true;
  });
}

function seccionesConConteo() {
  const conteo = new Map();
  for (const a of estado.datos.afirmaciones) {
    conteo.set(a.seccion, (conteo.get(a.seccion) ?? 0) + 1);
  }
  return [...conteo.entries()].sort((x, y) => y[1] - x[1]);
}

// El visor no juzga: solo marca lo que se ve a simple vista.
function tipoVisible(a) {
  if (a.texto.trim().startsWith("¿") || a.texto.trim().startsWith("¡")) {
    return "pregunta";
  }
  if (a.texto.trim().length < 30) {
    return "corta";
  }
  return null;
}

function renderMeta() {
  const d = estado.datos;
  const secciones = new Set(d.afirmaciones.map((a) => a.seccion));
  $("#meta").textContent =
    `${d.documento} · extractor ${d.extractor.version} · ` +
    `${d.afirmaciones.length} afirmaciones de ${d.episodios.length} episodios ` +
    `en ${secciones.size} secciones`;
}

function renderInterruptores() {
  const contenedor = $("#datos");
  contenedor.replaceChildren();
  const activo = new URLSearchParams(location.search).get("data") ?? DATOS[0].archivo;
  for (const d of DATOS) {
    const boton = document.createElement("button");
    boton.textContent = d.etiqueta;
    boton.dataset.activo = String(d.archivo === activo);
    boton.addEventListener("click", () => {
      const url = new URL(location);
      url.searchParams.set("data", d.archivo);
      history.replaceState(null, "", url);
      cargar(d.archivo);
    });
    contenedor.append(boton);
  }
}

function renderChips() {
  const contenedor = $("#secciones");
  contenedor.replaceChildren();
  const conteadas = seccionesConConteo();
  // Documentos reales traen cientos de secciones: top por conteo,
  // y la sección activa queda siempre visible aunque no entre en el top.
  const tope = conteadas.slice(0, 12);
  if (estado.seccion !== "todas" && !tope.some(([s]) => s === estado.seccion)) {
    tope.push(...conteadas.filter(([s]) => s === estado.seccion));
  }
  const opciones = [["todas", `todas (${estado.datos.afirmaciones.length})`],
    ...tope.map(([seccion, conteo]) => [seccion, `${seccion} (${conteo})`])];
  for (const [seccion, etiqueta] of opciones) {
    const boton = document.createElement("button");
    boton.textContent = etiqueta;
    boton.dataset.activo = String(estado.seccion === seccion);
    boton.addEventListener("click", () => {
      estado.seccion = seccion;
      estado.seleccionada = null;
      render();
    });
    contenedor.append(boton);
  }
}

function renderLista() {
  const lista = $("#afirmaciones");
  const filtradas = afirmacionesFiltradas();
  lista.replaceChildren();
  if (filtradas.length === 0) {
    const vacio = document.createElement("li");
    vacio.className = "vacio";
    vacio.textContent = "nada por acá con estos filtros";
    lista.append(vacio);
    return;
  }
  for (const a of filtradas) {
    const item = document.createElement("li");
    item.dataset.seleccionada = String(a.id === estado.seleccionada);
    const texto = document.createElement("p");
    texto.className = "texto";
    texto.textContent = a.texto;
    const tags = document.createElement("span");
    tags.className = "tags";
    const tagSeccion = document.createElement("span");
    tagSeccion.className = "tag";
    tagSeccion.textContent = a.seccion;
    const tagLinea = document.createElement("span");
    tagLinea.className = "tag";
    tagLinea.textContent = `L${a.linea}`;
    tags.append(tagSeccion, tagLinea);
    const tipo = tipoVisible(a);
    if (tipo) {
      const tagTipo = document.createElement("span");
      tagTipo.className = "tag";
      tagTipo.dataset.tipo = tipo;
      tagTipo.textContent = tipo;
      tags.append(tagTipo);
    }
    item.append(texto, tags);
    item.addEventListener("click", () => {
      estado.seleccionada = a.id;
      render();
    });
    lista.append(item);
  }
}

function renderEvidencia() {
  const panel = $("#evidencia");
  const seleccionada = estado.datos.afirmaciones.find(
    (a) => a.id === estado.seleccionada
  );
  if (!seleccionada) {
    panel.hidden = true;
    return;
  }
  panel.hidden = false;
  $("#cita").textContent = seleccionada.cita;
  $("#fuente").textContent =
    `${seleccionada.seccion} · línea ${seleccionada.linea} de ${estado.datos.documento}`;
}

function render() {
  renderMeta();
  renderChips();
  renderLista();
  renderEvidencia();
}

$("#busqueda").addEventListener("input", (evento) => {
  estado.busqueda = evento.target.value;
  render();
});

renderInterruptores();
await cargar(new URLSearchParams(location.search).get("data") ?? DATOS[0].archivo);
