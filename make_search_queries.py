import requests
import json
import traceback
import time

doi = set()
keywords = ["artifact centric", "artifact centric process mining", "artifact centric conformance checking", "artifact centric compliance checking"]
#keywords = ["artifact centric business process", "artifact centric process discovery", "modeling artifact centric", "artifact centric log extraction", "artifact centric choreographies", "artifact centric workflow", "artifact centric bpmn", "artifact centric verification"]

for k in keywords:
    url = "https://api.crossref.org/works?query="+k.replace(" ",".")
    try:
        resp = json.loads(requests.get(url).text)["message"]["items"]
        for item in resp:
            if "DOI" in item:
                doi.add(item["DOI"])
    except:
        traceback.print_exc()

    time.sleep(2)
doi = sorted(list(doi))
json.dump(doi, open("cit_doi.dump", "w"))
