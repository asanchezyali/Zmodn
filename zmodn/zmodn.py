import numpy as np
from .utils.adjoint_matrix import adjoint_matrix
from .utils.validate_matrix import validate_matrix
from .utils.modular_inverse import vectorize_modular_inverse

FUNCTIONS_HANDLER = dict()


class Zmodn:
    def __init__(self, matrix_integers, module):
        validated_matrix = validate_matrix(matrix_integers)
        if not validated_matrix:
            raise TypeError("Matrix must be a list of integers or a single integer")

        if not isinstance(module, (np.int64, int)) or module <= 0:
            raise ValueError("Module must be a positive integer")

        self.module = module
        self.representatives = np.array(validated_matrix) % module

    def __repr__(self):
        if len(self.representatives) == 1:
            return f"{self.representatives[0]} (mod {self.module})"
        else:
            return f"{self.representatives} (mod {self.module})"

    def __array_function__(self, func, types, args, kwargs):
        if func not in FUNCTIONS_HANDLER:
            return NotImplemented
        if not all(issubclass(t, Zmodn) for t in types):
            return NotImplemented
        return FUNCTIONS_HANDLER[func](*args, **kwargs)

    def implements(numpy_function):
        def decorator(function):
            FUNCTIONS_HANDLER[numpy_function] = function
            return function

        return decorator

    def _check_module_and_type(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError("Other must be a Zmodn object")
        if not self.module == other.module:
            raise ValueError("Modules must be equal")

    def _boolean_check_module_and_type(self, other):
        if not isinstance(other, self.__class__):
            return False
        if not self.module == other.module:
            return False
        return True

    def _check_square_matrix(self, matrix):
        if len(matrix.shape) != 2:
            raise ValueError("Matrix is no two-dimensional")
        if matrix.shape[0] != matrix.shape[1]:
            raise ValueError("Matrix is no square")

    def _check_invertible_matrix(self, matrix):
        determinant = int(np.linalg.det(matrix))
        if determinant == 0:
            raise ValueError("Matrix is no invertible")
        return determinant

    @property
    def classes(self):
        return [self.__class__(int(element), self.module) for element in self.representatives]

    def mod_inv(self):
        r"""
        Does not work for matrices

        Arguments:
            self (Zmodn): Zmodn object

        Returns:
            Zmodn: Zmodn object

        Raises:
            ValueError: If the Zmodn object has more than one representative

        Group:
            Modular arithmetic
        """
        integers_array = np.array(self.representatives).astype(int)
        repr_inverse = vectorize_modular_inverse(integers_array, self.module)
        return self.__class__(repr_inverse.tolist(), self.module)

    def inv(self):
        if len(self.representatives) == 1:
            return self.mod_inv()
        matrix = self.representatives.astype(int)
        self._check_square_matrix(matrix)
        determinant = self._check_invertible_matrix(matrix)
        adjoint = adjoint_matrix(matrix).astype(int)
        multiplier = int(self.__class__(1, self.module) / self.__class__(determinant, self.module))
        inverse_matrix = multiplier * adjoint
        return self.__class__(inverse_matrix.tolist(), self.module)

    @implements(np.add)
    def __add__(self, other):
        self._check_module_and_type(other)
        repr_sum = (np.array(self.representatives) + np.array(other.representatives)) % self.module
        return self.__class__(repr_sum.tolist(), self.module)

    @implements(np.subtract)
    def __sub__(self, other):
        self._check_module_and_type(other)
        repr_sub = (np.array(self.representatives) - np.array(other.representatives)) % self.module
        return self.__class__(repr_sub.tolist(), self.module)

    @implements(np.multiply)
    def __mul__(self, other):
        self._check_module_and_type(other)
        repr_mul = (np.array(self.representatives) * np.array(other.representatives)) % self.module
        return self.__class__(repr_mul.tolist(), self.module)

    @implements(np.dot)
    def __matmul__(self, other):
        self._check_module_and_type(other)
        repr_mul = (np.array(self.representatives) @ np.array(other.representatives)) % self.module
        return self.__class__(repr_mul.tolist(), self.module)

    @implements(np.divide)
    def __truediv__(self, other):
        self._check_module_and_type(other)
        repr_div = (np.array(self.representatives) * np.array(other.mod_inv().representatives)) % self.module
        return self.__class__(repr_div.tolist(), self.module)

    @implements(np.power)
    def __pow__(self, other):
        if not isinstance(other, int):
            raise TypeError("Exponent must be an integer")
        repr_pow = (np.array(self.representatives) ** other) % self.module
        return self.__class__(repr_pow.tolist(), self.module)

    @implements(np.negative)
    def __neg__(self):
        repr_neg = (-np.array(self.representatives)) % self.module
        return self.__class__(repr_neg.tolist(), self.module)

    @implements(np.positive)
    def __pos__(self):
        repr_pos = (+np.array(self.representatives)) % self.module
        return self.__class__(repr_pos.tolist(), self.module)

    def __eq__(self, other):
        if not self._boolean_check_module_and_type(other):
            return False
        return all(np.array(self.representatives) == np.array(other.representatives))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if not self._boolean_check_module_and_type(other):
            return False
        return all(np.array(self.representatives) < np.array(other.representatives))

    def __le__(self, other):
        if not self._boolean_check_module_and_type(other):
            return False
        return all(np.array(self.representatives) <= np.array(other.representatives))

    def __gt__(self, other):
        if not self._boolean_check_module_and_type(other):
            return False
        return all(np.array(self.representatives) > np.array(other.representatives))

    def __ge__(self, other):
        if not self._boolean_check_module_and_type(other):
            return False
        return all(np.array(self.representatives) >= np.array(other.representatives))

    def __hash__(self):
        return hash(tuple(self.representatives) + (self.module,))

    def __getitem__(self, key):
        return self.__class__(self.representatives[key].tolist(), self.module)

    def __setitem__(self, key, value):
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")
        self.representatives[key] = value % self.module

    def __delitem__(self, key):
        self.representatives = np.delete(self.representatives, key)

    def __len__(self):
        return len(self.representatives)

    def __iter__(self):
        return iter(self.classes)

    def __reversed__(self):
        return reversed(self.classes)

    def __contains__(self, item):
        return item in self.classes

    def __bool__(self):
        return bool(self.representatives.all())

    def __int__(self):
        if self.representatives.size != 1:
            raise ValueError("Cannot convert Zmodn object with more than one representative to an integer")
        return int(self.representatives[0])
