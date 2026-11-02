# Case studies

Hand-written and **never edited by the automation**. Status of every PR: [OPEN_SOURCE_CONTRIBUTIONS.md](OPEN_SOURCE_CONTRIBUTIONS.md). Last reviewed 2026-11-02.

Two kinds of evidence are kept apart throughout:

- **PR-reported validation:** tests and runs described in my own PR description. Useful, but self-reported.
- **Upstream outcome:** what the maintainer did (merged, squashed, consolidated, commented). This shows acceptance, not that the tests were independently re-run.

Most of this work was AI-assisted (stated in the PRs); I scoped the bugs, reviewed the diffs and ran or checked the tests.

---

## 1. Madeira: runtime and graphics fixes on iOS (C, Swift)

[willfaust/Madeira](https://github.com/willfaust/Madeira) runs Windows x64 games on iOS using FEX-Emu, Wine and DXMT. 13 PRs: 4 merged, 3 squashed onto `main`, 5 consolidated, 1 experimental draft.

### Startup buffer overwrite with long working directories ([#471](https://github.com/willfaust/Madeira/pull/471))
- **Problem:** a current directory of 260 or more UTF-16 units was copied into a slot sized for `MAX_PATH`; packing the next strings overwrote it.
- **Approach:** reserve `max(MAX_PATH·sizeof(WCHAR), actual bytes incl. NUL)` in both the initial and the child-process startup paths and report that capacity in `DosPath.MaximumLength`. Short paths keep the original size.
- **PR-reported validation:** a host reproduction compiles the real allocation and packing expressions under ASan/UBSan. The unchanged base fails 12 of 24 cases (including five buffer overflows); the patch passes 24/24. The modified file compiles for iOS arm64. The PR states that no device or gameplay run was performed and that a log-redaction test already failed before the change.
- **Upstream outcome:** maintainer squashed it onto `main` as `16b3382b`, keeping my authorship and sign-off.
- **Evidence:** [PR](https://github.com/willfaust/Madeira/pull/471) · [maintainer comment](https://github.com/willfaust/Madeira/pull/471#issuecomment-6461227579) · [commit 16b3382](https://github.com/willfaust/Madeira/commit/16b3382b95c1f4500b4efcb00619483974a83f78)

### Steam Cloud sync and unreadable saves ([#472](https://github.com/willfaust/Madeira/pull/472))
- **Problem:** a thrown file-read was treated like EOF, so a partial digest looked like a local edit and could schedule an automatic transfer.
- **Approach:** return no checksum on read errors, and keep a differing pair without a complete local checksum as a conflict.
- **PR-reported validation:** the existing suite plus eight added cases; two of them fail before the fix. Host-level only; no signed-in Steam transfer.
- **Upstream outcome:** squashed onto `main` as `0b4eee5a`.
- **Evidence:** [PR](https://github.com/willfaust/Madeira/pull/472) · [comment](https://github.com/willfaust/Madeira/pull/472#issuecomment-6461228278) · [commit 0b4eee5](https://github.com/willfaust/Madeira/commit/0b4eee5a6ca891b824c2f487438c347c780d5509)

### MoltenVK pipeline-cache export ([#456](https://github.com/willfaust/Madeira/pull/456)) and the opt-in Vulkan route ([#400](https://github.com/willfaust/Madeira/pull/400))
- **Problem:** in the pinned MoltenVK 1.4.2, `vkGetPipelineCacheData` returned `VK_INCOMPLETE` with zero bytes unless a NULL-size query came first, which the Vulkan spec does not require. Separately, Madeira had no Vulkan path for Windows x64 programs.
- **Approach:** #456 moves the existing size calculation ahead of both export branches (one-file patch to MoltenVK), adds a pinned source-build helper and a Windows x64/macOS regression. #400 adds an opt-in build route from Wine's Vulkan layer to MoltenVK with a retained `CAMetalLayer`, plus enumerate, clear/readback and present fixtures.
- **PR-reported validation:** #456 on an Apple M1 Pro: with the fix reverted, empty and populated caches return `VK_INCOMPLETE`/0 bytes; with only the fix, `VK_SUCCESS`/36 and 750 bytes. This exercises MoltenVK and Metal, not iOS or gameplay. #400 reports host checks, compile checks, and earlier broader experimental builds on an M5 iPad (GPU enumeration, 1024-byte readback verified, visible RGB rounds); it states that those builds contained extra changes and do not prove the reduced branch runs a game.
- **Upstream outcome:** both PRs were closed into maintainer integration PRs. My commits `2976e64` (#456) and `ac746ed` (#400) are ancestors of `main`; all eight files from #456 are byte-identical on `main`. The integration commit `7ed32a9` (#462) is on `main`. Not counted as merged.
- **Evidence:** [#456 comment](https://github.com/willfaust/Madeira/pull/456#issuecomment-6454188199) · [#400 comment](https://github.com/willfaust/Madeira/pull/400#issuecomment-6434402942) · [2976e64](https://github.com/willfaust/Madeira/commit/2976e6450520de092467f51cc5b796ea86ada046) · [ac746ed](https://github.com/willfaust/Madeira/commit/ac746eda2f6de26da0156d445d904331ff7b1429) · [7ed32a9](https://github.com/willfaust/Madeira/commit/7ed32a9be9e0729525b80d6bc726cc3a844ffaad)

### TaskbarList startup crash ([#451](https://github.com/willfaust/Madeira/pull/451))
- **Problem:** a game crashed at startup because the TaskbarList COM server was not shipped.
- **Approach:** package the registered `explorerframe.dll` server and add an x64 activation fixture.
- **PR-reported validation:** a run on a real iPad of the original #451 package (CoCreateInstance, HrInit and QueryInterface returned `S_OK`, fixture `failed=0`). The PR says this does not validate the later integrated build.
- **Independent feedback:** a user with an iPad reported the affected game then got past TaskbarList activation and created a window; a separate WebView2 requirement remained.
- **Upstream outcome:** consolidated into #444; commit `a0cfe59` is an ancestor of `main`, and the DLL, fixture and doc are byte-identical on `main`.
- **Evidence:** [user comment](https://github.com/willfaust/Madeira/pull/451#issuecomment-6436633656) · [maintainer comment](https://github.com/willfaust/Madeira/pull/451#issuecomment-6434410501) · [a0cfe59](https://github.com/willfaust/Madeira/commit/a0cfe594dc1533c96507e662502f976b2c0a7a47)

Also merged: [#399](https://github.com/willfaust/Madeira/pull/399) (SDK-portable rusage detection), [#458](https://github.com/willfaust/Madeira/pull/458) (documented compatibility observations with limits stated), [#486](https://github.com/willfaust/Madeira/pull/486) and [#501](https://github.com/willfaust/Madeira/pull/501).

---

## 2. PDFCraft: document-integrity fixes (TypeScript)

[PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) is a browser-based PDF toolkit. 14 PRs: 10 merged, 4 open.

### Rotate no longer drops forms, bookmarks and links ([#266](https://github.com/PDFCraftTool/pdfcraft/pull/266))
- **Problem:** rotating copied pages into a new document, so even a 0° rotation lost the form registry, outlines, page labels and attachments, and internal links pointed at pages absent from the output tree.
- **Approach:** when every resulting rotation is a multiple of 90°, update page rotation entries and save the original document; arbitrary angles keep the old embedding path.
- **PR-reported validation:** 11 regression cases fail on the original code; 12 real save/reload tests pass (editable form values, resolving links, attachment bytes, labels, rotation edge cases). Full suite 779 passed with 3 failing locale-catalog tests that also fail on the base commit. No production or native-reader run.
- **Upstream outcome:** merged by the maintainer organisation (no written review).
- **Evidence:** [PR #266](https://github.com/PDFCraftTool/pdfcraft/pull/266)

### Page labels: Unicode prefixes and a main-thread freeze ([#257](https://github.com/PDFCraftTool/pdfcraft/pull/257), [#264](https://github.com/PDFCraftTool/pdfcraft/pull/264))
- **Problem:** prefixes such as `章节-` were saved as mojibake because `PDFString.of` does not encode Unicode; a range like `1-100000000000000000000` made preview and export iterate beyond the document and block indefinitely.
- **Approach:** write prefixes with `PDFHexString.fromText` (UTF-16); clip range endpoints to the document and share one parser between preview and export.
- **PR-reported validation:** #257 adds five real-PDF round trips (four fail before the fix). #264 reproduces both parsers blocking past a two-second timeout and adds 23 focused tests including a save/reload check.
- **Upstream outcome:** both merged.
- **Evidence:** [#257](https://github.com/PDFCraftTool/pdfcraft/pull/257) · [#264](https://github.com/PDFCraftTool/pdfcraft/pull/264)

### Workflow filenames stay literal ([#254](https://github.com/PDFCraftTool/pdfcraft/pull/254))
- **Problem:** `budget_$&_{date}.pdf` was re-expanded during interpolation, corrupting the exported name.
- **Approach:** one case-insensitive, callback-based replacement pass.
- **PR-reported validation:** eight of nine new cases fail before the fix; a real `executeNode` regression checks the download filename and Blob.
- **Upstream outcome:** merged.
- **Evidence:** [PR #254](https://github.com/PDFCraftTool/pdfcraft/pull/254)

---

## 3. job-ops: timezone, parsing and import fixes (TypeScript)

[DaKheera47/job-ops](https://github.com/DaKheera47/job-ops) is a self-hosted job-search pipeline. 8 PRs: 3 merged, 5 open.

### Posting dates across time zones and DST ([#788](https://github.com/DaKheera47/job-ops/pull/788))
- **Problem:** in America/Toronto a date-only posting (`2026-05-25`) parsed at UTC midnight showed as May 24, adding a day to posting age and shifting sort order; dividing elapsed milliseconds by 24 h also miscounted days across a DST change.
- **Approach:** parse `YYYY-MM-DD` at local midnight and compare UTC day numbers built from local calendar components.
- **PR-reported validation:** six added cases; five failures before the fix in the Toronto run, all 14 pass after, and also under `TZ=UTC`, `Europe/London` and `Australia/Sydney`. Full suite and CI-parity checks pass. No browser end-to-end test.
- **Upstream outcome:** merged; maintainer: "nice! thanks for the contribution!"
- **Evidence:** [PR](https://github.com/DaKheera47/job-ops/pull/788) · [comment](https://github.com/DaKheera47/job-ops/pull/788#issuecomment-6445283059)

### Text-PDF import ([#789](https://github.com/DaKheera47/job-ops/pull/789)) and resume style metadata ([#787](https://github.com/DaKheera47/job-ops/pull/787))
- **Problem:** postings shared as PDFs could not be imported; Reactive Resume v5.3 style metadata was stripped by an older schema during import.
- **Approach:** #789 extracts text in the browser with PDF.js (10 MiB, 100 pages and 40,000-character limits, reject rather than truncate; nothing uploaded) and sends only the reviewed text to the existing analysis. #787 extends the shared types and schema to keep validated `stylesheet` and `styleRules`.
- **PR-reported validation:** #789: 25 focused tests, a real PDF.js read of a synthetic PDF, mocked AI and persistence, no live model and no native file-picker run. #787: three regressions and the full suite under `TZ=UTC`; it verifies metadata preservation, not rendered output.
- **Upstream outcome:** both merged with maintainer thanks.
- **Evidence:** [#789 comment](https://github.com/DaKheera47/job-ops/pull/789#issuecomment-6445274915) · [#787 comment](https://github.com/DaKheera47/job-ops/pull/787#issuecomment-6445299749)

---

## 4. WatDesk: original project (TypeScript)

[Jelly-RayTian/WatDesk](https://github.com/Jelly-RayTian/WatDesk) is my own Edge side-panel extension; it is not an external contribution.

- **Problem:** Waterloo deadlines, exams and grades live on separate sites (LEARN, Crowdmark, Odyssey) with no single view of what is due next.
- **Approach:** an Edge extension that reads each site in the user's own signed-in session and shows one timeline, a two-week workload view, an exam page and grades. Data stays in the browser; the extension never sees passwords or cookies and never submits anything. An anonymous usage counter is on by default and can be turned off.
- **Status:** public releases up to [v1.9.0](https://github.com/Jelly-RayTian/WatDesk/releases/latest); installed by loading the unpacked folder. The Edge Add-ons listing is under review.
- **Validation:** none is claimed here beyond the repository and releases themselves; I have not published independent test or user figures.
- **Evidence:** [repository](https://github.com/Jelly-RayTian/WatDesk) · [releases](https://github.com/Jelly-RayTian/WatDesk/releases)
