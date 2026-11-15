# MIL-002 First release

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Accepted | Claude (AI assistant) | S01 | Initial version; accepted after RC-006 (Go) | pending |

---

## Purpose

Decides whether the first release of the game meets the Business Case objectives: it plays a correct round, handles invalid input, is tested and is documented.

## Deliverable

The game in `src/rock_paper_scissors/`, its tests in `tests/`, and the project README, reviewed against the Python checklist `qc-programming-python.md` with an `RC-*` record.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The code review against `qc-programming-python.md` has verdict `Go` | An `RC-*` with `Go` | Any Mandatory criterion fails |
| 2 | All 9 combinations of player and computer choice give the expected result | 9 of 9 pass in `pytest` | Fewer than 9 |
| 3 | Input outside 0, 1, 2 and non-numeric input print a message and do not crash | Tests pass for both | A crash or no message |
| 4 | `pytest` passes on Python 3.13 | 100 % of tests pass | Any test fails |
| 5 | `rock-paper-scissors` starts the game after setup | The game starts | The command fails |
| 6 | The README follows the framework template and describes setup, run and tests | All template sections filled | A placeholder remains |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-001] | The accepted baseline and plan-first gate must hold before code or tests change |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1 to 4 and success criteria 1 to 4 | [BC-001] |
| Objective 5 and success criterion 5 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-16 - the end of the plan window set in [PP-001]; the Business Case sets no deadline.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Review the game code against the Python checklist | Review `game.py` and `__main__.py` against `qc-programming-python.md` and record an `RC-*`. Decide whether the coloured title, which the Business Case does not list, stays. Supports objectives 1 to 3. | No | |
| 2 | Fix the code review findings | Change `src/` and `tests/` only for the findings of task 1, keeping the scope to the narrowest release. Objective 5 needs the code to follow the checklist. | No | |
| 3 | Verify the success criteria in tests | Check that tests cover all 9 outcome combinations, invalid and non-numeric input, and that `pytest` passes on Python 3.13 and the `rock-paper-scissors` command starts the game (success criteria 1 to 4). | No | |
| 4 | Restore and complete the README from the framework template | The README in the working tree is the unfilled template; the real text is in the last commit. Fill the template sections with it, including the screenshot and the project documents appendix. | No | |
---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[MIL-001]: ./mil-001-baseline.md
