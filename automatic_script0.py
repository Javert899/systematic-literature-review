import os

listdir = os.listdir(".")

for file in listdir:
    if file.endswith("bib"):
        new_file = file.replace("bib", "json")
        print(file, new_file)
        os.system("python parse.py "+file+" "+new_file)
        os.system("python get_crossref.py "+new_file)
