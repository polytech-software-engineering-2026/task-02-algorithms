import pytest

from tests_reference.conftest import import_solution

DoubleConnectedNode, solution = import_solution(
    "tasks.data_structures.double_connected_node.solution",
    "DoubleConnectedNode",
    "solution",
)


def build_list(values):
    nodes = [DoubleConnectedNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
        nodes[i + 1].prev = nodes[i]
    return nodes[0] if nodes else None


def forward_values(head):
    values = []
    node = head
    while node is not None:
        values.append(node.value)
        node = node.next
    return values


def assert_links_symmetric(head):
    node = head
    assert node.prev is None
    prev = None
    while node is not None:
        assert node.prev is prev
        if node.next is not None:
            assert node.next.prev is node
        prev = node
        node = node.next


def test_single_node() -> None:
    head = build_list(["a"])
    new_head = solution(head)
    assert new_head is head
    assert new_head.next is None
    assert new_head.prev is None


def test_two_nodes() -> None:
    head = build_list(["a", "b"])
    new_head = solution(head)
    assert forward_values(new_head) == ["b", "a"]
    assert_links_symmetric(new_head)


def test_three_nodes() -> None:
    head = build_list(["a", "b", "c"])
    new_head = solution(head)
    assert forward_values(new_head) == ["c", "b", "a"]
    assert_links_symmetric(new_head)


def test_four_nodes_from_task_example() -> None:
    node3 = DoubleConnectedNode("node3")
    node2 = DoubleConnectedNode("node2")
    node1 = DoubleConnectedNode("node1")
    node0 = DoubleConnectedNode("node0")

    node0.next = node1
    node1.prev = node0
    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2

    new_head = solution(node0)

    assert new_head is node3
    assert node3.next is node2
    assert node2.next is node1
    assert node2.prev is node3
    assert node1.next is node0
    assert node1.prev is node2
    assert node0.prev is node1
    assert node0.next is None


def test_values_and_symmetry_on_five_nodes() -> None:
    head = build_list([1, 2, 3, 4, 5])
    new_head = solution(head)
    assert forward_values(new_head) == [5, 4, 3, 2, 1]
    assert_links_symmetric(new_head)


def test_reversed_twice_restores_original_order() -> None:
    head = build_list(list(range(10)))
    once = solution(head)
    twice = solution(once)
    assert forward_values(twice) == list(range(10))
    assert_links_symmetric(twice)


def test_duplicate_values_preserve_node_identity() -> None:
    head = build_list([1, 1, 2, 2])
    tail_before = head.next.next.next
    new_head = solution(head)
    assert new_head is tail_before
    assert forward_values(new_head) == [2, 2, 1, 1]


@pytest.mark.timeout(2)
def test_large_list_within_timeout() -> None:
    values = list(range(1000))
    head = build_list(values)
    new_head = solution(head)
    assert forward_values(new_head) == list(reversed(values))
    assert_links_symmetric(new_head)
