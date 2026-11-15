"""The coloured title shown at the start of the game."""

import os
import sys

TITLE = r"""
 ____   ___   ____ _  __
|  _ \ / _ \ / ___| |/ /
| |_) | | | | |   | ' /
|  _ <| |_| | |___| . \
|_| \_\\___/ \____|_|\_\
 ____   _    ____  _____ ____
|  _ \ / \  |  _ \| ____|  _ \
| |_) / _ \ | |_) |  _| | |_) |
|  __/ ___ \|  __/| |___|  _ <
|_| /_/   \_\_|   |_____|_| \_\
 ____   ____ ___ ____ ____   ___  ____  ____
/ ___| / ___|_ _/ ___/ ___| / _ \|  _ \/ ___|
\___ \| |    | |\___ \___ \| | | | |_) \___ \
 ___) | |___ | | ___) |__) | |_| |  _ < ___) |
|____/ \____|___|____/____/ \___/|_| \_\____/
"""

RESET = "\033[0m"
# One colour per word of the title: ROCK, PAPER, SCISSORS.
TITLE_COLORS = ["\033[91m", "\033[93m", "\033[96m"]
TITLE_LINES_PER_WORD = 5


def supports_color() -> bool:
    """Return True if ANSI colours should be used on stdout."""
    return sys.stdout.isatty() and "NO_COLOR" not in os.environ


def colorize_title(title: str = TITLE, enabled: bool | None = None) -> str:
    """Return the title with each word coloured, or unchanged if colour is off."""
    if enabled is None:
        enabled = supports_color()
    if not enabled:
        return title
    lines = title.strip("\n").split("\n")
    coloured = [
        f"{TITLE_COLORS[i // TITLE_LINES_PER_WORD]}{line}{RESET}"
        for i, line in enumerate(lines)
    ]
    return "\n" + "\n".join(coloured) + "\n"
