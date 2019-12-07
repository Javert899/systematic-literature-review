import os
import json

data = os.listdir("data_filtered")
for file in data:
    full_path = os.path.join("data_filtered", file)
    try:
        content = json.load(open(full_path, "rb"))
        print(content["message"]["title"][0])
    except:
        pass
