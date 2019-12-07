import json
import sys

F = open(sys.argv[1], "r")
content = F.read().split("\n\n")
json_dictio = {}
for row in content:
    rows = row.split("\n")[1:-1]
    entry = {}
    for r in rows:
        entry[r.split("=")[0].strip()] = r.split("{")[-1].split("}")[0]
    if "doi" in entry and "title" in entry:
        json_dictio[entry["doi"]] = entry
json.dump(json_dictio, open(sys.argv[2], "w"), indent=2)
