import pytest

from tests_reference.conftest import import_solution

Node, solution = import_solution("tasks.data_structures.update_list.solution", "Node", "solution")


def build_list(values):
    head = None
    tail = None
    for v in values:
        node = Node(v)
        if head is None:
            head = tail = node
        else:
            tail.next_item = node
            tail = node
    return head


def to_values(head):
    values = []
    node = head
    while node is not None:
        values.append(node.value)
        node = node.next_item
    return values


def test_task_example_remove_middle() -> None:
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)

    new_head = solution(node0, 1)

    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None


def test_remove_head() -> None:
    head = build_list(["a", "b", "c"])
    new_head = solution(head, 0)
    assert to_values(new_head) == ["b", "c"]


def test_remove_tail() -> None:
    head = build_list(["a", "b", "c"])
    new_head = solution(head, 2)
    assert to_values(new_head) == ["a", "b"]


def test_remove_only_element_returns_empty_list() -> None:
    head = build_list(["only"])
    new_head = solution(head, 0)
    assert new_head is None


def test_two_element_list_remove_first() -> None:
    head = build_list(["a", "b"])
    new_head = solution(head, 0)
    assert to_values(new_head) == ["b"]


def test_two_element_list_remove_second() -> None:
    head = build_list(["a", "b"])
    new_head = solution(head, 1)
    assert to_values(new_head) == ["a"]


def test_duplicate_values_removes_by_position_not_value() -> None:
    head = build_list(["a", "a", "b", "a"])
    new_head = solution(head, 1)
    assert to_values(new_head) == ["a", "b", "a"]


def test_integers_preserve_remaining_order() -> None:
    head = build_list([10, 20, 30, 40, 50])
    new_head = solution(head, 3)
    assert to_values(new_head) == [10, 20, 30, 50]


@pytest.mark.timeout(2)
def test_large_list_remove_middle_within_timeout() -> None:
    n = 5000
    head = build_list(list(range(n)))
    new_head = solution(head, n // 2)
    expected = list(range(n))
    expected.pop(n // 2)
    assert to_values(new_head) == expected
