import numpy as np


def adjoint_matrix(matrix):
    adjoint = np.zeros(matrix.shape, dtype=np.int16)
    amount_of_rows, amount_of_columns = matrix.shape
    for i in range(amount_of_rows):
        for j in range(amount_of_columns):
            cofactor_i_j = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
            determinant = int(np.linalg.det(cofactor_i_j))
            adjoint[i][j] = determinant * (-1) ** (i + j)
    return np.transpose(adjoint)
