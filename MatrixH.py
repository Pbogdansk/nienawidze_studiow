import numpy as np
def calcMatrixH(pc, xTable, yTable, dKsi, dEta, grid,weights):

    size = pc * pc

    x1 = xTable[0]
    y1 = yTable[0]
    x2 = xTable[1]
    y2 = yTable[1]
    x3 = xTable[2]
    y3 = yTable[2]
    x4 = xTable[3]
    y4 = yTable[3]

    matrixH = [[0 for i in range(4)] for j in range(4)]
    #interpolacja x i y metodą gaussa
    for i in range(size):
        x00 = dKsi[i][0] * x1 + dKsi[i][1] * x2 + dKsi[i][2] * x3 + dKsi[i][3] * x4
        x01 = dKsi[i][0] * y1 + dKsi[i][1] * y2 + dKsi[i][2] * y3 + dKsi[i][3] * y4
        x10 = dEta[i][0] * x1 + dEta[i][1] * x2 + dEta[i][2] * x3 + dEta[i][3] * x4
        x11 = dEta[i][0] * y1 + dEta[i][1] * y2 + dEta[i][2] * y3 + dEta[i][3] * y4

        print("")
        detJacobian = x00 * x11 - (x01 * x10)
        inverseDetJacobian = 1 / detJacobian


        shapeFunX = [0 for i in range(4)]
        shapeFunY = [0 for i in range(4)]

        for j in range(4):
            shapeFunX[j] = inverseDetJacobian * (-x01) * dEta[i][j] + inverseDetJacobian * x11 * dKsi[i][j]
            shapeFunY[j] = inverseDetJacobian * x00 * dEta[i][j] + inverseDetJacobian * (-x10) * dKsi[i][j]

        funTransX = np.reshape(shapeFunX, (4, 1))
        funTransY = np.reshape(shapeFunY, (4, 1))

        matrixH += grid.Conductivity * ((shapeFunX * funTransX) + (shapeFunY * funTransY)) * detJacobian * weights[i]

    return matrixH
