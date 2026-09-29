#!/usr/bin/env python3
"""Batch 16 rollback: restore the SEO title/description of every product and collection in plan.json from before.json."""
import json, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
B = json.load(open(os.path.join(HERE, "before.json"))); PLAN = json.load(open(os.path.join(HERE, "plan.json")))
def gql(q, v):
    out = subprocess.run(["shopify", "store", "execute", "--store", "7u2dfq-xf.myshopify.com", "--json", "--allow-mutations", "--query", q, "--variables", json.dumps(v)], capture_output=True, text=True).stdout
    print(out[out.find("{"):][:120])
for n in B["products"]["nodes"]:
    if n["handle"] in PLAN["products"]:
        gql("mutation($p: ProductUpdateInput!) { productUpdate(product: $p) { userErrors { message } } }", {"p": {"id": n["id"], "seo": {"title": n["seo"]["title"] or "", "description": n["seo"]["description"] or ""}}})
for n in B["collections"]["nodes"]:
    if n["handle"] in PLAN["collections"]:
        gql("mutation($c: CollectionInput!) { collectionUpdate(input: $c) { userErrors { message } } }", {"c": {"id": n["id"], "seo": {"title": n["seo"]["title"] or "", "description": n["seo"]["description"] or ""}}})
