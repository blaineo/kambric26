#!/usr/bin/env python3
"""Batch 14 rollback: delete the redirects this batch created (apply-log.json)."""
import json, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
for r in json.load(open(os.path.join(HERE, "apply-log.json")))["created"]:
    out = subprocess.run(["shopify", "store", "execute", "--store", "7u2dfq-xf.myshopify.com", "--json", "--allow-mutations", "--query",
        "mutation($id: ID!) { urlRedirectDelete(id: $id) { deletedUrlRedirectId userErrors { message } } }",
        "--variables", json.dumps({"id": r["id"]})], capture_output=True, text=True).stdout
    print(r["path"], out[out.find("{"):][:100])
