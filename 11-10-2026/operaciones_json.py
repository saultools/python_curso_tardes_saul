import json 
jsonfile = "../11-09-2026/11_countries.json"

def continentes():
    with open(jsonfile,"r") as f:
        return list(set(map(lambda p:p["region"],json.load(f))))

def paises():
    with open(jsonfile,"r") as f:
        return json.load(f)
        #return list(set(map(lambda p:p["name"],json.load(f))))