import numpy as np
from numpy import random

def CC(adjacentMatrix):
    n = adjacentMatrix.shape[1]
    C = np.mat(random.randint(0, 1, size=(1, n)))
    for i in range(0, n - 1):
        aa = [j for j in range(len(adjacentMatrix)) if adjacentMatrix[i, j] == 1]
        if len(aa) > 0:
            m = len(aa)
            if m > 1:
                num = 0
                for x in aa:
                    for y in aa:
                        if x != y and adjacentMatrix[x, y] == 1:
                            num += 1
                C[0, i] = num / m * (m - 1)
    return np.mean(C)

def getAdjacentNodes(nodes):
    iNodesLen = len(nodes)
    dicAdjacentNodes = dict()
    if len(nodes) > 0:
        for i in range(0, iNodesLen):
            for j in range(0, iNodesLen):
                if i != j and nodes[i, j] != 0:
                    if i not in dicAdjacentNodes.keys():
                        dicAdjacentNodes[i] = list()
                    dicAdjacentNodes[i].append(j)
    return dicAdjacentNodes
