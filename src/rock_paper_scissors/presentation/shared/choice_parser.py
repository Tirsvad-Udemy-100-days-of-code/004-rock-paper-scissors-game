"""Turns what the player typed into a choice."""

from rock_paper_scissors.domain.choice import Choice


def parse_choice(text: str) -> Choice | None:
    """Convert raw input to a choice, or None if it is not 0, 1 or 2."""
    try:
        value = int(text.strip())
    except ValueError:
        return None
    try:
        return Choice(value)
    except ValueError:
        return None
