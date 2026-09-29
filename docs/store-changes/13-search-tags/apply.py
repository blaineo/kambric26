#!/usr/bin/env python3
"""Batch 13 (owner-approved 2026-09-29): search tags. Adds tags only (tagsAdd); never removes.
Print names that live in custom fields, an unaccented "Matyo Floral", collection names, and
Arielle's archive label, so Shopify's native search finds them. `--dry-run` prints the plan.
rollback.py removes exactly the tags recorded in apply-log.json as newly added."""
import json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
STORE, SHOP_ID = "7u2dfq-xf.myshopify.com", "gid://shopify/Shop/71406846186"
DRY = "--dry-run" in sys.argv
PLAN = {
    "kati-slip-dress-in-matyo-floral":      ["Matyó Floral", "Matyo Floral", "Folklore"],
    "goldie-bandana-in-matyo-floral":       ["Matyó Floral", "Matyo Floral", "Folklore"],
    "jessie-slip-dress-in-twilight-plumes": ["Twilight Plumes", "Folklore"],
    "bodie-scarf-in-twilight-plumes":       ["Twilight Plumes", "Folklore"],
    "margit-one-piece":                     ["Matyo Floral", "Psychedelics", "Folklore", "Whimsy"],
    "zadie-linen-dress":                    ["Whimsy"],
    "esther-kaftan":                        ["Psychedelics"],
    "vera-car-coat":                        ["Matyo Floral", "Folklore"],
    "arielle-dress":                        ["Parlor Rose", "Folklore"],
}
B = json.load(open(os.path.join(HERE, "before.json")))
if B["shop"]["id"] != SHOP_ID: sys.exit("wrong store")
products = {p["handle"]: p for p in B["products"]["nodes"]}
log = {"added": {}}
for handle, tags in PLAN.items():
    p = products.get(handle) or sys.exit(f"missing product {handle}")
    new = [t for t in tags if t.lower() not in {x.lower() for x in p["tags"]}]
    print(f"{handle:38} + {new}")
    if DRY or not new: continue
    out = subprocess.run(["shopify", "store", "execute", "--store", STORE, "--json", "--allow-mutations", "--query",
        "mutation($id: ID!, $tags: [String!]!) { tagsAdd(id: $id, tags: $tags) { node { ... on Product { handle tags } } userErrors { field message } } }",
        "--variables", json.dumps({"id": p["id"], "tags": new})], capture_output=True, text=True).stdout
    r = json.loads(out[out.find("{"):])["tagsAdd"]
    if r["userErrors"]: json.dump(log, open(os.path.join(HERE, "apply-log.json"), "w"), indent=1); sys.exit(f"{handle}: {r['userErrors']}")
    log["added"][handle] = {"id": p["id"], "tags": new}
if not DRY:
    json.dump(log, open(os.path.join(HERE, "apply-log.json"), "w"), indent=1, ensure_ascii=False)
    print("done")
