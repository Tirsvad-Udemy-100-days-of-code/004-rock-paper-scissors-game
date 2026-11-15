[English](Architecture) · **Dansk** · [Bahasa Melayu](Architecture-ms)

# Arkitektur

Koden i `src/rock_paper_scissors/` følger en lagdelt (ren) arkitektur: reglerne afhænger hverken af konsollen eller af tilfældighedsgeneratoren.

| Lag | Pakke | Indeholder |
| --- | --- | --- |
| Domæne | `domain` | `Choice`, `RoundResult` og `determine_result`, spillets regler |
| Applikation | `application` | Use casen `PlayRound` og porten `ComputerChoiceSource` |
| Infrastruktur | `infrastructure` | `RandomChoiceSource`, som implementerer porten, og `bootstrap.main`, kompositionsroden |
| Præsentation | `presentation` | `PlayRoundCommand`, ASCII-kunsten, titlen og input-fortolkeren |

Importer peger indad: `domain` importerer intet fra de andre lag, `application` importerer `domain`, `presentation` importerer `application` og `domain`, og kun `infrastructure` importerer alle lag.

## Test

Testene i `tests/` afspejler lagene:

- `tests/unit`: reglerne, use casen (med en falsk computer) og præsentationens hjælpefunktioner
- `tests/integration`: den tilfældige valgkilde
- `tests/e2e`: en hel runde gennem `bootstrap.main` og en rigtig kørsel af `python -m rock_paper_scissors`

```bash
python -m pytest
```

## Værktøj

`ruff` formaterer og linter koden, og `mypy --strict` kontrollerer typerne; begge er sat op i `pyproject.toml`.

Tilbage til [Hjem](Home-da).
