# Rock Paper Scissors Game Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Accepted | Claude (AI assistant) | S01 | Initial version; Stakeholders filled from [SA-001]; accepted after RC-001 (Go) | [d3c74f5] |

---

## Executive Summary

A person learning Python needs a small, complete program that exercises
input, randomness and conditional logic. This project delivers a command-line
Rock, Paper, Scissors game played against the computer (Day 4 of Udemy's
*100 Days of Code: The Complete Python Pro Bootcamp*), built and documented to
the Software Quality Assurance (SQA) and Quality Control (QC)
framework so the learner also practises a disciplined
engineering process. The first release is the narrowest game that meets the
objectives; it is a prototype with no budget and a single person.

## Methodological and Standards Foundation

- **Method:** the plan-first workflow of the SQA and QC framework (Business
  Case, Stakeholder Analysis, Project Plan, milestones, tasks, then code), each
  step reviewed before the next.
- **Quality standard:** ISO/IEC 25010:2023 characteristics tag every QC
  criterion used to review the artifacts and the code.
- **Code:** Python 3.13 under the `coding-conventions` and
  `clean-architecture` skills of the framework: game rules kept apart from
  console input and output.

## Problem Statement

A learner who only reads about conditionals and random numbers does not know
whether they can combine them into a working program. A course exercise that is
written once, with no tests and no documents, also gives no practice in the
review and traceability habits of professional work.

## Business Opportunity

If the exercise is built as a small, tested and documented project, the learner
gains a finished reference program, evidence of having applied the course
material, and a worked example of the framework applied to a very small
project.

## Objectives

1. Deliver a game that lets a player choose Rock, Paper or Scissors and plays
   one round against a randomly choosing computer.
2. Decide every round correctly under the three rules (rock beats scissors,
   scissors beats paper, paper beats rock) and report a draw when both choices
   match.
3. Handle invalid input without crashing.
4. Verify the rules with automated tests.
5. Keep the project's documents and code consistent with the framework.

## Scope

### In Scope

- One command-line round: the player enters `0` (Rock), `1` (Paper) or
  `2` (Scissors).
- A random computer choice from the `random` module.
- Both choices shown as ASCII art, and the result: win, lose or draw.
- A message for invalid input.
- Automated tests for the game rules.
- The project documents the framework requires.

### Out of Scope

- A graphical or web interface.
- Score tracking, best-of-N rounds and replay.
- Networked or multi-player play.
- Any runtime dependency beyond the Python standard library.
- Packaging for distribution outside this repository.

## Expected Benefits

### Tangible Benefits

- A working, tested game that runs with one command.
- A set of reviewed project documents that can be reused as a template for
  other small exercises.

### Intangible Benefits

- Practice combining input, randomness and conditional logic.
- Practice with test-first thinking, review records and traceability.
- Confidence in applying the framework to a small project.

## Strategic Alignment

The project supports the learner's goal of completing the *100 Days of Code*
course (this is the fourth project) and of building a repeatable, disciplined
way of working that carries over to larger projects.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Correct outcome for every combination of player and computer choice | 9 of 9 combinations give the expected result | Automated tests, one case per combination |
| 2 | Invalid input is handled | 0 crashes; the player sees a message | Automated tests with input outside `0`, `1`, `2` and non-numeric text |
| 3 | The test suite passes | 100 % of tests pass | `pytest` on Python 3.13 |
| 4 | The game starts with one command | 1 command | Run `rock-paper-scissors` after setup |
| 5 | Required documents are accepted | Business Case, Stakeholder Analysis, Project Plan and 1 milestone each `Accepted` with a `Go` review | Artifact registry and review records |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The framework overhead is out of proportion to a small exercise | Documents take longer than the game | Keep each document short for the prototype stage; defer optional documents with an Architecture Decision Record (ADR) |
| The game code predates the plan, so the plan-first gate could be bypassed | Code not traceable to a task | Plan the existing code as the first milestone's tasks and review it against the Python checklist |
| The learner stops before the exercise is reviewed | Unreviewed documents and code | One reviewer (the Product Owner) checks each step before the next starts |

## Assumptions

- The idea is a hunch with nothing costly at stake, so the riskiest-assumption
  step is skipped.
- The only user is the learner; no other users are reachable or needed.
- Python 3.13 or newer is available on the learner's machine.

## Constraints

- Prototype stage: the smallest document set that meets the framework baseline.
- No budget and no deadline; one person.
- Python standard library only at runtime; `pytest` for tests.
- Command-line interface only.
- The project is licensed AGPL-3.0-or-later.

## Cost–Benefit Assessment

The assessment is qualitative on purpose: no money changes hands, the work is
done by one person for learning, and the benefits are learning outcomes that
have no price.

| Costs | Benefits |
| --- | --- |
| The learner's time to write the game, the tests and the documents | A tested, documented reference program |
| Time spent on reviews | A worked example of the framework on a small project |
| No licence, hosting or tooling cost | Practice that carries to larger projects |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Product Owner, learner, reviewer and approver: wants a working, tested and documented game |

## Recommendation

Proceed — the narrowest first release is cheap, low risk and meets the learning
objectives.

---

[SA-001]: ./stakeholder-analysis.md
[d3c74f5]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/004-rock-paper-scissors-game/commit/d3c74f56d4214003f20c8c78a96173b793e43a56
