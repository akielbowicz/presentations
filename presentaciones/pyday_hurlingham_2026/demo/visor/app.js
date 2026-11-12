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
let fPrueba = null; // el slider: ¿y si mido a esta tasa?

const canvas = document.getElementById("grafico");
const ctx = canvas.getContext("2d");
const slider = document.getElementById("tasa");

slider.addEventListener("input", () => {
  if (!contrato || tramoActivo === null) return;
  fPrueba = Number(slider.value);
  pintoGrafico();
});

fetch("data/recomendacion.json")
  .then((r) => {
    if (!r.ok) throw new Error(`HTTP ${r.status}`);
    return r.json();
  })
  .then((data) => {
    contrato = data;
    preparoEscala();
    preparoPrueba();
    pintoMeta();
    pintoChips();
    // deep-link ?tramo=N&tasa=H: abrir el visor ya contando esa parte
    const q = new URLSearchParams(location.search);
    const tramoQ = Math.trunc(Number(q.get("tramo")));
    activo(tramoQ >= 0 && tramoQ < contrato.segmentos.length ? tramoQ : 0);
    const tasaQ = Number(q.get("tasa"));
    if (tasaQ >= Number(slider.min) && tasaQ <= Number(slider.max)) {
      fPrueba = tasaQ;
      slider.value = tasaQ;
      pintoGrafico();
    }
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

/* El problema, hecho veredicto (idea de wanna: contrato con veredictos
   explícitos, falsable en ambas direcciones). El contrato manda: f_opt es
   el ritmo justo medido por el lab; Nyquist (2·f_dyn) es solo el piso.
   Un solo árbol de decisión produce palabra (estado), color (roja) y
   explicación (razon → porQue). */
function veredicto(seg, f) {
  if (seg.f_dyn == null || seg.f_opt == null)
    return { estado: "alcanza", razon: "sin-dinamica", roja: false };
  if (f >= seg.f_opt)
    return { estado: "alcanza", razon: "ritmo-justo", roja: false };
  if (f >= 2 * seg.f_dyn)
    return { estado: "existe pero miente", razon: "sobre-nyquist", roja: true };
  return { estado: "miente", razon: "bajo-nyquist", roja: true };
}

/* El por qué del veredicto, en palabras con los números del contrato. */
function porQue(seg, f, vered) {
  switch (vered.razon) {
    case "sin-dinamica":
      return "Este tramo no tiene dinámica medible: cualquier ritmo alcanza (el lab no midió f_dyn).";
    case "ritmo-justo":
      return `${f} Hz ≥ ${seg.f_opt} Hz (el ritmo justo que midió el lab): la forma no miente.`;
    case "sobre-nyquist": {
      const piso = (2 * seg.f_dyn).toFixed(1);
      return `${f} Hz superan Nyquist (2 · ${seg.f_dyn.toFixed(1)} = ${piso} Hz): la señal existe, pero su forma miente.`;
    }
    default: {
      const piso = (2 * seg.f_dyn).toFixed(1);
      return `${f} Hz ni alcanzan Nyquist (${piso} Hz): la medición miente.`;
    }
  }
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
  fPrueba = contrato.segmentos[i].f_opt; // cada tramo abre en su ritmo justo
  slider.value = fPrueba;
  slider.disabled = false;
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

/* El rango del slider cubre el f_opt más exigente del contrato: si una
   captura futura pide más que los 60 Hz de la grabación, hay dónde posar
   el slider sobre el ritmo justo en vez de quedar clampado. */
function preparoPrueba() {
  const maxOpt = Math.max(...contrato.segmentos.map((s) => s.f_opt || 0));
  slider.max = Math.max(Number(slider.max), Math.ceil(maxOpt));
}

function escalaY(valor) {
  const h = canvas.height;
  const rel = Math.max(-1.05, Math.min(1.05, (valor - centro) / techo));
  return h / 2 - rel * (h / 2 - 12);
}

function pintoGrafico() {
  const { t, a } = contrato.senial;
  const seg = contrato.segmentos[tramoActivo];
  if (!fPrueba) fPrueba = seg.f_opt;
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

  // tu prueba: reconstrucción al ritmo del slider — blanco si alcanza,
  // rojo si miente (el problema visible, no narrado)
  const vered = veredicto(seg, fPrueba);
  const pasoP = Math.max(1, Math.round(contrato.meta.f_medida / fPrueba));
  ctx.strokeStyle = vered.roja ? ROJO : BLANCO;
  ctx.lineWidth = 2.5;
  ctx.beginPath();
  let empezo = false;
  t.forEach((ti, i) => {
    if (i % pasoP !== 0) return;
    if (ti < seg.desde_s - 1 / fPrueba || ti > seg.hasta_s) return;
    const x = (ti / dur) * w;
    const y = escalaY(a[i]);
    empezo ? ctx.lineTo(x, y) : ctx.moveTo(x, y);
    empezo = true;
  });
  ctx.stroke();

  // lo que el contrato guarda (ritmo justo): puntos rojos
  const tDec = t.filter((_, i) => i % paso === 0);
  const aDec = a.filter((_, i) => i % paso === 0);
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
        `${seg.muestras_f_opt} de ${seg.muestras_60hz} muestras.`
      : `ni hace falta medir: era todo ruido.`);

  // el veredicto: el contrato traducido a palabras, con el por qué
  const badge = document.getElementById("veredicto");
  badge.hidden = false;
  badge.textContent = vered.estado;
  badge.className = vered.roja ? "miente" : "alcanza";
  document.getElementById("tasa-num").textContent = fPrueba;
  document.getElementById("por-que").textContent =
    "Prueba: " + porQue(seg, fPrueba, vered);
  document.getElementById("prueba-linea").style.color = vered.roja
    ? ROJO
    : BLANCO;
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

/* ─── Tercer acto: el grabador adaptativo sobre el stream real ───
   Mismo principio de la casa: consume un contrato JSON (grabacion.json,
   Lado A) y lo traduce a movimiento. Si el archivo no está, la sección
   se esconde: el visor nunca depende de que el lab haya corrido. */

const gcanvas = document.getElementById("g-canvas");
const gctx = gcanvas.getContext("2d");
const gBtn = document.getElementById("g-play");
let grab = null;
let gPlay = null; // id de requestAnimationFrame si está reproduciendo
let gPh = 0; // playhead en segundos
let gEscalaCache = null;

// bandas del canvas: señal arriba, tasa abajo
const G_BANDA = { senialY: 10, senialH: 195, tasaY: 250, tasaH: 55 };
const G_PLAY_S = 14; // los 46 s reales se reproducen en 14 s de proyección

fetch("data/grabacion.json")
  .then((r) => {
    if (!r.ok) throw new Error(`HTTP ${r.status}`);
    return r.json();
  })
  .then((data) => {
    grab = data;
    document.getElementById("g-cuenta").textContent =
      `${grab.resumen.guardadas} de ${grab.resumen.totales} muestras persistidas ` +
      `(${grab.resumen.pct}%), error de reconstrucción ${grab.resumen.error_reconstruccion_pct}% RMS. ` +
      `El offline ideal llega a 37% porque ve el futuro; decidir solo con pasado cuesta 21 puntos ` +
      `y sigue siendo menos de la mitad que los 60 Hz crudos.`;
    pintoGrabador(gPlay ? gPh : grab.meta.duracion_s + 0.5, false);
    // ?reproducir: abrir directamente con la película en movimiento
    if (new URLSearchParams(location.search).has("reproducir")) gToggle();
  })
  .catch(() => {
    document.getElementById("grabador").hidden = true;
  });

function gTasaEn(t) {
  // arranca conservador: plena tasa hasta la primera decisión
  let f = grab.meta.f_medida;
  for (const [td, ft] of grab.decisiones) {
    if (td <= t) f = ft;
    else break;
  }
  return f;
}

function gEscala() {
  if (gEscalaCache) return gEscalaCache;
  const a = grab.senial.a;
  const c = a.reduce((s, x) => s + x, 0) / a.length;
  const d = a.map((x) => Math.abs(x - c)).sort((x, y) => x - y);
  gEscalaCache = { c, t: Math.max(d[Math.floor(d.length * 0.985)] || 1, 0.5) };
  return gEscalaCache;
}

function gY(valor) {
  const { c, t: techo } = gEscala();
  const rel = Math.max(-1.05, Math.min(1.05, (valor - c) / techo));
  return G_BANDA.senialY + G_BANDA.senialH / 2 - rel * (G_BANDA.senialH / 2 - 8);
}

function gYtasa(f) {
  return G_BANDA.tasaY + G_BANDA.tasaH * (1 - f / 60);
}

function pintoGrabador(ph, conVentana) {
  if (!grab) return;
  const w = gcanvas.width;
  const dur = grab.meta.duracion_s;

  gctx.clearRect(0, 0, w, gcanvas.height);

  // banda de la tasa: fondo distinto para separar los dos mundos
  gctx.fillStyle = "#161613";
  gctx.fillRect(0, G_BANDA.tasaY - 14, w, G_BANDA.tasaH + 28);

  // grilla de tiempo compartida
  gctx.strokeStyle = "#2c2c2a";
  gctx.fillStyle = GRIS;
  gctx.font = "12px monospace";
  gctx.lineWidth = 1;
  [0, 0.25, 0.5, 0.75, 1].forEach((fr) => {
    const x = Math.round(fr * w) + 0.5;
    gctx.beginPath();
    gctx.moveTo(x, 0);
    gctx.lineTo(x, gcanvas.height);
    gctx.stroke();
    gctx.fillText(`${Math.round(fr * dur)} s`, Math.min(x + 4, w - 30), G_BANDA.tasaY + G_BANDA.tasaH + 12);
  });

  // la ventana RAM de 2 s deslizando (solo durante la reproducción)
  if (conVentana) {
    const vs = grab.meta.ventana_muestras / grab.meta.f_medida;
    const x0 = (Math.max(0, ph - vs) / dur) * w;
    const x1 = (ph / dur) * w;
    gctx.fillStyle = "rgba(200, 53, 52, .12)";
    gctx.fillRect(x0, 0, x1 - x0, G_BANDA.senialY + G_BANDA.senialH);
  }

  // la verdad gris hasta el playhead
  gctx.strokeStyle = GRIS;
  gctx.lineWidth = 1;
  gctx.beginPath();
  grab.senial.t.forEach((ti, i) => {
    if (ti > ph) return;
    const x = (ti / dur) * w;
    i === 0 ? gctx.moveTo(x, gY(grab.senial.a[i])) : gctx.lineTo(x, gY(grab.senial.a[i]));
  });
  gctx.stroke();

  // lo persistido: puntos rojos ≤ ph
  gctx.fillStyle = ROJO;
  grab.guardadas.t.forEach((ti, i) => {
    if (ti > ph) return;
    const x = (ti / dur) * w;
    gctx.fillRect(x - 1.5, gY(grab.guardadas.a[i]) - 1.5, 3, 3);
  });

  // la traza de tasa: escalón blanco en la banda inferior
  gctx.strokeStyle = BLANCO;
  gctx.lineWidth = 1.5;
  gctx.beginPath();
  let fPrev = grab.meta.f_medida;
  gctx.moveTo(0, gYtasa(fPrev));
  grab.decisiones.forEach(([td, ft]) => {
    if (td > ph) return;
    const x = (td / dur) * w;
    gctx.lineTo(x, gYtasa(fPrev));
    gctx.lineTo(x, gYtasa(ft));
    fPrev = ft;
  });
  gctx.lineTo((ph / dur) * w, gYtasa(fPrev));
  gctx.stroke();

  // marcas de decisión sobre la banda de tasa
  gctx.fillStyle = GRIS;
  gctx.font = "11px monospace";
  grab.decisiones.forEach(([td, ft]) => {
    if (td > ph) return;
    const x = (td / dur) * w;
    gctx.fillRect(x, G_BANDA.tasaY - 12, 1, 6);
    gctx.fillText(`${ft}`, x + 3, G_BANDA.tasaY - 4);
  });

  // playhead
  if (ph < dur) {
    gctx.strokeStyle = BLANCO;
    gctx.lineWidth = 1;
    const x = (ph / dur) * w;
    gctx.beginPath();
    gctx.moveTo(x, 0);
    gctx.lineTo(x, gcanvas.height);
    gctx.stroke();
  }

  gContadores(ph);
}

function gContadores(ph) {
  const f = gTasaEn(ph);
  const badge = document.getElementById("g-tasa");
  badge.textContent = `${f} Hz`;
  badge.classList.toggle("activa", f < 60);
  let n = 0;
  while (n < grab.guardadas.t.length && grab.guardadas.t[n] <= ph) n++;
  document.getElementById("g-muestras").textContent =
    `${n} de ${grab.resumen.totales} muestras persistidas`;
}

function gToggle() {
  if (gPlay) {
    cancelAnimationFrame(gPlay);
    gPlay = null;
    gBtn.textContent = "▶ seguir";
    return;
  }
  const dur = grab.meta.duracion_s;
  if (gPh >= dur) gPh = 0;
  let last = null;
  gBtn.textContent = "⏸ pausa";
  const paso = (ts) => {
    if (last === null) last = ts;
    gPh += ((ts - last) / 1000) * (dur / G_PLAY_S);
    last = ts;
    if (gPh >= dur) {
      gPh = dur;
      pintoGrabador(dur, false);
      gPlay = null;
      gBtn.textContent = "▶ reproducir de nuevo";
      return;
    }
    pintoGrabador(gPh, true);
    gPlay = requestAnimationFrame(paso);
  };
  gPlay = requestAnimationFrame(paso);
}

gBtn.addEventListener("click", () => grab && gToggle());
