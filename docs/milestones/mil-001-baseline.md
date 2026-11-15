# MIL-001 Baseline

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Accepted | Claude (AI assistant) | S01 | Initial version; accepted after RC-005 (Go) | pending |

---

## Purpose

Decides whether the project baseline is complete enough to start the first release: the problem, the people and the schedule are written down and reviewed.

## Deliverable

The accepted Business Case ([BC-001]), Stakeholder Analysis ([SA-001]), Project Plan ([PP-001]) and both milestone documents, with ADR-0001 and ADR-0002 recording the skipped optional documents, and the framework repository rules applied.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | BC-001, SA-001 and ADR-0001 are `Accepted` with a `Go` review | RC-001, RC-002 and RC-003 say `Go` | Any of them is `Proposed` or has a `No-Go` |
| 2 | PP-001, MIL-001, MIL-002 and ADR-0002 are `Accepted` with a `Go` review | Their review records say `Go` | Any of them is `Proposed` or has a `No-Go` |
| 3 | `check-editorconfig.sh`, `check-languages.sh` and `check-qc-tags.sh` pass | All three exit 0 | Any exits non-zero |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | First gateway |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 5: keep the project's documents and code consistent with the framework; success criterion 5 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-15 - the first day of the plan window set in [PP-001]; the Business Case sets no deadline.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Apply the framework repository rules | Add the root `.editorconfig`, the project registry, the framework git hooks and the prompt log, as `AGENTS.md` requires, so every later change is checked the same way. | No | |
| 2 | Accept the Business Case, Stakeholder Analysis and ADR-0001 | Review the three documents against their QC checklists and record RC-001, RC-002 and RC-003; the game cannot be planned until the problem and the people are accepted. | No | |
| 3 | Accept the Project Plan, the milestones and ADR-0002 | Review the plan, both milestones and the decision to skip user stories and use cases; this makes the plan-first gate pass for MIL-002. | No | |
---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
