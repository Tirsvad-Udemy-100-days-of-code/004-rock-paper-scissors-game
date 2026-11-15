# Second review of the wiki

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-016 |
| CrossReference | [QC-LANG-001], [QC-WIKI-001], [MIL-003], [RC-013] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Accepted | Claude (AI assistant) | S01 | Initial version; accepted on S01's instruction in chat, 2026-11-15 | [974b467] |

---

## Artifact Under Review

- Instance reviewed: the wiki in `docs/wiki/`: five pages in English, Danish and Malay, and `_Sidebar` (task 4 of [MIL-003])
- Checklist used: [QC-WIKI-001]
- Scope: full second review after the Danish and Malay editions; earlier record [RC-013]
- Language and domain: en / it (the artifact's Metadata rows)
- Language reviewer: none named yet
- Mode: autonomous, not independent (the AI assistant ran the checklist; S01 is the reviewer and accepted the plan change in chat on 2026-11-15, but has not confirmed the Danish or Malay text)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The wiki has a `_Sidebar.md`, because the host lists subpages only through it (Mandatory) | Pass | `_Sidebar.md` exists. |
| 2 | The sidebar starts with the wiki's title in bold, then one list of the pages in the primary language (English), `Home` first (Mandatory) | Pass | Title in bold, then one list of the five English pages with `Home` first. |
| 3 | The page list holds a link to every English page of the wiki, and no link points to a page that does not exist (Mandatory) | Pass | The list links all five English pages; a link check of every wiki link found no dead one. |
| 4 | A `**Related**` section follows the page list only when the wiki has related wikis (for example the checklists wiki for a framework wiki); each entry is a link to that wiki's Home. A wiki with nothing related has no such section (Mandatory) | Pass | No related wiki, so no `Related` section. |
| 5 | A `**Languages**` section is the last section of the sidebar. It has one line per language, the language written in that language, linking to that language's `Home` page (Mandatory) | Pass | `**Languages**` is last, with `English: [Home](Home)`, `Dansk: [Hjem](Home-da)` and `Bahasa Melayu: [Utama](Home-ms)`. |
| 6 | The sidebar does not repeat the page list per language (Mandatory) | Pass | The page list appears once. |
| 7 | A sidebar produced by a generator carries a comment that says so and names the generator; the generator is changed, not the page (Mandatory) | N-A | The sidebar is written by hand. |
| 8 | The wiki has a `Languages` line on each page (criterion 11), so the sidebar is not the only way to switch language (Optional) | Pass | Every page has the language line. |
| 9 | Every wiki exists in English and, as a minimum, in the language the project's registry names as the PO language; further languages are added on top, never instead of English (Mandatory) | Pass | English plus Danish and Malay; the PO language `en` is met. |
| 10 | Every English page has a page in each other language of the wiki: the page sets are identical (Mandatory) | Pass | Each language has the same five pages: 5 English, 5 `-da`, 5 `-ms`. |
| 11 | Every page starts with the language line, with the current language in bold and a link to the same page in each other language (Mandatory) | Pass | Every page starts with the language line, the current language in bold and links to the same page in the other two. |
| 12 | A page in a language other than English is named `<Page>-<code>.md`, with a BCP 47 code; English has no suffix (Mandatory) | Pass | `-da` and `-ms` are BCP 47 codes; English has no suffix. |
| 13 | Code blocks, commands, file names and IDs stay in English in every language (Mandatory) | Pass | Code blocks, commands, file names and IDs are English in every language. |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change, not only in the repository (Mandatory) | Pending | Only checkable on the published wiki after the merge; task 5 of [MIL-003] does that. |
| 15 | A change to the layout rules (sections, order, naming) is made in the generator or template and in this checklist's source rules together (Optional) | N-A | No layout rule of the framework is changed. |
| 16 | The wiki folder (`docs/wiki/`) is flat: every page, `Home.md` and `_Sidebar.md` included, is directly in it, and languages are told apart by file name, never by a subfolder (Mandatory) | Pass | All sixteen files are directly in `docs/wiki/`; languages are told apart by file name. |

## Language and Domain Results

Checklist used: [QC-LANG-001].

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder (Mandatory) | N-A | Wiki pages are not artifacts and have no Metadata table. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list (Mandatory) | N-A | Wiki pages have no `Language` or `Domain` row; the languages are in the file names. |
| 3 | The content (prose and table cells) is written in the stated language (Mandatory) | Pending | All prose and table cells are in the language of the edition. AI proposal for the Danish and the Malay edition; only a reader of the language can confirm it, and S01 has not yet. |
| 4 | The register matches the one the registry gives for the artifact type (Mandatory) | Pass | Written for a newcomer in plain IT Professional language. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms (Mandatory) | Pending | Terms follow the English pages and common Danish and Malay IT usage. No dictionary exists yet. AI proposal for the Danish and the Malay edition; only a reader of the language can confirm it, and S01 has not yet. |
| 6 | Metadata keys, section headings, IDs and statuses are in English (Mandatory) | N-A | Wiki pages have no Metadata keys; file names and code are English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document (Mandatory) | Pass | No translated twin exists beside the pages. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again (Mandatory) | N-A | The editions are new. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly (Mandatory) | Pending | A reader competent in the language and the domain must confirm the terms. AI proposal for the Danish and the Malay edition; only a reader of the language can confirm it, and S01 has not yet. |
| 10 | Abbreviations are spelled out on first use, in the stated language (Optional) | Pass | SQA and QC are spelled out on first use on `Home` in each edition. |

## Overall Verdict

Go-with-conditions: every Mandatory criterion of [QC-WIKI-001] passes except criterion 14 (published check, Pending), and Language and Domain criteria 3, 5 and 9 are Pending for the Danish and Malay editions because only a reader of each language can confirm them. The pages have no dead link in the repository. The wiki becomes Go when the published wiki is checked and the language criteria are confirmed.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| S01 confirms Language and Domain criteria 3, 5 and 9 for the Danish edition | S01 | 2026-11-22 |
| S01 confirms the same criteria for the Malay edition, or names a language reviewer who reads Malay (added to the Stakeholder Analysis) | S01 | 2026-11-22 |
| After the merge, check the sidebar, every page in the three languages and every link on the published wiki, and record a delta review of criterion 14 | S01 | 2026-11-16 |

---

[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
[MIL-003]: ../../milestones/mil-003-wiki.md
[RC-013]: ./rc-013-wiki-first-review.md
[974b467]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/004-rock-paper-scissors-game/commit/974b46770f865529c2f2d8808e7e6e97b4ccbc66
