#!/usr/bin/env python3
"""Batch 08 (🟢, run only after owner approval): Phase 4 content import. Shopify-hosted only.

  1. Pages: create about, events, wholesale, size-guide, shipping, returns; update the existing
     `contact` page (title, body, SEO). Bodies come from store-data/phase4/pages/*.html with the
     leading <h1> (the theme renders the title) and the CTA links (now template button blocks) removed.
  2. Blog `journal` (comments closed) + its 5 posts (cover image fetched by Shopify from the export URL).
  3. Metaobject definition `kambric_event` + the 3 exported events.
  4. Menus: add Story / Events / Journal to `main-menu`; fill `footer-info` with the 5 info pages.

`--dry-run` builds and prints every mutation's variables without calling the store.
Stops at the first userError; everything created so far is in apply-log.json for rollback.py.
"""
import json, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "../../store-data/phase4")
STORE, SHOP_ID = "7u2dfq-xf.myshopify.com", "gid://shopify/Shop/71406846186"
DRY = "--dry-run" in sys.argv
BEFORE = json.load(open(os.path.join(HERE, "before.json")))
CONTACT_ID = "gid://shopify/Page/113644699882"
LOG = {"pages_created": [], "contact_updated": False, "blog": None, "articles": [],
       "definition": None, "events": [], "menus_updated": []}

def save():
    if not DRY: json.dump(LOG, open(os.path.join(HERE, "apply-log.json"), "w"), indent=1)

def gql(query, variables=None, mutation=True):
    if DRY and mutation:
        name = re.search(r"\{\s*(\w+)", query).group(1)
        print(f"DRY {name}: {json.dumps(variables, ensure_ascii=False)[:400]}")
        return None
    cmd = ["shopify", "store", "execute", "--store", STORE, "--json", "--query", query]
    if variables: cmd += ["--variables", json.dumps(variables)]
    if mutation: cmd.append("--allow-mutations")
    out = subprocess.run(cmd, capture_output=True, text=True)
    try: return json.loads(out.stdout[out.stdout.find("{"):])
    except Exception: LOG["error"] = out.stdout + out.stderr; save(); sys.exit(f"GraphQL call failed:\n{out.stdout}\n{out.stderr}")

def run(query, variables, field):
    r = gql(query, variables)
    if r is None: return None
    errs = r[field].get("userErrors") or []
    if errs: LOG["error"] = {field: errs, "variables": variables}; save(); sys.exit(f"{field} userErrors: {errs}")
    return r[field]

def seo(title=None, description=None):
    m = []
    if title: m.append({"namespace": "global", "key": "title_tag", "type": "single_line_text_field", "value": title})
    if description: m.append({"namespace": "global", "key": "description_tag", "type": "single_line_text_field", "value": description})
    return m

def page_body(file):
    html = open(os.path.join(DATA, "pages", file)).read()
    html = re.sub(r"^\s*<h1>.*?</h1>\s*", "", html, flags=re.S)             # title is the theme's H1
    html = re.sub(r"\s*<p><a [^>]*>[^<]*</a></p>", "", html)                 # CTAs are button blocks
    if file == "size-guide.html":  # table + fit note are the template's size-table section
        html = html.split("<h2>", 1)[0]
    return html.strip()

shop = gql("{ shop { id } }", mutation=False)
if shop["shop"]["id"] != SHOP_ID: sys.exit(f"wrong store: {shop}")
if any(p["handle"] != "contact" and p["handle"] in
       {"about", "events", "wholesale", "size-guide", "shipping", "returns"} for p in BEFORE["pages"]["nodes"]):
    sys.exit("a page handle already exists: re-snapshot and review")

# 1. Pages -----------------------------------------------------------------------------------
PAGE_CREATE = """mutation($page: PageCreateInput!) { pageCreate(page: $page) {
  page { id handle templateSuffix } userErrors { field message code } } }"""
PAGE_UPDATE = """mutation($id: ID!, $page: PageUpdateInput!) { pageUpdate(id: $id, page: $page) {
  page { id handle title } userErrors { field message code } } }"""

page_ids = {"contact": CONTACT_ID}
new_pages = [
    {"title": "About", "handle": "about", "templateSuffix": "about", "body": "", "isPublished": True,
     "metafields": seo("About | Kambric Goods", "The story of Kambric Goods: designer Daisy Hartmann reviving her grandmother Kati's archive of 300+ hand-painted mid-century textile prints from Montreal.")},
    {"title": "Events", "handle": "events", "templateSuffix": "events", "body": "", "isPublished": True,
     "metafields": seo("Events | Kambric Goods", "Find Kambric Goods in person — pop-ups, markets, and trunk shows across the Bay Area and beyond.")},
]
for p in json.load(open(os.path.join(DATA, "pages/pages.json"))):
    spec = {"title": p["title"], "body": page_body(p["body_file"]),
            "templateSuffix": p["handle"], "metafields": seo(p["seo"]["title"], p["seo"]["description"])}
    if p["handle"] == "contact":
        r = run(PAGE_UPDATE, {"id": CONTACT_ID, "page": spec}, "pageUpdate")
        LOG["contact_updated"] = True; save()
    else:
        new_pages.append({**spec, "handle": p["handle"], "isPublished": True})
for spec in new_pages:
    r = run(PAGE_CREATE, {"page": spec}, "pageCreate")
    pid = r["page"]["id"] if r else f"<{spec['handle']}>"
    page_ids[spec["handle"]] = pid
    if r: LOG["pages_created"].append({"handle": spec["handle"], "id": pid}); save()

# 2. Journal ---------------------------------------------------------------------------------
r = run("""mutation($blog: BlogCreateInput!) { blogCreate(blog: $blog) {
  blog { id handle } userErrors { field message code } } }""",
        {"blog": {"title": "Journal", "handle": "journal", "commentPolicy": "CLOSED"}}, "blogCreate")
blog_id = r["blog"]["id"] if r else "<journal>"
if r: LOG["blog"] = blog_id; save()

for post in json.load(open(os.path.join(DATA, "journal/posts.json"))):
    article = {"blogId": blog_id, "title": post["title"], "handle": post["handle"],
               "body": post["body_html"], "summary": post["summary_html"], "tags": post["tags"],
               "isPublished": True, "publishDate": post["published_at"], "author": {"name": "Kambric Goods"},
               "image": {"url": post["image"]["source_url"], "altText": post["image"]["alt"]},
               "metafields": seo(None, post["seo"]["description"])}
    r = run("""mutation($article: ArticleCreateInput!) { articleCreate(article: $article) {
      article { id handle } userErrors { field message code } } }""", {"article": article}, "articleCreate")
    if r: LOG["articles"].append({"handle": post["handle"], "id": r["article"]["id"]}); save()

# 3. Events ----------------------------------------------------------------------------------
def fd(key, name, type_, description=None, validations=None, required=False):
    d = {"key": key, "name": name, "type": type_, "required": required}
    if description: d["description"] = description
    if validations: d["validations"] = validations
    return d

definition = {"name": "Event", "type": "kambric_event", "displayNameKey": "title",
              "access": {"storefront": "PUBLIC_READ"},
              "fieldDefinitions": [
    fd("title", "Title", "single_line_text_field", required=True),
    fd("start_date", "Start date", "date", "Leave blank for a TBA / undated event."),
    fd("date_label", "Date label override", "single_line_text_field",
       'Shown instead of the formatted Start date, e.g. "TBA" or "Summer 2026".'),
    fd("time_label", "Time", "single_line_text_field", 'e.g. "6-8pm". Only shown on upcoming events.'),
    fd("venue", "Venue", "single_line_text_field"),
    fd("city", "City", "single_line_text_field"),
    fd("description", "Description", "multi_line_text_field"),
    fd("image", "Image", "file_reference", "Not shown on the page; used in the event's structured data.",
       [{"name": "file_type_options", "value": '["Image"]'}]),
    fd("url", "URL", "url", "Optional RSVP, Instagram post or venue link."),
    fd("status_override", "Status override", "single_line_text_field",
       "Only for an undated event that should list as past, or to force a dated event into the other list.",
       [{"name": "choices", "value": '["upcoming","past"]'}]),
]}
r = run("""mutation($definition: MetaobjectDefinitionCreateInput!) { metaobjectDefinitionCreate(definition: $definition) {
  metaobjectDefinition { id type } userErrors { field message code } } }""", {"definition": definition},
        "metaobjectDefinitionCreate")
if r: LOG["definition"] = r["metaobjectDefinition"]["id"]; save()

for ev in json.load(open(os.path.join(DATA, "events/events.json"))):
    f = ev["fields"]
    fields = [{"key": k, "value": f[k]} for k in ("title", "start_date", "time_label", "venue", "city", "description") if f.get(k)]
    r = run("""mutation($metaobject: MetaobjectCreateInput!) { metaobjectCreate(metaobject: $metaobject) {
      metaobject { id handle } userErrors { field message code } } }""",
            {"metaobject": {"type": "kambric_event", "handle": ev["handle"], "fields": fields}}, "metaobjectCreate")
    if r: LOG["events"].append({"handle": ev["handle"], "id": r["metaobject"]["id"]}); save()

# 4. Menus -----------------------------------------------------------------------------------
MENU_UPDATE = """mutation($id: ID!, $title: String!, $handle: String!, $items: [MenuItemUpdateInput!]!) {
  menuUpdate(id: $id, title: $title, handle: $handle, items: $items) {
    menu { id handle items { title url } } userErrors { field message code } } }"""

def keep(item):  # an existing item, re-sent as-is (ids keep it the same item)
    out = {"id": item["id"], "title": item["title"], "type": item["type"]}
    if item.get("resourceId"): out["resourceId"] = item["resourceId"]
    elif item.get("url"): out["url"] = item["url"]
    out["items"] = [keep(c) for c in item.get("items", [])]
    return out

menus = {m["handle"]: m for m in BEFORE["menus"]["nodes"]}
main = menus["main-menu"]
run(MENU_UPDATE, {"id": main["id"], "title": main["title"], "handle": "main-menu", "items":
    [keep(i) for i in main["items"]] + [
        {"title": "Story", "type": "PAGE", "resourceId": page_ids["about"]},
        {"title": "Events", "type": "PAGE", "resourceId": page_ids["events"]},
        {"title": "Journal", "type": "BLOG", "resourceId": blog_id}]}, "menuUpdate")
LOG["menus_updated"].append("main-menu"); save()

info = menus["footer-info"]
run(MENU_UPDATE, {"id": info["id"], "title": info["title"], "handle": "footer-info", "items": [
    {"title": t, "type": "PAGE", "resourceId": page_ids[h]} for t, h in
    [("Contact Us", "contact"), ("Wholesale", "wholesale"), ("Size Guide", "size-guide"),
     ("Shipping", "shipping"), ("Returns & Exchanges", "returns")]]}, "menuUpdate")
LOG["menus_updated"].append("footer-info"); save()

print("dry run complete" if DRY else f"done: {json.dumps(LOG)}")
