# ABOUTME: Checks the reference-test helper that imports student solutions.
# ABOUTME: A missing solution is skipped; a solution with a broken import must fail.
import importlib
from pathlib import Path

import pytest

from tests_reference.conftest import import_solution_module


def make_package(root: Path, name: str, files: dict[str, str]) -> None:
    package = root / name
    package.mkdir()
    (package / "__init__.py").write_text("")
    for filename, source in files.items():
        (package / filename).write_text(source)
    importlib.invalidate_caches()


def test_missing_solution_is_skipped(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    make_package(tmp_path, "pkg_without_solution", {})
    monkeypatch.syspath_prepend(tmp_path)

    # pytest.skip/pytest.fail raise BaseException subclasses: catch any outcome
    # so a wrong one makes this test fail instead of being reported as skipped.
    with pytest.raises(BaseException) as outcome:
        import_solution_module("pkg_without_solution.solution")

    assert outcome.type is pytest.skip.Exception
    assert "ещё не создан" in str(outcome.value)


def test_solution_with_broken_import_fails(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    make_package(
        tmp_path,
        "pkg_with_broken_import",
        {"solution.py": "from no_such_module_anywhere import Something\n"},
    )
    monkeypatch.syspath_prepend(tmp_path)

    with pytest.raises(BaseException) as outcome:
        import_solution_module("pkg_with_broken_import.solution")

    assert outcome.type is pytest.fail.Exception, str(outcome.value)
    assert "no_such_module_anywhere" in str(outcome.value)
