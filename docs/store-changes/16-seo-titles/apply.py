#!/usr/bin/env python3
"""Batch 16: search-listing (SEO) titles for the 9 products and 6 category/sale collections, plus the Sale
description. Only the SEO fields change; page names and on-page headings stay. The theme appends
" | Kambric Goods". `--dry-run` prints only; rollback.py restores before.json."""
import json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); DRY = "--dry-run" in sys.argv
B = json.load(open(os.path.join(HERE, "before.json"))); PLAN = json.load(open(os.path.join(HERE, "plan.json")))
prods = {n["handle"]: n for n in B["products"]["nodes"]}; cols = {n["handle"]: n for n in B["collections"]["nodes"]}
def gql(q, v):
    if DRY: return None
    out = subprocess.run(["shopify", "store", "execute", "--store", "7u2dfq-xf.myshopify.com", "--json", "--allow-mutations", "--query", q, "--variables", json.dumps(v)], capture_output=True, text=True).stdout
    r = json.loads(out[out.find("{"):]); k = next(iter(r))
    if r[k]["userErrors"]: sys.exit(f"{k}: {r[k]['userErrors']}")
for h, t in PLAN["products"].items():
    n = prods[h]; print(f"product {h:38} {n['seo']['title']!r} -> {t!r} ({len(t) + 16} chars with suffix)")
    gql("mutation($p: ProductUpdateInput!) { productUpdate(product: $p) { userErrors { field message } } }",
        {"p": {"id": n["id"], "seo": {"title": t, "description": n["seo"]["description"]}}})
for h, c in PLAN["collections"].items():
    n = cols[h]; desc = c.get("description", n["seo"]["description"])
    print(f"collection {h:12} {n['seo']['title']!r} -> {c['title']!r}" + (f" + description" if "description" in c else ""))
    gql("mutation($c: CollectionInput!) { collectionUpdate(input: $c) { userErrors { field message } } }",
        {"c": {"id": n["id"], "seo": {"title": c["title"], "description": desc}}})
print("dry run complete" if DRY else "done")
