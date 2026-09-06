import random

import pytest

from tests_reference.conftest import import_solution

insertion_sort = import_solution("tasks.sorts.insertion_sort.solution", "insertion_sort")


@pytest.mark.parametrize(
    ("arr", "expected"),
    [
        ([], []),
        ([3], [3]),
        ([9, 5, 1, 4, 3], [1, 3, 4, 5, 9]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([2, -1, 2, -1, 0], [-1, -1, 0, 2, 2]),
        ([0, 0, 0], [0, 0, 0]),
        ([-5, -1, -10, -3], [-10, -5, -3, -1]),
    ],
)
def test_cases(arr: list[int], expected: list[int]) -> None:
    assert insertion_sort(arr) == expected


def test_does_not_mutate_input() -> None:
    arr = [3, 1, 2]
    original = list(arr)
    insertion_sort(arr)
    assert arr == original


@pytest.mark.timeout(2)
def test_random_large_input_within_timeout() -> None:
    random.seed(1)
    arr = [random.randint(-1000, 1000) for _ in range(1000)]
    assert insertion_sort(arr) == sorted(arr)
