from Grid import Grid
from MatrixH import calcMatrixH
from MatrixC import calcMatrixC
from MatrixHBC import calcMatrixHBC
import math
import numpy as np
import functions as fn

grid = Grid('Test2_4_4_MixGrid.txt')

elements = grid.elements

pc = 2
size = pc * pc
dKsi = [[0 for i in range(4)] for j in range(size)]
dEta = [[0 for i in range(4)] for j in range(size)]
ksi = [0 for i in range(size)]
eta = [0 for i in range(size)]
weights = [0 for i in range(size)]
aggregationArrC = [[0 for i in range(grid.NodesNumber)] for j in range(grid.NodesNumber)]
aggregationArrCBC = [[0 for i in range(grid.NodesNumber)] for j in range(grid.NodesNumber)]
aggregationArrC = [[0 for i in range(grid.NodesNumber)] for j in range(grid.NodesNumber)]
matrixHBCp = []
globalVectorP = [[0 for i in range(1)] for j in range(grid.NodesNumber)]

def calcWeights(w):
    index = 0
    for i in range(pc):
        for j in range(pc):
            weights[index] += float(w[i]) * float(w[j])
            index += 1

def uniwersalElement(pc):
         global ksi
         global eta
         size = pc * pc

         if (pc == 2):

           ksi = [-1 / math.sqrt(3), 1 / math.sqrt(3), 1 / math.sqrt(3), -1 / math.sqrt(3)]
           eta = [-1 / math.sqrt(3), -1 / math.sqrt(3), 1 / math.sqrt(3), 1 / math.sqrt(3)]
           w = [1, 1]
           calcWeights(w)
           global matrixHBCp
           hbcPkt = [
               [-math.sqrt(1 / 3), -1],
               [math.sqrt(1 / 3), -1],
               [1, -math.sqrt(1 / 3)],
               [1, math.sqrt(1 / 3)],
               [math.sqrt(1 / 3), 1],
               [-math.sqrt(1 / 3), 1],
               [-1, math.sqrt(1 / 3)],
               [-1, -math.sqrt(1 / 3)]
           ]
           for i in range(len(hbcPkt)):
               matrixHBCp += [hbcPkt[i]]

           for i in range(size):
             dKsi[i][0] = -0.25 * (1 - eta[i])
             dKsi[i][1] = 0.25 * (1 - eta[i])
             dKsi[i][2] = 0.25 * (1 + eta[i])
             dKsi[i][3] = -0.25 * (1 + eta[i])

             dEta[i][0] = -0.25 * (1 - ksi[i])
             dEta[i][1] = -0.25 * (1 + ksi[i])
             dEta[i][2] = 0.25 * (1 + ksi[i])
             dEta[i][3] = 0.25 * (1 - ksi[i])

           print("pochodne dla ksi:")
           for i in range(4):
             for j in range(4):
                 print(dKsi[i][j], end=" ")
             print("")

           print("pochodne dla eta:")
           for i in range(4):
             for j in range(4):
                 print(dEta[i][j], end=" ")
             print("")

         elif (pc == 3):

             ksi = [-math.sqrt(3/5), -math.sqrt(3/5), -math.sqrt(3/5), 0, 0, 0, math.sqrt(3/5), math.sqrt(3/5), math.sqrt(3/5)]
             eta = [-math.sqrt(3/5), 0, math.sqrt(3/5), -math.sqrt(3/5), 0, math.sqrt(3/5), -math.sqrt(3/5), 0, math.sqrt(3/5)]
             w = [5/9, 8/9, 5/9]
             calcWeights(w)

             hbcPkt = [
                 [-math.sqrt(3/5), -1],
                 [0, -1],
                 [math.sqrt(3/5), -1],
                 [1, -math.sqrt(3/5)],
                 [1, 0],
                 [1, math.sqrt(3/5)],
                 [math.sqrt(3/5), 1],
                 [0, 1],
                 [-math.sqrt(3/5), 1],
                 [-1, math.sqrt(3/5)],
                 [-1, 0],
                 [-1, -math.sqrt(3/5)]
             ]

             for i in range(len(hbcPkt)):
                 matrixHBCp += [hbcPkt[i]]

             for i in range(size):
                 dKsi[i][0] = -0.25 * (1 - eta[i])
                 dKsi[i][1] = 0.25 * (1 - eta[i])
                 dKsi[i][2] = 0.25 * (1 + eta[i])
                 dKsi[i][3] = -0.25 * (1 + eta[i])

                 dEta[i][0] = -0.25 * (1 - ksi[i])
                 dEta[i][1] = -0.25 * (1 + ksi[i])
                 dEta[i][2] = 0.25 * (1 + ksi[i])
                 dEta[i][3] = 0.25 * (1 - ksi[i])

             print("pochodne dla ksi:")
             for i in range(4):
                 for j in range(4):
                     print(dKsi[i][j], end=" ")
                 print("")

             print("pochodne dla eta:")
             for i in range(4):
                 for j in range(4):
                     print(dEta[i][j], end=" ")
                 print("")

         elif (pc == 4):

            ksi = [-0.861136, -0.339981, 0.339981, 0.861136, -0.861136, -0.339981, 0.339981, 0.861136, -0.861136, -0.339981, 0.339981, 0.861136, -0.861136, -0.339981, 0.339981, 0.861136]
            eta = [-0.861136, -0.861136, -0.861136, -0.861136, -0.339981, -0.339981, -0.339981, -0.339981, 0.339981, 0.339981, 0.339981, 0.339981, 0.861136, 0.861136, 0.861136, 0.861136]
            w = [(18 - math.sqrt(30)) / 36,
                 (18 + math.sqrt(30)) / 36,
                 (18 + math.sqrt(30)) / 36,
                 (18 - math.sqrt(30)) / 36]
            calcWeights(w)

            hbcPkt = [
                [-0.861136, -1],
                [-0.339981, -1],
                [0.339981, -1],
                [0.861136, -1],
                [1, -0.861136],
                [1, -0.339981],
                [1, 0.339981],
                [1, 0.861136],
                [0.861136, 1],
                [0.339981, 1],
                [-0.339981, 1],
                [-0.861136, 1],
                [-1, 0.861136],
                [-1, 0.339981],
                [-1, -0.339981],
                [-1, -0.861136]
            ]

            for i in range(len(hbcPkt)):
                matrixHBCp += [hbcPkt[i]]

            for i in range(size):
                dKsi[i][0] = -0.25 * (1 - eta[i])
                dKsi[i][1] = 0.25 * (1 - eta[i])
                dKsi[i][2] = 0.25 * (1 + eta[i])
                dKsi[i][3] = -0.25 * (1 + eta[i])

                dEta[i][0] = -0.25 * (1 - ksi[i])
                dEta[i][1] = -0.25 * (1 + ksi[i])
                dEta[i][2] = 0.25 * (1 + ksi[i])
                dEta[i][3] = 0.25 * (1 - ksi[i])

            print("pochodne dla ksi:")
            for i in range(4):
                for j in range(4):
                    print(dKsi[i][j], end=" ")
                print("")

            print("pochodne dla eta:")
            for i in range(4):
                for j in range(4):
                    print(dEta[i][j], end=" ")
                print("")
         #return dKsi, dEta
         else:
             print("error nieobsługiwana liczba punktów całkowania")



def calcVectorP(element):
    pcIndex = 0
    vectorP = [[0 for i in range(1)] for j in range(4)]

    for i in range(len(element.nodes)):
        bc = False

        if (i == 3):
            if (element.nodes[i].bc == 1 and element.nodes[0].bc == 1):
                borderCheck = element.nodes[0]
                bc = True
        else:
            if (element.nodes[i].bc == 1 and element.nodes[i + 1].bc == 1):
                borderCheck = element.nodes[i + 1]
                bc = True

        if bc:
            detJacobian = (math.sqrt((pow(borderCheck.x - element.nodes[i].x, 2)) + (pow(borderCheck.y - element.nodes[i].y, 2)))) / 2
            for j in range(pcIndex, pcIndex+pc, 1):
                for k in range(4):
                    fun = getattr(fn, 'N' + str(k))
                    vectorP[k][0] += fun(matrixHBCp[j][0], matrixHBCp[j][1]) * detJacobian * grid.Tot * grid.Alfa

        pcIndex += pc

    return vectorP

uniwersalElement(pc)

for element in grid.elements:
    nodeX = [element.nodes[0].x, element.nodes[1].x, element.nodes[2].x, element.nodes[3].x]
    nodeY = [element.nodes[0].y, element.nodes[1].y, element.nodes[2].y, element.nodes[3].y]
    #macierzH liczenie
    matrixH = calcMatrixH(pc, nodeX, nodeY, dKsi, dEta, grid, weights)
    matrixH = np.array(matrixH)
    #MacierzC liczenie
    matrixC = calcMatrixC(pc, nodeX, nodeY,dKsi, dEta, grid, weights, ksi, eta)
    print("Macierz H dla elementu", element.id)
    print(matrixH)
    #Macierz Hbc liczenie
    matrixHbc = calcMatrixHBC(element,pc, grid,matrixHBCp)
    #dodawanie H+Hbc
    matrixHHbc = matrixH + matrixHbc
    print("Macierz H z Hbc dla element", element.id)
    print(matrixHHbc)
    #wektor P liczenie
    vectorP = calcVectorP(element)
    #tablica id węzłów
    nodeIdArr = [element.nodes[0].id - 1, element.nodes[1].id - 1, element.nodes[2].id - 1, element.nodes[3].id - 1]

    for i in range(4):
        for j in range(4):
            aggregationArrC[nodeIdArr[i]][nodeIdArr[j]] += matrixH[i][j]
            aggregationArrCBC[nodeIdArr[i]][nodeIdArr[j]] += matrixH[i][j] + matrixHbc[i][j]
            aggregationArrC[nodeIdArr[i]][nodeIdArr[j]] += matrixC[i][j]

    for i in range(4):
        globalVectorP[nodeIdArr[i]][0] += vectorP[i][0]


for element in grid.elements:

    matrixHbc = calcMatrixHBC(element,pc, grid,matrixHBCp)
    matrixHbc = np.array(matrixHbc)
    print(" ")
    print("macierz hbc dla elementu", element.id)
    print(matrixHbc)
    print(" ")

print()
print("Macierz agregacji H:")
aggregationArrC = np.array(aggregationArrC)
for i in aggregationArrC:
    for j in i:
        print(j, end=" ")
    print()

print()
print("Macierz agregacji H z BC:")
aggregationArrCBC = np.array(aggregationArrCBC)
for i in aggregationArrCBC:
    for j in i:
        print(j, end=" ")
    print()

print()
print("Wektor P:")
globalVectorP = np.array(globalVectorP)
print(globalVectorP)

print()
print("Macierz agregacji C:")
aggregationArrC = np.array(aggregationArrC)
for i in aggregationArrC:
    for j in i:
        print(j, end=" ")
    print()




t1 = [[grid.InitialTemp for i in range(1)] for j in range(grid.NodesNumber)]
t1 = np.array(t1)

for i in range(int(grid.SimulationStepTime), int(grid.SimulationTime + 1), int(grid.SimulationStepTime)):

    argument1 = aggregationArrCBC + (aggregationArrC / grid.SimulationStepTime)
    argument2 = np.dot((aggregationArrC/grid.SimulationStepTime), t1)
    argument2 = argument2 + globalVectorP

    t1 = np.linalg.solve(argument1,argument2)

    print("")
    print("Temeratury dla kroku", i)
    print("")
    print(t1)
