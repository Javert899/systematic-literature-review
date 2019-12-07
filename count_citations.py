import os
import re
import json
import traceback

data = os.listdir("data")
dictio_cit_years = {}
for file in data:
    dictio_cit_years[file] = []
    full_path = os.path.join("data", file)
    try:
        content = json.load(open(full_path, "rb"))
        stru = json.dumps(content["message"], indent=2)
        if "reference\"" in stru:
            print(content["message"].keys())
        if "reference" in content["message"]:
            for item in content["message"]["reference"]:
                text = item["unstructured"]
                match = re.match(r'.*(20[0-1][0-9])', text)
                if match is not None:
                    dictio_cit_years[file].append(int(match.group(1)))
                else:
                    match = re.match(r'.*(19[7-9][0-9])', text)
                    if match is not None:
                        dictio_cit_years[file].append(int(match.group(1)))
    except:
        print("BBBB")
        traceback.print_exc()

json.dump(dictio_cit_years, open("no_citations_file.dump", "w"))
