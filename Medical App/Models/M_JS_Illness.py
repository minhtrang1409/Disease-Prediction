import json
from Models.M_Illness import Illness

f = open('Data/illnesses.json', 'r', encoding = 'utf-8')

data = json.load(f)

# lstIllness = []
# data1 = ['Diarrhoea', 'Coughing', 'Muscle pain', 'Runny or blocked nose']

# for item in data["illness"]:
#     name = item["name"]
#     symptoms = item['symptoms']
#     illness = Illness(name, symptoms)
#     illness.MatchingSymptoms(data1)
#     lstIllness.append(illness)

# for index in lstIllness:
#     print(index.percentage)


def ParseIllnesses(selectedItems):
    lstIllness = []
    for item in data["illness"]:
        name = item["name"]
        symptoms = item['symptoms']
        illness = Illness(name, symptoms)
        illness.MatchingSymptoms(selectedItems)
        lstTuple = illness.ReturnTuple()
        if illness.percentage >= 10:
            lstIllness.append(lstTuple)
    # sorted(lstIllness, key=lambda item: item[2])
    return lstIllness

def GetListIllnessInfo():
    lstName = []
    lstSymptom = []
    for item in data["illness"]:
        lstName.append(item["name"])
        lstSymptom.append(item['symptoms'])
    return [lstName, lstSymptom]