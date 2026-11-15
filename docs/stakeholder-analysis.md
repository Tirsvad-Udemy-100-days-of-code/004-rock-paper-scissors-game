# Rock Paper Scissors Game Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Accepted | Claude (AI assistant) | S01 | Initial version; accepted after RC-002 (Go) | pending |

---

## Purpose

This analysis names the people involved in the Rock Paper Scissors Game and
what each needs from it, so owners, reviewers and the concerns behind the
Business Case ([BC-001]) can be cited by ID. It uses the power/interest grid to
classify stakeholders and the FURPS+ model (Functionality, Usability, Reliability, Performance, Supportability, plus design, implementation, interface and physical constraints) to classify their concerns. The
project is a one-person learning prototype, so the register is short.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Product Owner, learner (player), reviewer and approver | Independent | HIGH | HIGH | Manage Closely | A working, tested and documented game that proves the course material was understood |

## Power/Interest Classification Rationale

- **Manage Closely:** S01 decides the scope, plays the game, reviews every
  document and accepts it, so holds all the power and all the interest. There
  are no other stakeholders in the other quadrants.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | Every round gives the correct result | Functionality |
| CN-002 | S01 | A mistyped choice does not crash the game | Reliability |
| CN-003 | S01 | The game starts with one command and is easy to play | Usability |
| CN-004 | S01 | The code is easy to read and change | Supportability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| CM-001 | Chat with the artificial intelligence (AI) assistant | After each document | Draft for review and acceptance | Every phase |
| CM-002 | Pull request | Once per milestone | Changes for review | Every milestone |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S01 is both the author's principal and the reviewer, so a review is not independent | S01 | The AI assistant is named as author in the Version History, S01 is the reviewer, and a review is marked independent only when someone other than S01 does it |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001 | [BC-001] Objective 2: decide every round correctly |
| S01 | CN-002 | [BC-001] Objective 3: handle invalid input without crashing |
| S01 | CN-003 | [BC-001] Objective 1: let a player choose and play one round |
| S01 | CN-004 | [BC-001] Objective 5: keep documents and code consistent with the framework |

## Sign-Off

| Stakeholder | Decision | Date |
| --- | --- | --- |
| S01 | Accepted after RC-002 (Go) | 2026-11-15 |

---

[BC-001]: ./business-case.md
