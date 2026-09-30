#!/usr/bin/env python3
"""Batch 17 rollback: restore the Returns page body from before.json."""
import json, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); page = json.load(open(os.path.join(HERE, "before.json")))["pages"]["nodes"][0]
out = subprocess.run(["shopify", "store", "execute", "--store", "7u2dfq-xf.myshopify.com", "--json", "--allow-mutations", "--query",
    "mutation($id: ID!, $p: PageUpdateInput!) { pageUpdate(id: $id, page: $p) { userErrors { message } } }",
    "--variables", json.dumps({"id": page["id"], "p": {"body": page["body"]}})], capture_output=True, text=True).stdout
print(out[out.find("{"):][:200])
