#!/usr/bin/env python3
"""Batch 06 apply (run only after owner approval): create the 68 URL redirects from
docs/redirects-draft.csv, 17 per request (aliased urlRedirectCreate). Rows that Shopify
rejects (userErrors) create nothing and are reported; every created ID goes to apply-log.json.
Redirects only fire on the Shopify-hosted storefront; kambricgoods.com (Replit) is a separate app."""
import csv, json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
STORE, SHOP_ID = "7u2dfq-xf.myshopify.com", "gid://shopify/Shop/71406846186"
rows = list(csv.DictReader(open(os.path.join(HERE, "../../redirects-draft.csv"))))

def gql(q, mutation=True):
    cmd = ["shopify", "store", "execute", "--store", STORE, "--json", "--query", q] + (["--allow-mutations"] if mutation else [])
    out = subprocess.run(cmd, capture_output=True, text=True).stdout
    return json.loads(out[out.find("{"):])

if gql("{ shop { id } }", False)["shop"]["id"] != SHOP_ID: sys.exit("wrong store")
log = {"created": [], "rejected": []}
for start in range(0, len(rows), 17):
    chunk = rows[start:start + 17]
    body = "\n".join(
        f'r{i}: urlRedirectCreate(urlRedirect: {{ path: {json.dumps(r["Redirect from"])}, target: {json.dumps(r["Redirect to"])} }}) '
        f'{{ urlRedirect {{ id path target }} userErrors {{ field message code }} }}' for i, r in enumerate(chunk))
    res = gql("mutation {\n" + body + "\n}")
    for i, r in enumerate(chunk):
        x = res[f"r{i}"]
        if x["userErrors"]: log["rejected"].append({"path": r["Redirect from"], "target": r["Redirect to"], "errors": x["userErrors"]})
        else: log["created"].append(x["urlRedirect"])
    json.dump(log, open(os.path.join(HERE, "apply-log.json"), "w"), indent=1)
print(f"created {len(log['created'])}, rejected {len(log['rejected'])}")
for r in log["rejected"]: print("  rejected:", r["path"], r["errors"])
