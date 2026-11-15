# MIL-003 Wiki

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Accepted | Claude (AI assistant) | S01 | Initial version; accepted after RC-011 (Go) | [4f0682a] |

---

## Purpose

Decides whether the project's wiki gives a newcomer a map of the game, how to install and play it, how it is built and where the project documents are, and whether it is published on the git host.

## Deliverable

The wiki in `docs/wiki/` (flat folder): `Home`, `Install`, `Play`, `Architecture`, `Project-Documents` and `_Sidebar`, in English only because the PO language is `en`, reviewed against `QC-WIKI-001` with an `RC-*` record and checked on the published wiki after the merge.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `docs/wiki/` holds the five pages and `_Sidebar.md` directly, with no subfolder | All six files are in the folder | A file is missing or in a subfolder |
| 2 | The sidebar lists every page once, with `Home` first, and every link resolves | Every link in `_Sidebar.md` and the pages points to an existing page | A page is missing from the sidebar or a link is dead |
| 3 | Every command and file name in the pages is real | The commands run and the files exist | A command fails or a file does not exist |
| 4 | The wiki review against `QC-WIKI-001` has verdict `Go` | An `RC-*` with `Go` | Any Mandatory criterion fails |
| 5 | The published wiki shows the sidebar and the pages | The host's wiki pages return content after the merge | A page does not load |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-002] | The wiki describes the delivered game, its layers and its commands |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 5: keep the project's documents consistent with the framework; scope item "the project documents the framework requires" | [BC-001] |

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
| 1 | Write the English wiki pages | Write `Home`, `Install`, `Play`, `Architecture` and `Project-Documents` in `docs/wiki/` from the README, the code layers and the project documents, so a newcomer can install, play and understand the game. | No | |
| 2 | Write the wiki sidebar | Write `_Sidebar.md` as the map of the wiki: the title in bold, one list of the pages with `Home` first, and a `Languages` section last, as `framework/process/wiki.md` requires. | No | |
| 3 | Review the wiki against QC-WIKI-001 | Review the pages and sidebar against the wiki checklist and record an `RC-*`, so the wiki is reviewed like any other change. | No | |
| 4 | Publish the wiki and check it | Merge the pages so the host publishes them, then check the sidebar, every page and every link on the published wiki (criterion 14 of the wiki checklist). | No | |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[MIL-002]: ./mil-002-first-release.md
[4f0682a]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/004-rock-paper-scissors-game/commit/4f0682a2233d43d9da078d6dfcecf3cfcb2a1c84
