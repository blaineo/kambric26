#!/usr/bin/env python3
"""Batch 12 (🔴 shared metafield; owner-approved 2026-09-29): in kambric.prints, change every
"collection": "botanicals" (Whimsy's old handle) to "whimsy". Nothing else in the JSON changes.
Products: margit-one-piece (1), zadie-linen-dress (3), and drafts linen-napkins (2), linen-tea-towel (2),
linen-tablecloth (1). Values come from before.json; `--dry-run` prints the diff only.
rollback.py writes the before.json values back verbatim.
"""
import json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
STORE, SHOP_ID = "7u2dfq-xf.myshopify.com", "gid://shopify/Shop/71406846186"
DRY = "--dry-run" in sys.argv
B = json.load(open(os.path.join(HERE, "before.json")))
if B["shop"]["id"] != SHOP_ID: sys.exit("wrong store in before.json")

changes = []
for p in B["products"]["nodes"]:
    prints = json.loads(p["prints"]["value"])
    n = 0
    for entry in prints:
        if entry.get("collection") == "botanicals":
            entry["collection"] = "whimsy"; n += 1
    if n:
        changes.append({"ownerId": p["id"], "namespace": "kambric", "key": "prints", "type": "json",
                        "value": json.dumps(prints, ensure_ascii=False)})
        print(f"{p['handle']:20} {p['status']:7} {n} entr{'y' if n == 1 else 'ies'} botanicals -> whimsy")
if DRY: sys.exit(0)

cmd = ["shopify", "store", "execute", "--store", STORE, "--json", "--allow-mutations", "--query",
       "mutation($m: [MetafieldsSetInput!]!) { metafieldsSet(metafields: $m) { metafields { owner { ... on Product { handle } } key } userErrors { field message } } }",
       "--variables", json.dumps({"m": changes})]
out = subprocess.run(cmd, capture_output=True, text=True).stdout
r = json.loads(out[out.find("{"):])
json.dump(r, open(os.path.join(HERE, "apply-result.json"), "w"), indent=1)
errs = r["metafieldsSet"]["userErrors"]
sys.exit(f"userErrors: {errs}") if errs else print("updated:", [m["owner"]["handle"] for m in r["metafieldsSet"]["metafields"]])
