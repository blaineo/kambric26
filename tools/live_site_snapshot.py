#!/usr/bin/env python3
"""Snapshot what kambricgoods.com (the live Replit site) publicly serves, and diff snapshots.

Read-only: GET requests to the live site's public endpoints only. Used around every
approved store-change batch (docs/store-changes/README.md): snapshot before, snapshot
after, diff. Any difference in catalog data means the batch touched the live site ->
stop and roll back.

Usage:
  tools/live_site_snapshot.py snapshot <out.json>
  tools/live_site_snapshot.py diff <before.json> <after.json>   # exit 1 on differences
"""
import json
import re
import sys
import urllib.request

BASE = "https://kambricgoods.com"
ENDPOINTS = ["/api/collections", "/api/products", "/api/product-redirects", "/api/monogram"]
# Volatile keys that change without any store edit (cache stamps etc.).
VOLATILE = {"updatedAt", "createdAt", "generatedAt", "cachedAt", "timestamp"}


def get(path):
    req = urllib.request.Request(BASE + path, headers={"User-Agent": "kambric26-snapshot"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode()


def scrub(value):
    if isinstance(value, dict):
        return {k: scrub(v) for k, v in sorted(value.items()) if k not in VOLATILE}
    if isinstance(value, list):
        return [scrub(v) for v in value]
    return value


def snapshot():
    data = {path: scrub(json.loads(get(path))) for path in ENDPOINTS}
    collections = data["/api/collections"]
    items = collections if isinstance(collections, list) else collections.get("collections", [])
    for col in items:
        slug = col.get("slug") or col.get("handle")
        if slug:
            path = f"/api/collections/{slug}"
            data[path] = scrub(json.loads(get(path)))
    sitemap = get("/sitemap.xml")
    data["/sitemap.xml#locs"] = sorted(re.findall(r"<loc>([^<]+)</loc>", sitemap))
    return data


def diff(before, after):
    changes = []
    for key in sorted(set(before) | set(after)):
        if before.get(key) != after.get(key):
            changes.append(key)
    return changes


def main():
    if len(sys.argv) == 3 and sys.argv[1] == "snapshot":
        data = snapshot()
        with open(sys.argv[2], "w") as fh:
            json.dump(data, fh, indent=1, sort_keys=True, ensure_ascii=False)
        print(f"snapshot: {len(data)} endpoints -> {sys.argv[2]}")
    elif len(sys.argv) == 4 and sys.argv[1] == "diff":
        before, after = (json.load(open(p)) for p in sys.argv[2:4])
        changes = diff(before, after)
        if changes:
            print("LIVE SITE CHANGED:", *changes, sep="\n  ")
            sys.exit(1)
        print(f"no change on kambricgoods.com ({len(before)} endpoints compared)")
    else:
        print(__doc__)
        sys.exit(2)


if __name__ == "__main__":
    main()
