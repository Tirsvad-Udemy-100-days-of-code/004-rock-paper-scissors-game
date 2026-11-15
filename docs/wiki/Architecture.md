**English**

# Architecture

The code in `src/rock_paper_scissors/` follows a layered (clean) architecture: the rules do not depend on the console or on the random number generator.

| Layer | Package | Holds |
| --- | --- | --- |
| Domain | `domain` | `Choice`, `RoundResult` and `determine_result`, the rules of the game |
| Application | `application` | The `PlayRound` use case and the `ComputerChoiceSource` port |
| Infrastructure | `infrastructure` | `RandomChoiceSource`, which implements the port, and `bootstrap.main`, the composition root |
| Presentation | `presentation` | The `PlayRoundCommand`, the ASCII art, the title and the input parser |

Imports point inward: `domain` imports nothing from the other layers, `application` imports `domain`, `presentation` imports `application` and `domain`, and only `infrastructure` imports every layer.

## Tests

The tests in `tests/` mirror the layers:

- `tests/unit`: the rules, the use case (with a fake computer) and the presentation helpers
- `tests/integration`: the random choice source
- `tests/e2e`: a full round through `bootstrap.main`, and a real run of `python -m rock_paper_scissors`

```bash
python -m pytest
```

## Tooling

`ruff` formats and lints the code, and `mypy --strict` checks the types; both are configured in `pyproject.toml`.

Back to [Home](Home).
