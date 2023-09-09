from Node import Node
from Element import Element


class Grid:
    lines = []
    SimulationTime = 0
    SimulationStepTime = 0
    Conductivity = 0
    Alfa = 0
    Tot = 0
    InitialTemp = 0
    Density = 0
    SpecificHeat = 0
    NodesNumber = 0
    ElementsNumber = 0
    elements = []
    nodes = []

    def __init__(self, gridName):
        self.setFileLines(gridName)
        self.setParameters()
        self.setNodes()
        self.setElements()

    def setFileLines(self, gridName):
        with open('./' + gridName) as f:
            self.lines = [line.rstrip('\n') for line in f]

    def setElements(self):
        correctedLines = []
        for line in self.lines:
            line = line.replace(",", "")
            correctedLines += [line.split()]

        for i in range(len(correctedLines)):
            if correctedLines[i][0] == '*Element':
                while correctedLines[i+1][0] != '*BC':
                    element = Element(int(correctedLines[i+1][0]))
                    for j in range(1, 5):
                        for Node in self.nodes:
                            if Node.id == int(correctedLines[i+1][j]):
                                element.addNode(Node)
                    self.elements += [element]
                    i += 1

    def setNodes(self):
        bcArray = self.lines[-1].replace(",", "").split()

        correctedLines = []
        for line in self.lines:
            line = line.replace(",", "")
            correctedLines += [line.split()]

        for i in range(len(correctedLines)):
            if correctedLines[i][0] == '*Node':
                while correctedLines[i+1][0] != '*Element':
                    id = int(correctedLines[i+1][0])
                    x = float(correctedLines[i+1][1])
                    y = float(correctedLines[i+1][2])
                    bc = 0
                    for bcElem in bcArray:
                        if id == int(bcElem):
                            bc = 1
                    self.nodes += [Node(id, x, y, bc)]
                    i += 1

    def setParameters(self, ):
        correctedLines = []
        for line in self.lines:
            line = line.rsplit(' ', 1)
            correctedLines += [line]

        len_lines = len(correctedLines)

        for i in range(len_lines):
            if correctedLines[i][0] != '*Node':
                if correctedLines[i][0] == 'Nodes number':
                    self.NodesNumber = int(correctedLines[i][1])
                if correctedLines[i][0] == 'Elements number':
                    self.ElementsNumber = int(correctedLines[i][1])
                setattr(self, correctedLines[i][0], float(correctedLines[i][1]))
            else:
                return


