"""Merge locale fragments (e.g. from parallel agents) into the theme locale files.

Usage: python3 merge_locales.py <fragment.json> [...]
Each fragment: {"storefront": {...}, "schema": {...}}. Conflicting leaf values abort.
"""
import json
import os
import re
import sys

THEME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "locales") + os.sep
TARGETS = {"storefront": THEME + "en.default.json", "schema": THEME + "en.default.schema.json"}


def load(path):
    raw = open(path).read()
    return json.loads(re.sub(r",(\s*[}\]])", r"\1", raw))


def merge(dst, src, path=""):
    for key, value in src.items():
        here = f"{path}.{key}" if path else key
        if isinstance(value, dict):
            node = dst.setdefault(key, {})
            if not isinstance(node, dict):
                raise SystemExit(f"conflict at {here}: string vs object")
            merge(node, value, here)
        elif key in dst and dst[key] != value:
            raise SystemExit(f"conflict at {here}: {dst[key]!r} != {value!r}")
        else:
            dst[key] = value


targets = {name: load(path) for name, path in TARGETS.items()}
for fragment_path in sys.argv[1:]:
    fragment = load(fragment_path)
    for name in TARGETS:
        merge(targets[name], fragment.get(name, {}))
    print("merged", fragment_path)

for name, path in TARGETS.items():
    open(path, "w").write(json.dumps(targets[name], indent=2, ensure_ascii=False) + "\n")
