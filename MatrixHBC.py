import numpy as np
import math
import functions as fn

def calcMatrixHBC(element, pc, grid, matrixHBCp):
    matrixHBC = [[0 for i in range(4)] for j in range(4)]
    pcIndex = 0
    MatrixBcPoint = [0 for i in range(4)]

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
                    MatrixBcPoint[k] = fun(matrixHBCp[j][0], matrixHBCp[j][1])

                matrixBCPointTrans = np.reshape(MatrixBcPoint, (4, 1))
                matrixHBC += (MatrixBcPoint * matrixBCPointTrans) * detJacobian * grid.Alfa * 1

        pcIndex += pc

    return matrixHBC

