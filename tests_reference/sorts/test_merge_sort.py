import random

import pytest

from tests_reference.conftest import import_solution_module

_module = import_solution_module("tasks.sorts.merge_sort.solution")

_merge_sort = getattr(_module, "merge_sort", None)
_merge_sort_inplace = getattr(_module, "merge_sort_inplace", None)

if _merge_sort is None and _merge_sort_inplace is None:
    pytest.skip(
        "tasks/sorts/merge_sort/solution.py не содержит ни merge_sort, ни merge_sort_inplace",
        allow_module_level=True,
    )


def sorted_by_student(arr: list[int]) -> list[int]:
    """Единая точка вызова для обоих разрешённых интерфейсов задачи."""
    if _merge_sort is not None:
        return _merge_sort(list(arr))
    copy = list(arr)
    _merge_sort_inplace(copy)
    return copy


@pytest.mark.parametrize(
    ("arr", "expected"),
    [
        ([], []),
        ([3], [3]),
        ([4, 5, 3, 0, 1, 2], [0, 1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([2, -1, 2, -1, 0], [-1, -1, 0, 2, 2]),
        ([0, 0, 0], [0, 0, 0]),
        ([1_000_000_000, -1_000_000_000], [-1_000_000_000, 1_000_000_000]),
    ],
)
def test_cases(arr: list[int], expected: list[int]) -> None:
    assert sorted_by_student(arr) == expected


@pytest.mark.timeout(2)
def test_random_large_input_within_timeout() -> None:
    random.seed(3)
    arr = [random.randint(-10_000, 10_000) for _ in range(20_000)]
    assert sorted_by_student(arr) == sorted(arr)


@pytest.mark.timeout(2)
def test_reverse_sorted_large_input_within_timeout() -> None:
    arr = list(range(20_000, 0, -1))
    assert sorted_by_student(arr) == sorted(arr)
