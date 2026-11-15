"""The computer chooses at random."""

import random

from rock_paper_scissors.domain.choice import Choice


class RandomChoiceSource:
    """Implements the computer choice port with the ``random`` module."""

    def next_choice(self) -> Choice:
        """Return a random choice."""
        return Choice(random.randint(0, len(Choice) - 1))
