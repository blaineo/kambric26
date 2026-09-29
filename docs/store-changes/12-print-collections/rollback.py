#!/usr/bin/env python3
"""Batch 12 rollback: write the original kambric.prints values (before.json) back verbatim."""
import json, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
B = json.load(open(os.path.join(HERE, "before.json")))
m = [{"ownerId": p["id"], "namespace": "kambric", "key": "prints", "type": "json", "value": p["prints"]["value"]}
     for p in B["products"]["nodes"] if p["prints"]]
out = subprocess.run(["shopify", "store", "execute", "--store", "7u2dfq-xf.myshopify.com", "--json", "--allow-mutations", "--query",
    "mutation($m: [MetafieldsSetInput!]!) { metafieldsSet(metafields: $m) { metafields { key } userErrors { field message } } }",
    "--variables", json.dumps({"m": m})], capture_output=True, text=True).stdout
print(out[out.find("{"):][:500])
