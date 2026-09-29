#!/usr/bin/env python3
"""Batch 03b rollback: restore main-menu, shop-categories, footer and footer-info from menus-before.json."""
import json, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
MENUS = {m["handle"]: m for m in json.load(open(os.path.join(HERE, "menus-before.json")))["menus"]["nodes"]}

def restore(item):
    out = {"title": item["title"], "type": item["type"]}
    if item.get("resourceId"): out["resourceId"] = item["resourceId"]
    elif item.get("url"): out["url"] = item["url"]
    out["items"] = [restore(c) for c in item.get("items", [])]
    return out

M = """mutation($id: ID!, $title: String!, $handle: String!, $items: [MenuItemUpdateInput!]!) {
  menuUpdate(id: $id, title: $title, handle: $handle, items: $items) { menu { handle } userErrors { field message } } }"""
for handle in ("main-menu", "shop-categories", "footer", "footer-info"):
    m = MENUS[handle]
    v = {"id": m["id"], "title": m["title"], "handle": handle, "items": [restore(i) for i in m["items"]]}
    out = subprocess.run(["shopify", "store", "execute", "--store", "7u2dfq-xf.myshopify.com", "--json", "--allow-mutations",
                          "--query", M, "--variables", json.dumps(v)], capture_output=True, text=True).stdout
    print(handle, out[out.find("{"):][:200])
