#!/usr/bin/env python3
"""Batch 20: product photo descriptions (alt text) from descriptions.csv via fileUpdate.
Guards: right store; the LIVE theme already has the "Print | description" gallery code (otherwise the old
code would show the whole string and lose print grouping); every current alt still equals before.json.
`--dry-run` prints the changes and writes nothing. Rollback: rollback.py (restores current_alt)."""
import csv, json, os, subprocess, sys, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__)); DRY = "--dry-run" in sys.argv
STORE, SHOP_ID = "7u2dfq-xf.myshopify.com", "gid://shopify/Shop/71406846186"
def gql(q, v=None, m=False):
    cmd = ["shopify", "store", "execute", "--store", STORE, "--json", "--query", q] + (["--variables", json.dumps(v)] if v else []) + (["--allow-mutations"] if m else [])
    s = subprocess.run(cmd, capture_output=True, text=True).stdout
    d = json.loads(s[s.find("\n{\n") + 1:] if "\n{\n" in s else s[s.find("{"):]); return d.get("data", d)
rows = list(csv.DictReader(open(os.path.join(HERE, "descriptions.csv"))))
if gql("{ shop { id } }")["shop"]["id"] != SHOP_ID: sys.exit("wrong store")
html = urllib.request.urlopen(urllib.request.Request("https://kambricgoods.com/products/kati-slip-dress-in-matyo-floral",
                                                     headers={"User-Agent": "kg-batch20"})).read().decode()
if "view 1 of 8" not in html:
    msg = "The live theme doesn't have the new gallery code yet (commit 51543db). Push it first."
    if not DRY: sys.exit(msg)
    print("WARNING (dry run continues):", msg)
ids = [r["media_id"] for r in rows]
now = {}
for i in range(0, len(ids), 50):
    for n in gql("query($ids: [ID!]!) { nodes(ids: $ids) { ... on MediaImage { id alt } } }", {"ids": ids[i:i+50]})["nodes"]:
        now[n["id"]] = n["alt"] or ""
drift = [r for r in rows if now.get(r["media_id"]) != r["current_alt"]]
if drift: sys.exit(f"{len(drift)} alts changed since the snapshot, e.g. {drift[0]['handle']} #{drift[0]['n']}: {now.get(drift[0]['media_id'])!r}")
for r in rows: print(f"{r['handle']} #{r['n']}: {r['current_alt']!r} -> {r['new_alt']!r}")
if DRY: sys.exit("dry run: nothing written")
done = []
for i in range(0, len(rows), 25):
    chunk = rows[i:i+25]
    r = gql("mutation($f: [FileUpdateInput!]!) { fileUpdate(files: $f) { files { id alt } userErrors { field message } } }",
            {"f": [{"id": x["media_id"], "alt": x["new_alt"]} for x in chunk]}, m=True)["fileUpdate"]
    if r["userErrors"]: json.dump(done, open(os.path.join(HERE, "apply-log.json"), "w")); sys.exit(f"stopped: {r['userErrors']}")
    done += [x["media_id"] for x in chunk]; print(f"updated {len(done)}/{len(rows)}")
json.dump(done, open(os.path.join(HERE, "apply-log.json"), "w")); print("done")
