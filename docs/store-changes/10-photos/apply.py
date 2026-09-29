#!/usr/bin/env python3
"""Batch 10 apply (🟢, run only after owner approval): upload the 16 home/About/Events photos to
Content -> Files. Steps, all logged to apply-log.json:
  1. stagedUploadsCreate  -> temporary upload targets (no store content yet)
  2. POST each file to its target (Shopify's staged storage)
  3. fileCreate           -> 16 Files with alt text
  4. poll fileStatus until READY, then record each file's final CDN filename
Setting the photos on the sections is a theme change (set_templates.py), not store data.
Aborts on any userErrors or a shop-ID mismatch; rollback.py deletes whatever was created.
"""
import json, subprocess, sys, time, os
HERE = os.path.dirname(os.path.abspath(__file__))
M = json.load(open(os.path.join(HERE, "manifest.json")))
LOG = {"steps": []}

def gql(query, variables=None, mutation=True):
    cmd = ["shopify", "store", "execute", "--store", M["store"], "--json", "--query", query]
    if variables: cmd += ["--variables", json.dumps(variables)]
    if mutation: cmd.append("--allow-mutations")
    out = subprocess.run(cmd, capture_output=True, text=True)
    text = out.stdout[out.stdout.find("{"):]
    try: return json.loads(text)
    except Exception: sys.exit(f"GraphQL call failed:\n{out.stdout}\n{out.stderr}")

def save(): json.dump(LOG, open(os.path.join(HERE, "apply-log.json"), "w"), indent=1)

def check(result, field):
    errs = result[field].get("userErrors") or []
    if errs: LOG["error"] = errs; save(); sys.exit(f"{field} userErrors: {errs}")

shop = gql("{ shop { id } }", mutation=False)
if shop["shop"]["id"] != M["shop_id"]: sys.exit(f"wrong store: {shop}")

imgs = M["images"]
staged = gql("""mutation($input: [StagedUploadInput!]!) { stagedUploadsCreate(input: $input) {
  stagedTargets { url resourceUrl parameters { name value } } userErrors { field message } } }""",
  {"input": [{"filename": i["filename"], "mimeType": i["mime"], "resource": "IMAGE", "httpMethod": "POST",
              "fileSize": str(os.path.getsize(os.path.join(M["source_dir"], i["source"])))} for i in imgs]})
check(staged, "stagedUploadsCreate"); targets = staged["stagedUploadsCreate"]["stagedTargets"]
LOG["steps"].append({"staged": [t["resourceUrl"] for t in targets]}); save()

for i, t in zip(imgs, targets):
    form = sum([["-F", f"{p['name']}={p['value']}"] for p in t["parameters"]], [])
    r = subprocess.run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", *form,
                        "-F", f"file=@{os.path.join(M['source_dir'], i['source'])}", t["url"]], capture_output=True, text=True)
    if not r.stdout.startswith("2"): LOG["error"] = f"upload {i['filename']} HTTP {r.stdout}"; save(); sys.exit(LOG["error"])
LOG["steps"].append({"uploaded": len(imgs)}); save()

created = gql("""mutation($files: [FileCreateInput!]!) { fileCreate(files: $files) {
  files { id alt fileStatus } userErrors { field message code } } }""",
  {"files": [{"originalSource": t["resourceUrl"], "contentType": "IMAGE", "alt": i["alt"], "filename": i["filename"]}
             for i, t in zip(imgs, targets)]})
check(created, "fileCreate"); files = created["fileCreate"]["files"]
LOG["files"] = [{"id": f["id"], "filename": i["filename"]} for f, i in zip(files, imgs)]; save()

for _ in range(60):
    st = gql("query($ids: [ID!]!) { nodes(ids: $ids) { ... on MediaImage { id fileStatus } } }",
             {"ids": [f["id"] for f in files]}, mutation=False)
    statuses = [n["fileStatus"] for n in st["nodes"]]
    if all(s == "READY" for s in statuses): break
    if any(s == "FAILED" for s in statuses): LOG["error"] = statuses; save(); sys.exit(f"file processing failed: {statuses}")
    time.sleep(3)
else:
    LOG["error"] = "files not READY after 180s"; save(); sys.exit(LOG["error"])


done = gql("query($ids: [ID!]!) { nodes(ids: $ids) { ... on MediaImage { id image { url } } } }",
           {"ids": [f["id"] for f in files]}, mutation=False)
for entry, node in zip(LOG["files"], done["nodes"]):
    entry["cdn_filename"] = node["image"]["url"].split("/files/")[1].split("?")[0]
save()
print("batch 10 applied:", [(f["filename"], f["cdn_filename"]) for f in LOG["files"]])
