import os
import time
import os
import traceback
import json
import requests
import time
import sys

scholar_entries = json.load(open(sys.argv[1], "rb"))
try:
    os.mkdir("data")
except:
    pass

for index, entry in enumerate(scholar_entries):
    target_file = "data/"+"".join([x for x in str(entry) if x.isalnum()])+".dump"
    if not os.path.exists(target_file):
        content = requests.get("http://api.crossref.org/works/"+str(entry)).text
        F = open(target_file, "w")
        F.write(content)
        F.close()
        print(content)
        print("done", entry)
        time.sleep(2)
