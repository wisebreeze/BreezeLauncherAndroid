#!/usr/bin/env python3
"""Patch parts[].url in update.json for a given part name.

Usage: patch_part_url.py <part_name> <part_url>

Called by release-on-tag.yml after each split part is uploaded to the
Gitee release, so update.json on main always reflects the latest
uploaded part URL.
"""
import json
import sys

if len(sys.argv) != 3:
    print(f"usage: {sys.argv[0]} <part_name> <part_url>", file=sys.stderr)
    sys.exit(2)

name, url = sys.argv[1], sys.argv[2]
path = "update/update.json"

with open(path) as f:
    d = json.load(f)

patched = False
for p in d.get("parts", []):
    if p.get("name") == name:
        p["url"] = url
        patched = True

if not patched:
    print(f"warn: no part named {name!r} in {path}", file=sys.stderr)

with open(path, "w") as out:
    json.dump(d, out, indent=2)
    out.write("\n")
