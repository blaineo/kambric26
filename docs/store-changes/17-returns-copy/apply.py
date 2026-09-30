#!/usr/bin/env python3
"""Batch 17: Returns page states who pays return shipping (matches the Google markup).
Replaces one sentence in the 'Start a Return' section. `--dry-run` prints the new body; rollback.py restores before.json."""
import json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); DRY = "--dry-run" in sys.argv
page = json.load(open(os.path.join(HERE, "before.json")))["pages"]["nodes"][0]
old = "<p>Get in touch with your order number and we'll send you simple return instructions.</p>"
new = ("<p>Get in touch with your order number and we'll email you a return label and simple instructions.</p>\n"
       "<p>Return shipping is deducted from your refund.</p>")
assert old in page["body"], "Returns page changed since the snapshot; re-snapshot"
body = page["body"].replace(old, new)
print(body)
if DRY: sys.exit(0)
out = subprocess.run(["shopify", "store", "execute", "--store", "7u2dfq-xf.myshopify.com", "--json", "--allow-mutations", "--query",
    "mutation($id: ID!, $p: PageUpdateInput!) { pageUpdate(id: $id, page: $p) { page { id } userErrors { field message } } }",
    "--variables", json.dumps({"id": page["id"], "p": {"body": body}})], capture_output=True, text=True).stdout
print(out[out.find("{"):][:300])
