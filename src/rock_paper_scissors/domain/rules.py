"""The rules of Rock, Paper, Scissors."""

from enum import Enum

from rock_paper_scissors.domain.choice import Choice


class RoundResult(Enum):
    """The result of one round from the player's point of view."""

    WIN = "win"
    LOSE = "lose"
    DRAW = "draw"


def determine_result(player: Choice, computer: Choice) -> RoundResult:
    """Return the result of a round from the player's point of view."""
    if player == computer:
        return RoundResult.DRAW
    # Each choice beats the one before it (paper > rock, scissors > paper,
    # rock > scissors).
    if (player - computer) % len(Choice) == 1:
        return RoundResult.WIN
    return RoundResult.LOSE
