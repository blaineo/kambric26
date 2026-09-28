#!/usr/bin/env python3
"""Batch 06 rollback: before.json shows the store had no URL redirects, so rollback =
delete every redirect created (IDs from apply-log.json)."""
import json, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
ids = [r["id"] for r in json.load(open(os.path.join(HERE, "apply-log.json")))["created"]]
q = "mutation($ids: [ID!]!) { urlRedirectBulkDeleteByIds(ids: $ids) { job { id done } userErrors { field message } } }"
out = subprocess.run(["shopify", "store", "execute", "--store", "7u2dfq-xf.myshopify.com", "--json", "--allow-mutations",
                      "--query", q, "--variables", json.dumps({"ids": ids})], capture_output=True, text=True).stdout
print(out[out.find("{"):])
