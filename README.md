# Ray Tian

Honours Mathematics (Co-operative Program) student at the **University of Waterloo**, interested in **software engineering, data science and quantitative development**. I build small, careful tools and contribute fixes to open-source projects, with an emphasis on reproducing a bug first and testing the fix.

**Portfolio:** [jelly-raytian.github.io](https://jelly-raytian.github.io/) · [中文](https://jelly-raytian.github.io/zh/)

## Open-source contributions

Verified against GitHub and upstream `main` history. Each pull request is counted once, under one status.

<!-- BEGIN GENERATED:stats -->
| External PRs | Officially merged | Squashed onto upstream main | Consolidated, commits in upstream main | Open / draft |
|--:|--:|--:|--:|--:|
| **53** | **34** | **3** | **5** | **9 / 1** |
<!-- END GENERATED:stats -->

- **Officially merged** means GitHub marks the PR merged.
- **Squashed** means a maintainer applied my PR to `main` as a commit authored by me and said so; GitHub shows it as closed.
- **Consolidated** means the maintainer folded the PR into a larger integration PR; my authored commits are in `main`'s history. These are not counted as merged.

**[Full record: every PR, status, evidence and maintainer comments →](OPEN_SOURCE_CONTRIBUTIONS.md)** · **[Case studies →](CASE_STUDIES.md)**

### Selected contributions

| Project | Contribution | Outcome |
|---|---|---|
| [willfaust/Madeira](https://github.com/willfaust/Madeira) (C, Swift; Wine/FEX on iOS) | Fixed a startup buffer overwrite for working directories of 260+ characters, with an ASan/UBSan reproduction ([#471](https://github.com/willfaust/Madeira/pull/471)); stopped Steam Cloud sync from treating unreadable saves as local edits ([#472](https://github.com/willfaust/Madeira/pull/472)); Vulkan, TaskbarList and UTF-8 launch-path work ([#400](https://github.com/willfaust/Madeira/pull/400), [#451](https://github.com/willfaust/Madeira/pull/451), [#456](https://github.com/willfaust/Madeira/pull/456), [#465](https://github.com/willfaust/Madeira/pull/465)) | 4 merged, 3 squashed onto `main`, 5 consolidated, 1 experimental draft |
| [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) (TypeScript) | PDF document-integrity fixes: rotate keeps forms, bookmarks and links ([#266](https://github.com/PDFCraftTool/pdfcraft/pull/266)); Unicode page-label prefixes ([#257](https://github.com/PDFCraftTool/pdfcraft/pull/257)); freeze on oversized label ranges ([#264](https://github.com/PDFCraftTool/pdfcraft/pull/264)) | 10 merged, 4 open |
| [DaKheera47/job-ops](https://github.com/DaKheera47/job-ops) (TypeScript) | Timezone/DST-correct posting dates ([#788](https://github.com/DaKheera47/job-ops/pull/788)); text-PDF import ([#789](https://github.com/DaKheera47/job-ops/pull/789)); resume style metadata ([#787](https://github.com/DaKheera47/job-ops/pull/787)) | 3 merged, 5 open |

Many of these were developed with AI coding assistance, which the PR descriptions state. Test results quoted in the case studies are the ones each PR reports; I mark where upstream validation is independent.

## Projects

- **[WatDesk](https://github.com/Jelly-RayTian/WatDesk)**: an Edge side-panel extension that gathers Waterloo deadlines, exams and grades from LEARN, Crowdmark and Odyssey into one timeline. Data stays in the browser; passwords are never read. TypeScript, [v1.9.0 released](https://github.com/Jelly-RayTian/WatDesk/releases/latest); Edge Add-ons listing is still under review. Independent student project, not a University of Waterloo product.
- **[WechatSignals](https://github.com/Jelly-RayTian/WechatSignals)**: local-first macOS client for analysing one-to-one WeChat chats (read-only access, anonymisation, SQLite, Keychain). TypeScript.
- **[CodeCompass](https://github.com/Jelly-RayTian/CodeCompass)** and **[Chronicle](https://github.com/Jelly-RayTian/Chronicle)**: local-first desktop apps in Rust (Tauri for CodeCompass).
- **[Madeira-Experimental](https://github.com/Jelly-RayTian/Madeira-Experimental)**: an unofficial research fork exploring Windows x64 Vulkan on iPad. Incomplete, and not an official Madeira port.

## Technologies (from the code above)

TypeScript · Rust · C · Swift (small changes) · Python (tests and tooling) · Vulkan/MoltenVK basics · PDF internals (pdf-lib, PDF.js) · Git, GitHub Actions

## Education

University of Waterloo, Honours Bachelor of Mathematics (Co-operative Program), started September 2026. Currently looking for software engineering co-op and internship opportunities.

<sub>Statistics are refreshed by [a scheduled workflow](.github/workflows/update-contributions.yml); see [MAINTAINING.md](MAINTAINING.md).</sub>
