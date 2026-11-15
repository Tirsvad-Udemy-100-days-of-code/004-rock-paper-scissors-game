import pytest

from rock_paper_scissors.domain.choice import Choice


@pytest.mark.parametrize(
    ("choice", "number", "name"),
    [
        (Choice.ROCK, 0, "Rock"),
        (Choice.PAPER, 1, "Paper"),
        (Choice.SCISSORS, 2, "Scissors"),
    ],
)
def test_choice_has_number_and_display_name(
    choice: Choice, number: int, name: str
) -> None:
    assert choice == number
    assert choice.display_name == name
