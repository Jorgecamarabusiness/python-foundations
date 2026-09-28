# Python foundations · Jorge Cámara

Two individual school projects from April–May 2023, recovered from the author's archive. The original Python files are preserved byte-for-byte with shorter filenames. The documentation, verification runner and browser replay were added in September 2026 with AI assistance.

## Projects

- **Autonomous maze:** a right-hand wall follower with position and direction state. The two supplied maps reach the final row in **712** and **1,015** moves.
- **ASCII automaton:** two populations, probabilistic movement and timed events over **28 cycles**. Updates happen in place; it is not an implementation of Conway's Game of Life.

## Run the original programs

Python 3, standard library only. Run from the `source` directory:

```text
python maze.py
python automaton.py
```

The original maze script selects `laberinto1.txt`. The verification runner selects the second map in memory without editing the archived file.

## Verify and replay

```text
python build_demo.py
python -m http.server 8091 --bind 127.0.0.1
```

Open `http://127.0.0.1:8091/demo/` to inspect the recorded output. The viewer does not execute Python in the browser. It replays states emitted by the actual archived programs, with accelerated playback and a scrubber. Random seed `2023` is set externally for a reproducible automaton example.

`evidence/verification.json` records file hashes, runtime and verified outputs. The solver is only verified against the two supplied maps. It is an early learning artifact, not a general-purpose pathfinding library.

## Publication boundary

This package contains only the two programs, their text maps, documentation and the new output viewer. It contains no school records, grades, addresses, classmate names, client projects, credentials or private application data. No permissive software licence is granted here; rights remain with the author unless a licence is added explicitly.

## Español

Dos proyectos individuales de Bachillerato de abril–mayo de 2023: un agente que recorre dos laberintos siguiendo la pared derecha y un autómata ASCII con dos poblaciones y eventos temporales. Los archivos originales se conservan sin cambiar su contenido. La presentación y las comprobaciones son de septiembre de 2026, añadidas con asistencia de IA; no se presentan como una interfaz creada en 2023.
