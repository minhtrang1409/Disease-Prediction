class Illness():
    def __init__(self, name, symptoms):
        self.name = name
        self.symptoms = self.SplitSymptoms(symptoms)
        self.percentage = 0

    def SplitSymptoms(self, symptoms):
        lstSymptoms = symptoms.split("; ")
        return lstSymptoms

    def ReturnTuple(self):
        lstTuple = []
        lstTuple.append(self.name)
        lstTuple.append(self.symptoms)
        lstTuple.append(self.percentage)
        return tuple(lstTuple)

    def MatchingSymptoms(self, data):
        match = 0
        total = len(self.symptoms)
        for item in data:
            for pos in self.symptoms:
                if item in pos:
                    match = match + 1
        self.percentage = round(match/total*100, 2)