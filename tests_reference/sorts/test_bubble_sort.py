import pytest

from tests_reference.conftest import import_solution

bubble_sort = import_solution("tasks.sorts.bubble_sort.solution", "bubble_sort")


def test_already_sorted_single_snapshot() -> None:
    assert bubble_sort([1, 2, 3]) == [[1, 2, 3]]


def test_reverse_sorted_three_elements() -> None:
    assert bubble_sort([3, 2, 1]) == [[2, 1, 3], [1, 2, 3]]


def test_negative_and_positive_mix() -> None:
    assert bubble_sort([7, -2, -1]) == [[-2, -1, 7]]


def test_task_example() -> None:
    assert bubble_sort([3, 7, 9, 4, 3, 1, 8, 5]) == [
        [3, 7, 4, 3, 1, 8, 5, 9],
        [3, 4, 3, 1, 7, 5, 8, 9],
        [3, 3, 1, 4, 5, 7, 8, 9],
        [3, 1, 3, 4, 5, 7, 8, 9],
        [1, 3, 3, 4, 5, 7, 8, 9],
    ]

    assert bubble_sort([1, 2, 3, 4, 5]) == [[1, 2, 3, 4, 5]]


def test_two_elements_unsorted() -> None:
    assert bubble_sort([2, 1]) == [[1, 2]]


def test_two_elements_sorted() -> None:
    assert bubble_sort([1, 2]) == [[1, 2]]


def test_all_equal_elements_single_snapshot() -> None:
    assert bubble_sort([5, 5, 5, 5]) == [[5, 5, 5, 5]]


def test_last_snapshot_is_always_fully_sorted() -> None:
    snapshots = bubble_sort([9, 1, 8, 2, 7, 3])
    assert snapshots[-1] == sorted([9, 1, 8, 2, 7, 3])


@pytest.mark.timeout(3)
def test_medium_input_within_timeout() -> None:
    arr = list(range(500, 0, -1))
    snapshots = bubble_sort(arr)
    assert snapshots[-1] == sorted(arr)
