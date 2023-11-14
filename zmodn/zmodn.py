import numpy as np
from .utils.modular_inverse import vectorize_modular_inverse
from .utils.adjoint_matrix import adjoint_matrix
from .utils.validate_matrix import validate_matrix

FUNCTIONS_HANDLER = dict()


class Zmodn:
    """
    A class for representing integers modulo a given prime number.

    This class provides methods for performing arithmetic operations on integers modulo a given prime number. It can be
    used for applications such as cryptography and computer algebra.

    Attributes:
        representatives: A NumPy array containing the representatives of the Zmodn object.
        module: The prime number modulo which the Zmodn object is defined.

    Methods:
        mod_inv(): Computes the modular inverse of the Zmodn object.
        inv(): Computes the inverse of the Zmodn object, assuming it is a square matrix.
        __add__(other): Adds two Zmodn objects.
        __sub__(other): Subtracts two Zmodn objects.
        __mul__(other): Multiplies two Zmodn objects.
        __truediv__(other): Divides two Zmodn objects.
        __pow__(other): Raises the Zmodn object to the given power.

    Examples:

    ```python
    import numpy as np
    from zmodn import Zmodn

    # Create a Zmodn object with the representatives 2 and 3 modulo 5
    zmodn = Zmodn([2, 3], 5)

    # Print the representatives of the Zmodn object
    print(zmodn.representatives)

    # Add two Zmodn objects
    zmodn_sum = zmodn + Zmodn([1, 4], 5)

    # Print the representatives of the sum
    print(zmodn_sum.representatives)

    # Multiply two Zmodn objects
    zmodn_product = zmodn * Zmodn([1, 4], 5)

    # Print the representatives of the product
    print(zmodn_product.representatives)

    # Compute the modular inverse of a Zmodn object
    zmodn_inverse = zmodn.mod_inv()

    # Print the representatives of the modular inverse
    print(zmodn_inverse.representatives)
    ```
    """

    def __init__(self, matrix_integers, module):
        validated_matrix = validate_matrix(matrix_integers)
        if validated_matrix:
            self.representatives = np.array(validated_matrix) % module
            self.module = module
        else:
            raise TypeError("Matrix must be a list of integers or a single integer")

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
        if not self.module == other.module or not isinstance(other, self.__class__):
            raise ValueError("Modules must be equal")

    def _check_square_matrix(self, matrix):
        if matrix.shape[0] != matrix.shape[1]:
            raise ValueError("Matrix is no square")

    def _check_invertible_matrix(self, matrix):
        determinant = int(np.linalg.det(matrix))
        if determinant == 0:
            raise ValueError("Matrix is no invertible")
        return determinant

    def mod_inv(self):
        integers_array = np.array(self.representatives).astype(int)
        repr_inverse = vectorize_modular_inverse(integers_array, self.module)
        return self.__class__(repr_inverse.tolist(), self.module)

    def inv(self):
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
        self._check_module_and_type(other)
        return all(np.array(self.representatives) == np.array(other.representatives))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        self._check_module_and_type(other)
        return all(np.array(self.representatives) < np.array(other.representatives))

    def __le__(self, other):
        self._check_module_and_type(other)
        return all(np.array(self.representatives) <= np.array(other.representatives))

    def __gt__(self, other):
        self._check_module_and_type(other)
        return all(np.array(self.representatives) > np.array(other.representatives))

    def __ge__(self, other):
        self._check_module_and_type(other)
        return all(np.array(self.representatives) >= np.array(other.representatives))

    def __hash__(self):
        return hash(tuple(self.representatives))

    def __getitem__(self, key):
        return self.representatives[key]

    def __setitem__(self, key, value):
        self.representatives[key] = value

    def __len__(self):
        return len(self.representatives)

    def __iter__(self):
        return iter(self.representatives)

    def __reversed__(self):
        return reversed(self.representatives)

    def __contains__(self, item):
        return item in self.representatives

    def __index__(self):
        return self.representatives.__index__()

    def __bool__(self):
        return bool(self.representatives)

    def __int__(self):
        return int(self.representatives)
