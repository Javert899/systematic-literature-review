import os
import json
import traceback
import shutil

try:
    os.mkdir("data_filtered")
except:
    pass

data = os.listdir("data")
for file in data:
    if not os.path.exists(os.path.join("data_filtered", file)):
        full_path = os.path.join("data", file)
        try:
            content = json.load(open(full_path, "rb"))
            text = content["message"]["title"][0].lower()
            if ("artifact" in text or "object" in text) and ("centric" in text or "business" in text or "process" in text) and not ("software" in text):
                print(text)
                consent = None
                while (consent != "yes" and consent != "no"):
                    consent = input("accept? -> ")
                if consent == "yes":
                    shutil.copyfile(os.path.join("data", file), os.path.join("data_filtered", file))
        except:
            pass
