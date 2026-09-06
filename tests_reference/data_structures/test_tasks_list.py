import pytest

from tests_reference.conftest import import_solution

Node, solution = import_solution("tasks.data_structures.tasks_list.solution", "Node", "solution")


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


def test_single_element(capsys: pytest.CaptureFixture[str]) -> None:
    head = build_list(["only"])
    solution(head)
    out = capsys.readouterr().out.splitlines()
    assert out == ["only"]


def test_task_example(capsys: pytest.CaptureFixture[str]) -> None:
    head = build_list(["node0", "node1", "node2", "node3"])
    solution(head)
    out = capsys.readouterr().out.splitlines()
    assert out == ["node0", "node1", "node2", "node3"]


def test_preserves_order_with_integers(capsys: pytest.CaptureFixture[str]) -> None:
    head = build_list([10, 20, 30, 40, 50])
    solution(head)
    out = capsys.readouterr().out.splitlines()
    assert out == ["10", "20", "30", "40", "50"]


def test_duplicate_values(capsys: pytest.CaptureFixture[str]) -> None:
    head = build_list(["a", "a", "b", "a"])
    solution(head)
    out = capsys.readouterr().out.splitlines()
    assert out == ["a", "a", "b", "a"]


def test_negative_numbers(capsys: pytest.CaptureFixture[str]) -> None:
    head = build_list([-1, -2, 0, 3])
    solution(head)
    out = capsys.readouterr().out.splitlines()
    assert out == ["-1", "-2", "0", "3"]


def test_does_not_return_anything() -> None:
    head = build_list(["a", "b"])
    assert solution(head) is None


@pytest.mark.timeout(2)
def test_large_list_within_timeout(capsys: pytest.CaptureFixture[str]) -> None:
    n = 5000
    head = build_list(list(range(n)))
    solution(head)
    out = capsys.readouterr().out.splitlines()
    assert out == [str(i) for i in range(n)]
