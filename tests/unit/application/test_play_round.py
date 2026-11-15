from rock_paper_scissors.application.use_cases.play_round import PlayRound
from rock_paper_scissors.domain.choice import Choice
from rock_paper_scissors.domain.rules import RoundResult


class FixedChoiceSource:
    """A fake computer that always makes the same choice."""

    def __init__(self, choice: Choice) -> None:
        self._choice = choice

    def next_choice(self) -> Choice:
        return self._choice


def test_play_round_returns_both_choices_and_the_result() -> None:
    outcome = PlayRound(FixedChoiceSource(Choice.SCISSORS)).execute(Choice.ROCK)

    assert outcome.player == Choice.ROCK
    assert outcome.computer == Choice.SCISSORS
    assert outcome.result == RoundResult.WIN


def test_play_round_reports_a_draw_when_choices_match() -> None:
    outcome = PlayRound(FixedChoiceSource(Choice.PAPER)).execute(Choice.PAPER)

    assert outcome.result == RoundResult.DRAW
