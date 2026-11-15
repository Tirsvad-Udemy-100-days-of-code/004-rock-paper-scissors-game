"""The port the game needs to obtain the computer's choice."""

from typing import Protocol

from rock_paper_scissors.domain.choice import Choice


class ComputerChoiceSource(Protocol):
    """Supplies the computer's choice for one round."""

    def next_choice(self) -> Choice:
        """Return the computer's choice."""
        ...
