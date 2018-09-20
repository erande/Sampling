import numpy as np
from numpy import random
from random import choice
import op
import display

class BasicRW:

    def __init__(self):
        self._rows = self._cols = 100
        self.size = 0.5

        self.sourceNode = np.mat(random.randint(0, 2, size=(self._rows, self._cols)))
        self.samplingNode = np.mat(random.randint(0, 1, size=(self._rows, self._cols)))

        self._dicSourceAdjacentNodes = dict()
        self._iSamplingLen = 0
        self._listSelectNodes = set()

        self._readyData()

    def _readyData(self):
        for i in range(0, self._rows):
            self.sourceNode[i, i] = 0
        self.sourceNode = np.triu(self.sourceNode)
        self.sourceNode += self.sourceNode.T - np.diag(self.sourceNode.diagonal())

        self._dicSourceAdjacentNodes = op.getAdjacentNodes(self.sourceNode)
        self._iSamplingLen = int(self.size * len(self._dicSourceAdjacentNodes.keys()))
        print('sampling nodes:', self._iSamplingLen)

    def _clear(self):
        self._listSelectNodes = set()
        self.samplingNode = np.mat(random.randint(0, 1, size=(self._rows, self._cols)))


    def _rw(self, firstStratNode):
        self._clear()
        print('first strat node:', firstStratNode)
        x = firstStratNode
        length = self._iSamplingLen
        while (length > 0):
            self._listSelectNodes.add(x)

            neighbour = self._dicSourceAdjacentNodes[x]
            y = choice(neighbour)

            if self.samplingNode[x, y] == 0:
                length -= 1
                self.samplingNode[x, y] = 1
            self.samplingNode[y, x] = 1
            x = y

    def _afterRW(self):
        if len(self._listSelectNodes) > 0:
            for i in self._listSelectNodes:
                for j in self._listSelectNodes:
                    if i != j:
                        if self.sourceNode[i, j] == 1:
                            self.samplingNode[i, j] = 1
                            self.samplingNode[j, i] = 1

    def rw1(self):
        firstStratNode = random.choice(list(self._dicSourceAdjacentNodes))
        self._rw(firstStratNode)

    def rw_incident_edges(self):
        firstStratNode = random.choice(list(self._dicSourceAdjacentNodes))
        self._rw(firstStratNode)
        self._afterRW()


    def rw_my(self):
        arrayRowsSum = self.sourceNode.sum(axis=1)
        firstStratNode = np.argmax(arrayRowsSum)
        self._rw(firstStratNode)
        self._afterRW()

def test_source(test):
    # print(test.sourceNode)
    print('source CC:', op.CC(test.sourceNode))
    return test.sourceNode

def test2(test):
    test.rw_incident_edges()
    # print(test.samplingNode)
    print('rw sample CC:', op.CC(test.samplingNode))
    return test.samplingNode

def test_my_rw(test):
    test.rw_my()
    # print(test.samplingNode)
    print('my sample CC:', op.CC(test.samplingNode))
    return test.samplingNode

if __name__ == '__main__':
    for i in range(1, 10):
        print('The ', i, 'sampling start...............................................')
        test = BasicRW()
        source = test_source(test)
        sample1 = test2(test)
        sample2 = test_my_rw(test)
        print('source == sample1:', (source == sample2).all())
        print('sample1 == sample2:', (sample1 == sample2).all())
        print()
        listSourceDegree = list(source.sum(axis=1))
        # display.degreeDistribute2(listSourceDegree)

        listSample1Degree = list(sample1.sum(axis=1))
        # display.degreeDistribute2(listSample1Degree)

        # display.degreeDistribute3(listSourceDegree, listSample1Degree)

        listSample2Degree = list(sample2.sum(axis=1))
        display.degreeDistribute3(listSourceDegree, listSample1Degree, listSample2Degree)



