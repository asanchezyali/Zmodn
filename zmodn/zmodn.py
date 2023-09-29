import numpy as np


class Zmodn:
    def __init__(self, module: int = 2):
        self._representative = None
        self.module = module

    @property
    def representative(self):
        return self._representative

    @representative.setter
    def representative(self, value):
        self._representative = value

    def _check_same_module(self, other):
        if not self.module == other.module and not isinstance(other, self.__class__):
            raise ValueError(
                f"Cannot operate {self} and {other}, they are not in the same module"
            )

    def __call__(self, integer: int):
        congruence_class = self.__class__(self.module)
        congruence_class.representative = integer % self.module
        return congruence_class

    def __int__(self):
        return self.representative

    def __repr__(self):
        return f"{self.representative} (mod {self.module})"

    def __add__(self, other: int):
        self._check_same_module(other)
        return self.__call__(self.representative + other.representative)

    def __sub__(self, other: int):
        self._check_same_module(other)
        return self.__call__(self.representative - other.representative)

    def __mul__(self, other: int):
        self._check_same_module(other)
        return self.__call__(self.representative * other.representative)

    def __gt__(self, other: int):
        self._check_same_module(other)
        return self.representative > other.representative

    def __lt__(self, other: int):
        self._check_same_module(other)
        return self.representative < other.representative

    def multiplicative_inverse(self):
        if self.representative == 0:
            raise ZeroDivisionError("Cannot compute the multiplicative inverse of 0")
        aux1 = 0
        aux2 = 1
        y = self.representative
        x = self.module
        while y != 0:
            q, r = divmod(x, y)
            x, y = y, r
            aux1, aux2 = aux2, aux1 - q * aux2
        if x == 1:
            return self.__call__(aux1 % self.module)
        else:
            raise ValueError(f"{self.representative} is not coprime to {self.module}")

    def __truediv__(self, other):
        self._check_same_module(other)
        return self.__call__(self.representative) * other.multiplicative_inverse()
    
    def astype(self, dtype):
        return dtype(self.representative)


class ZmodnArray:
    def __init__(self, module):
        self.module = module
        self._representatives = None
        self.congruence_class = Zmodn(module)

    @property
    def representatives(self):
        return self._representatives

    @representatives.setter
    def representatives(self, value):
        self._representatives = value

    def _check_same_module(self, other):
        if not self.module == other.module and not isinstance(other, self.__class__):
            raise ValueError(
                f"Cannot add {self} and {other}, they are not in the same module"
            )

    def __call__(self, integers: list):
        congruence_class_array = self.__class__(self.module)
        congruence_class = np.vectorize(self.congruence_class)
        congruence_class_array.representatives = np.array(congruence_class(integers))
        return congruence_class_array

    def __repr__(self):
        return f"{self.representatives.astype(int)} (mod {self.module})"

    def __add__(self, other: list):
        self._check_same_module(other)
        return self.__call__((self.representatives + other.representatives).astype(int))

    def __sub__(self, other: list):
        self._check_same_module(other)
        return self.__call__((self.representatives - other.representatives).astype(int))
    
    def __isub__(self, other: list):
        self._check_same_module(other)
        return self.__call__((self.representatives - other.representatives).astype(int))

    def __mul__(self, other: list):
        self._check_same_module(other)
        return self.__call__(
            (np.dot(self.representatives, other.representatives)).astype(int)
        )

    @staticmethod
    def adjoint_of_matrix(matrix):
        adjoint = np.zeros(matrix.shape, dtype=np.int16)
        amount_of_rows, amount_of_columns = matrix.shape
        for i in range(amount_of_rows):
            for j in range(amount_of_columns):
                cofactor_i_j = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
                determinant = int(np.linalg.det(cofactor_i_j))
                adjoint[i][j] = determinant * (-1) ** (i + j)
        return np.transpose(adjoint)

    def inv(self):
        matrix = self.representatives.astype(int)
        if matrix.shape[0] != matrix.shape[1]:
            raise ValueError("Matrix is not square")
        determinant = int(np.linalg.det(matrix))
        if determinant == 0:
            raise ValueError("Matrix is not invertible")
        adjoint = ZmodnArray.adjoint_of_matrix(matrix)
        return self.__call__(
            int(self.congruence_class(1) / self.congruence_class(determinant))
            * adjoint.astype(int)
        )

    def _get_pivot_position(matrix, index):
        return np.argmax(matrix[index:, index]) + index, index

    def _get_pivot(matrix, index_row, index_col):
        return matrix[index_row, index_col]

    def _swap_rows(matrix, index_row_1, index_row_2):
        matrix[[index_row_1, index_row_2]] = matrix[[index_row_2, index_row_1]]

    def rref(self):
        dim_row, dim_col = self.representatives.shape
        matrix_rref = self.representatives.copy()
        num_loop = min(dim_row, dim_col)

        for index in range(num_loop):
            pivot_row, pivot_col = __class__._get_pivot_position(matrix_rref, index)
            pivot = ZmodnArray._get_pivot(matrix_rref, pivot_row, pivot_col)

            if pivot == Zmodn(self.module)(0):
                continue

            if pivot_row != index:
                ZmodnArray._swap_rows(matrix_rref, index, pivot_row)

            for row in range(index + 1, dim_row):
                multiplier = Zmodn(matrix_rref[row, index],  self / pivot
                row_to_add = self.__call__(
                    matrix_rref[index, index:].astype(int) * multiplier.representative
                )
                print(row_to_add)
                print(matrix_rref[row, index:])
                matrix_rref[row, index:] -= row_to_add
        return self.__call__(matrix_rref.astype(int))
