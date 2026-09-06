import random

import pytest

from tests_reference.conftest import import_solution

quick_sort = import_solution("tasks.sorts.quick_sort.solution", "quick_sort")


@pytest.mark.parametrize(
    ("arr", "expected"),
    [
        ([], []),
        ([3], [3]),
        ([3, 7, 9, 4, 3, 1, 8, 5], [1, 3, 3, 4, 5, 7, 8, 9]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([2, -1, 2, -1, 0], [-1, -1, 0, 2, 2]),
        ([0, 0, 0, 0], [0, 0, 0, 0]),
        ([1_000_000_000, -1_000_000_000, 0], [-1_000_000_000, 0, 1_000_000_000]),
    ],
)
def test_cases(arr: list[int], expected: list[int]) -> None:
    assert quick_sort(arr) == expected


def test_does_not_mutate_input() -> None:
    arr = [3, 1, 2]
    original = list(arr)
    quick_sort(arr)
    assert arr == original


@pytest.mark.timeout(2)
def test_random_large_input_within_timeout() -> None:
    random.seed(2)
    arr = [random.randint(-10_000, 10_000) for _ in range(5000)]
    assert quick_sort(arr) == sorted(arr)


@pytest.mark.timeout(3)
def test_already_sorted_large_input_no_worst_case_blowup() -> None:
    # Наивный выбор опорного элемента (первый/последний) на уже отсортированном
    # массиве даёт линейную глубину рекурсии — RecursionError или таймаут здесь
    # означает не "случайную неудачу", а конкретную ошибку выбора pivot.
    arr = list(range(5000))
    assert quick_sort(arr) == arr


@pytest.mark.timeout(2)
def test_reverse_sorted_large_input() -> None:
    arr = list(range(5000, 0, -1))
    assert quick_sort(arr) == sorted(arr)
