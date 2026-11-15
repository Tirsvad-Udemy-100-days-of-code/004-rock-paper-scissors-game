import pytest

from rock_paper_scissors.domain.choice import Choice
from rock_paper_scissors.domain.rules import RoundResult, determine_result


@pytest.mark.parametrize(
    ("player", "computer", "expected"),
    [
        (Choice.ROCK, Choice.ROCK, RoundResult.DRAW),
        (Choice.PAPER, Choice.PAPER, RoundResult.DRAW),
        (Choice.SCISSORS, Choice.SCISSORS, RoundResult.DRAW),
        (Choice.ROCK, Choice.SCISSORS, RoundResult.WIN),
        (Choice.PAPER, Choice.ROCK, RoundResult.WIN),
        (Choice.SCISSORS, Choice.PAPER, RoundResult.WIN),
        (Choice.SCISSORS, Choice.ROCK, RoundResult.LOSE),
        (Choice.ROCK, Choice.PAPER, RoundResult.LOSE),
        (Choice.PAPER, Choice.SCISSORS, RoundResult.LOSE),
    ],
)
def test_determine_result_for_every_combination(
    player: Choice, computer: Choice, expected: RoundResult
) -> None:
    assert determine_result(player, computer) == expected
