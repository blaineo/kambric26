#!/usr/bin/env python3
"""Batch 18 (GSC cleanup): (1) 14 URL redirects from redirects.csv (incl. /blogs/news -> /blogs/journal,
which only fires once the empty News blog is deleted), (2) seo.hidden = 1 on Shopify's automatic
"frontpage" collection (drops it from the sitemap), (3) article field "Products in this story"
(kambric.products, list.product_reference) + values: arielle-dress post -> Arielle Slip Dress;
chainstitch post -> Goldie Bandana, Bodie Scarf (the monogrammable accessories).
`--dry-run` prints only; apply-log.json drives rollback.py."""
import csv, json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); DRY = "--dry-run" in sys.argv
B = json.load(open(os.path.join(HERE, "before.json")))
if B["shop"]["id"] != "gid://shopify/Shop/71406846186": sys.exit("wrong store")
P = {n["handle"]: n["id"] for n in B["products"]["nodes"]}; A = {n["handle"]: n["id"] for n in B["articles"]["nodes"]}
FRONT = B["collections"]["nodes"][0]["id"]
LOG = {"redirects": [], "frontpage_hidden": False, "definition": None, "article_fields": []}
def save():
    if not DRY: json.dump(LOG, open(os.path.join(HERE, "apply-log.json"), "w"), indent=1)
def gql(q, v):
    if DRY: return None
    out = subprocess.run(["shopify", "store", "execute", "--store", "7u2dfq-xf.myshopify.com", "--json", "--allow-mutations", "--query", q, "--variables", json.dumps(v)], capture_output=True, text=True).stdout
    r = json.loads(out[out.find("{"):]); k = next(iter(r))
    if r[k].get("userErrors"): save(); sys.exit(f"{k}: {r[k]['userErrors']}")
    return r[k]
for row in csv.DictReader(open(os.path.join(HERE, "redirects.csv"))):
    print("redirect", row["Redirect from"], "->", row["Redirect to"])
    r = gql("mutation($r: UrlRedirectInput!) { urlRedirectCreate(urlRedirect: $r) { urlRedirect { id path } userErrors { field message } } }",
            {"r": {"path": row["Redirect from"], "target": row["Redirect to"]}})
    if r: LOG["redirects"].append(r["urlRedirect"]); save()
print("frontpage collection: seo.hidden = 1")
if gql("mutation($m: [MetafieldsSetInput!]!) { metafieldsSet(metafields: $m) { metafields { id } userErrors { field message } } }",
       {"m": [{"ownerId": FRONT, "namespace": "seo", "key": "hidden", "type": "number_integer", "value": "1"}]}):
    LOG["frontpage_hidden"] = True; save()
print("definition: Article kambric.products (Products in this story)")
r = gql("mutation($d: MetafieldDefinitionInput!) { metafieldDefinitionCreate(definition: $d) { createdDefinition { id } userErrors { field message } } }",
        {"d": {"name": "Products in this story", "namespace": "kambric", "key": "products", "type": "list.product_reference",
               "ownerType": "ARTICLE", "description": "Products shown under the post and linked back from their product pages.",
               "access": {"storefront": "PUBLIC_READ"}}})
if r: LOG["definition"] = r["createdDefinition"]["id"]; save()
VALUES = {"arielle-dress": ["arielle-dress"], "chainstitch": ["goldie-bandana-in-matyo-floral", "bodie-scarf-in-twilight-plumes"]}
for art, prods in VALUES.items():
    print("article", art, "->", prods)
    if gql("mutation($m: [MetafieldsSetInput!]!) { metafieldsSet(metafields: $m) { metafields { id } userErrors { field message } } }",
           {"m": [{"ownerId": A[art], "namespace": "kambric", "key": "products", "type": "list.product_reference", "value": json.dumps([P[h] for h in prods])}]}):
        LOG["article_fields"].append(A[art]); save()
print("dry run complete" if DRY else "done"); save()
