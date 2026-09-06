import pytest

from tests_reference.conftest import import_solution

is_correct_bracket_seq = import_solution(
    "tasks.data_structures.bracket_sequence.solution", "is_correct_bracket_seq"
)


@pytest.mark.parametrize(
    "s",
    [
        "",
        "()",
        "[]",
        "{}",
        "()[]{}",
        "{[()]}",
        "((()))",
        "([{}])",
    ],
)
def test_valid_sequences(s: str) -> None:
    assert is_correct_bracket_seq(s) is True


@pytest.mark.parametrize(
    "s",
    [
        "(",
        ")",
        "(]",
        "([)]",
        "]",
        "((())",
        "{[(])}",
        "}{",
    ],
)
def test_invalid_sequences(s: str) -> None:
    assert is_correct_bracket_seq(s) is False


@pytest.mark.timeout(2)
def test_large_nested_sequence_within_timeout() -> None:
    s = "(" * 50_000 + ")" * 50_000
    assert is_correct_bracket_seq(s) is True


@pytest.mark.timeout(2)
def test_large_flat_sequence_within_timeout() -> None:
    s = "()" * 50_000
    assert is_correct_bracket_seq(s) is True
