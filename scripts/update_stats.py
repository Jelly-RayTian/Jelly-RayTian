#!/usr/bin/env python3
"""Refresh PR statuses and statistics. Standard library only, GET requests only.

Reads  data/curated.json   (hand-written; never modified here)
Writes data/prs.json       (snapshot of live GitHub facts + derived status)
Edits  only the blocks between <!-- BEGIN GENERATED:x --> / <!-- END GENERATED:x -->
       in README.md and OPEN_SOURCE_CONTRIBUTIONS.md.

A closed PR is never classified as integrated automatically. Only PRs listed in
curated.json with class "squashed" / "consolidated" get that label, and the script
then re-checks that their cited commits are still reachable from the default branch.

Usage: python3 scripts/update_stats.py [--check] [--allow-shrink]
  --check         exit 1 if generated files would change (no writes)
  --allow-shrink  accept fewer PRs than the previous snapshot
Auth: GITHUB_TOKEN env var, else `gh auth token`, else anonymous (low rate limit).
"""
import json, os, re, subprocess, sys, time, urllib.error, urllib.request
from collections import OrderedDict
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
API = "https://api.github.com"
LABEL = OrderedDict([
    ("merged", "Merged"),
    ("squashed", "Closed, squashed onto main"),
    ("consolidated", "Closed, consolidated (commits in main history)"),
    ("retained", "Closed, retained in a replacement PR"),
    ("open", "Open"),
    ("draft", "Draft / experimental"),
    ("closed_unverified", "Closed, no verified integration"),
])


def token():
    t = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if t:
        return t
    try:
        return subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return None


TOKEN = token()


def get(url, ok_404=False):
    """GET with retry, rate-limit wait and Link-header pagination. Returns (json, next_url)."""
    for attempt in range(5):
        req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json",
                                                   "User-Agent": "contrib-stats"})
        if TOKEN:
            req.add_header("Authorization", f"Bearer {TOKEN}")
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                remaining = int(r.headers.get("X-RateLimit-Remaining", "1"))
                reset = int(r.headers.get("X-RateLimit-Reset", "0"))
                nxt = re.search(r'<([^>]+)>;\s*rel="next"', r.headers.get("Link", ""))
                body = json.load(r)
                if remaining <= 1:
                    wait = max(0, reset - int(time.time())) + 1
                    if wait > 300:
                        sys.exit(f"Rate limit exhausted; resets in {wait}s. Re-run later.")
                    time.sleep(wait)
                return body, (nxt.group(1) if nxt else None)
        except urllib.error.HTTPError as e:
            if e.code == 404 and ok_404:
                return None, None
            if e.code in (403, 429) and e.headers.get("X-RateLimit-Remaining") == "0":
                wait = max(0, int(e.headers.get("X-RateLimit-Reset", "0")) - int(time.time())) + 1
                if wait > 300:
                    sys.exit(f"Rate limit exhausted; resets in {wait}s. Re-run later.")
                time.sleep(wait)
            elif e.code in (500, 502, 503, 504, 403, 429):
                time.sleep(2 ** attempt * 2)
            else:
                sys.exit(f"HTTP {e.code} for {url}")
        except urllib.error.URLError:
            time.sleep(2 ** attempt * 2)
    sys.exit(f"Giving up on {url}")


def paginate(url):
    out = []
    while url:
        body, url = get(url)
        out.extend(body["items"] if isinstance(body, dict) and "items" in body else body)
        time.sleep(0.3)
    return out


def on_branch(repo, branch, sha):
    """True if sha is an ancestor of (or equal to) branch."""
    body, _ = get(f"{API}/repos/{repo}/compare/{sha}...{branch}?per_page=1", ok_404=True)
    return bool(body) and body.get("status") in ("ahead", "identical")


def short(d):
    return d[:10] if d else ""


def collect(curated):
    user = curated["owner"]
    items = paginate(f"{API}/search/issues?q=author:{user}+type:pr&per_page=100")
    seen, branches, prs = set(), {}, []
    for it in items:
        repo = it["repository_url"].split("/repos/")[1]
        key = f"{repo}#{it['number']}"
        if key in seen:
            continue
        seen.add(key)
        if repo not in branches:
            info = get(f"{API}/repos/{repo}")[0]
            branches[repo] = None if info["private"] else info["default_branch"]  # never publish private repos
        if branches[repo] is None:
            continue
        p, _ = get(f"{API}/repos/{repo}/pulls/{it['number']}")
        c = curated["prs"].get(key, {})
        merged = bool(p["merged_at"])
        cls = c.get("class")
        warn = None
        if merged:
            status = "merged"
        elif p["state"] == "open":
            status = "draft" if p["draft"] else "open"
            if cls:
                warn = f"curated class '{cls}' but PR is open"
        elif cls in ("squashed", "consolidated", "retained"):
            status = cls
        else:
            status = "closed_unverified"
        in_main = None  # None = not applicable
        if merged:
            in_main = on_branch(repo, branches[repo], p["merge_commit_sha"])
        elif status in ("squashed", "consolidated"):
            shas = [m for e in c.get("evidence", []) for m in re.findall(r"/commit/([0-9a-f]{40})", e["url"])]
            in_main = bool(shas) and all(on_branch(repo, branches[repo], s) for s in shas)
            if not in_main:
                warn = "cited commits are not (all) reachable from the default branch; review curated entry"
        if merged and not in_main:
            warn = "merge commit not reachable from default branch"
        prs.append(OrderedDict(
            key=key, repo=repo, number=p["number"], url=p["html_url"], title=p["title"],
            state=p["state"], draft=p["draft"], merged_at=p["merged_at"], created_at=p["created_at"],
            closed_at=p["closed_at"], additions=p["additions"], deletions=p["deletions"],
            changed_files=p["changed_files"], status=status, in_main=in_main,
            default_branch=branches[repo], warning=warn))
    prs.sort(key=lambda x: (x["repo"].lower(), x["number"]))
    return prs


def stats(prs, user):
    ext = [p for p in prs if p["repo"].split("/")[0].lower() != user.lower()]
    own = [p for p in prs if p["repo"].split("/")[0].lower() == user.lower()]
    def count(lst):
        c = OrderedDict((k, 0) for k in LABEL)
        for p in lst:
            c[p["status"]] += 1
        return c
    repos = OrderedDict()
    for p in ext:
        repos.setdefault(p["repo"], []).append(p)
    return ext, own, count(ext), count(own), repos


def render_summary(prs, user):
    ext, own, ce, co, repos = stats(prs, user)
    L = ["| Repository | PRs | Merged | Squashed onto main | Consolidated | Open | Draft | Closed, unverified |",
         "|---|--:|--:|--:|--:|--:|--:|--:|"]
    for r, lst in repos.items():
        c = OrderedDict((k, sum(1 for p in lst if p["status"] == k)) for k in LABEL)
        L.append(f"| [{r}](https://github.com/{r}) | {len(lst)} | {c['merged']} | {c['squashed']} | {c['consolidated']} | {c['open']} | {c['draft']} | {c['closed_unverified'] + c['retained']} |")
    L.append(f"| **External total** | **{len(ext)}** | **{ce['merged']}** | **{ce['squashed']}** | **{ce['consolidated']}** | **{ce['open']}** | **{ce['draft']}** | **{ce['closed_unverified'] + ce['retained']}** |")
    L += ["", f"Pull requests in my own repositories (not counted above): **{len(own)}** "
          f"({co['merged']} merged, {co['closed_unverified']} closed unmerged, {co['open'] + co['draft']} open). "
          f"All PRs authored by `{user}`: **{len(prs)}**."]
    return "\n".join(L)


def render_readme_stats(prs, user):
    ext, own, ce, co, repos = stats(prs, user)
    return "\n".join([
        "| External PRs | Officially merged | Squashed onto upstream main | Consolidated, commits in upstream main | Open / draft |",
        "|--:|--:|--:|--:|--:|",
        f"| **{len(ext)}** | **{ce['merged']}** | **{ce['squashed']}** | **{ce['consolidated']}** | **{ce['open']} / {ce['draft']}** |"])


def render_external(prs, curated, user):
    ext, _, _, _, repos = stats(prs, user)
    out = []
    for r, lst in repos.items():
        out += [f"### [{r}](https://github.com/{r})", "",
                "| PR | Title | Status | In upstream main |", "|--:|---|---|---|"]
        for p in lst:
            im = {True: "Yes", False: "**No, review**", None: "n/a"}[p["in_main"]]
            out.append(f"| [#{p['number']}]({p['url']}) | {p['title']} | {LABEL[p['status']]} | {im} |")
        out.append("")
        for p in lst:
            c = curated["prs"].get(p["key"], {})
            out += [f"#### [{r}#{p['number']}]({p['url']}): {p['title']}", ""]
            out.append(f"- **Description:** {c.get('summary', '_Not yet curated._')}")
            st = LABEL[p["status"]]
            if p["merged_at"]:
                st += f" on {short(p['merged_at'])}"
            elif p["closed_at"]:
                st += f" (closed {short(p['closed_at'])}, GitHub does not mark it merged)"
            out.append(f"- **GitHub status:** {st}; opened {short(p['created_at'])}; +{p['additions']} / −{p['deletions']} in {p['changed_files']} files.")
            if p["in_main"] is True and p["status"] == "merged":
                out.append(f"- **In upstream `{p['default_branch']}`:** Yes, the merge commit is reachable from `{p['default_branch']}` (checked via the compare API).")
            elif p["in_main"] is True:
                out.append(f"- **In upstream `{p['default_branch']}`:** Yes, by curated evidence below; cited commits re-checked as reachable from `{p['default_branch']}`.")
            elif p["in_main"] is False:
                out.append("- **In upstream main:** ⚠ check failed; see warning below.")
            else:
                out.append("- **In upstream main:** Not applicable (not merged or integrated).")
            acks = c.get("ack", [])
            out.append("- **Maintainer / reviewer:** " + ("; ".join(f"[{a['text']}]({a['url']})" for a in acks) if acks else "No comment or review on the PR."))
            if c.get("evidence"):
                out.append("- **Upstream commits:** " + "; ".join(f"[{e['label']}]({e['url']})" for e in c["evidence"]))
            if c.get("related"):
                out.append("- **Replacement / consolidation:** " + "; ".join(f"[{e['label']}]({e['url']})" for e in c["related"]))
            if c.get("note"):
                out.append(f"- **Note:** {c['note']}")
            if p["warning"]:
                out.append(f"- **⚠ Warning:** {p['warning']}")
            out += [f"- **Last verified:** {curated['verified_on']} (curated notes) / {{GEN_DATE}} (live status)", ""]
    return "\n".join(out)


def render_own(prs, user):
    _, own, _, _, _ = stats(prs, user)
    L = ["| Repository | PR | Title | Status |", "|---|--:|---|---|"]
    for p in own:
        L.append(f"| {p['repo']} | [#{p['number']}]({p['url']}) | {p['title']} | {LABEL[p['status']]}{' ' + short(p['merged_at']) if p['merged_at'] else ''} |")
    return "\n".join(L)


def splice(path, name, body):
    text = open(path, encoding="utf-8").read()
    pat = re.compile(rf"(<!-- BEGIN GENERATED:{name} -->\n).*?(<!-- END GENERATED:{name} -->)", re.S)
    if not pat.search(text):
        sys.exit(f"Missing markers for {name} in {path}")
    return pat.sub(lambda m: m.group(1) + body + "\n" + m.group(2), text)


def build(prs, curated, gen_date):
    user = curated["owner"]
    docs = {}
    p = os.path.join(ROOT, "OPEN_SOURCE_CONTRIBUTIONS.md")
    t = open(p, encoding="utf-8").read()
    for name, body in (("summary", render_summary(prs, user)),
                       ("external", render_external(prs, curated, user).replace("{GEN_DATE}", gen_date)),
                       ("own", render_own(prs, user))):
        pat = re.compile(rf"(<!-- BEGIN GENERATED:{name} -->\n).*?(<!-- END GENERATED:{name} -->)", re.S)
        if not pat.search(t):
            sys.exit(f"Missing markers for {name}")
        t = pat.sub(lambda m: m.group(1) + body + "\n" + m.group(2), t)
    t = re.sub(r"(<!-- GEN_DATE -->).*?(<!-- /GEN_DATE -->)", rf"\g<1>{gen_date}\g<2>", t)
    docs[p] = t
    p2 = os.path.join(ROOT, "README.md")
    docs[p2] = splice(p2, "stats", render_readme_stats(prs, user))
    return docs


def main():
    check, shrink = "--check" in sys.argv, "--allow-shrink" in sys.argv
    curated = json.load(open(os.path.join(ROOT, "data/curated.json"), encoding="utf-8"))
    snap_path = os.path.join(ROOT, "data/prs.json")
    old = json.load(open(snap_path)) if os.path.exists(snap_path) else None
    prs = collect(curated)
    if old and len(prs) < len(old["prs"]) and not shrink:
        sys.exit(f"Found {len(prs)} PRs but snapshot has {len(old['prs'])}; refusing (use --allow-shrink).")
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    # keep the previous date when nothing changed, so reruns produce no diff
    gen_date = old["generated_on"] if old and old["prs"] == json.loads(json.dumps(prs)) else today
    docs = build(prs, curated, gen_date)
    snap = json.dumps(OrderedDict(generated_on=gen_date, prs=prs), indent=2, ensure_ascii=False) + "\n"
    changed = [path for path, txt in docs.items() if open(path, encoding="utf-8").read() != txt]
    if not old or json.dumps(json.loads(snap), sort_keys=True) != json.dumps(old, sort_keys=True):
        changed.append(snap_path)
    for p in prs:
        if p["warning"]:
            print(f"WARNING {p['key']}: {p['warning']}", file=sys.stderr)
    uncurated = [p["key"] for p in prs if p["key"] not in curated["prs"] and p["repo"].split("/")[0] != curated["owner"]]
    if uncurated:
        print("Not yet curated (shown with live status only): " + ", ".join(uncurated), file=sys.stderr)
    if check:
        print("changed:", [os.path.relpath(c, ROOT) for c in changed])
        sys.exit(1 if changed else 0)
    for path, txt in docs.items():
        open(path, "w", encoding="utf-8").write(txt)
    open(snap_path, "w", encoding="utf-8").write(snap)
    print(f"{len(prs)} PRs; updated: {[os.path.relpath(c, ROOT) for c in changed] or 'nothing'}")


if __name__ == "__main__":
    main()
