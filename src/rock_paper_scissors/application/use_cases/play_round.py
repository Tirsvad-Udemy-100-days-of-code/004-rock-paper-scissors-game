"""The use case: play one round against the computer."""

from dataclasses import dataclass

from rock_paper_scissors.application.ports.choice_source import ComputerChoiceSource
from rock_paper_scissors.domain.choice import Choice
from rock_paper_scissors.domain.rules import RoundResult, determine_result


@dataclass(frozen=True)
class RoundOutcome:
    """Both choices of a round and its result for the player."""

    player: Choice
    computer: Choice
    result: RoundResult


class PlayRound:
    """Plays one round of the player's choice against the computer's."""

    def __init__(self, choice_source: ComputerChoiceSource) -> None:
        self._choice_source = choice_source

    def execute(self, player: Choice) -> RoundOutcome:
        """Play a round and return its outcome."""
        computer = self._choice_source.next_choice()
        return RoundOutcome(player, computer, determine_result(player, computer))
