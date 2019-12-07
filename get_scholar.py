import json
import os
import time
import scholarly
import os
import traceback


scholar_entries = json.load(open("artifact_centric_models.json", "rb"))
try:
    os.mkdir("data2")
except:
    pass

for index, entry in enumerate(scholar_entries):
    target_file = "data2/"+"".join([x for x in str(entry) if x.isalnum()])+".dump"
    if not os.path.exists(target_file):
        print(entry)
        try:
            search_query = scholarly.search_pubs_query(scholar_entries[entry]["title"])
            cur = next(search_query)
            while cur != None:
                F = open(target_file, "w")
                F.write(str(cur))
                F.close()
                print("done",entry)
                break
        except:
            traceback.print_exc()
    time.sleep(10)
