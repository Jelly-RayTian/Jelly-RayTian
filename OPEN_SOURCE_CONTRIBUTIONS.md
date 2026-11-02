# Open-source contributions

Complete record of pull requests authored by [`Jelly-RayTian`](https://github.com/Jelly-RayTian), checked against GitHub and upstream repositories. Live status last refreshed: <!-- GEN_DATE -->2026-11-02<!-- /GEN_DATE -->. Curated notes last verified: 2026-11-02.

Contents: [Statistics](#statistics) · [Status definitions](#status-definitions) · [Key acknowledgments](#key-acknowledgments) · [External contributions by repository](#external-contributions-by-repository) · [PRs in my own repositories](#pull-requests-in-my-own-repositories) · [How this was verified](#how-this-was-verified) · [Case studies](CASE_STUDIES.md)

> **AI assistance.** Most of these changes were developed with AI coding assistance (the PR descriptions say so). I direct the work, review the diffs, run the tests and answer maintainers; I do not claim every line was hand-written.

## Statistics

<!-- BEGIN GENERATED:summary -->
| Repository | PRs | Merged | Squashed onto main | Consolidated | Open | Draft | Closed, unverified |
|---|--:|--:|--:|--:|--:|--:|--:|
| [DaKheera47/job-ops](https://github.com/DaKheera47/job-ops) | 9 | 3 | 0 | 0 | 6 | 0 | 0 |
| [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | 23 | 10 | 0 | 0 | 13 | 0 | 0 |
| [willfaust/Madeira](https://github.com/willfaust/Madeira) | 14 | 4 | 3 | 5 | 1 | 1 | 0 |
| **External total** | **46** | **17** | **3** | **5** | **20** | **1** | **0** |

Pull requests in my own repositories (not counted above): **9** (8 merged, 1 closed unmerged, 0 open). All PRs authored by `Jelly-RayTian`: **55**.
<!-- END GENERATED:summary -->

"Squashed" and "consolidated" PRs are **not** counted as merged. Each is counted exactly once, under its own status; replacement PRs written by maintainers are not counted at all.

## Status definitions

| Status | Meaning | Evidence required |
|---|---|---|
| **Merged** | GitHub marks the PR merged. | `merged_at` set and merge commit reachable from the default branch (checked automatically). |
| **Closed, squashed onto main** | Closed without a merge flag; a maintainer squashed it onto main and said so. | Maintainer comment **and** a commit authored by me, reachable from main. Curated by hand. |
| **Closed, consolidated** | Closed because a maintainer folded it into a replacement PR; my authored commits are in main's history. | Maintainer comment **and** my commit SHAs verified as ancestors of main. Curated by hand. |
| **Retained in replacement (unproven)** | Maintainer says it was kept in a replacement PR, with no proof it reached main. | None. Currently 0 PRs. |
| **Open / Draft** | Under review or experimental. | None; no integration claimed. |
| **Closed, no verified integration** | Closed and nothing shows it landed. | Currently 0 PRs. |

A maintainer's thanks, or a PR simply being closed, is never treated as integration.

## Key acknowledgments

- **Madeira maintainer, #471 and #472:** "Squashed onto main as 16b3382b (your authorship and sign-off kept)" ([#471](https://github.com/willfaust/Madeira/pull/471#issuecomment-6461227579)); same for 0b4eee5a ([#472](https://github.com/willfaust/Madeira/pull/472#issuecomment-6461228278)).
- **Madeira maintainer, #473:** fix is on main as dab079b7 ([comment](https://github.com/willfaust/Madeira/pull/473#issuecomment-6567717620)).
- **Madeira maintainer, #456 and #465:** contributions folded into the integration PRs #462 and #461 with author history retained ([#456](https://github.com/willfaust/Madeira/pull/456#issuecomment-6454188199), [#465](https://github.com/willfaust/Madeira/pull/465#issuecomment-6459661572)).
- **Independent Madeira user, #451:** after the TaskbarList fix the affected game "no longer crashes at startup" ([comment](https://github.com/willfaust/Madeira/pull/451#issuecomment-6436633656)).
- **job-ops maintainer, #787–#789:** thanked after merging each ([#787](https://github.com/DaKheera47/job-ops/pull/787#issuecomment-6445299749), [#788](https://github.com/DaKheera47/job-ops/pull/788#issuecomment-6445283059), [#789](https://github.com/DaKheera47/job-ops/pull/789#issuecomment-6445274915)).
- PDFCraft: ten PRs merged by the maintainer organisation with no written comments.

## External contributions by repository

<!-- BEGIN GENERATED:external -->
### [DaKheera47/job-ops](https://github.com/DaKheera47/job-ops)

| PR | Title | Status | In upstream main |
|--:|---|---|---|
| [#787](https://github.com/DaKheera47/job-ops/pull/787) | fix(resume): retain semantic style metadata across import and export | Merged | Yes |
| [#788](https://github.com/DaKheera47/job-ops/pull/788) | fix(jobs): preserve local posting dates across timezones and DST | Merged | Yes |
| [#789](https://github.com/DaKheera47/job-ops/pull/789) | feat(manual-import): read job descriptions from text PDFs | Merged | Yes |
| [#791](https://github.com/DaKheera47/job-ops/pull/791) | feat: optional lean scoring and Claude CLI modes to reduce AI usage | Open | n/a |
| [#792](https://github.com/DaKheera47/job-ops/pull/792) | feat: add Simplified Chinese (zh-CN) interface language | Open | n/a |
| [#793](https://github.com/DaKheera47/job-ops/pull/793) | feat: add include/exclude keyword filters to the jobs list | Open | n/a |
| [#794](https://github.com/DaKheera47/job-ops/pull/794) | fix(llm): preserve fenced text and complete JSON response values | Open | n/a |
| [#795](https://github.com/DaKheera47/job-ops/pull/795) | feat(jobs): export filtered and selected jobs to CSV | Open | n/a |
| [#801](https://github.com/DaKheera47/job-ops/pull/801) | feat(settings): refresh model suggestions without changing selection | Open | n/a |

#### [DaKheera47/job-ops#787](https://github.com/DaKheera47/job-ops/pull/787): fix(resume): retain semantic style metadata across import and export

- **Description:** Preserves Reactive Resume v5.3 semantic style metadata (stylesheet, styleRules) across import, template merge and export, with validation of style targets and values.
- **GitHub status:** Merged on 2026-10-27; opened 2026-10-25; +208 / −1 in 6 files.
- **In upstream `main`:** Yes, the merge commit is reachable from `main` (checked via the compare API).
- **Maintainer / reviewer:** [Maintainer: "thanks for the contribution!"](https://github.com/DaKheera47/job-ops/pull/787#issuecomment-6445299749)
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [DaKheera47/job-ops#788](https://github.com/DaKheera47/job-ops/pull/788): fix(jobs): preserve local posting dates across timezones and DST

- **Description:** Parses date-only postings at local midnight and counts calendar days across DST so posting age, tooltip and sort are right in America/Toronto.
- **GitHub status:** Merged on 2026-10-27; opened 2026-10-27; +49 / −8 in 3 files.
- **In upstream `main`:** Yes, the merge commit is reachable from `main` (checked via the compare API).
- **Maintainer / reviewer:** [Maintainer: "nice! thanks for the contribution!"](https://github.com/DaKheera47/job-ops/pull/788#issuecomment-6445283059)
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [DaKheera47/job-ops#789](https://github.com/DaKheera47/job-ops/pull/789): feat(manual-import): read job descriptions from text PDFs

- **Description:** Manual Import accepts text PDFs: client-side PDF.js extraction with size/page/character limits, reviewed text sent through the existing analysis flow.
- **GitHub status:** Merged on 2026-10-27; opened 2026-10-27; +388 / −4 in 7 files.
- **In upstream `main`:** Yes, the merge commit is reachable from `main` (checked via the compare API).
- **Maintainer / reviewer:** [Maintainer: "good fix! thanks for the contribution!"](https://github.com/DaKheera47/job-ops/pull/789#issuecomment-6445274915)
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [DaKheera47/job-ops#791](https://github.com/DaKheera47/job-ops/pull/791): feat: optional lean scoring and Claude CLI modes to reduce AI usage

- **Description:** Optional lean scoring and Claude CLI modes to reduce AI usage.
- **GitHub status:** Open; opened 2026-10-27; +288 / −4 in 13 files.
- **In upstream main:** Not applicable (not merged or integrated).
- **Maintainer / reviewer:** No comment or review on the PR.
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [DaKheera47/job-ops#792](https://github.com/DaKheera47/job-ops/pull/792): feat: add Simplified Chinese (zh-CN) interface language

- **Description:** Adds a Simplified Chinese (zh-CN) interface language.
- **GitHub status:** Open; opened 2026-10-27; +3282 / −2183 in 84 files.
- **In upstream main:** Not applicable (not merged or integrated).
- **Maintainer / reviewer:** No comment or review on the PR.
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [DaKheera47/job-ops#793](https://github.com/DaKheera47/job-ops/pull/793): feat: add include/exclude keyword filters to the jobs list

- **Description:** Include/exclude keyword filters for the jobs list.
- **GitHub status:** Open; opened 2026-10-27; +243 / −0 in 13 files.
- **In upstream main:** Not applicable (not merged or integrated).
- **Maintainer / reviewer:** No comment or review on the PR.
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [DaKheera47/job-ops#794](https://github.com/DaKheera47/job-ops/pull/794): fix(llm): preserve fenced text and complete JSON response values

- **Description:** LLM responses: preserves fenced text and completes JSON response values.
- **GitHub status:** Open; opened 2026-10-27; +116 / −2 in 4 files.
- **In upstream main:** Not applicable (not merged or integrated).
- **Maintainer / reviewer:** No comment or review on the PR.
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [DaKheera47/job-ops#795](https://github.com/DaKheera47/job-ops/pull/795): feat(jobs): export filtered and selected jobs to CSV

- **Description:** Exports filtered and selected jobs to CSV.
- **GitHub status:** Open; opened 2026-10-28; +400 / −4 in 7 files.
- **In upstream main:** Not applicable (not merged or integrated).
- **Maintainer / reviewer:** No comment or review on the PR.
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [DaKheera47/job-ops#801](https://github.com/DaKheera47/job-ops/pull/801): feat(settings): refresh model suggestions without changing selection

- **Description:** _Not yet curated._
- **GitHub status:** Open; opened 2026-11-02; +187 / −2 in 3 files.
- **In upstream main:** Not applicable (not merged or integrated).
- **Maintainer / reviewer:** No comment or review on the PR.
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

### [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft)

| PR | Title | Status | In upstream main |
|--:|---|---|---|
| [#252](https://github.com/PDFCraftTool/pdfcraft/pull/252) | fix(studio): show, reorder and remove files before appending | Merged | Yes |
| [#253](https://github.com/PDFCraftTool/pdfcraft/pull/253) | fix(editor): select previous query when reopening find | Merged | Yes |
| [#254](https://github.com/PDFCraftTool/pdfcraft/pull/254) | fix(workflow): preserve literal values during token interpolation | Merged | Yes |
| [#255](https://github.com/PDFCraftTool/pdfcraft/pull/255) | fix(bookmarks): preserve subtree on descendant drop | Merged | Yes |
| [#257](https://github.com/PDFCraftTool/pdfcraft/pull/257) | fix(page-labels): preserve Unicode prefixes in saved PDFs | Merged | Yes |
| [#264](https://github.com/PDFCraftTool/pdfcraft/pull/264) | fix(page-labels): prevent oversized ranges from freezing preview and export | Merged | Yes |
| [#265](https://github.com/PDFCraftTool/pdfcraft/pull/265) | fix(pdf-to-zip): preserve documents with duplicate filenames | Merged | Yes |
| [#266](https://github.com/PDFCraftTool/pdfcraft/pull/266) | fix(rotate): retain editable forms, bookmarks and internal links | Merged | Yes |
| [#267](https://github.com/PDFCraftTool/pdfcraft/pull/267) | fix(bookmarks): retain destination position, zoom and fit mode | Merged | Yes |
| [#268](https://github.com/PDFCraftTool/pdfcraft/pull/268) | fix(metadata): preserve unedited fields and honor date opt-out | Merged | Yes |
| [#273](https://github.com/PDFCraftTool/pdfcraft/pull/273) | feat(reader): add remembered right-to-left spread order | Open | n/a |
| [#274](https://github.com/PDFCraftTool/pdfcraft/pull/274) | fix(editor): preserve object aspect ratio while Shift-resizing | Open | n/a |
| [#277](https://github.com/PDFCraftTool/pdfcraft/pull/277) | feat(bookmarks): move multi-selections across the outline tree | Open | n/a |
| [#278](https://github.com/PDFCraftTool/pdfcraft/pull/278) | test(editor): cover editing PDFs containing zero-width spaces | Open | n/a |
| [#280](https://github.com/PDFCraftTool/pdfcraft/pull/280) | fix(reverse): retain forms, bookmarks, links and metadata when reversing pages | Open | n/a |
| [#281](https://github.com/PDFCraftTool/pdfcraft/pull/281) | fix(add-blank-page): retain forms, bookmarks, links and metadata | Open | n/a |
| [#282](https://github.com/PDFCraftTool/pdfcraft/pull/282) | fix(remove-blank-pages): retain forms, bookmarks, links and metadata | Open | n/a |
| [#283](https://github.com/PDFCraftTool/pdfcraft/pull/283) | fix(background-color): retain forms, bookmarks, links and metadata | Open | n/a |
| [#284](https://github.com/PDFCraftTool/pdfcraft/pull/284) | fix(rotate-custom): retain forms, bookmarks, links and metadata for right-angle rotations | Open | n/a |
| [#285](https://github.com/PDFCraftTool/pdfcraft/pull/285) | fix: let page-embedding tools handle blank pages that have no content stream | Open | n/a |
| [#286](https://github.com/PDFCraftTool/pdfcraft/pull/286) | fix(organize): retain forms, bookmarks, links and metadata in the pdf-lib path | Open | n/a |
| [#287](https://github.com/PDFCraftTool/pdfcraft/pull/287) | fix(fix-page-size): honour the /Rotate of source pages | Open | n/a |
| [#288](https://github.com/PDFCraftTool/pdfcraft/pull/288) | fix(n-up): honour the /Rotate of source pages | Open | n/a |

#### [PDFCraftTool/pdfcraft#252](https://github.com/PDFCraftTool/pdfcraft/pull/252): fix(studio): show, reorder and remove files before appending

- **Description:** Studio: show, reorder and remove files before appending.
- **GitHub status:** Merged on 2026-10-27; opened 2026-10-25; +160 / −1 in 2 files.
- **In upstream `main`:** Yes, the merge commit is reachable from `main` (checked via the compare API).
- **Maintainer / reviewer:** No comment or review on the PR.
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [PDFCraftTool/pdfcraft#253](https://github.com/PDFCraftTool/pdfcraft/pull/253): fix(editor): select previous query when reopening find

- **Description:** Editor: reopening Find selects the previous query.
- **GitHub status:** Merged on 2026-10-27; opened 2026-10-25; +79 / −1 in 2 files.
- **In upstream `main`:** Yes, the merge commit is reachable from `main` (checked via the compare API).
- **Maintainer / reviewer:** No comment or review on the PR.
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [PDFCraftTool/pdfcraft#254](https://github.com/PDFCraftTool/pdfcraft/pull/254): fix(workflow): preserve literal values during token interpolation

- **Description:** Workflow filename interpolation keeps substituted values literal (e.g. $& and {date} inside a filename) using a single-pass token replacement.
- **GitHub status:** Merged on 2026-10-27; opened 2026-10-25; +53 / −10 in 3 files.
- **In upstream `main`:** Yes, the merge commit is reachable from `main` (checked via the compare API).
- **Maintainer / reviewer:** No comment or review on the PR.
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [PDFCraftTool/pdfcraft#255](https://github.com/PDFCraftTool/pdfcraft/pull/255): fix(bookmarks): preserve subtree on descendant drop

- **Description:** Bookmarks: dropping a node onto its own descendant preserves the subtree.
- **GitHub status:** Merged on 2026-10-27; opened 2026-10-25; +104 / −8 in 2 files.
- **In upstream `main`:** Yes, the merge commit is reachable from `main` (checked via the compare API).
- **Maintainer / reviewer:** No comment or review on the PR.
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [PDFCraftTool/pdfcraft#257](https://github.com/PDFCraftTool/pdfcraft/pull/257): fix(page-labels): preserve Unicode prefixes in saved PDFs

- **Description:** Page labels: writes prefixes as UTF-16 text strings so Chinese, Greek, Hebrew and emoji survive save and reload.
- **GitHub status:** Merged on 2026-10-27; opened 2026-10-26; +28 / −1 in 2 files.
- **In upstream `main`:** Yes, the merge commit is reachable from `main` (checked via the compare API).
- **Maintainer / reviewer:** No comment or review on the PR.
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [PDFCraftTool/pdfcraft#264](https://github.com/PDFCraftTool/pdfcraft/pull/264): fix(page-labels): prevent oversized ranges from freezing preview and export

- **Description:** Page labels: clips oversized ranges to the document and shares one parser so preview and export no longer freeze.
- **GitHub status:** Merged on 2026-10-29; opened 2026-10-27; +110 / −113 in 5 files.
- **In upstream `main`:** Yes, the merge commit is reachable from `main` (checked via the compare API).
- **Maintainer / reviewer:** No comment or review on the PR.
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [PDFCraftTool/pdfcraft#265](https://github.com/PDFCraftTool/pdfcraft/pull/265): fix(pdf-to-zip): preserve documents with duplicate filenames

- **Description:** PDF to ZIP: preserves documents with duplicate filenames.
- **GitHub status:** Merged on 2026-10-29; opened 2026-10-27; +84 / −3 in 3 files.
- **In upstream `main`:** Yes, the merge commit is reachable from `main` (checked via the compare API).
- **Maintainer / reviewer:** No comment or review on the PR.
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [PDFCraftTool/pdfcraft#266](https://github.com/PDFCraftTool/pdfcraft/pull/266): fix(rotate): retain editable forms, bookmarks and internal links

- **Description:** Rotate: updates page rotation in place for multiples of 90 degrees so forms, bookmarks, links, attachments and labels survive.
- **GitHub status:** Merged on 2026-10-30; opened 2026-10-28; +127 / −9 in 3 files.
- **In upstream `main`:** Yes, the merge commit is reachable from `main` (checked via the compare API).
- **Maintainer / reviewer:** No comment or review on the PR.
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [PDFCraftTool/pdfcraft#267](https://github.com/PDFCraftTool/pdfcraft/pull/267): fix(bookmarks): retain destination position, zoom and fit mode

- **Description:** Bookmarks: retains destination position, zoom and fit mode.
- **GitHub status:** Merged on 2026-10-29; opened 2026-10-28; +137 / −18 in 5 files.
- **In upstream `main`:** Yes, the merge commit is reachable from `main` (checked via the compare API).
- **Maintainer / reviewer:** No comment or review on the PR.
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [PDFCraftTool/pdfcraft#268](https://github.com/PDFCraftTool/pdfcraft/pull/268): fix(metadata): preserve unedited fields and honor date opt-out

- **Description:** Metadata: preserves unedited fields and honours the date opt-out.
- **GitHub status:** Merged on 2026-10-29; opened 2026-10-28; +67 / −1 in 3 files.
- **In upstream `main`:** Yes, the merge commit is reachable from `main` (checked via the compare API).
- **Maintainer / reviewer:** No comment or review on the PR.
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [PDFCraftTool/pdfcraft#273](https://github.com/PDFCraftTool/pdfcraft/pull/273): feat(reader): add remembered right-to-left spread order

- **Description:** Reader: remembered right-to-left spread order.
- **GitHub status:** Open; opened 2026-10-29; +183 / −1 in 7 files.
- **In upstream main:** Not applicable (not merged or integrated).
- **Maintainer / reviewer:** No comment or review on the PR.
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [PDFCraftTool/pdfcraft#274](https://github.com/PDFCraftTool/pdfcraft/pull/274): fix(editor): preserve object aspect ratio while Shift-resizing

- **Description:** Editor: preserves object aspect ratio while Shift-resizing.
- **GitHub status:** Open; opened 2026-10-29; +110 / −3 in 5 files.
- **In upstream main:** Not applicable (not merged or integrated).
- **Maintainer / reviewer:** No comment or review on the PR.
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [PDFCraftTool/pdfcraft#277](https://github.com/PDFCraftTool/pdfcraft/pull/277): feat(bookmarks): move multi-selections across the outline tree

- **Description:** Bookmarks: move multi-selections across the outline tree.
- **GitHub status:** Open; opened 2026-11-02; +290 / −86 in 6 files.
- **In upstream main:** Not applicable (not merged or integrated).
- **Maintainer / reviewer:** No comment or review on the PR.
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [PDFCraftTool/pdfcraft#278](https://github.com/PDFCraftTool/pdfcraft/pull/278): test(editor): cover editing PDFs containing zero-width spaces

- **Description:** Test: covers editing PDFs containing zero-width spaces.
- **GitHub status:** Open; opened 2026-11-02; +164 / −0 in 4 files.
- **In upstream main:** Not applicable (not merged or integrated).
- **Maintainer / reviewer:** No comment or review on the PR.
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [PDFCraftTool/pdfcraft#280](https://github.com/PDFCraftTool/pdfcraft/pull/280): fix(reverse): retain forms, bookmarks, links and metadata when reversing pages

- **Description:** _Not yet curated._
- **GitHub status:** Open; opened 2026-11-02; +91 / −13 in 2 files.
- **In upstream main:** Not applicable (not merged or integrated).
- **Maintainer / reviewer:** No comment or review on the PR.
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [PDFCraftTool/pdfcraft#281](https://github.com/PDFCraftTool/pdfcraft/pull/281): fix(add-blank-page): retain forms, bookmarks, links and metadata

- **Description:** _Not yet curated._
- **GitHub status:** Open; opened 2026-11-02; +85 / −26 in 2 files.
- **In upstream main:** Not applicable (not merged or integrated).
- **Maintainer / reviewer:** No comment or review on the PR.
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [PDFCraftTool/pdfcraft#282](https://github.com/PDFCraftTool/pdfcraft/pull/282): fix(remove-blank-pages): retain forms, bookmarks, links and metadata

- **Description:** _Not yet curated._
- **GitHub status:** Open; opened 2026-11-02; +92 / −5 in 2 files.
- **In upstream main:** Not applicable (not merged or integrated).
- **Maintainer / reviewer:** No comment or review on the PR.
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [PDFCraftTool/pdfcraft#283](https://github.com/PDFCraftTool/pdfcraft/pull/283): fix(background-color): retain forms, bookmarks, links and metadata

- **Description:** _Not yet curated._
- **GitHub status:** Open; opened 2026-11-02; +122 / −26 in 2 files.
- **In upstream main:** Not applicable (not merged or integrated).
- **Maintainer / reviewer:** No comment or review on the PR.
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [PDFCraftTool/pdfcraft#284](https://github.com/PDFCraftTool/pdfcraft/pull/284): fix(rotate-custom): retain forms, bookmarks, links and metadata for right-angle rotations

- **Description:** _Not yet curated._
- **GitHub status:** Open; opened 2026-11-02; +94 / −4 in 2 files.
- **In upstream main:** Not applicable (not merged or integrated).
- **Maintainer / reviewer:** No comment or review on the PR.
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [PDFCraftTool/pdfcraft#285](https://github.com/PDFCraftTool/pdfcraft/pull/285): fix: let page-embedding tools handle blank pages that have no content stream

- **Description:** _Not yet curated._
- **GitHub status:** Open; opened 2026-11-02; +108 / −9 in 12 files.
- **In upstream main:** Not applicable (not merged or integrated).
- **Maintainer / reviewer:** No comment or review on the PR.
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [PDFCraftTool/pdfcraft#286](https://github.com/PDFCraftTool/pdfcraft/pull/286): fix(organize): retain forms, bookmarks, links and metadata in the pdf-lib path

- **Description:** _Not yet curated._
- **GitHub status:** Open; opened 2026-11-02; +107 / −11 in 2 files.
- **In upstream main:** Not applicable (not merged or integrated).
- **Maintainer / reviewer:** No comment or review on the PR.
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [PDFCraftTool/pdfcraft#287](https://github.com/PDFCraftTool/pdfcraft/pull/287): fix(fix-page-size): honour the /Rotate of source pages

- **Description:** _Not yet curated._
- **GitHub status:** Open; opened 2026-11-02; +56 / −8 in 2 files.
- **In upstream main:** Not applicable (not merged or integrated).
- **Maintainer / reviewer:** No comment or review on the PR.
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [PDFCraftTool/pdfcraft#288](https://github.com/PDFCraftTool/pdfcraft/pull/288): fix(n-up): honour the /Rotate of source pages

- **Description:** _Not yet curated._
- **GitHub status:** Open; opened 2026-11-02; +67 / −8 in 2 files.
- **In upstream main:** Not applicable (not merged or integrated).
- **Maintainer / reviewer:** No comment or review on the PR.
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

### [willfaust/Madeira](https://github.com/willfaust/Madeira)

| PR | Title | Status | In upstream main |
|--:|---|---|---|
| [#396](https://github.com/willfaust/Madeira/pull/396) | ntdll: scope failed fixed-address relocation to the existing helper workaround | Closed, consolidated (commits in main history) | Yes |
| [#399](https://github.com/willfaust/Madeira/pull/399) | build: detect optional rusage diagnostic fields in the iOS SDK | Merged | Yes |
| [#400](https://github.com/willfaust/Madeira/pull/400) | vulkan: add an opt-in Windows x64 iOS route and reproduction fixtures | Closed, consolidated (commits in main history) | Yes |
| [#451](https://github.com/willfaust/Madeira/pull/451) | wine-pe: ship the registered TaskbarList COM server and add x64 activation coverage | Closed, consolidated (commits in main history) | Yes |
| [#456](https://github.com/willfaust/Madeira/pull/456) | vulkan: isolate the direct pipeline-cache export sizing fix and regression | Closed, consolidated (commits in main history) | Yes |
| [#458](https://github.com/willfaust/Madeira/pull/458) | docs: record Detroit iPad menu and interactive scene with screenshots | Merged | Yes |
| [#465](https://github.com/willfaust/Madeira/pull/465) | ntdll: decode UTF-8 launch folders before setting the Windows working directory | Closed, consolidated (commits in main history) | Yes |
| [#471](https://github.com/willfaust/Madeira/pull/471) | ntdll: reserve enough startup storage for long working directories | Closed, squashed onto main | Yes |
| [#472](https://github.com/willfaust/Madeira/pull/472) | steam: avoid automatic cloud transfers for unreadable local saves | Closed, squashed onto main | Yes |
| [#473](https://github.com/willfaust/Madeira/pull/473) | runtime: release task and copied values in entitlement checks | Closed, squashed onto main | Yes |
| [#486](https://github.com/willfaust/Madeira/pull/486) | steam: propagate local depot write errors without retrying healthy CDNs | Merged | Yes |
| [#501](https://github.com/willfaust/Madeira/pull/501) | move: log an original that cannot be removed after a verified copy | Merged | Yes |
| [#502](https://github.com/willfaust/Madeira/pull/502) | vulkan: expose the complete experimental source profile and reproduction artifacts | Draft / experimental | n/a |
| [#544](https://github.com/willfaust/Madeira/pull/544) | README: say how to add a game after installing | Open | n/a |

#### [willfaust/Madeira#396](https://github.com/willfaust/Madeira/pull/396): ntdll: scope failed fixed-address relocation to the existing helper workaround

- **Description:** Restricts failed fixed-address relocation in the iOS ntdll virtual-memory layer to the existing helper workaround; adds a regression fixture.
- **GitHub status:** Closed, consolidated (commits in main history) (closed 2026-10-27, GitHub does not mark it merged); opened 2026-10-20; +250 / −1 in 3 files.
- **In upstream `main`:** Yes, by curated evidence below; cited commits re-checked as reachable from `main`.
- **Maintainer / reviewer:** [Maintainer: covered by #447; fixed-address fix and regression tests retained, original commits and author details kept.](https://github.com/willfaust/Madeira/pull/396#issuecomment-6431649070)
- **Upstream commits:** [08bd6e0 (my commit, ancestor of main)](https://github.com/willfaust/Madeira/commit/08bd6e0bbaaeb678b37c0288c1ef4dfd97e7465d)
- **Replacement / consolidation:** [#447 (replacement, closed)](https://github.com/willfaust/Madeira/pull/447); [#461 (merged integration)](https://github.com/willfaust/Madeira/pull/461)
- **Note:** tests/x64/fixed-reserve.c is byte-identical on main; virtual_ios.c and the host check were edited later.
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [willfaust/Madeira#399](https://github.com/willfaust/Madeira/pull/399): build: detect optional rusage diagnostic fields in the iOS SDK

- **Description:** Detects optional rusage diagnostic fields in the iOS SDK so the build works across SDK versions.
- **GitHub status:** Merged on 2026-10-24; opened 2026-10-21; +121 / −1 in 4 files.
- **In upstream `main`:** Yes, the merge commit is reachable from `main` (checked via the compare API).
- **Maintainer / reviewer:** No comment or review on the PR.
- **Upstream commits:** [a24f19d on main](https://github.com/willfaust/Madeira/commit/a24f19d)
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [willfaust/Madeira#400](https://github.com/willfaust/Madeira/pull/400): vulkan: add an opt-in Windows x64 iOS route and reproduction fixtures

- **Description:** Opt-in Windows x64 Vulkan route for iOS (Wine Vulkan forwarding to MoltenVK via a retained CAMetalLayer), with enumerate, clear/readback and present fixtures and host checks.
- **GitHub status:** Closed, consolidated (commits in main history) (closed 2026-10-27, GitHub does not mark it merged); opened 2026-10-21; +1622 / −2 in 26 files.
- **In upstream `main`:** Yes, by curated evidence below; cited commits re-checked as reachable from `main`.
- **Maintainer / reviewer:** [Maintainer: work retained in #454 with source commits and author credit; #400 retained-layer surface lifetime and failure handling kept.](https://github.com/willfaust/Madeira/pull/400#issuecomment-6434402942); [Maintainer: combined failure and lifetime checks from #88 into this PR (4014c312).](https://github.com/willfaust/Madeira/pull/400#issuecomment-6430070567)
- **Upstream commits:** [ac746ed (my commit, ancestor of main)](https://github.com/willfaust/Madeira/commit/ac746eda2f6de26da0156d445d904331ff7b1429); [7860030 (my merge of main, ancestor of main)](https://github.com/willfaust/Madeira/commit/786003017bf63218399324e1c368b5493133e1a2); [7ed32a9 = #462 integration commit on main](https://github.com/willfaust/Madeira/commit/7ed32a9be9e0729525b80d6bc726cc3a844ffaad)
- **Replacement / consolidation:** [#454 (replacement, closed)](https://github.com/willfaust/Madeira/pull/454); [#462 (integration, closed; commit on main)](https://github.com/willfaust/Madeira/pull/462)
- **Note:** Ancestry and file presence on main verified (build/vulkan-ios/*, tests/host/check-vulkan-*.py, tests/x64/vulkan-*.c). I did not verify that every line of the original route is unchanged, nor that the route runs in the current main build.
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [willfaust/Madeira#451](https://github.com/willfaust/Madeira/pull/451): wine-pe: ship the registered TaskbarList COM server and add x64 activation coverage

- **Description:** Ships the registered TaskbarList COM server (explorerframe.dll) in the Wine PE package and adds x64 activation coverage; fixes a startup crash reported by a user.
- **GitHub status:** Closed, consolidated (commits in main history) (closed 2026-10-27, GitHub does not mark it merged); opened 2026-10-27; +209 / −1 in 6 files.
- **In upstream `main`:** Yes, by curated evidence below; cited commits re-checked as reachable from `main`.
- **Maintainer / reviewer:** [Maintainer: retained in #444 with source commits and author credit.](https://github.com/willfaust/Madeira/pull/451#issuecomment-6434410501); [Independent user (cx-game3601): with the explorerframe.dll stub, the affected game gets past TaskbarList activation and creates a window (a separate WebView2 issue remains).](https://github.com/willfaust/Madeira/pull/451#issuecomment-6436633656)
- **Upstream commits:** [a0cfe59 (my commit, ancestor of main)](https://github.com/willfaust/Madeira/commit/a0cfe594dc1533c96507e662502f976b2c0a7a47); [7ed32a9 = #462 integration commit on main](https://github.com/willfaust/Madeira/commit/7ed32a9be9e0729525b80d6bc726cc3a844ffaad)
- **Replacement / consolidation:** [#444 (replacement, closed)](https://github.com/willfaust/Madeira/pull/444)
- **Note:** explorerframe.dll, docs/TASKBARLIST.md, the host check and the x64 fixture are byte-identical on main. The device run in my own PR comment was on the original #451 package, not the integrated build.
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [willfaust/Madeira#456](https://github.com/willfaust/Madeira/pull/456): vulkan: isolate the direct pipeline-cache export sizing fix and regression

- **Description:** Isolated MoltenVK 1.4.2 backport so a direct vkGetPipelineCacheData call succeeds without a prior size query, plus a source-build helper and an x64/macOS Vulkan regression.
- **GitHub status:** Closed, consolidated (commits in main history) (closed 2026-10-27, GitHub does not mark it merged); opened 2026-10-27; +339 / −1 in 8 files.
- **In upstream `main`:** Yes, by curated evidence below; cited commits re-checked as reachable from `main`.
- **Maintainer / reviewer:** [Maintainer: included in #462; patch, helper and regression retained byte for byte; source head and author history remain.](https://github.com/willfaust/Madeira/pull/456#issuecomment-6454188199)
- **Upstream commits:** [2976e64 (my commit, ancestor of main)](https://github.com/willfaust/Madeira/commit/2976e6450520de092467f51cc5b796ea86ada046); [7ed32a9 = #462 integration commit on main](https://github.com/willfaust/Madeira/commit/7ed32a9be9e0729525b80d6bc726cc3a844ffaad)
- **Replacement / consolidation:** [#462 (integration, closed; commit on main)](https://github.com/willfaust/Madeira/pull/462)
- **Note:** All 8 files from my commit are byte-identical on main (verified by blob hash).
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [willfaust/Madeira#458](https://github.com/willfaust/Madeira/pull/458): docs: record Detroit iPad menu and interactive scene with screenshots

- **Description:** Documents Detroit: Become Human menu and interactive-scene observations on an experimental iPad build, with screenshots and explicit limits.
- **GitHub status:** Merged on 2026-10-28; opened 2026-10-27; +1889 / −15 in 27 files.
- **In upstream `main`:** Yes, the merge commit is reachable from `main` (checked via the compare API).
- **Maintainer / reviewer:** No comment or review on the PR.
- **Upstream commits:** [fed7f6a on main](https://github.com/willfaust/Madeira/commit/fed7f6a)
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [willfaust/Madeira#465](https://github.com/willfaust/Madeira/pull/465): ntdll: decode UTF-8 launch folders before setting the Windows working directory

- **Description:** Decodes the UTF-8 initial working directory before building its NT path (non-ASCII launch folders), with host regression and Windows probe.
- **GitHub status:** Closed, consolidated (commits in main history) (closed 2026-10-28, GitHub does not mark it merged); opened 2026-10-28; +195 / −11 in 4 files.
- **In upstream `main`:** Yes, by curated evidence below; cited commits re-checked as reachable from `main`.
- **Maintainer / reviewer:** [Maintainer: UTF-8 working-directory fix, host regression, Windows probe and documentation now included in #461; original commit retained in the merge history.](https://github.com/willfaust/Madeira/pull/465#issuecomment-6459661572)
- **Upstream commits:** [28ce806 (my commit, ancestor of main)](https://github.com/willfaust/Madeira/commit/28ce806af787222e65bb60e86c447ef04ace812e); [a9ce1d4 = #461 (merged) on main](https://github.com/willfaust/Madeira/commit/a9ce1d403b608108a141a260dccefe73cde940b4)
- **Replacement / consolidation:** [#461 (merged integration PR, not mine)](https://github.com/willfaust/Madeira/pull/461); [#462](https://github.com/willfaust/Madeira/pull/462)
- **Note:** Docs and fixture are byte-identical on main; env_ios.c was edited later (including by #471).
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [willfaust/Madeira#471](https://github.com/willfaust/Madeira/pull/471): ntdll: reserve enough startup storage for long working directories

- **Description:** Reserves enough startup storage for current directories of 260+ UTF-16 units so later strings no longer overwrite the directory; ASan/UBSan host reproduction (12/24 cases failed on base, 24/24 pass).
- **GitHub status:** Closed, squashed onto main (closed 2026-10-28, GitHub does not mark it merged); opened 2026-10-28; +205 / −10 in 3 files.
- **In upstream `main`:** Yes, by curated evidence below; cited commits re-checked as reachable from `main`.
- **Maintainer / reviewer:** [Maintainer: squashed onto main as 16b3382b, authorship and sign-off kept.](https://github.com/willfaust/Madeira/pull/471#issuecomment-6461227579)
- **Upstream commits:** [16b3382 (author: me, ancestor of main)](https://github.com/willfaust/Madeira/commit/16b3382b95c1f4500b4efcb00619483974a83f78)
- **Note:** Closed by hand because its branch history contained the #461 draft head.
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [willfaust/Madeira#472](https://github.com/willfaust/Madeira/pull/472): steam: avoid automatic cloud transfers for unreadable local saves

- **Description:** Stops Steam Cloud sync from treating an unreadable local save or incomplete checksum as proof of a local edit (no automatic upload; keeps it as a conflict); eight added cases.
- **GitHub status:** Closed, squashed onto main (closed 2026-10-28, GitHub does not mark it merged); opened 2026-10-28; +54 / −4 in 3 files.
- **In upstream `main`:** Yes, by curated evidence below; cited commits re-checked as reachable from `main`.
- **Maintainer / reviewer:** [Maintainer: squashed onto main as 0b4eee5a, authorship and sign-off kept.](https://github.com/willfaust/Madeira/pull/472#issuecomment-6461228278)
- **Upstream commits:** [0b4eee5 (author: me, ancestor of main)](https://github.com/willfaust/Madeira/commit/0b4eee5a6ca891b824c2f487438c347c780d5509)
- **Note:** Closed by hand for the same reason as #471.
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [willfaust/Madeira#473](https://github.com/willfaust/Madeira/pull/473): runtime: release task and copied values in entitlement checks

- **Description:** Balances Core Foundation ownership (task and copied values) in runtime entitlement checks.
- **GitHub status:** Closed, squashed onto main (closed 2026-11-02, GitHub does not mark it merged); opened 2026-10-28; +3947 / −64 in 62 files.
- **In upstream `main`:** Yes, by curated evidence below; cited commits re-checked as reachable from `main`.
- **Maintainer / reviewer:** [Maintainer: on main as dab079b7, part of wave 6 (c3279921); closed because stacked commits were already on main.](https://github.com/willfaust/Madeira/pull/473#issuecomment-6567717620)
- **Upstream commits:** [dab079b (author: me, ancestor of main)](https://github.com/willfaust/Madeira/commit/dab079b70bba7e2b37e3c7f7326130c503fb2ead)
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [willfaust/Madeira#486](https://github.com/willfaust/Madeira/pull/486): steam: propagate local depot write errors without retrying healthy CDNs

- **Description:** Propagates local depot write errors instead of retrying healthy CDNs in the Steam downloader.
- **GitHub status:** Merged on 2026-11-02; opened 2026-10-29; +147 / −4 in 2 files.
- **In upstream `main`:** Yes, the merge commit is reachable from `main` (checked via the compare API).
- **Maintainer / reviewer:** No comment or review on the PR.
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [willfaust/Madeira#501](https://github.com/willfaust/Madeira/pull/501): move: log an original that cannot be removed after a verified copy

- **Description:** Logs an original that cannot be removed after a verified copy during a move.
- **GitHub status:** Merged on 2026-11-02; opened 2026-10-31; +7 / −1 in 1 files.
- **In upstream `main`:** Yes, the merge commit is reachable from `main` (checked via the compare API).
- **Maintainer / reviewer:** No comment or review on the PR.
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [willfaust/Madeira#502](https://github.com/willfaust/Madeira/pull/502): vulkan: expose the complete experimental source profile and reproduction artifacts

- **Description:** Draft: exposes the complete experimental Vulkan source profile and reproduction artifacts (Detroit iPad investigation).
- **GitHub status:** Draft / experimental; opened 2026-10-31; +11728 / −0 in 50 files.
- **In upstream main:** Not applicable (not merged or integrated).
- **Maintainer / reviewer:** No comment or review on the PR.
- **Note:** Experimental draft; no integration claimed.
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

#### [willfaust/Madeira#544](https://github.com/willfaust/Madeira/pull/544): README: say how to add a game after installing

- **Description:** _Not yet curated._
- **GitHub status:** Open; opened 2026-11-02; +5 / −0 in 1 files.
- **In upstream main:** Not applicable (not merged or integrated).
- **Maintainer / reviewer:** No comment or review on the PR.
- **Last verified:** 2026-11-02 (curated notes) / 2026-11-02 (live status)

<!-- END GENERATED:external -->

## Pull requests in my own repositories

These are not external contributions and are excluded from the statistics above.

<!-- BEGIN GENERATED:own -->
| Repository | PR | Title | Status |
|---|--:|---|---|
| Jelly-RayTian/Chronicle | [#1](https://github.com/Jelly-RayTian/Chronicle/pull/1) | [codex] Add Milestone 1 folder management and metadata scanning | Merged 2026-07-07 |
| Jelly-RayTian/CodeCompass | [#1](https://github.com/Jelly-RayTian/CodeCompass/pull/1) | Release hardening for v1.0.2 | Merged 2026-07-27 |
| Jelly-RayTian/WatDesk | [#1](https://github.com/Jelly-RayTian/WatDesk/pull/1) | Fix automatic sync opening Learn, Crowdmark and Odyssey tabs | Merged 2026-10-27 |
| Jelly-RayTian/WatDesk | [#2](https://github.com/Jelly-RayTian/WatDesk/pull/2) | Add optional Möbius settings sync and LEARN Module Quiz schedules | Closed, no verified integration |
| Jelly-RayTian/WatDesk | [#3](https://github.com/Jelly-RayTian/WatDesk/pull/3) | WatDesk 1.3: reliable academic sync and a redesigned workspace | Merged 2026-10-27 |
| Jelly-RayTian/WatDesk | [#14](https://github.com/Jelly-RayTian/WatDesk/pull/14) | feat: continue setup with one source, add two-week workload view | Merged 2026-10-29 |
| Jelly-RayTian/WatDesk | [#15](https://github.com/Jelly-RayTian/WatDesk/pull/15) | fix: stop reporting duplicate exam listings as conflicts; add course filter to exams | Merged 2026-10-29 |
| Jelly-RayTian/WatDesk | [#16](https://github.com/Jelly-RayTian/WatDesk/pull/16) | feat: Liquid Glass design, designed pickers, searchable time zones, optional course websites | Merged 2026-10-29 |
| Jelly-RayTian/WatDesk | [#17](https://github.com/Jelly-RayTian/WatDesk/pull/17) | feat: WatDesk 1.9.0 usage counting and bilingual documentation | Merged 2026-10-29 |
<!-- END GENERATED:own -->

## How this was verified

- PR list: GitHub search `author:Jelly-RayTian type:pr` (paginated), then `GET /repos/{repo}/pulls/{n}` for each. No cached numbers.
- Merged PRs: merge commit checked as reachable from the default branch with the compare API.
- Squashed / consolidated PRs: maintainer comments read in full; commit SHAs checked as ancestors of Madeira `main` (blobless clone, `git merge-base --is-ancestor`), and the files my commits introduced checked for presence on main. For #396, #451, #456 and #465 some or all files are byte-identical on main; others were later edited, so these entries say "commits in history", not "unchanged".
- Test results quoted in case studies are what each PR description *reports*; they are not independent upstream validation unless stated.
- Refresh: `python3 scripts/update_stats.py`, or the scheduled workflow (see [MAINTAINING.md](MAINTAINING.md)).
