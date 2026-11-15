# Review of the wiki

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-013 |
| CrossReference | [QC-LANG-001], [QC-WIKI-001], [MIL-003] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Proposed | Claude (AI assistant) | S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: the wiki in `docs/wiki/` (`Home`, `Install`, `Play`, `Architecture`, `Project-Documents`, `_Sidebar`), task 3 of [MIL-003]
- Checklist used: [QC-WIKI-001]
- Scope: full review; the language rules of [QC-LANG-001] are applied to the pages where they apply (a wiki page has no Metadata table)
- Language and domain: en / it
- Language reviewer: none (S01 reads the language and knows the domain)
- Mode: autonomous, not independent (the AI assistant ran the checklist; S01 is the reviewer and accepted the wiki plan in chat on 2026-11-15)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The wiki has a `_Sidebar.md`, because the host lists subpages only through it (Mandatory) | Pass | `docs/wiki/_Sidebar.md` exists. |
| 2 | The sidebar starts with the wiki's title in bold, then one list of the pages in the primary language (English), `Home` first (Mandatory) | Pass | The sidebar starts with the bold title `Rock Paper Scissors Game`, then one list of the English pages with `Home` first. |
| 3 | The page list holds a link to every English page of the wiki, and no link points to a page that does not exist (Mandatory) | Pass | The list links `Home`, `Install`, `Play`, `Architecture` and `Project-Documents`, which are all five pages; a link check of every wiki link found no dead one. |
| 4 | A `**Related**` section follows the page list only when the wiki has related wikis (for example the checklists wiki for a framework wiki); each entry is a link to that wiki's Home. A wiki with nothing related has no such section (Mandatory) | Pass | The wiki has no related wiki, so the sidebar has no `Related` section. |
| 5 | A `**Languages**` section is the last section of the sidebar. It has one line per language, the language written in that language, linking to that language's `Home` page (Mandatory) | Pass | `**Languages**` is the last section with one line: `English: [Home](Home)`. |
| 6 | The sidebar does not repeat the page list per language (Mandatory) | Pass | The page list appears once. |
| 7 | A sidebar produced by a generator carries a comment that says so and names the generator; the generator is changed, not the page (Mandatory) | N-A | The sidebar is written by hand, not by a generator. |
| 8 | The wiki has a `Languages` line on each page (criterion 11), so the sidebar is not the only way to switch language (Optional) | Pass | Every page has the language line. |
| 9 | Every wiki exists in English and, as a minimum, in the language the project's registry names as the PO language; further languages are added on top, never instead of English (Mandatory) | Pass | The wiki is in English; the PO language in the registry is `en`, so English alone meets the minimum. |
| 10 | Every English page has a page in each other language of the wiki: the page sets are identical (Mandatory) | Pass | There is one language, so the page sets are identical. |
| 11 | Every page starts with the language line, with the current language in bold and a link to the same page in each other language (Mandatory) | Pass | Every page starts with `**English**`; there is no other language to link to. |
| 12 | A page in a language other than English is named `<Page>-<code>.md`, with a BCP 47 code; English has no suffix (Mandatory) | Pass | The pages have no language suffix, as English requires. |
| 13 | Code blocks, commands, file names and IDs stay in English in every language (Mandatory) | Pass | Commands, file names and IDs are English and match the repository. |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change, not only in the repository (Mandatory) | Pending | The wiki can only be checked on the host after the merge publishes it; task 4 of [MIL-003] does that, and a delta review closes this criterion. |
| 15 | A change to the layout rules (sections, order, naming) is made in the generator or template and in this checklist's source rules together (Optional) | N-A | No layout rule of the framework is changed. |
| 16 | The wiki folder (`docs/wiki/`) is flat: every page, `Home.md` and `_Sidebar.md` included, is directly in it, and languages are told apart by file name, never by a subfolder (Mandatory) | Pass | All six files are directly in `docs/wiki/`; there is no subfolder. |

## Language and Domain Results

Checklist used: [QC-LANG-001].

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder (Mandatory) | N-A | Wiki pages are not artifacts and have no Metadata table. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list (Mandatory) | N-A | Wiki pages have no `Language` or `Domain` row; the language is English and the PO language is `en`. |
| 3 | The content (prose and table cells) is written in the stated language (Mandatory) | Pass | All prose and table cells are English. AI proposal, confirmed by S01 when accepting the wiki plan in chat on 2026-11-15. |
| 4 | The register matches the one the registry gives for the artifact type (Mandatory) | Pass | Written for a newcomer in plain IT Professional English. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms (Mandatory) | Pass | Terms match the project documents (gateway, use case layer names). No dictionary exists yet. AI proposal, confirmed by S01 when accepting the wiki plan in chat on 2026-11-15. |
| 6 | Metadata keys, section headings, IDs and statuses are in English (Mandatory) | N-A | Wiki pages have no Metadata keys; file names are English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document (Mandatory) | Pass | No translated twin exists. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again (Mandatory) | N-A | The wiki is new; no language change. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly (Mandatory) | Pass | Domain terms are used correctly. AI proposal, confirmed by S01 when accepting the wiki plan in chat on 2026-11-15. |
| 10 | Abbreviations are spelled out on first use, in the stated language (Optional) | Pass | SQA and QC are spelled out on first use on `Home`; other abbreviations are standard. |

## Overall Verdict

Go-with-conditions: every Mandatory criterion of [QC-WIKI-001] passes except criterion 14, which is Pending because the published wiki can only be checked after the merge. The pages have no dead link in the repository. When the published wiki is checked and criterion 14 passes, a delta review gives Go.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| After the merge, check the sidebar, every page and every link on the published wiki, and record a delta review of criterion 14 | S01 | 2026-11-16 |

---

[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
[MIL-003]: ../../milestones/mil-003-wiki.md
