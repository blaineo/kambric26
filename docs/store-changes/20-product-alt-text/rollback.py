#!/usr/bin/env python3
"""Batch 20 rollback: restore every photo's alt text to current_alt in descriptions.csv (the before.json values)."""
import csv, json, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
rows = list(csv.DictReader(open(os.path.join(HERE, "descriptions.csv"))))
for i in range(0, len(rows), 25):
    v = {"f": [{"id": x["media_id"], "alt": x["current_alt"]} for x in rows[i:i+25]]}
    s = subprocess.run(["shopify", "store", "execute", "--store", "7u2dfq-xf.myshopify.com", "--json", "--allow-mutations", "--query",
        "mutation($f: [FileUpdateInput!]!) { fileUpdate(files: $f) { userErrors { field message } } }", "--variables", json.dumps(v)],
        capture_output=True, text=True).stdout
    print(s[s.find("{"):][-200:])
