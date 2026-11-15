"""The three choices a player can make."""

from enum import IntEnum


class Choice(IntEnum):
    """A choice in Rock, Paper, Scissors; the value is the number the player types."""

    ROCK = 0
    PAPER = 1
    SCISSORS = 2

    @property
    def display_name(self) -> str:
        """Return the name shown to the player, for example ``Rock``."""
        return self.name.capitalize()
