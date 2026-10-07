#!/usr/bin/env python3
"""Batch 18 rollback: delete the redirects and article values created, the article field definition,
and the frontpage seo.hidden flag (apply-log.json)."""
import json, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); L = json.load(open(os.path.join(HERE, "apply-log.json")))
B = json.load(open(os.path.join(HERE, "before.json")))
def gql(q, v):
    out = subprocess.run(["shopify", "store", "execute", "--store", "7u2dfq-xf.myshopify.com", "--json", "--allow-mutations", "--query", q, "--variables", json.dumps(v)], capture_output=True, text=True).stdout
    print(out[out.find("{"):][:120])
for r in L["redirects"]: gql("mutation($id: ID!) { urlRedirectDelete(id: $id) { userErrors { message } } }", {"id": r["id"]})
if L["article_fields"]: gql("mutation($m: [MetafieldIdentifierInput!]!) { metafieldsDelete(metafields: $m) { userErrors { message } } }", {"m": [{"ownerId": a, "namespace": "kambric", "key": "products"} for a in L["article_fields"]]})
if L["definition"]: gql("mutation($id: ID!) { metafieldDefinitionDelete(id: $id, deleteAllAssociatedMetafields: true) { userErrors { message } } }", {"id": L["definition"]})
if L["frontpage_hidden"]: gql("mutation($m: [MetafieldIdentifierInput!]!) { metafieldsDelete(metafields: $m) { userErrors { message } } }", {"m": [{"ownerId": B["collections"]["nodes"][0]["id"], "namespace": "seo", "key": "hidden"}]})
