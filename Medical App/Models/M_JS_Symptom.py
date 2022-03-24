import json

f = open('Data/symptoms.json', 'r', encoding = 'utf-8')

data = json.load(f)

lstSymptom = []

def ParseSymptoms():
    for item in data["symptom"]:
        lstSymptom.append(item["name"])
    return lstSymptom

def SearchSymptoms(key):
    lst = []
    for item in data["symptom"]:
        if key.lower() in item["name"].lower():
            lst.append(item["name"])
    return lst

