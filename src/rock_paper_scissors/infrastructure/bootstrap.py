"""The composition root: creates the objects and starts the game."""

from rock_paper_scissors.application.use_cases.play_round import PlayRound
from rock_paper_scissors.infrastructure.random_choice_source import RandomChoiceSource
from rock_paper_scissors.presentation.commands.play_round_command import (
    PlayRoundCommand,
)


def main() -> None:
    """Start the game with the real computer player and the console."""
    PlayRoundCommand(PlayRound(RandomChoiceSource())).run()
