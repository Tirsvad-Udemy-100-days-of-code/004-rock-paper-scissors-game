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
| 2026-11-15 | Deprecated | Claude (AI assistant) | S01 | Initial version; accepted after RC-011 (Go) | [4f0682a] |
| 2026-11-15 | Accepted | Claude (AI assistant) | S01 | Added Danish and Malay editions to the deliverable and a translation task, at S01's request; accepted after RC-014 (Go) | pending |

---

## Purpose

Decides whether the project's wiki gives a newcomer a map of the game, how to install and play it, how it is built and where the project documents are, and whether it is published on the git host.

## Deliverable

The wiki in `docs/wiki/` (flat folder): the pages `Home`, `Install`, `Play`, `Architecture` and `Project-Documents`, each in English, Danish and Malay, and `_Sidebar`, in English, Danish (`-da`) and Malay (`-ms`), reviewed against `QC-WIKI-001` with an `RC-*` record and checked on the published wiki after the merge.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `docs/wiki/` holds the five pages in three languages and `_Sidebar.md` directly, with no subfolder | All sixteen files are in the folder | A file is missing or in a subfolder |
| 2 | The sidebar lists every English page once, with `Home` first, has a `Languages` section with English, Danish and Malay last, and every link resolves | Every link in `_Sidebar.md` and the pages points to an existing page | A page is missing from the sidebar or a link is dead |
| 3 | Every command and file name in the pages is real, and every language has the same pages | The commands run, the files exist and the page sets are identical | A command fails, a file does not exist or a page is missing in a language |
| 4 | The wiki review against `QC-WIKI-001` has verdict `Go` | An `RC-*` with `Go` | Any Mandatory criterion fails |
| 5 | The published wiki shows the sidebar and the pages in all three languages | The host's wiki pages return content after the merge | A page does not load |

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
| 3 | Translate the wiki into Danish and Malay | Write `-da` and `-ms` editions of the five pages, add the language line to every page and the two languages to the sidebar, so the wiki also reads in the languages S01 asked for. | No | |
| 4 | Review the wiki against QC-WIKI-001 | Review the pages and sidebar against the wiki checklist and record an `RC-*`, so the wiki is reviewed like any other change. | No | |
| 5 | Publish the wiki and check it | Merge the pages so the host publishes them, then check the sidebar, every page and every link on the published wiki (criterion 14 of the wiki checklist). | No | |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[MIL-002]: ./mil-002-first-release.md
[4f0682a]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/004-rock-paper-scissors-game/commit/4f0682a2233d43d9da078d6dfcecf3cfcb2a1c84
