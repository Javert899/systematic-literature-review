import os
import re
import json
import traceback

doi = set()
data = os.listdir("data")
dictio_cit_years = {}
for file in data:
    dictio_cit_years[file] = []
    full_path = os.path.join("data", file)
    try:
        content = json.load(open(full_path, "rb"))
        if "reference" in content["message"]:
            #print("MESSAGE ", content["message"])
            for item in content["message"]["reference"]:
                #print(item.keys())
                if "DOI" in item and "unstructured" in item:
                    text = item["unstructured"].lower()
                    if "artifact" in text and ("centric" in text or "business" in text):
                        doi.add(item["DOI"])
    except:
        #traceback.print_exc()
        pass

doi = sorted(list(doi))
json.dump(doi, open("cit_doi.dump", "w"))
