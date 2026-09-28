#!/usr/bin/env python3
"""Batch 02 rollback: before.json shows no card/header values and no such Files existed,
so rollback = delete the 6 metafields set, then delete the Files created (IDs from apply-log.json)."""
import json, subprocess, os
HERE = os.path.dirname(os.path.abspath(__file__))
M = json.load(open(os.path.join(HERE, "manifest.json"))); L = json.load(open(os.path.join(HERE, "apply-log.json")))
def run(q, v):
    out = subprocess.run(["shopify", "store", "execute", "--store", M["store"], "--json", "--allow-mutations",
                          "--query", q, "--variables", json.dumps(v)], capture_output=True, text=True)
    print(out.stdout[out.stdout.find("{"):])
run("""mutation($m: [MetafieldIdentifierInput!]!) { metafieldsDelete(metafields: $m) { deletedMetafields { key ownerId } userErrors { message } } }""",
    {"m": [{"ownerId": i["collection"], "namespace": "kambric", "key": i["key"]} for i in M["images"]]})
if L.get("files"):
    run("""mutation($ids: [ID!]!) { fileDelete(fileIds: $ids) { deletedFileIds userErrors { message } } }""",
        {"ids": [f["id"] for f in L["files"]]})
