import random

import pytest

from tests_reference.conftest import import_solution

binary_search = import_solution("tasks.recursion.binary_search.solution", "binary_search")


def test_empty_array() -> None:
    assert binary_search([], 10) == -1


def test_single_element_found() -> None:
    assert binary_search([5], 5) == 0


def test_single_element_not_found() -> None:
    assert binary_search([5], 1) == -1


def test_found_first_element() -> None:
    arr = [1, 3, 5, 7, 9]
    assert binary_search(arr, 1) == 0


def test_found_last_element() -> None:
    arr = [1, 3, 5, 7, 9]
    assert binary_search(arr, 9) == 4


def test_found_middle_element() -> None:
    arr = [1, 3, 5, 7, 9]
    assert binary_search(arr, 5) == 2


def test_not_found_between_elements() -> None:
    arr = [1, 3, 5]
    assert binary_search(arr, 2) == -1


def test_not_found_below_range() -> None:
    arr = [1, 3, 5]
    assert binary_search(arr, -100) == -1


def test_not_found_above_range() -> None:
    arr = [1, 3, 5]
    assert binary_search(arr, 100) == -1


def test_duplicates_return_any_matching_index() -> None:
    arr = [1, 2, 2, 4, 7]
    result = binary_search(arr, 2)
    assert result != -1
    assert arr[result] == 2


def test_negative_numbers() -> None:
    arr = [-9, -5, -1, 0, 3]
    assert binary_search(arr, -5) == 1


@pytest.mark.timeout(2)
def test_many_queries_on_large_array_within_timeout() -> None:
    n = 200_000
    arr = list(range(0, 2 * n, 2))  # 0, 2, 4, ..., чётные числа

    random.seed(4)
    targets = [random.randrange(0, 2 * n) for _ in range(2000)]
    for target in targets:
        result = binary_search(arr, target)
        if target % 2 == 0 and target < 2 * n:
            assert result == target // 2
        else:
            assert result == -1
