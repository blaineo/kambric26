#!/usr/bin/env python3
"""Batch 11 rollback: before.json shows no Files with these names existed, so rollback = revert the
template photo settings (git: sections/footer-group.json (newsletter_popup image)), then delete
the Files created (IDs from apply-log.json)."""
import json, subprocess, os
HERE = os.path.dirname(os.path.abspath(__file__))
M = json.load(open(os.path.join(HERE, "manifest.json"))); L = json.load(open(os.path.join(HERE, "apply-log.json")))
if L.get("files"):
    out = subprocess.run(["shopify", "store", "execute", "--store", M["store"], "--json", "--allow-mutations",
        "--query", "mutation($ids: [ID!]!) { fileDelete(fileIds: $ids) { deletedFileIds userErrors { message } } }",
        "--variables", json.dumps({"ids": [f["id"] for f in L["files"]]})], capture_output=True, text=True)
    print(out.stdout[out.stdout.find("{"):])
