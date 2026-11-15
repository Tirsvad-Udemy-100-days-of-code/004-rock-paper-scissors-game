"""ASCII art for each choice."""

from rock_paper_scissors.domain.choice import Choice

ROCK = r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

PAPER = r"""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

SCISSORS = r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

_ART_BY_CHOICE = {Choice.ROCK: ROCK, Choice.PAPER: PAPER, Choice.SCISSORS: SCISSORS}


def art_for(choice: Choice) -> str:
    """Return the ASCII art of a choice."""
    return _ART_BY_CHOICE[choice]
