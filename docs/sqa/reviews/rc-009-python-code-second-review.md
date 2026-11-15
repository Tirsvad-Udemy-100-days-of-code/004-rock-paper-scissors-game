# Review of the game source code, second review

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-009 |
| CrossReference | [QC-PY-001], [RC-008], [MIL-002], [ADR-0002] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Accepted | Claude (AI assistant) | S01 | Initial version; accepted on S01's instruction in chat, 2026-11-15 | pending |

---

## Artifact Under Review

- Instance reviewed: the game source code in `src/rock_paper_scissors/` and the tests in `tests/` after the fixes of [MIL-002] task 2
- Checklist used: [QC-PY-001]
- Scope: full review, after the No-Go of [RC-008]
- Language and domain: n/a (source code)
- Language reviewer: none
- Mode: autonomous, not independent (the AI assistant ran the checklist; S01 is the reviewer and accepted the plan in chat on 2026-11-15)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) (Mandatory) | Pass | Modules and functions use `snake_case`, classes `PascalCase`, constants `UPPER_SNAKE`. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes (Mandatory) | Pass | Names state purpose (`PlayRound`, `ComputerChoiceSource`, `determine_result`). |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions (Mandatory) | Pass | `pyproject.toml` configures `ruff`; `ruff format` and `ruff check` report no change and no finding, with no suppression. |
| 4 | Every function and method signature is type-annotated, including `-> None` (Mandatory) | Pass | Every function and method is annotated, tests included; `mypy --strict src tests` reports no issues. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) (Mandatory) | Pass | `parse_choice` catches only `ValueError`; there is no bare `except`. |
| 6 | No mutable default arguments and no shadowed builtins (Mandatory) | Pass | No mutable defaults; no builtin shadowed. |
| 7 | Files, locks and connections are managed with context managers (Mandatory) | N-A | The code opens no file, lock or connection. |
| 8 | Public modules, classes and functions have docstrings that say what, not how (Optional) | Pass | Public modules, classes and functions have docstrings that say what. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output (Mandatory) | Pass | `print` writes the game output to the player, not diagnostics; no secret or personal data is printed. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded (Mandatory) | N-A | No Design Class Diagram exists; [ADR-0002] records that none is written. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network (Mandatory) | Pass | 30 tests (unit, integration, end to end) are named for behaviour and do not depend on order or the network. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment (Optional) | Pass | `mypy --strict` passes; the code uses no `Any`. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused (Optional) | Pass | The `dev` extra declares `pytest>=8,<10`, `ruff` and `mypy` with bounds, and all are used. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike (Mandatory) | Pass | The rules live once in `domain/rules.py`; the messages and art live once in `presentation`. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles (Mandatory) | Pass | `domain` imports only itself; `application` imports `domain`; `presentation` imports `application` and `domain`; only `infrastructure` imports every layer; no cycle. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations (Mandatory) | Pass | Each module has one reason to change (rules, use case, random source, art, title, parser, command); the use case depends on the `ComputerChoiceSource` protocol, which `RandomChoiceSource` implements. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward (Mandatory) | Pass | `src/rock_paper_scissors` has `domain`, `application`, `infrastructure` and `presentation` packages; tests are in `tests/unit`, `tests/integration` and `tests/e2e`. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files (Mandatory) | Pass | All names are English, lower case, with no space. |

## Overall Verdict

Go: all 18 criteria of [QC-PY-001] are Pass or N-A with a reason, so the four blocking findings of [RC-008] (criteria 3, 15, 16, 17) and the optional finding (13) are closed. The behaviour is unchanged: the 9 outcome combinations, invalid input and the start command are covered by the 30 tests, which pass on Python 3.13.14.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | - | - |

---

[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[MIL-002]: ../milestones/mil-002-first-release.md
[ADR-0002]: ../adr/adr-0002-skip-user-stories-and-use-cases.md
[RC-008]: ./rc-008-python-code-first-review.md
