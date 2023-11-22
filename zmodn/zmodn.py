import numpy as np
from .utils.adjoint_matrix import adjoint_matrix
from .utils.validate_matrix import validate_matrix
from .utils.modular_inverse import vectorize_modular_inverse

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
        __matmul__(other): Multiplies two Zmodn objects.
        __truediv__(other): Divides two Zmodn objects.
        __pow__(other): Raises the Zmodn object to the given power.
        __neg__(): Negates the Zmodn object.
        __pos__(): Returns the Zmodn object.
        __eq__(other): Checks if two Zmodn objects are equal.
        __ne__(other): Checks if two Zmodn objects are not equal.
        __lt__(other): Checks if the Zmodn object is less than the other Zmodn object.
        __le__(other): Checks if the Zmodn object is less than or equal to the other Zmodn object.
        __gt__(other): Checks if the Zmodn object is greater than the other Zmodn object.
        __ge__(other): Checks if the Zmodn object is greater than or equal to the other Zmodn object.
        __hash__(): Returns the hash of the Zmodn object.
        __getitem__(key): Returns the representative at the given index.
        __setitem__(key, value): Sets the representative at the given index to the given value.
        __len__(): Returns the number of representatives of the Zmodn object.
        __iter__(): Returns an iterator over the representatives of the Zmodn object.
        __reversed__(): Returns a reverse iterator over the representatives of the Zmodn object.
        __contains__(item): Checks if the Zmodn object contains the given representative.
        __bool__(): Returns True if the Zmodn object is not empty, False otherwise.
        __int__(): Returns the representative of the Zmodn object.

    Examples:

    ```python
    import numpy as np
    from zmodn import Zmodn

    # Create a Zmodn object with the representatives 2 and 3 modulo 5
    zmodn = Zmodn([2, 3], 5)

    # Add two Zmodn objects
    zmodn_sum = zmodn + Zmodn([1, 4], 5)

    # Subtract two Zmodn objects
    zmodn_difference = zmodn - Zmodn([1, 4], 5)

    # Multiply two Zmodn objects
    zmodn_product = zmodn * Zmodn([1, 4], 5)

    # Divide two Zmodn objects
    zmodn_quotient = zmodn / Zmodn([1, 4], 5)

    # Compute the modular inverse of a Zmodn object
    zmodn_inverse = zmodn.mod_inv()
    ```
    """

    def __init__(self, matrix_integers, module):
        """
        The function initializes an object with a matrix of integers and a module, and performs validation on the matrix before assigning it to the object.

        :param matrix_integers: The `matrix_integers` parameter is the input matrix that you want to perform operations on. It can be either a list of integers or a single integer
        :param module: The `module` parameter is an integer that represents the modulus value. It is used to perform the modulo operation on each element of the matrix. The modulo operation calculates the remainder when dividing each element by the modulus value
        """
        validated_matrix = validate_matrix(matrix_integers)
        if validated_matrix:
            self.representatives = np.array(validated_matrix) % module
            self.module = module
        else:
            raise TypeError("Matrix must be a list of integers or a single integer")

    def __repr__(self):
        """
        The `__repr__` function returns a string representation of an object, including its representatives and module.
        :return: The `__repr__` method is returning a string representation of the object. If the length of the `representatives` list is 1, it returns a string with the first element of the list followed by " (mod {self.module})". Otherwise, it returns a string with the entire `representatives` list followed by " (mod {self.module})".
        """
        if len(self.representatives) == 1:
            return f"{self.representatives[0]} (mod {self.module})"
        else:
            return f"{self.representatives} (mod {self.module})"

    def __array_function__(self, func, types, args, kwargs):
        """
        The `__array_function__` method is used to handle array functions for objects of type `Zmodn`.

        :param func: The `func` parameter is the function being called. It is a reference to the function object itself
        :param types: A tuple of types that are being passed as arguments to the function
        :param args: args is a tuple containing the positional arguments passed to the function
        :param kwargs: kwargs is a dictionary that contains any additional keyword arguments passed to the function
        :return: The code is returning the result of calling the function specified by `func` with the arguments `args` and `kwargs`.
        """
        if func not in FUNCTIONS_HANDLER:
            return NotImplemented
        if not all(issubclass(t, Zmodn) for t in types):
            return NotImplemented
        return FUNCTIONS_HANDLER[func](*args, **kwargs)

    def implements(numpy_function):
        """
        The `implements` function is a decorator that registers a function as the implementation for a specific numpy function.

        :param numpy_function: The `numpy_function` parameter is the name of a NumPy function that you want to implement
        :return: The decorator function is being returned.
        """

        def decorator(function):
            FUNCTIONS_HANDLER[numpy_function] = function
            return function

        return decorator

    def _check_module_and_type(self, other):
        """
        The function checks if the input object is of the same class and has the same module as the current object.

        :param other: The `other` parameter is an object that is being compared to the current object. It is expected to be an instance of the same class as the current object (`self.__class__`)
        """
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
