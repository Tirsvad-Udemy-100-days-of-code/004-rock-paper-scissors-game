# Review of the game source code, first review

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-008 |
| CrossReference | [QC-PY-001], [MIL-002], [ADR-0002] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Accepted | Claude (AI assistant) | S01 | Initial version; accepted on S01's instruction in chat, 2026-11-15 | pending |

---

## Artifact Under Review

- Instance reviewed: the game source code, `src/rock_paper_scissors/game.py`, `__main__.py`, `__init__.py` and `tests/test_game.py` as of the start of [MIL-002]
- Checklist used: [QC-PY-001]
- Scope: full review (first review; MIL-002 task 1)
- Language and domain: n/a (source code)
- Language reviewer: none
- Mode: autonomous, not independent (the AI assistant ran the checklist; S01 is the reviewer and accepted the plan in chat on 2026-11-15)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) (Mandatory) | Pass | `snake_case` functions, `UPPER_SNAKE` constants. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes (Mandatory) | Pass | Names state purpose (`determine_result`, `parse_choice`, `colorize_title`). |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions (Mandatory) | Fail | `pyproject.toml` has no `[tool.ruff]` configuration, and `ruff format --check` says 1 file would be reformatted. |
| 4 | Every function and method signature is type-annotated, including `-> None` (Mandatory) | Pass | Every function is annotated; `mypy --strict src` reports no issues. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) (Mandatory) | Pass | `parse_choice` catches only `ValueError` and returns `None` on purpose; no bare `except`. |
| 6 | No mutable default arguments and no shadowed builtins (Mandatory) | Pass | No mutable defaults; no builtin shadowed. |
| 7 | Files, locks and connections are managed with context managers (Mandatory) | N-A | The code opens no file, lock or connection. |
| 8 | Public modules, classes and functions have docstrings that say what, not how (Optional) | Pass | Public functions have docstrings that say what. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output (Mandatory) | Pass | `print` writes the game's own output to the player; it is not diagnostic logging, and no secret or personal data is printed. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded (Mandatory) | N-A | No Design Class Diagram exists; [ADR-0002] records that no use case or design artifact is written. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network (Mandatory) | Pass | `tests/test_game.py` has 20 tests that do not depend on order or the network. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment (Optional) | Pass | `mypy --strict src` reports no issues and the code uses no `Any`. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused (Optional) | Fail | The `dev` extra declares `pytest>=8`, a lower bound only, not a pin. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike (Mandatory) | Pass | Each rule and constant is defined once. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles (Mandatory) | Fail | `determine_result` (a business rule) lives in `game.py` beside `os`, `sys`, `input` and `print`; the rules cannot be imported without the console code. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations (Mandatory) | Fail | `game.py` changes for five reasons: the rules, the ASCII art, the colours, the input parsing and the console flow. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward (Mandatory) | Fail | All code is in one flat package module, `game.py`; there are no `domain`, `application`, `infrastructure` or `presentation` packages, and tests are not under `unit`, `integration` and `e2e`. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files (Mandatory) | Pass | All file and folder names are English, lower case, with no space. |

## Overall Verdict

No-Go: Mandatory criteria 3, 15, 16 and 17 fail, which are blocking findings, and optional criterion 13 fails. The behaviour is correct and the 20 tests pass, so the fix keeps the behaviour and changes only the structure and the tooling configuration. The coloured title, which [BC-001] does not list, stays: it is part of the ASCII art display and costs no extra scope.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Configure `ruff` and `mypy --strict` in `pyproject.toml` and format the code (criterion 3) | S01 | 2026-11-16 |
| Pin the `pytest` version in the `dev` extra (criterion 13) | S01 | 2026-11-16 |
| Split `game.py` into `domain`, `application`, `infrastructure` and `presentation` packages with the rules in `domain` (criteria 15, 16, 17) | S01 | 2026-11-16 |
| Move the tests under `tests/unit` and `tests/e2e` (criterion 17) | S01 | 2026-11-16 |

---

[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[MIL-002]: ../milestones/mil-002-first-release.md
[ADR-0002]: ../adr/adr-0002-skip-user-stories-and-use-cases.md
[BC-001]: ../business-case.md
