#sai parthish mandumula.
import sys

def CalculateUnknownStates(GivenStates):
    ToBeComputedStates = []
    for state in lstAllStates:
        if state not in GivenStates:
            ToBeComputedStates.append(state)
    return ToBeComputedStates

def ProbabilitySpaceofAlarm(item, totalprobabilty):
    target = ''
    for r in totalprobabilty:
        if r == "Bt" or r == "Bf" or r == "Et" or r == "Ef":
            target = target + r
    if item == "At":
        return eval(target)
    else:
        return 1 - eval(target)
def PopulateBaysianNetwork(GivenStates):
    presentStates = []
    for g in GivenStates:
        if g not in presentStates:
            presentStates.append(g[0])

    if len(presentStates) == 5:
        return ComputeProbability([GivenStates])
    else:
        ToBeComputedStates = CalculateUnknownStates(presentStates)
        UnknownStates = ProbabilityspaceofTruthTable(ToBeComputedStates)
        ClearStates = GivenStates[:]
        ProbabilitySpace = TotalProbabilitySpace(GivenStates, UnknownStates, ClearStates)
        return ComputeProbability(ProbabilitySpace)

def ProbabilitySpaceofJohn(item, ProbabilitySpace):
    for r in ProbabilitySpace:
        if r == "At" and item == "Jt":
            return Jt
        elif r == "At" and item == "Jf":
            return 1 - Jt
        if r == "Af" and item == "Jt":
            return Jf
        if r == "Af" and item == "Jf":
            return 1 - Jf

def TotalProbabilitySpace(GivenStates,UnknownStates,ClearStates):
    UpdatedProbabilityEvents = []
    for row in UnknownStates:
        for variable in row:
            GivenStates.append(variable)
        UpdatedProbabilityEvents.append(GivenStates)
        GivenStates = ClearStates[:]
    return UpdatedProbabilityEvents

def ProbabilitySpaceofMary(item, ProbabilitySpace):
    for r in ProbabilitySpace:
        if r == "At" and item == "Mt":
            return Mt
        elif r == "At" and item == "Mf":
            return 1 - Mt
        if r == "Af" and item == "Mt":
            return Mf
        if r == "Af" and item == "Mf":
            return 1 - Mf
def ProbabilityspaceofTruthTable(GivenStates):
    UnknownStates = []
    for row in GenerateGroundTruth(len(GivenStates)):
        currentProbabilities = []
        for i, CurrentState in enumerate(row):
            currentProbabilities.append(GivenStates[i] + CurrentState)
        UnknownStates.append(currentProbabilities)
    return  UnknownStates

def GenerateGroundTruth(size):
    if size < 1:
        return [[]]
    entry = GenerateGroundTruth(size-1)
    return [row + [v] for row in entry for v in ['t', 'f']]

def ComputeProbability(ProbabilitySpace):
    currentieration = 0
    for totalprobabilty in ProbabilitySpace:
        computation = 1
        for item in totalprobabilty:
            if item == "At" or item == "Af":
                correlatedProbability = ProbabilitySpaceofAlarm(item, totalprobabilty)
                computation = computation * correlatedProbability
            elif item == "Jt" or item == "Jf":
                correlatedProbability = ProbabilitySpaceofJohn(item, totalprobabilty)
                computation = computation * correlatedProbability
            elif item == "Mt" or item == "Mf":
                correlatedProbability = ProbabilitySpaceofMary(item, totalprobabilty)
                computation = computation * correlatedProbability
            else:
                computation = computation * eval(item)
        currentieration += computation
    return currentieration


lstAllStates = ["B","M","A","E","J"]

Bt = 0.001
Bf = 0.999

Et = 0.002
Ef = 0.998

BtEt = EtBt = 0.95
BtEf = EfBt = 0.94
BfEt = EtBf = 0.29
BfEf = EfBf = 0.001

Jt = 0.90
Jf = 0.05

Mt = 0.70
Mf = 0.01

GivenStates = []
ParseGiven = 0
for i in range(0, len(sys.argv)):
    if i == 0:
        pass
    elif sys.argv[i] == "given":
        ParseGiven = i
    else:
        GivenStates.append(sys.argv[i])

ComputeProbabiltyofDividend = PopulateBaysianNetwork(GivenStates)

if ParseGiven == 0:
    print(ComputeProbabiltyofDividend)
else:
    DivisorList = []
    for i in range(ParseGiven + 1, len(sys.argv)):
        DivisorList.append(sys.argv[i])

    ComputeProbabiltyofDivisor = PopulateBaysianNetwork(DivisorList)
    print("Final probability: " +  str(ComputeProbabiltyofDividend/ComputeProbabiltyofDivisor))
