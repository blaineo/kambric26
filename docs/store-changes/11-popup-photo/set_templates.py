#!/usr/bin/env python3
"""Theme step after batch 11: set the pop-up image setting to the uploaded File."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, "../../..")
M = json.load(open(os.path.join(HERE, "manifest.json"))); L = json.load(open(os.path.join(HERE, "apply-log.json")))
names = {f["filename"]: f["cdn_filename"] for f in L["files"]}
for i in M["images"]:
    path = os.path.join(ROOT, i["file"]); raw = open(path).read()
    header = raw[:raw.find("{")] if raw.lstrip().startswith("/*") else ""
    data = json.loads(raw[len(header):])
    data["sections"][i["section"]].setdefault("settings", {})[i["setting"]] = "shopify://shop_images/" + names[i["filename"]]
    open(path, "w").write(header + json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(i["file"], "set")
