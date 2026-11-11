/* muestreo — visor del contrato JSON que produce el lab (Lado A).
   Vanilla JS a propósito: el contrato es el JSON, no un framework.

   Regla de la casa: el contrato habla en números (f_opt, k, σ);
   este visor los traduce a palabras. El JSON no cambia. */
"use strict";

const ROJO = "#C83534";
const GRIS = "#8a8a86";
const BLANCO = "#FBFAFA";

let contrato = null;
let tramoActivo = null;

const canvas = document.getElementById("grafico");
const ctx = canvas.getContext("2d");

fetch("data/recomendacion.json")
  .then((r) => {
    if (!r.ok) throw new Error(`HTTP ${r.status}`);
    return r.json();
  })
  .then((data) => {
    contrato = data;
    preparoEscala();
    pintoMeta();
    pintoChips();
    pintoGrafico();
    pintoTabla();
  })
  .catch(() => {
    // fetch() bajo file:// está bloqueado: sin servidor no hay visor.
    document.getElementById("error").hidden = false;
  });

/* Traducción del dato a palabras: qué tan fuerte se movió el teléfono
   en cada tramo, según lo que el análisis pidió medir. La captura
   sintética ya trae nombre propio; la real llega como "t=0s". */
function describo(s) {
  if (!s.nombre.startsWith("t=")) return s.nombre;
  if (s.f_opt <= 3) return "quieto";
  if (s.f_opt <= 16) return "se mueve poco";
  if (s.f_opt <= 30) return "se mueve mucho";
  return "sacudón";
}

function totalMuestras() {
  return contrato.segmentos.reduce(
    (acc, s) => ({ a: acc.a + s.muestras_60hz, b: acc.b + s.muestras_f_opt }),
    { a: 0, b: 0 }
  );
}

function pintoMeta() {
  const m = contrato.meta;
  document.getElementById("meta").textContent =
    `El teléfono grabó ${m.duracion_s} s a ${m.f_captura} Hz: ` +
    `${m.n_muestras} lecturas de aceleración. ¿Cuántas hacían falta de verdad?`;

  const t = totalMuestras();
  document.getElementById("ahorro").textContent =
    `Con medir al ritmo justo alcanzan ${t.b} de ${t.a} muestras ` +
    `(${Math.round((100 * t.b) / t.a)}%): el resto era ruido.`;
}

function pintoChips() {
  const nav = document.getElementById("chips");
  contrato.segmentos.forEach((s, i) => {
    const chip = document.createElement("div");
    chip.className = "chip";
    chip.innerHTML =
      `<strong>${describo(s)}</strong> ${Math.round(s.desde_s)}–${Math.round(s.hasta_s)} s · ` +
      `alcanzan ${s.f_opt} Hz`;
    chip.title = `${s.muestras_f_opt} de ${s.muestras_60hz} muestras alcanzan`;
    chip.addEventListener("click", () => activo(i));
    nav.appendChild(chip);
  });
  tramoActivo = 0;
  nav.firstChild.classList.add("activa");
}

function activo(i) {
  tramoActivo = i;
  document.querySelectorAll(".chip").forEach((c, j) =>
    c.classList.toggle("activa", j === i)
  );
  pintoGrafico();
}

/* Escala Y contra el dato real: centrada en la media y con techo en el
   desvío típico del 98.5% de las muestras. La escala vieja (σ·40) era
   para el sintético: con la captura real (picos de 17 g) saturaba todo. */
let centro = 0;
let techo = 1;
function preparoEscala() {
  const { a } = contrato.senial;
  centro = a.reduce((s, x) => s + x, 0) / a.length;
  const desvios = a.map((x) => Math.abs(x - centro)).sort((x, y) => x - y);
  techo = Math.max(desvios[Math.floor(desvios.length * 0.985)] || 1, 0.5);
}

function escalaY(valor) {
  const h = canvas.height;
  const rel = Math.max(-1.05, Math.min(1.05, (valor - centro) / techo));
  return h / 2 - rel * (h / 2 - 12);
}

function pintoGrafico() {
  const { t, a } = contrato.senial;
  const seg = contrato.segmentos[tramoActivo];
  const paso = Math.max(1, Math.round(contrato.meta.f_medida / seg.f_opt));
  const dur = contrato.meta.duracion_s;
  const w = canvas.width;
  const h = canvas.height;

  ctx.clearRect(0, 0, w, h);

  // grilla de tiempo: dónde empieza y termina cada momento
  ctx.strokeStyle = "#2c2c2a";
  ctx.fillStyle = GRIS;
  ctx.font = "12px monospace";
  ctx.lineWidth = 1;
  [0, 0.25, 0.5, 0.75, 1].forEach((f) => {
    const x = Math.round(f * w) + 0.5;
    ctx.beginPath();
    ctx.moveTo(x, 0);
    ctx.lineTo(x, h);
    ctx.stroke();
    ctx.fillText(`${Math.round(f * dur)} s`, Math.min(x + 4, w - 30), h - 6);
  });

  // zona del tramo activo
  const x0 = (seg.desde_s / dur) * w;
  const x1 = (seg.hasta_s / dur) * w;
  ctx.fillStyle = "rgba(200, 53, 52, .12)";
  ctx.fillRect(x0, 0, x1 - x0, h);

  // toda la data (60 Hz): gris
  ctx.strokeStyle = GRIS;
  ctx.lineWidth = 1;
  ctx.beginPath();
  t.forEach((ti, i) => {
    const x = (ti / dur) * w;
    const y = escalaY(a[i]);
    i === 0 ? ctx.moveTo(x, y) : ctx.lineTo(x, y);
  });
  ctx.stroke();

  // lo que alcanza guardar (ritmo recomendado): blanco + puntos rojos
  const tDec = t.filter((_, i) => i % paso === 0);
  const aDec = a.filter((_, i) => i % paso === 0);
  ctx.strokeStyle = BLANCO;
  ctx.lineWidth = 1.5;
  ctx.beginPath();
  tDec.forEach((ti, i) => {
    const x = (ti / dur) * w;
    const y = escalaY(aDec[i]);
    i === 0 ? ctx.moveTo(x, y) : ctx.lineTo(x, y);
  });
  ctx.stroke();
  ctx.fillStyle = ROJO;
  tDec.forEach((ti, i) => {
    const x = (ti / dur) * w;
    ctx.fillRect(x - 1.5, escalaY(aDec[i]) - 1.5, 3, 3);
  });

  // leyenda dentro del tramo
  ctx.fillStyle = BLANCO;
  ctx.font = "13px monospace";
  ctx.fillText(
    `${describo(seg)}: ${seg.muestras_60hz} muestras a 60 Hz → bastan ${seg.muestras_f_opt} a ${seg.f_opt} Hz`,
    Math.max(x0 + 8, 8),
    20
  );

  document.getElementById("hint").textContent =
    `${describo(seg)} entre ${Math.round(seg.desde_s)} y ${Math.round(seg.hasta_s)} s — ` +
    (seg.k
      ? `con ${seg.f_opt} lectura${seg.f_opt === 1 ? "" : "s"} por segundo alcanza: ` +
        `${seg.muestras_f_opt} de ${seg.muestras_60hz} muestras (1 de cada ${paso}).`
      : `ni hace falta medir: era todo ruido.`);
}

function pintoTabla() {
  const tabla = document.getElementById("tabla");
  const filas = contrato.segmentos
    .filter((s) => s.k)
    .map(
      (s) =>
        `<tr><td>${describo(s)}</td><td>${Math.round(s.desde_s)}–${Math.round(s.hasta_s)} s</td>` +
        `<td>${s.a_max}</td><td>${s.v_max}</td>` +
        `<td>${s.f_dyn} Hz</td><td><strong>${s.f_opt} Hz</strong></td>` +
        `<td>${s.muestras_f_opt}/${s.muestras_60hz}</td><td>${s.k}</td></tr>`
    );
  tabla.innerHTML =
    "<tr><th>qué pasaba</th><th>ventana</th><th>a máx (m/s²)</th><th>v máx (m/s)</th>" +
    "<th>movimiento (f_dyn)</th><th>alcanzan (f_opt)</th><th>guardan</th><th>k</th></tr>" +
    filas.join("");
}
