#!/usr/bin/env python3
"""Batch 08 rollback: undo exactly what apply-log.json says was done, newest first.

  1. Menus: restore `main-menu` and `footer-info` items from before.json.
  2. Delete the 3 events, then the `kambric_event` definition.
  3. Delete the 5 articles, then the `journal` blog.
  4. Delete the created pages; restore the `contact` page (title, empty body, no SEO fields)
     from before-contact.json.
`--dry-run` prints the plan without calling the store.
"""
import json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
STORE, SHOP_ID = "7u2dfq-xf.myshopify.com", "gid://shopify/Shop/71406846186"
DRY = "--dry-run" in sys.argv
LOG = json.load(open(os.path.join(HERE, "apply-log.json")))
BEFORE = json.load(open(os.path.join(HERE, "before.json")))
CONTACT = json.load(open(os.path.join(HERE, "before-contact.json")))["pages"]["nodes"][0]

def gql(query, variables=None, mutation=True):
    if DRY and mutation: print("DRY", query.split("(")[0].split()[-1], json.dumps(variables)[:300]); return None
    cmd = ["shopify", "store", "execute", "--store", STORE, "--json", "--query", query]
    if variables: cmd += ["--variables", json.dumps(variables)]
    if mutation: cmd.append("--allow-mutations")
    out = subprocess.run(cmd, capture_output=True, text=True).stdout
    r = json.loads(out[out.find("{"):])
    for v in r.values():
        if isinstance(v, dict) and v.get("userErrors"): print("userErrors:", v["userErrors"])
    return r

if gql("{ shop { id } }", mutation=False)["shop"]["id"] != SHOP_ID: sys.exit("wrong store")

def restore(item):
    out = {"title": item["title"], "type": item["type"]}
    if item.get("resourceId"): out["resourceId"] = item["resourceId"]
    elif item.get("url"): out["url"] = item["url"]
    out["items"] = [restore(c) for c in item.get("items", [])]
    return out

menus = {m["handle"]: m for m in BEFORE["menus"]["nodes"]}
for handle in reversed(LOG["menus_updated"]):
    m = menus[handle]
    gql("""mutation($id: ID!, $title: String!, $handle: String!, $items: [MenuItemUpdateInput!]!) {
      menuUpdate(id: $id, title: $title, handle: $handle, items: $items) { menu { id } userErrors { field message } } }""",
        {"id": m["id"], "title": m["title"], "handle": handle, "items": [restore(i) for i in m["items"]]})

for e in LOG["events"]:
    gql("mutation($id: ID!) { metaobjectDelete(id: $id) { deletedId userErrors { field message } } }", {"id": e["id"]})
if LOG["definition"]:
    gql("mutation($id: ID!) { metaobjectDefinitionDelete(id: $id) { deletedId userErrors { field message } } }",
        {"id": LOG["definition"]})

for a in LOG["articles"]:
    gql("mutation($id: ID!) { articleDelete(id: $id) { deletedArticleId userErrors { field message } } }", {"id": a["id"]})
if LOG["blog"]:
    gql("mutation($id: ID!) { blogDelete(id: $id) { deletedBlogId userErrors { field message } } }", {"id": LOG["blog"]})

for p in LOG["pages_created"]:
    gql("mutation($id: ID!) { pageDelete(id: $id) { deletedPageId userErrors { field message } } }", {"id": p["id"]})
if LOG["contact_updated"]:
    gql("""mutation($id: ID!, $page: PageUpdateInput!) { pageUpdate(id: $id, page: $page) {
      page { id title } userErrors { field message } } }""",
        {"id": CONTACT["id"], "page": {"title": CONTACT["title"], "body": CONTACT["body"], "templateSuffix": CONTACT["templateSuffix"]}})
    r = gql("""{ page(id: "%s") { t: metafield(namespace: "global", key: "title_tag") { id }
      d: metafield(namespace: "global", key: "description_tag") { id } } }""" % CONTACT["id"], mutation=False)
    ids = [{"ownerId": CONTACT["id"], "namespace": "global", "key": k}
           for k, alias in (("title_tag", "t"), ("description_tag", "d")) if r["page"][alias]]
    if ids:
        gql("mutation($m: [MetafieldIdentifierInput!]!) { metafieldsDelete(metafields: $m) { deletedMetafields { key } userErrors { field message } } }",
            {"m": ids})
print("rollback complete" if not DRY else "dry run complete")
