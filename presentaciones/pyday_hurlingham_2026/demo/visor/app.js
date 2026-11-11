/* muestreo — visor del contrato JSON que produce el lab (Lado A).
   Vanilla JS a propósito: el contrato es el JSON, no un framework. */
"use strict";

const ROJO = "#C83534";
const GRIS = "#8a8a86";
const BLANCO = "#FBFAFA";

let contrato = null;
let tramoActivo = null;

const canvas = document.getElementById("grafico");
const ctx = canvas.getContext("2d");

fetch("data/recomendacion.json")
  .then((r) => r.json())
  .then((data) => {
    contrato = data;
    pintoMeta();
    pintoChips();
    pintoGrafico();
    pintoTabla();
  });

function pintoMeta() {
  const m = contrato.meta;
  document.getElementById("meta").textContent =
    `${m.fuente} · captura a ${m.f_captura} Hz · ${m.duracion_s} s · ` +
    `${m.n_muestras} muestras · piso de ruido σ = ${m.sigma} m/s²`;

  const total60 = contrato.segmentos.reduce((s, x) => s + x.muestras_60hz, 0);
  const totalOpt = contrato.segmentos.reduce((s, x) => s + x.muestras_f_opt, 0);
  document.getElementById("ahorro").textContent =
    `Con la tasa recomendada por tramo alcanzan ${totalOpt} de ${total60} muestras ` +
    `(${Math.round((100 * totalOpt) / total60)}%): el resto era ruido.`;
}

function pintoChips() {
  const nav = document.getElementById("chips");
  contrato.segmentos.forEach((s, i) => {
    const chip = document.createElement("div");
    chip.className = "chip";
    chip.innerHTML =
      `<strong>${s.nombre}</strong> ${s.desde_s}–${s.hasta_s}s · ` +
      `f_opt ${s.f_opt} Hz · ${s.redundancia_pct}% ruido`;
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

function escalaY(valor) {
  const max = contrato.meta.sigma * 40; // margen para ver la dinámica y el ruido
  const h = canvas.height;
  return h / 2 - (valor / max) * (h / 2 - 10);
}

function pintoGrafico() {
  const { t, a } = contrato.senial;
  const seg = contrato.segmentos[tramoActivo];
  const paso = Math.max(1, Math.round(contrato.meta.f_medida / seg.f_opt));

  ctx.clearRect(0, 0, canvas.width, canvas.height);
  const w = canvas.width;

  // zona del tramo activo
  const x0 = (seg.desde_s / contrato.meta.duracion_s) * w;
  const x1 = (seg.hasta_s / contrato.meta.duracion_s) * w;
  ctx.fillStyle = "rgba(200, 53, 52, .12)";
  ctx.fillRect(x0, 0, x1 - x0, canvas.height);

  // señal completa (60 Hz): gris
  ctx.strokeStyle = GRIS;
  ctx.lineWidth = 1;
  ctx.beginPath();
  t.forEach((ti, i) => {
    const x = (ti / contrato.meta.duracion_s) * w;
    const y = escalaY(a[i]);
    i === 0 ? ctx.moveTo(x, y) : ctx.lineTo(x, y);
  });
  ctx.stroke();

  // señal decimada al ritmo recomendado: blanca (línea) + roja (muestras)
  const tDec = t.filter((_, i) => i % paso === 0);
  const aDec = a.filter((_, i) => i % paso === 0);
  ctx.strokeStyle = BLANCO;
  ctx.lineWidth = 1.5;
  ctx.beginPath();
  tDec.forEach((ti, i) => {
    const x = (ti / contrato.meta.duracion_s) * w;
    const y = escalaY(aDec[i]);
    i === 0 ? ctx.moveTo(x, y) : ctx.lineTo(x, y);
  });
  ctx.stroke();
  ctx.fillStyle = ROJO;
  tDec.forEach((ti, i) => {
    const x = (ti / contrato.meta.duracion_s) * w;
    ctx.fillRect(x - 1, escalaY(aDec[i]) - 1, 3, 3);
  });

  // leyenda dentro del tramo
  ctx.fillStyle = BLANCO;
  ctx.font = "13px monospace";
  ctx.fillText(
    `${seg.nombre}: ${seg.muestras_60hz} muestras a 60 Hz → ${seg.muestras_f_opt} a ${seg.f_opt} Hz`,
    Math.max(x0 + 8, 8), 20
  );

  document.getElementById("hint").textContent =
    `Puntos rojos: las ${tDec.length} muestras que sobreviven a ${seg.f_opt} Hz ` +
    `(1 de cada ${paso}). La línea gris tenía ${seg.muestras_60hz}.` +
    (seg.k ? ` La regla: f_dyn = ${seg.f_dyn} Hz → k = ${seg.k}.` : " Tramo sin dinámica: ni hace falta medir.");
}

function pintoTabla() {
  const tabla = document.getElementById("tabla");
  const filas = contrato.segmentos
    .filter((s) => s.k)
    .map(
      (s) =>
        `<tr><td>${s.nombre}</td><td>${s.desde_s}–${s.hasta_s}s</td>` +
        `<td>a_max ${s.a_max}</td><td>v_max ${s.v_max}</td>` +
        `<td>f_dyn ${s.f_dyn} Hz</td><td><strong>f_opt ${s.f_opt} Hz</strong></td>` +
        `<td>k ${s.k}</td></tr>`
    );
  tabla.innerHTML =
    "<tr><th>tramo</th><th>ventana</th><th>a_max</th><th>v_max</th>" +
    "<th>f_dyn</th><th>recomendado</th><th>k</th></tr>" + filas.join("");
}
