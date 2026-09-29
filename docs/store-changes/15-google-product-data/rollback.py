#!/usr/bin/env python3
"""Batch 15 rollback (apply-log.json): clear the SKUs set, delete the category fields set, restore the
4 categories (all were empty/Uncategorized before), delete the created Nylon/Lycra/Blue entries."""
import json, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); L = json.load(open(os.path.join(HERE, "apply-log.json")))
def gql(q, v):
    out = subprocess.run(["shopify", "store", "execute", "--store", "7u2dfq-xf.myshopify.com", "--json", "--allow-mutations", "--query", q, "--variables", json.dumps(v)], capture_output=True, text=True).stdout
    print(out[out.find("{"):][:160])
for h, s in L["skus"].items():
    gql("mutation($p: ID!, $v: [ProductVariantsBulkInput!]!) { productVariantsBulkUpdate(productId: $p, variants: $v) { userErrors { message } } }",
        {"p": s["productId"], "v": [{"id": vid, "inventoryItem": {"sku": ""}} for vid in s["variants"]]})
if L["metafields"]:
    gql("mutation($m: [MetafieldIdentifierInput!]!) { metafieldsDelete(metafields: $m) { userErrors { message } } }",
        {"m": [{"ownerId": m["ownerId"], "namespace": "shopify", "key": m["key"]} for m in L["metafields"]]})
for h, c in L["categories"].items():
    gql("mutation($p: ProductUpdateInput!) { productUpdate(product: $p) { userErrors { message } } }", {"p": {"id": c["id"], "category": c["before"]}})
for mid in L["metaobjects"]:
    gql("mutation($id: ID!) { metaobjectDelete(id: $id) { userErrors { message } } }", {"id": mid})
