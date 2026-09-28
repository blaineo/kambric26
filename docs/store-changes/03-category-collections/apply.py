#!/usr/bin/env python3
"""Batch 03 (🔴, run AT CUTOVER only, after owner approval): create the 5 category
collections + Sale as automated collections AND publish them to the Online Store channel.

Publishing to Online Store makes them visible on kambricgoods.com too (finding.md), which is
why this waits for cutover. `--dry-run` prints every mutation without touching the store.

Rules checked read-only on 2026-09-28 (rule-check-products.json): Dresses 4 products,
Kaftans 1, Coats 1, Swimwear 1, Accessories 2, Sale 1 (Margit); the monogram fee is excluded
by the hidden-tag rule. Re-run the rule check before cutover if the catalog changed.
"""
import csv, json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
STORE, SHOP_ID = "7u2dfq-xf.myshopify.com", "gid://shopify/Shop/71406846186"
ONLINE_STORE = "gid://shopify/Publication/134219858154"  # verified in before.json
DRY = "--dry-run" in sys.argv
COPY = {r["collection_handle"]: r for r in csv.DictReader(open(os.path.join(HERE, "../../store-data/collection-copy.csv")))}
NOT_HIDDEN = {"column": "TAG", "relation": "NOT_EQUALS", "condition": "hidden"}

def spec(handle, title, rule, template):
    c = COPY[handle]
    desc = c["description_to_set"].strip()
    seo_title, seo_desc = c["seo_title"].strip(), c["seo_description"].strip()
    if handle == "sale":  # the old sale copy is stale promo text: the owner writes new copy
        desc = seo_desc = ""; seo_title = "Sale | Kambric Goods"
    return {"title": title, "handle": handle, "templateSuffix": template,
            "descriptionHtml": f"<p>{desc}</p>" if desc else "",
            "seo": {"title": seo_title, "description": seo_desc},
            "ruleSet": {"appliedDisjunctively": False, "rules": [rule, NOT_HIDDEN]}}

COLLECTIONS = [spec(h, t, {"column": "TYPE", "relation": "EQUALS", "condition": t}, "category")
               for h, t in [("dresses", "Dresses"), ("kaftans", "Kaftans"), ("coats", "Coats"),
                            ("swimwear", "Swimwear"), ("accessories", "Accessories")]]
COLLECTIONS.append(spec("sale", "Sale", {"column": "VARIANT_COMPARE_AT_PRICE", "relation": "GREATER_THAN", "condition": "0"}, "sale"))

CREATE = """mutation($input: CollectionInput!) { collectionCreate(input: $input) {
  collection { id handle templateSuffix } userErrors { field message } } }"""
PUBLISH = """mutation($id: ID!, $pub: ID!) { publishablePublish(id: $id, input: [{ publicationId: $pub }]) {
  userErrors { field message } } }"""

def gql(query, variables=None, mutation=True):
    if DRY and mutation:
        print("DRY RUN", query.split("(")[0].replace("mutation", "").strip() or "mutation", json.dumps(variables, ensure_ascii=False)); return None
    cmd = ["shopify", "store", "execute", "--store", STORE, "--json", "--query", query]
    if variables: cmd += ["--variables", json.dumps(variables)]
    if mutation: cmd.append("--allow-mutations")
    out = subprocess.run(cmd, capture_output=True, text=True).stdout
    return json.loads(out[out.find("{"):])

shop = gql("{ shop { id } }", mutation=False)
if shop["shop"]["id"] != SHOP_ID: sys.exit(f"wrong store: {shop}")
log = {"created": []}
for c in COLLECTIONS:
    r = gql(CREATE, {"input": c})
    if DRY: gql(PUBLISH, {"id": f"<id of {c['handle']}>", "pub": ONLINE_STORE}); continue
    errs = r["collectionCreate"]["userErrors"]
    if errs: log["error"] = errs; break
    cid = r["collectionCreate"]["collection"]["id"]; log["created"].append({"handle": c["handle"], "id": cid})
    p = gql(PUBLISH, {"id": cid, "pub": ONLINE_STORE})
    if p["publishablePublish"]["userErrors"]: log["error"] = p["publishablePublish"]["userErrors"]; break
if not DRY:
    json.dump(log, open(os.path.join(HERE, "apply-log.json"), "w"), indent=1)
    sys.exit(f"stopped: {log['error']} (rollback.py removes what was created)") if "error" in log else print("created + published:", [c["handle"] for c in log["created"]])
