"""Execute the archived programs and publish a replay of their actual output."""
import contextlib
import hashlib
import io
import json
import os
from pathlib import Path
import random
import sys

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "source"


def run_archived(filename, map_name=None):
    code = (SOURCE / filename).read_text(encoding="utf-8-sig")
    if map_name:
        code = code.replace('open("laberinto1.txt",', f'open("{map_name}",')
    namespace = {"__name__": "__main__"}
    captured = io.StringIO()
    previous = Path.cwd()
    random.seed(2023)
    try:
        os.chdir(SOURCE)
        with contextlib.redirect_stdout(captured):
            exec(compile(code, filename, "exec"), namespace)
    finally:
        os.chdir(previous)
    return captured.getvalue(), namespace


def collect_maze(map_name, expected):
    output, state = run_archived("maze.py", map_name)
    lines = output.splitlines()
    height = len(state["tablero"])
    frames = []
    i = 0
    while i < len(lines):
        if lines[i].isdigit():
            frames.append("\n".join(lines[i + 1:i + 1 + height]))
            i += height + 1
        i += 1
    final_frame = "".join("".join(row) for row in state["tablero"]).rstrip("\n")
    frames.append(final_frame)
    steps = state["pasos"] - 1
    assert steps == expected, (map_name, steps, expected)
    assert state["pos_i"] == height - 1, "Agent did not reach the last row"
    return {"id": map_name, "name": map_name, "frames": frames, "steps": steps,
            "rows": height, "columns": len(state["tablero"][0]) - 1,
            "finalPosition": [state["pos_i"], state["pos_j"]],
            "label": f"{steps} moves · original right-hand wall follower"}


def main():
    maze1 = collect_maze("laberinto1.txt", 712)
    maze2 = collect_maze("laberinto2.txt", 1015)
    output, state = run_archived("automaton.py")
    lines = [line for line in output.splitlines() if line]
    height = state["ALTO"]
    frames = ["\n".join(lines[i:i + height]) for i in range(0, len(lines), height)]
    assert state["repeticiones"] == 28
    assert all(len(frame.splitlines()) == 13 for frame in frames)
    automaton = {"id": "automaton", "name": "ASCII automaton", "frames": frames,
                 "steps": 28, "rows": 13, "columns": 30,
                 "label": "28 cycles · fixed seed 2023 for reproducible playback"}
    demos = [maze1, maze2, automaton]
    packed = []
    for demo in demos:
        frames = demo["frames"]
        deltas = []
        for previous, current in zip(frames, frames[1:]):
            assert len(previous) == len(current)
            changes = [[i, value] for i, value in enumerate(current) if previous[i] != value]
            rebuilt = list(previous)
            for i, value in changes:
                rebuilt[i] = value
            assert "".join(rebuilt) == current
            deltas.append(changes)
        packed.append({**{k: v for k, v in demo.items() if k != "frames"},
                       "first": frames[0], "deltas": deltas})
    (ROOT / "demo" / "replay-data.js").write_text(
        "window.REPLAY_DATA = " + json.dumps(packed, ensure_ascii=True, separators=(",", ":")) + ";\n", encoding="utf-8")
    evidence = {"verifiedOn": "2026-09-28", "python": sys.version.split()[0],
                "programs": [{k: v for k, v in d.items() if k != "frames"} for d in demos],
                "sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                           for p in sorted(SOURCE.iterdir()) if p.is_file()},
                "method": "Execute original programs; capture stdout; replay output. Only the second maze input is substituted in memory. Automaton seed set externally.",
                "limits": "Only the two supplied mazes are verified. The automaton uses sequential in-place updates, not Conway's Game of Life."}
    (ROOT / "evidence" / "verification.json").write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"maze1Moves": maze1["steps"], "maze2Moves": maze2["steps"], "automatonCycles": 28}))


if __name__ == "__main__":
    main()
