# Rock Paper Scissors Game Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Deprecated | Claude (AI assistant) | S01 | Added the source code row and RC-009, RC-010; accepted on S01's instruction in chat, 2026-11-15 | [1428c08] |
| 2026-11-15 | Accepted | Claude (AI assistant) | S01 | Added MIL-003, the wiki, RC-011, RC-012 and RC-013; accepted on S01's instruction in chat, 2026-11-15 | [4f0682a] |

---

## Purpose

Tracks backward and forward links between artifact instances so that the
cross-artifact traceability of the project is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | Business Case | en | it | - | [SA-001], [ADR-0001], [ADR-0002], [PP-001] | [RC-001] |
| [SA-001] | Stakeholder Analysis | en | it | [BC-001] | - | [RC-002] |
| [ADR-0001] | Architecture Decision Record | - | - | [BC-001] | - | [RC-003] |
| [ADR-0002] | Architecture Decision Record | - | - | [BC-001], [SA-001] | [MIL-001], [MIL-002] | [RC-007] |
| [PP-001] | Project Plan | en | it | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003] | [RC-012] |
| [MIL-001] | Milestone | en | it | [PP-001] | [MIL-002] | [RC-005] |
| [MIL-002] | Milestone | en | it | [MIL-001] | Source code, [MIL-003] | [RC-006] |
| [MIL-003] | Milestone | en | it | [MIL-002] | Wiki | [RC-011] |
| Source code (`src/`, `tests/`) | Python code | - | - | [MIL-002] | - | [RC-009] |
| Wiki (`docs/wiki/`) | Wiki | en | - | [MIL-003] | - | [RC-013] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | - | - | - | Gap |
| CN-002 | - | - | - | Gap |
| CN-003 | - | - | - | Gap |
| CN-004 | - | - | - | Gap |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| - | - | None found | - | - | - |

## Coverage Notes

- No view, Test Plan, Project Plan or milestone exists yet, so every concern is
  a Gap until the design and test artifacts are written.
- `-` in Upstream means foundational, in Downstream that nothing is built on it
  yet, and in Last Reviewed that no `RC-*` exists yet.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[ADR-0001]: ../adr/adr-0001-skip-optional-analysis-documents.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-adr-0001.md
[RC-004]: ./reviews/rc-004-project-plan.md
[RC-005]: ./reviews/rc-005-mil-001.md
[RC-006]: ./reviews/rc-006-mil-002.md
[RC-007]: ./reviews/rc-007-adr-0002.md
[RC-009]: ./reviews/rc-009-python-code-second-review.md
[RC-010]: ./reviews/rc-010-project-plan-delta.md
[RC-011]: ./reviews/rc-011-mil-003.md
[RC-012]: ./reviews/rc-012-project-plan-wiki.md
[RC-013]: ./reviews/rc-013-wiki-first-review.md
[MIL-003]: ../milestones/mil-003-wiki.md
[ADR-0002]: ../adr/adr-0002-skip-user-stories-and-use-cases.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-baseline.md
[MIL-002]: ../milestones/mil-002-first-release.md
[d3c74f5]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/004-rock-paper-scissors-game/commit/d3c74f56d4214003f20c8c78a96173b793e43a56
[1428c08]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/004-rock-paper-scissors-game/commit/1428c081485708bd32faf83a277b5f47b43ef5c1
[4f0682a]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/004-rock-paper-scissors-game/commit/4f0682a2233d43d9da078d6dfcecf3cfcb2a1c84
