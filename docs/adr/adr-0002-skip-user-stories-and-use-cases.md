# Skip user stories and use cases

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0002 |
| CrossReference | [BC-001], [SA-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Accepted | Claude (AI assistant) | S01 | Initial version; accepted after RC-007 (Go) | [d3c74f5] |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The journey offers candidate user stories (`US`) and a use case diagram (`UCD`)
before the milestones. The game has one actor (S01, the player) and one actor
goal: play a round against the computer. Options: write a user story and a use
case with their design artifacts (system sequence diagram, domain model and so
on), write only a user story, or skip both and plan the work as technical
tasks that cite the Business Case objectives.

## Decision

Skip the user stories, the use case diagram and the use cases. The milestones'
tasks are plain technical tasks that cite the objectives of [BC-001].

## Consequences

**Positive:**

- No documents for a single, obvious goal; the plan stays proportionate to a
  one-person prototype.
- Every task still traces to a Business Case objective.

**Negative:**

- No use case, so no system sequence diagram, operation contract or design
  class diagram to review the code against; the Python checklist and the tests
  are the only design evidence.
- A second actor or goal later makes this decision obsolete: add the stories
  and supersede this ADR.

## Affected Artifacts

- [BC-001] - the objectives the tasks cite instead of a use case.
- [SA-001] - S01 is the only actor.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[d3c74f5]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/004-rock-paper-scissors-game/commit/d3c74f56d4214003f20c8c78a96173b793e43a56
