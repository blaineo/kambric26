#!/usr/bin/env python3
"""Batch 15 (owner-approved 2026-09-29: "batch them all, the shop owner will edit where necessary"):
product data for Google free listings. Draft values from the product descriptions; the owner reviews.

  1. Categories (Google taxonomy): Jessie -> Dresses, Bodie -> Scarves & Shawls,
     Goldie -> Bandanas & Headties, Esther -> Kaftans.
  2. Category fields: Fabric and Color/pattern on the 6 products missing them (new taxonomy
     entries Nylon, Lycra, Blue are created first).
  3. SKUs on every variant of the active catalog: KG-<PRODUCT>-<PRINT>-<SIZE>
     (single-print products carry their print; the monogram fee is KG-MONOGRAM).

`--dry-run` prints everything and writes nothing. Stops at the first userError; apply-log.json
records what was done for rollback.py.
"""
import json, os, re, subprocess, sys, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__))
STORE, SHOP_ID = "7u2dfq-xf.myshopify.com", "gid://shopify/Shop/71406846186"
DRY = "--dry-run" in sys.argv
B = json.load(open(os.path.join(HERE, "before.json")))
if B["shop"]["id"] != SHOP_ID: sys.exit("wrong store")
P = {p["handle"]: p for p in B["products"]["nodes"]}
FAB = {m["displayName"]: m["id"] for m in B["fab"]["nodes"]}
COL = {m["displayName"]: m["id"] for m in B["col"]["nodes"]}
LOG = {"metaobjects": [], "categories": {}, "metafields": [], "skus": {}}

def save():
    if not DRY: json.dump(LOG, open(os.path.join(HERE, "apply-log.json"), "w"), indent=1, ensure_ascii=False)

def gql(q, v=None, m=True):
    if DRY and m: return None
    cmd = ["shopify", "store", "execute", "--store", STORE, "--json", "--query", q] + (["--variables", json.dumps(v)] if v else []) + (["--allow-mutations"] if m else [])
    out = subprocess.run(cmd, capture_output=True, text=True)
    try: return json.loads(out.stdout[out.stdout.find("{"):])
    except Exception: save(); sys.exit(f"call failed: {out.stdout[-400:]} {out.stderr[-400:]}")

def check(r, field):
    if r is None: return None
    errs = r[field].get("userErrors") or []
    if errs: save(); sys.exit(f"{field}: {errs}")
    return r[field]

# 1. New taxonomy entries ------------------------------------------------------------------------
NEW = [("shopify--fabric", "Nylon", [("label", "Nylon"), ("taxonomy_reference", "gid://shopify/TaxonomyValue/16990")]),
       ("shopify--fabric", "Lycra", [("label", "Lycra"), ("taxonomy_reference", "gid://shopify/TaxonomyValue/1007")]),
       ("shopify--color-pattern", "Blue", [("label", "Blue"), ("color", "#2F4B8A"),
         ("color_taxonomy_reference", '["gid://shopify/TaxonomyValue/2"]'), ("pattern_taxonomy_reference", "gid://shopify/TaxonomyValue/2874")])]
for mtype, name, fields in NEW:
    pool = FAB if mtype == "shopify--fabric" else COL
    if name in pool: continue
    print(f"create {mtype} {name}")
    r = check(gql("mutation($m: MetaobjectCreateInput!) { metaobjectCreate(metaobject: $m) { metaobject { id } userErrors { field message } } }",
                  {"m": {"type": mtype, "fields": [{"key": k, "value": v} for k, v in fields]}}), "metaobjectCreate")
    pool[name] = r["metaobject"]["id"] if r else f"<new {name}>"
    if r: LOG["metaobjects"].append(pool[name]); save()

# 2. Categories ----------------------------------------------------------------------------------
CATS = {"jessie-slip-dress-in-twilight-plumes": "aa-1-4", "bodie-scarf-in-twilight-plumes": "aa-2-26",
        "goldie-bandana-in-matyo-floral": "aa-2-4", "esther-kaftan": "aa-1-23-12"}
for h, cat in CATS.items():
    p = P[h]; print(f"category {h}: {(p['category'] or {}).get('id')} -> {cat}")
    r = check(gql("mutation($p: ProductUpdateInput!) { productUpdate(product: $p) { product { id category { id } } userErrors { field message } } }",
                  {"p": {"id": p["id"], "category": f"gid://shopify/TaxonomyCategory/{cat}"}}), "productUpdate")
    if r: LOG["categories"][h] = {"id": p["id"], "before": (p["category"] or {}).get("id")}; save()

# 3. Fabric + Color/pattern ----------------------------------------------------------------------
ATTR = {  # from the product descriptions; the owner corrects anything off
    "kati-slip-dress-in-matyo-floral":      (["Viscose"], ["Floral", "Red"]),
    "jessie-slip-dress-in-twilight-plumes": (["Viscose"], ["Blue", "Floral"]),
    "bodie-scarf-in-twilight-plumes":       (["Silk", "Cotton"], ["Blue", "Floral"]),
    "goldie-bandana-in-matyo-floral":       (["Cotton"], ["Floral", "Red"]),
    "margit-one-piece":                     (["Nylon", "Lycra"], ["Geometric", "Floral"]),
    "esther-kaftan":                        (["Viscose"], ["Geometric", "Floral"]),
}
mf = []
for h, (fabs, cols) in ATTR.items():
    p = P[h]
    if not p["fabric"]: mf.append({"ownerId": p["id"], "namespace": "shopify", "key": "fabric", "type": "list.metaobject_reference", "value": json.dumps([FAB[f] for f in fabs])})
    if not p["color"]: mf.append({"ownerId": p["id"], "namespace": "shopify", "key": "color-pattern", "type": "list.metaobject_reference", "value": json.dumps([COL[c] for c in cols])})
    print(f"fields {h}: fabric {fabs if not p['fabric'] else '(kept)'} color {cols if not p['color'] else '(kept)'}")
r = check(gql("mutation($m: [MetafieldsSetInput!]!) { metafieldsSet(metafields: $m) { metafields { id key owner { ... on Product { handle } } } userErrors { field message } } }", {"m": mf}), "metafieldsSet")
if r: LOG["metafields"] = [{"ownerId": m["ownerId"], "key": m["key"]} for m in mf]; save()

# 4. SKUs ----------------------------------------------------------------------------------------
def code(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^A-Z0-9]+", "", s.upper())
PRODUCT_CODE = {"kati-slip-dress-in-matyo-floral": "KATI", "jessie-slip-dress-in-twilight-plumes": "JESSIE",
                "bodie-scarf-in-twilight-plumes": "BODIE", "goldie-bandana-in-matyo-floral": "GOLDIE",
                "margit-one-piece": "MARGIT", "zadie-linen-dress": "ZADIE", "esther-kaftan": "ESTHER",
                "vera-car-coat": "VERA", "arielle-dress": "ARIELLE", "chainstitch-monogram": "MONOGRAM"}
SINGLE_PRINT = {"kati-slip-dress-in-matyo-floral": "MATYO", "goldie-bandana-in-matyo-floral": "MATYO",
                "jessie-slip-dress-in-twilight-plumes": "TWILIGHT", "bodie-scarf-in-twilight-plumes": "TWILIGHT"}
PRINT_CODE = {"Dahlia Seed": "DAHLIA", "Moon Illusion": "MOON", "Good Vibrations": "GOODVIBES", "Pastel Asterisk": "PASTEL",
              "Orange Asterisk": "ORANGE", "Magnolia": "MAGNOLIA", "Matyó Floral": "MATYO", "Wildflowers": "WILDFLOWERS",
              "Candied Plaid": "PLAID", "Cherry Coupe": "CHERRY", "Midnight Plumes": "MIDNIGHT", "Terracotta": "TERRACOTTA", "Olive": "OLIVE"}
seen = set()
for h, p in P.items():
    if h not in PRODUCT_CODE: continue
    updates = []
    for v in p["variants"]["nodes"]:
        if v["sku"]: continue
        opts = {o["name"]: o["value"] for o in v["selectedOptions"]}
        parts = ["KG", PRODUCT_CODE[h]]
        pr = opts.get("Print") or opts.get("Colorway")
        if pr: parts.append(PRINT_CODE.get(pr, code(pr)))
        elif h in SINGLE_PRINT: parts.append(SINGLE_PRINT[h])
        size = opts.get("Size")
        if size and size.lower() not in ("default title", "one size", "os"): parts.append("-".join(code(x) for x in size.split("/")))
        sku = "-".join(parts)
        if sku in seen: sku += "-" + v["id"].split("/")[-1][-4:]
        seen.add(sku); updates.append({"id": v["id"], "inventoryItem": {"sku": sku}})
    if not updates: continue
    print(f"skus {h}: {len(updates)} e.g. {updates[0]['inventoryItem']['sku']}")
    r = check(gql("mutation($p: ID!, $v: [ProductVariantsBulkInput!]!) { productVariantsBulkUpdate(productId: $p, variants: $v) { productVariants { id sku } userErrors { field message } } }",
                  {"p": p["id"], "v": updates}), "productVariantsBulkUpdate")
    if r: LOG["skus"][h] = {"productId": p["id"], "variants": [u["id"] for u in updates]}; save()

print("dry run complete" if DRY else "done"); save()
