# Maintaining the contribution statistics

## What is automated

`scripts/update_stats.py` (Python 3 standard library only) does GET requests to the GitHub API and:

1. lists every PR authored by `Jelly-RayTian` (paginated search), skips private repositories, fetches each PR;
2. sets the status: `merged` if GitHub says so (and checks the merge commit is on the default branch), `open`/`draft` from state, otherwise `closed_unverified`;
3. rewrites only the `<!-- BEGIN GENERATED:… -->` blocks in `README.md` and `OPEN_SOURCE_CONTRIBUTIONS.md`, and `data/prs.json`.

It waits out rate limits (stops if the reset is more than five minutes away), retries transient errors, refuses to shrink the PR list unless `--allow-shrink` is given, and keeps the previous date when nothing changed, so reruns are safe and produce no diff.

## What is never automated

- A closed PR is never labelled squashed or consolidated by the script. That comes only from `data/curated.json`, and the script then re-checks that the cited commit SHAs are still reachable from the default branch (it warns otherwise).
- `data/curated.json`, `CASE_STUDIES.md` and all text outside generated blocks are never modified.

## Adding or reclassifying a PR

New PRs appear automatically with live status and "Not yet curated". To add a summary, acknowledgments or evidence, add an entry to `data/curated.json` keyed `owner/repo#number`. To mark a closed PR as integrated, first confirm a maintainer statement and commit ancestry (for example `git merge-base --is-ancestor <sha> main`), put the 40-character commit URLs in `evidence`, then set `"class"`.

## Running

```bash
python3 scripts/update_stats.py            # refresh files
python3 scripts/update_stats.py --check    # exit 1 if anything would change
```

Uses `GITHUB_TOKEN`, else `gh auth token`.

## Workflow

`.github/workflows/update-contributions.yml` runs weekly (Mondays 06:00 UTC) and on manual `workflow_dispatch`. API access is read-only; the job token has `contents: write` only so it can commit the refreshed generated files back to this repository. It never touches other repositories.

To disable: GitHub, Actions tab, select the workflow, "…", Disable workflow (or delete the file). To change the schedule, edit the `cron` line.
- The hand-written table in README "Selected contributions" repeats per-repo counts; update it by hand when the generated numbers change.
