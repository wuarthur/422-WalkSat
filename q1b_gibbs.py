import matplotlib.pyplot as plt
import random


def initializeDist():
    pTable = dict()
    pTable[("a0", "b1")] = 5
    pTable[("a1", "b1")] = 10
    pTable[("b1", "c0")] = 1
    pTable[("b1", "c1")] = 100
    pTable[("c0", "d0")] = 1
    pTable[("c0", "d1")] = 100
    pTable[("c1", "d0")] = 100
    pTable[("c1", "d1")] = 1
    pTable[("a0", "d0")] = 100
    pTable[("a0", "d1")] = 1
    pTable[("a1", "d0")] = 1
    pTable[("a1", "d1")] = 100

    return pTable

def normalize(probT, probF):
    total = float(probT + probF)
    return float(probT) / total, float(probF) / total

def getProb(numTrues, numSamples):
    return float(numTrues) / float(numSamples)

def sample(n):
    B = "b1"
    a, c, d = "a1", "c1", "d1"
    pTable = initializeDist()
    results = list()
    numTrueA = 0

    switch = 1
    for i in range(n):
        # sample A
        if switch == 1:
            probAT = pTable["a1", B] * pTable["a1", d]
            probAF = pTable["a0", B] * pTable["a0", d]
            normProbAT, normProbAF = normalize(probAT, probAF)
            sample = random.random()
            if sample <= normProbAF:
                a = "a0"
            else:
                a = "a1"
                numTrueA += 1

            totalProbA = getProb(numTrueA, i+1)
            results.append(totalProbA)
            switch += 1

        # sample C
        elif switch == 2:
            probCT = pTable[B, "c1"] * pTable["c1", d]
            probCF = pTable[B, "c0"] * pTable["c0", d]
            normProbCT, normProbCF = normalize(probCT, probCF)
            sample = random.random()

            if sample <= normProbCF:
                c = "c0"
            else:
                c = "c1"

            if a == "a1":
                numTrueA += 1

            totalProbA = getProb(numTrueA, i+1)
            results.append(totalProbA)
            switch += 1

        # sample D
        elif switch == 3:
            probDT = pTable[a, "d1"] * pTable[c, "d1"]
            probDF = pTable[a, "d0"] * pTable[c, "d0"]
            normProbDT, normProbDF = normalize(probDT, probDF)
            sample = random.random()

            if sample <= normProbDF:
                d = "d0"
            else:
                d = "d1"

            if a == "a1":
                numTrueA += 1

            totalProbA = getProb(numTrueA, i+1)
            results.append(totalProbA)
            switch = 1

    return results


def plotResults(data):
    varElimA1 = 0.0566
    plt.plot(data, label="Gibbs Sampling")
    plt.axhline(y=varElimA1, color="red", label="Variable Elimination")
    gibbsA1 = data.pop()
    plt.text(100005, varElimA1+0.006, str(varElimA1), color="red")
    plt.text(100005, gibbsA1-0.007, str(gibbsA1), color="blue")
    plt.ylim(-0.05, 0.5)
    plt.xlabel("# of samples")
    plt.ylabel("P(a|b)")
    plt.title("Gibbs Sampling Results")
    plt.legend()
    plt.show()


results = sample(100000)
plotResults(results)
