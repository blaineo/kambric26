#!/usr/bin/env python3
"""Theme step after batch 10: point each section/block image setting at its uploaded File
(`shopify://shop_images/<cdn filename>`, the format the theme editor itself writes)."""
import json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "../../..")
M = json.load(open(os.path.join(HERE, "manifest.json"))); L = json.load(open(os.path.join(HERE, "apply-log.json")))
names = {f["filename"]: f["cdn_filename"] for f in L["files"]}
by_template = {}
for i in M["images"]: by_template.setdefault(i["template"], []).append(i)
for t, items in by_template.items():
    path = os.path.join(ROOT, "templates", f"{t}.json")
    raw = open(path).read()
    header = raw[:raw.find("{")] if raw.lstrip().startswith("/*") else ""
    data = json.loads(raw[len(header):])
    for i in items:
        sec = data["sections"][i["section"]]
        target = sec["blocks"][i["block"]] if i["block"] else sec
        target.setdefault("settings", {})[i["setting"]] = "shopify://shop_images/" + names[i["filename"]]
    open(path, "w").write(header + json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(t, len(items), "images set")
