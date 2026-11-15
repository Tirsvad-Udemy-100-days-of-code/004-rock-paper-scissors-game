# Rock Paper Scissors Game Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Proposed | Claude (AI assistant) | S01 | Initial version | pending |
| 2026-11-15 | Proposed | Claude (AI assistant) | S01 | Added PP-001, MIL-001, MIL-002 and ADR-0002 | pending |

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
| [PP-001] | Project Plan | en | it | [BC-001], [SA-001] | [MIL-001], [MIL-002] | [RC-004] |
| [MIL-001] | Milestone | en | it | [PP-001] | [MIL-002] | [RC-005] |
| [MIL-002] | Milestone | en | it | [MIL-001] | - | [RC-006] |

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
[ADR-0002]: ../adr/adr-0002-skip-user-stories-and-use-cases.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-baseline.md
[MIL-002]: ../milestones/mil-002-first-release.md
