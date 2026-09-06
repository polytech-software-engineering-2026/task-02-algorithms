import random

import pytest

from tests_reference.conftest import import_solution

StackMax = import_solution("tasks.data_structures.stack_max.solution", "StackMax")


def test_empty_stack() -> None:
    stack = StackMax()
    assert stack.get_max() == "None"
    assert stack.pop() == "error"


def test_single_push() -> None:
    stack = StackMax()
    stack.push(7)
    assert stack.get_max() == 7


def test_task_example_1() -> None:
    stack = StackMax()
    assert stack.get_max() == "None"
    stack.push(7)
    stack.pop()
    stack.push(-2)
    stack.push(-1)
    stack.pop()
    assert stack.get_max() == -2
    assert stack.get_max() == -2


def test_task_example_2() -> None:
    stack = StackMax()
    assert stack.get_max() == "None"
    assert stack.pop() == "error"
    assert stack.pop() == "error"
    assert stack.pop() == "error"
    stack.push(10)
    assert stack.get_max() == 10
    stack.push(-9)


def test_task_example_from_description() -> None:
    stack = StackMax()
    assert stack.get_max() == "None"
    assert stack.pop() == "error"

    stack.push(7)
    assert stack.get_max() == 7

    stack.push(1)
    stack.push(3)
    assert stack.get_max() == 7

    stack.pop()
    stack.pop()
    assert stack.get_max() == 7

    stack.pop()
    assert stack.get_max() == "None"


def test_max_updates_after_popping_current_max() -> None:
    stack = StackMax()
    stack.push(1)
    stack.push(5)
    stack.push(3)
    assert stack.get_max() == 5

    stack.pop()  # снимает 3
    assert stack.get_max() == 5

    stack.pop()  # снимает 5, максимум пересчитывается
    assert stack.get_max() == 1

    stack.pop()  # снимает 1
    assert stack.get_max() == "None"


def test_duplicate_max_values() -> None:
    stack = StackMax()
    stack.push(5)
    stack.push(5)
    stack.push(3)
    assert stack.get_max() == 5

    stack.pop()
    assert stack.get_max() == 5

    stack.pop()
    assert stack.get_max() == 5

    stack.pop()
    assert stack.get_max() == "None"


def test_negative_values_only() -> None:
    stack = StackMax()
    for x in [-5, -1, -10, -3]:
        stack.push(x)
    assert stack.get_max() == -1


def test_get_max_does_not_mutate_stack() -> None:
    stack = StackMax()
    stack.push(4)
    stack.push(9)
    first = stack.get_max()
    second = stack.get_max()
    assert first == second == 9
    stack.pop()
    assert stack.get_max() == 4


@pytest.mark.timeout(2)
def test_large_random_sequence_within_timeout() -> None:
    random.seed(42)
    n = 20_000
    values = [random.randint(-100_000, 100_000) for _ in range(n)]

    stack = StackMax()
    running_max = []
    for x in values:
        stack.push(x)
        running_max.append(x if not running_max else max(running_max[-1], x))

    assert stack.get_max() == running_max[-1]

    for _ in range(n):
        stack.pop()
        running_max.pop()
        expected = running_max[-1] if running_max else "None"
        assert stack.get_max() == expected
