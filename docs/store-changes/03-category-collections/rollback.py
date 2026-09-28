#!/usr/bin/env python3
"""Batch 03 rollback: before.json shows none of the six handles existed, so rollback = delete the
collections created (IDs from apply-log.json). Deleting also unpublishes them from kambricgoods.com."""
import json, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
for c in json.load(open(os.path.join(HERE, "apply-log.json")))["created"]:
    out = subprocess.run(["shopify", "store", "execute", "--store", "7u2dfq-xf.myshopify.com", "--json", "--allow-mutations",
        "--query", "mutation($id: ID!) { collectionDelete(input: { id: $id }) { deletedCollectionId userErrors { message } } }",
        "--variables", json.dumps({"id": c["id"]})], capture_output=True, text=True).stdout
    print(c["handle"], out[out.find("{"):].strip())
