#!/usr/bin/env python3
"""Batch 03b (run right after batch 03 has created + published the collections): menu links.

Reads the new collection IDs from apply-log.json and the current menus from menus-before.json:
  - main-menu:       Shop gets children Dresses, Kaftans, Coats, Swimwear, Accessories, Sale
  - shop-categories: All + the five categories (the Shop page's tab strip; no Sale, as live)
  - footer:          the Shop column: the five categories + Sale ("Search" dropped, as live)
  - footer-info:     appends "Your Privacy Choices" (moved from footer; Shopify's US privacy link)
Existing items keep their IDs. `--dry-run` prints the variables without calling the store.
rollback-menus.py restores all four menus from menus-before.json.
"""
import json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
STORE, SHOP_ID = "7u2dfq-xf.myshopify.com", "gid://shopify/Shop/71406846186"
DRY = "--dry-run" in sys.argv
LOG = json.load(open(os.path.join(HERE, "apply-log.json")))
MENUS = {m["handle"]: m for m in json.load(open(os.path.join(HERE, "menus-before.json")))["menus"]["nodes"]}
ids = {c["handle"]: c["id"] for c in LOG["created"]}
missing = [h for h in ("dresses", "kaftans", "coats", "swimwear", "accessories", "sale") if h not in ids]
if missing: sys.exit(f"batch 03 hasn't created: {missing}")

def gql(query, variables=None, mutation=True):
    if DRY and mutation: print("DRY", json.dumps(variables, ensure_ascii=False)[:600]); return None
    cmd = ["shopify", "store", "execute", "--store", STORE, "--json", "--query", query]
    if variables: cmd += ["--variables", json.dumps(variables)]
    if mutation: cmd.append("--allow-mutations")
    out = subprocess.run(cmd, capture_output=True, text=True).stdout
    return json.loads(out[out.find("{"):])

def keep(item):
    out = {"id": item["id"], "title": item["title"], "type": item["type"]}
    if item.get("resourceId"): out["resourceId"] = item["resourceId"]
    elif item.get("url"): out["url"] = item["url"]
    out["items"] = [keep(c) for c in item.get("items", [])]
    return out

def col(title, handle): return {"title": title, "type": "COLLECTION", "resourceId": ids[handle], "items": []}
CATS = [("Dresses", "dresses"), ("Kaftans", "kaftans"), ("Coats", "coats"), ("Swimwear", "swimwear"), ("Accessories", "accessories")]

if gql("{ shop { id } }", mutation=False)["shop"]["id"] != SHOP_ID: sys.exit("wrong store")

main = [keep(i) for i in MENUS["main-menu"]["items"]]
for i in main:
    if i["title"] == "Shop": i["items"] = [col(t, h) for t, h in CATS] + [col("Sale", "sale")]
tabs = [keep(i) for i in MENUS["shop-categories"]["items"] if i["type"] == "CATALOG"] + [col(t, h) for t, h in CATS]
privacy = [keep(i) for i in MENUS["footer"]["items"] if i["title"] == "Your Privacy Choices"]
footer = [col(t, h) for t, h in CATS] + [col("Sale", "sale")]
info = [keep(i) for i in MENUS["footer-info"]["items"]] + [{k: v for k, v in p.items() if k != "id"} for p in privacy]

M = """mutation($id: ID!, $title: String!, $handle: String!, $items: [MenuItemUpdateInput!]!) {
  menuUpdate(id: $id, title: $title, handle: $handle, items: $items) { menu { handle items { title url items { title url } } } userErrors { field message } } }"""
result = {}
for handle, items in (("main-menu", main), ("shop-categories", tabs), ("footer", footer), ("footer-info", info)):
    m = MENUS[handle]
    r = gql(M, {"id": m["id"], "title": m["title"], "handle": handle, "items": items})
    if r is None: continue
    errs = r["menuUpdate"]["userErrors"]
    if errs: sys.exit(f"{handle}: {errs} (rollback-menus.py restores all four)")
    result[handle] = r["menuUpdate"]["menu"]
if not DRY:
    json.dump(result, open(os.path.join(HERE, "menus-apply-result.json"), "w"), indent=1, ensure_ascii=False)
    print("menus updated:", list(result))
