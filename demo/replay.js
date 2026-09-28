"use strict";
const spanish = new URLSearchParams(location.search).get("lang") === "es";
const text = spanish ? {
  play: "Reproducir", pause: "Pausar", reset: "Reiniciar",
  eyebrow: "JORGE CÁMARA · ARCHIVO DE APRENDIZAJE · 2023",
  title: "De las reglas al movimiento.",
  intro: "Dos primeros programas en Python. Este visor reproduce su salida real de consola; la presentación se añadió en 2026. Los algoritmos originales se conservan.",
  programLabel: "Programa", positionLabel: "Estado registrado", contextTitle: "Qué demuestra el código", notes: "Leer las notas del proyecto",
  note: "Reproducción acelerada. Mueve el control para inspeccionar cada estado. Sin cuentas, analítica, servicios de red ni datos privados.",
  maze: "Un agente sigue la pared derecha guardando su posición y orientación en una matriz de caracteres. Los dos mapas incluidos llegan a una salida: 712 y 1.015 movimientos. La prueba acredita estos dos mapas, no cualquier laberinto posible.",
  automaton: "Dos poblaciones, reglas de movimiento y eventos temporales evolucionan durante 28 ciclos. Una semilla aleatoria fija permite repetir esta muestra. La matriz se modifica en orden, así que el orden de actualización influye en el resultado. Es una simulación académica original, no el Juego de la Vida de Conway."
} : {
  play: "Play", pause: "Pause", reset: "Restart",
  maze: "A right-hand wall-following agent stores its position and orientation in a character grid. Both supplied maps reach an exit: 712 and 1,015 moves. This verifies these two inputs, not every possible maze.",
  automaton: "Two populations, movement rules and timed events evolve for 28 cycles. A fixed random seed makes this replay reproducible. The grid is updated in place, so update order affects the result. This is an original classroom simulation, not Conway’s Game of Life."
};
document.documentElement.lang = spanish ? "es" : "en";
if (spanish) {
  document.title = "Fundamentos Python · Jorge Cámara";
  for (const id of ["eyebrow", "title", "intro", "programLabel", "positionLabel", "contextTitle", "notes", "note"])
    document.getElementById(id).textContent = text[id];
  ["Laberinto · mapa 1", "Laberinto · mapa 2", "Autómata ASCII"].forEach((label, index) => document.getElementById("program").options[index].textContent = label);
  document.querySelector("nav").setAttribute("aria-label", "Idioma");
  document.querySelector("section").setAttribute("aria-label", "Salida registrada del programa");
  document.querySelector(".screen").setAttribute("aria-label", "Salida de consola desplazable");
  document.getElementById("frame").setAttribute("aria-label", "Estado del programa");
}
const programs = window.REPLAY_DATA.map(program => {
  const frames = [program.first];
  let current = Array.from(program.first);
  for (const delta of program.deltas) {
    for (const [index, character] of delta) current[index] = character;
    frames.push(current.join(""));
  }
  return { ...program, frames };
});
const controls = Object.fromEntries(["program", "play", "reset", "position", "counter", "frame", "details", "explanation"].map(id => [id, document.getElementById(id)]));
let chosen = 0;
let index = 0;
let timer;
controls.reset.textContent = text.reset;
function stop() { clearInterval(timer); timer = undefined; controls.play.textContent = text.play; }
function render() {
  const program = programs[chosen];
  controls.frame.textContent = program.frames[index];
  controls.counter.textContent = `${index + 1} / ${program.frames.length}`;
  controls.position.value = index;
}
function select() {
  stop(); chosen = Number(controls.program.value); index = 0;
  controls.position.max = programs[chosen].frames.length - 1;
  controls.details.textContent = spanish ? (chosen < 2 ? `${programs[chosen].steps} movimientos · seguidor original de pared derecha` : "28 ciclos · semilla 2023 para repetir la muestra") : programs[chosen].label;
  controls.explanation.textContent = chosen < 2 ? text.maze : text.automaton;
  render();
}
controls.program.addEventListener("change", select);
controls.reset.addEventListener("click", () => { stop(); index = 0; render(); });
controls.position.addEventListener("input", () => { stop(); index = Number(controls.position.value); render(); });
controls.play.addEventListener("click", () => {
  if (timer) return stop();
  if (index === programs[chosen].frames.length - 1) index = 0;
  controls.play.textContent = text.pause;
  timer = setInterval(() => {
    index = Math.min(index + (chosen < 2 ? 4 : 1), programs[chosen].frames.length - 1);
    render();
    if (index === programs[chosen].frames.length - 1) stop();
  }, chosen < 2 ? 50 : 250);
});
select();
