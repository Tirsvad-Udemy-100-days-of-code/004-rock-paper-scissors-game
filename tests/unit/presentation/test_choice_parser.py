import pytest

from rock_paper_scissors.domain.choice import Choice
from rock_paper_scissors.presentation.shared.choice_parser import parse_choice


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("0", Choice.ROCK),
        (" 1 ", Choice.PAPER),
        ("2", Choice.SCISSORS),
        ("3", None),
        ("-1", None),
        ("rock", None),
        ("", None),
    ],
)
def test_parse_choice(text: str, expected: Choice | None) -> None:
    assert parse_choice(text) == expected
