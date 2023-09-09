import numpy as np
import functions as fn
def calcMatrixC(pc, nodeX, nodeY, dKsi, dEta, grid, weights, ksi, eta):

    size = pc * pc
    matrixCpoint = [[0 for i in range(4)] for j in range(size)]
    matrixC = np.zeros((4, 4))

    x1 = nodeX[0]
    y1 = nodeY[0]
    x2 = nodeX[1]
    y2 = nodeY[1]
    x3 = nodeX[2]
    y3 = nodeY[2]
    x4 = nodeX[3]
    y4 = nodeY[3]

    for i in range(size):
        x00 = dKsi[i][0] * x1 + dKsi[i][1] * x2 + dKsi[i][2] * x3 + dKsi[i][3] * x4
        x01 = dKsi[i][0] * y1 + dKsi[i][1] * y2 + dKsi[i][2] * y3 + dKsi[i][3] * y4
        x10 = dEta[i][0] * x1 + dEta[i][1] * x2 + dEta[i][2] * x3 + dEta[i][3] * x4
        x11 = dEta[i][0] * y1 + dEta[i][1] * y2 + dEta[i][2] * y3 + dEta[i][3] * y4
        jacobian = float(x00 * x11 - (x01 * x10))

        for j in range(4):
            fun = getattr(fn, 'N' + str(j))
            matrixCpoint[i][j] = fun(ksi[i], eta[i])

        tempMatrix = np.array(matrixCpoint[i])
        tempMatrixtTrans = np.reshape(tempMatrix, (4, 1))

        matrixC += tempMatrix * tempMatrixtTrans * weights[i] * jacobian * grid.SpecificHeat * grid.Density


    return matrixC
