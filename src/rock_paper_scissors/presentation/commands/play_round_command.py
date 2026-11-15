"""The console command that plays one round."""

import os

from rock_paper_scissors.application.use_cases.play_round import PlayRound
from rock_paper_scissors.domain.rules import RoundResult
from rock_paper_scissors.presentation.shared.ascii_art import art_for
from rock_paper_scissors.presentation.shared.choice_parser import parse_choice
from rock_paper_scissors.presentation.shared.title import colorize_title

PROMPT = "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
INVALID_INPUT_MESSAGE = "You typed an invalid number. You lose!"
_RESULT_MESSAGES = {
    RoundResult.WIN: "You win!",
    RoundResult.LOSE: "You lose!",
    RoundResult.DRAW: "It's a draw!",
}


class PlayRoundCommand:
    """Reads the player's choice, plays a round and shows the outcome."""

    def __init__(self, play_round: PlayRound) -> None:
        self._play_round = play_round

    def run(self) -> None:
        """Run the command on the console."""
        os.system("")  # enables ANSI escape handling on Windows consoles
        print(colorize_title())
        player = parse_choice(input(PROMPT))
        if player is None:
            print(INVALID_INPUT_MESSAGE)
            return

        outcome = self._play_round.execute(player)
        print(f"You chose {player.display_name}:{art_for(outcome.player)}")
        computer = outcome.computer
        print(f"Computer chose {computer.display_name}:{art_for(computer)}")
        print(_RESULT_MESSAGES[outcome.result])
