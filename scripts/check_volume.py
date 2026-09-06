#!/usr/bin/env python3
"""Проверяет минимальный объём задания 1: 3 data_structures + 2 sorts + 1 recursion."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = {
    "data_structures": 3,
    "sorts": 2,
    "recursion": 1,
}


def solved_tasks(section: str) -> list[str]:
    section_dir = ROOT / "tasks" / section
    if not section_dir.is_dir():
        return []
    return sorted(p.parent.name for p in section_dir.glob("*/solution.py"))


def main() -> int:
    ok = True
    for section, minimum in REQUIRED.items():
        done = solved_tasks(section)
        status = "OK" if len(done) >= minimum else "НЕ ДОСТАТОЧНО"
        print(f"{section}: {len(done)}/{minimum} — {status} {done}")
        if len(done) < minimum:
            ok = False

    if not ok:
        print(
            "\nМинимальный объём задания не набран. "
            "Нужно решить ещё задачи и добавить tasks/<раздел>/<задача>/solution.py",
            file=sys.stderr,
        )
        return 1

    print("\nМинимальный объём набран.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
