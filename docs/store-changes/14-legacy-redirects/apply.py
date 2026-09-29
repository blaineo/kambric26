#!/usr/bin/env python3
"""Batch 14: 301s for the pre-Replit (Squarespace-era) URLs search engines still list.
Reads redirects.csv (path,target,basis,note). Skips a path that already has a redirect.
`--dry-run` prints only. rollback.py deletes the redirects recorded in apply-log.json.
/terms-conditions -> /policies/terms-of-service is held back until the Terms policy exists."""
import csv, json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
STORE = "7u2dfq-xf.myshopify.com"; DRY = "--dry-run" in sys.argv
def gql(q, v=None, m=True):
    cmd = ["shopify", "store", "execute", "--store", STORE, "--json", "--query", q] + (["--variables", json.dumps(v)] if v else []) + (["--allow-mutations"] if m else [])
    out = subprocess.run(cmd, capture_output=True, text=True).stdout; return json.loads(out[out.find("{"):])
existing = {r["path"] for r in gql("{ urlRedirects(first: 250) { nodes { path } } }", m=False)["urlRedirects"]["nodes"]}
rows = list(csv.DictReader(open(os.path.join(HERE, "redirects.csv"))))
log = {"created": []}
for r in rows:
    if r["path"] in existing: print("skip (exists)", r["path"]); continue
    print(f"{r['path']:52} -> {r['target']}")
    if DRY: continue
    res = gql("mutation($r: UrlRedirectInput!) { urlRedirectCreate(urlRedirect: $r) { urlRedirect { id path target } userErrors { field message } } }",
              {"r": {"path": r["path"], "target": r["target"]}})["urlRedirectCreate"]
    if res["userErrors"]: print("  !!", res["userErrors"]); continue
    log["created"].append(res["urlRedirect"])
if not DRY:
    json.dump(log, open(os.path.join(HERE, "apply-log.json"), "w"), indent=1); print(len(log["created"]), "created")
