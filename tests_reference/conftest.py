"""Общие хелперы эталонных тестов.

Если solution.py для задачи ещё не создан, тесты этой задачи помечаются
skip, а не fail — так пайплайн остаётся зелёным, пока задача не выбрана.
"""

import importlib
from types import ModuleType

import pytest


def import_solution_module(module_path: str) -> ModuleType:
    file_path = f"{module_path.replace('.', '/')}.py"
    try:
        return importlib.import_module(module_path)
    except ModuleNotFoundError as error:
        missing_module = error.name
    # Skip only when the solution file itself is absent. If the file exists but
    # one of its own imports is broken, the tests must fail, not silently skip.
    if missing_module == module_path:
        pytest.skip(f"{file_path} ещё не создан", allow_module_level=True)
    pytest.fail(
        f"{file_path} не импортируется: не найден модуль '{missing_module}'. "
        "Проверьте импорты в начале файла: модули задания импортируются от корня "
        "репозитория (например, `from tasks.sorts.merge_sort.solution import merge_sort`). "
        f'Увидеть ошибку локально: uv run python -c "import {module_path}"',
        pytrace=False,
    )


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
