#!/usr/bin/env python3
"""Batch 13 rollback: remove exactly the tags apply.py added (apply-log.json)."""
import json, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
for handle, a in json.load(open(os.path.join(HERE, "apply-log.json")))["added"].items():
    out = subprocess.run(["shopify", "store", "execute", "--store", "7u2dfq-xf.myshopify.com", "--json", "--allow-mutations", "--query",
        "mutation($id: ID!, $tags: [String!]!) { tagsRemove(id: $id, tags: $tags) { userErrors { field message } } }",
        "--variables", json.dumps({"id": a["id"], "tags": a["tags"]})], capture_output=True, text=True).stdout
    print(handle, out[out.find("{"):][:120])
