import numpy as np
from numpy import random


class BasicRW:   
    
    rows = cols = 10000
    sourceNode = np.mat(random.randint(0,2,size=(rows,cols)))
    size = 0.5
    coreNode = []
    samplingNode = np.mat(random.randint(0,1,size=(int(np.sqrt(size * rows)),int(np.sqrt(size * rows)))))

    def __init__(self, *args, **kwargs):
        pass

    def findCoreNode():
        pass

    def getAdjacentMatrix(nodes):
        return nodes.sum(axis=1)


if __name__ == '__main__':
    test = BasicRW
   
    print(test.getAdjacentMatrix(test.sourceNode))