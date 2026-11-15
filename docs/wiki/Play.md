**English** · [Dansk](Play-da) · [Bahasa Melayu](Play-ms)

# Play

## Start the game

With the virtual environment active, run either command:

```bash
python -m rock_paper_scissors
```

```bash
rock-paper-scissors
```

## Rules

Type `0` for Rock, `1` for Paper or `2` for Scissors.

| You | Computer | Result |
| --- | --- | --- |
| Rock | Scissors | You win |
| Scissors | Paper | You win |
| Paper | Rock | You win |
| Same choice | Same choice | Draw |

Any other input (for example `3` or `rock`) prints a message and ends the round with a loss; the game never crashes on bad input.

## Colour

The title is coloured when the output is a terminal. Set the `NO_COLOR` environment variable to turn colour off.

See also [Install](Install) and [Architecture](Architecture).
