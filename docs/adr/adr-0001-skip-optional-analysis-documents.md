# Skip the optional analysis documents

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Accepted | Claude (AI assistant) | S01 | Initial version; accepted after RC-003 (Go) | [d3c74f5] |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The Business Case (BC-001) may be supported by optional analysis documents: KPI
Definitions (KPI), a Business Model Canvas (BMC), a Business Process Model and Notation (BPMN) process model and a
Risk Analysis (RA) that tests the riskiest assumption. The project is a
single-person learning prototype with no budget, no revenue and no business
process, and its idea is a hunch with nothing costly at stake. Options: write
all four, write only the KPI, or skip all four.

## Decision

Skip KPI, BMC, BPMN and RA. The measurable success criteria live in the
Business Case itself, and the riskiest assumption is recorded there as an
untested assumption.

## Consequences

**Positive:**

- Less documentation overhead for a small exercise.
- The success criteria stay in one place, next to the objectives.

**Negative:**

- No separate KPI document, so a criterion cannot be reviewed against the KPI
  checklist.
- The riskiest assumption is never tested; this is accepted because nothing
  costly depends on it.

## Affected Artifacts

- [BC-001] — success criteria and assumptions are stated in the document
  itself.

---

[BC-001]: ../business-case.md
[d3c74f5]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/004-rock-paper-scissors-game/commit/d3c74f56d4214003f20c8c78a96173b793e43a56
