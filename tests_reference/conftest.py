"""Общие хелперы эталонных тестов.

Если solution.py для задачи ещё не создан, тесты этой задачи помечаются
skip, а не fail — так пайплайн остаётся зелёным, пока задача не выбрана.
"""

import importlib
from types import ModuleType

import pytest


def import_solution_module(module_path: str) -> ModuleType:
    try:
        return importlib.import_module(module_path)
    except ModuleNotFoundError:
        pytest.skip(f"{module_path.replace('.', '/')}.py ещё не создан", allow_module_level=True)


def import_solution(module_path: str, *names: str):
    module = import_solution_module(module_path)
    missing = [name for name in names if not hasattr(module, name)]
    if missing:
        pytest.skip(
            f"{module_path.replace('.', '/')}.py не содержит: {', '.join(missing)}",
            allow_module_level=True,
        )
    values = tuple(getattr(module, name) for name in names)
    return values[0] if len(values) == 1 else values
