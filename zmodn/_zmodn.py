import numpy as np
from .utils.adjoint_matrix import adjoint_matrix
from .utils.validate_matrix import validate_matrix
from .utils.modular_inverse import vectorize_modular_inverse

FUNCTIONS_HANDLER = dict()


class Zmodn:
    r"""
    Represents elements in the ring of integers modulo n $(Z/nZ)$.

    This class provides operations for modular arithmetic, including addition,
    subtraction, multiplication, division, and exponentiation. It also supports
    matrix operations and modular inverses.

    Group:
        Modular Arithmetic
    """

    def __init__(self, matrix_integers, module):
        r"""
        Initialize a Zmodn object.

        Args:
            matrix_integers (int, list, or numpy.ndarray): The integer(s) to be represented in Z/nZ.
            module (int): The modulus n for Z/nZ.

        Raises:
            TypeError: If matrix_integers is not a valid input type.
            ValueError: If module is not a positive integer.
        """
        validated_matrix = validate_matrix(matrix_integers)
        if not validated_matrix:
            raise TypeError("Matrix must be a list of integers or a single integer")

        if not isinstance(module, (np.int64, int)) or module <= 0:
            raise ValueError("Module must be a positive integer")

        self.module = module
        self.representatives = np.array(validated_matrix) % module

    def __repr__(self):
        r"""
        Return a string representation of the Zmodn object.

        Returns:
            str: String representation of the Zmodn object.
        """
        if len(self.representatives) == 1:
            return f"{self.representatives[0]} (mod {self.module})"
        else:
            return f"{self.representatives} (mod {self.module})"

    def __array_function__(self, func, types, args, kwargs):
        r"""
        Implement NumPy's __array_function__ protocol for custom array-like behavior.

        Args:
            func (callable): The NumPy function being called.
            types (tuple): The types of arguments passed to the function.
            args (tuple): The arguments passed to the function.
            kwargs (dict): The keyword arguments passed to the function.

        Returns:
            The result of the NumPy function applied to Zmodn objects, or NotImplemented.
        """
        if func not in FUNCTIONS_HANDLER:
            return NotImplemented
        if not all(issubclass(t, Zmodn) for t in types):
            return NotImplemented
        return FUNCTIONS_HANDLER[func](*args, **kwargs)

    @staticmethod
    def implements(numpy_function):
        r"""
        Decorator to register implementations of NumPy functions for Zmodn objects.

        Args:
            numpy_function (callable): The NumPy function to implement.

        Returns:
            callable: Decorator function.
        """

        def decorator(function):
            FUNCTIONS_HANDLER[numpy_function] = function
            return function

        return decorator

    def _check_module_and_type(self, other):
        r"""
        Check if the other object is a Zmodn instance with the same module.

        Args:
            other: Object to compare with.

        Raises:
            TypeError: If other is not a Zmodn object.
            ValueError: If the modules are not equal.
        """
        if not isinstance(other, self.__class__):
            raise TypeError("Other must be a Zmodn object")
        if not self.module == other.module:
            raise ValueError("Modules must be equal")

    def _boolean_check_module_and_type(self, other):
        r"""
        Check if the other object is a Zmodn instance with the same module.

        Args:
            other: Object to compare with.

        Returns:
            bool: True if other is a Zmodn object with the same module, False otherwise.
        """
        if not isinstance(other, self.__class__):
            return False
        if not self.module == other.module:
            return False
        return True

    def _check_square_matrix(self, matrix):
        r"""
        Check if the matrix is square.

        Args:
            matrix (numpy.ndarray): Matrix to check.

        Raises:
            ValueError: If the matrix is not two-dimensional or not square.
        """
        if len(matrix.shape) != 2:
            raise ValueError("Matrix is not two-dimensional")
        if matrix.shape[0] != matrix.shape[1]:
            raise ValueError("Matrix is not square")

    def _check_invertible_matrix(self, matrix):
        r"""
        Check if the matrix is invertible and return its determinant.

        Args:
            matrix (numpy.ndarray): Matrix to check.

        Returns:
            int: Determinant of the matrix.

        Raises:
            ValueError: If the matrix is not invertible.
        """
        determinant = int(np.linalg.det(matrix))
        if determinant == 0:
            raise ValueError("Matrix is not invertible")
        return determinant

    @property
    def classes(self):
        r"""
        Return the representatives of the Zmodn object as a list of Zmodn objects.

        Returns:
            list: List of Zmodn objects, each representing one element.
        """
        return [self.__class__(int(element), self.module) for element in self.representatives]

    def mod_inv(self):
        r"""
        Compute the modular inverse of the Zmodn object.

        Returns:
            Zmodn: Modular inverse as a Zmodn object.

        Raises:
            ValueError: If the Zmodn object represents a matrix (use inv() for matrices).
        """
        integers_array = np.array(self.representatives).astype(int)
        repr_inverse = vectorize_modular_inverse(integers_array, self.module)
        return self.__class__(repr_inverse.tolist(), self.module)

    def inv(self):
        r"""
        Compute the inverse of the Zmodn object (for both scalars and matrices).

        Returns:
            Zmodn: Inverse as a Zmodn object.

        Raises:
            ValueError: If the matrix is not square or not invertible.
        """
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
        r"""
        Add two Zmodn objects.

        Args:
            other (Zmodn): The Zmodn object to add.

        Returns:
            Zmodn: The result of the addition.

        Raises:
            TypeError: If other is not a Zmodn object.
            ValueError: If the modules are not equal.
        """
        self._check_module_and_type(other)
        repr_sum = (np.array(self.representatives) + np.array(other.representatives)) % self.module
        return self.__class__(repr_sum.tolist(), self.module)

    @implements(np.subtract)
    def __sub__(self, other):
        r"""
        Subtract two Zmodn objects.

        Args:
            other (Zmodn): The Zmodn object to subtract.

        Returns:
            Zmodn: The result of the subtraction.

        Raises:
            TypeError: If other is not a Zmodn object.
            ValueError: If the modules are not equal.
        """
        self._check_module_and_type(other)
        repr_sub = (np.array(self.representatives) - np.array(other.representatives)) % self.module
        return self.__class__(repr_sub.tolist(), self.module)

    @implements(np.multiply)
    def __mul__(self, other):
        r"""
        Multiply two Zmodn objects.

        Args:
            other (Zmodn): The Zmodn object to multiply.

        Returns:
            Zmodn: The result of the multiplication.

        Raises:
            TypeError: If other is not a Zmodn object.
            ValueError: If the modules are not equal.
        """
        self._check_module_and_type(other)
        repr_mul = (np.array(self.representatives) * np.array(other.representatives)) % self.module
        return self.__class__(repr_mul.tolist(), self.module)

    @implements(np.dot)
    def __matmul__(self, other):
        r"""
        Perform matrix multiplication of two Zmodn objects.

        Args:
            other (Zmodn): The Zmodn object to multiply.

        Returns:
            Zmodn: The result of the matrix multiplication.

        Raises:
            TypeError: If other is not a Zmodn object.
            ValueError: If the modules are not equal or if the matrices are incompatible.
        """
        self._check_module_and_type(other)
        repr_mul = (np.array(self.representatives) @ np.array(other.representatives)) % self.module
        return self.__class__(repr_mul.tolist(), self.module)

    @implements(np.divide)
    def __truediv__(self, other):
        r"""
        Divide two Zmodn objects.

        Args:
            other (Zmodn): The Zmodn object to divide by.

        Returns:
            Zmodn: The result of the division.

        Raises:
            TypeError: If other is not a Zmodn object.
            ValueError: If the modules are not equal or if other is not invertible.
        """
        self._check_module_and_type(other)
        repr_div = (np.array(self.representatives) * np.array(other.mod_inv().representatives)) % self.module
        return self.__class__(repr_div.tolist(), self.module)

    @implements(np.power)
    def __pow__(self, other):
        r"""
        Raise Zmodn object to a power.

        Args:
            other (int): The exponent.

        Returns:
            Zmodn: The result of the exponentiation.

        Raises:
            TypeError: If the exponent is not an integer.
        """
        if not isinstance(other, int):
            raise TypeError("Exponent must be an integer")
        repr_pow = (np.array(self.representatives) ** other) % self.module
        return self.__class__(repr_pow.tolist(), self.module)

    @implements(np.negative)
    def __neg__(self):
        r"""
        Negate the Zmodn object.

        Returns:
            Zmodn: The negation of the Zmodn object.
        """
        repr_neg = (-np.array(self.representatives)) % self.module
        return self.__class__(repr_neg.tolist(), self.module)

    @implements(np.positive)
    def __pos__(self):
        r"""
        Return the positive of the Zmodn object (identity operation).

        Returns:
            Zmodn: The Zmodn object itself.
        """
        repr_pos = (+np.array(self.representatives)) % self.module
        return self.__class__(repr_pos.tolist(), self.module)

    def __eq__(self, other):
        r"""
        Check if two Zmodn objects are equal.

        Args:
            other: Object to compare with.

        Returns:
            bool: True if the objects are equal, False otherwise.
        """
        if not self._boolean_check_module_and_type(other):
            return False
        return all(np.array(self.representatives) == np.array(other.representatives))

    def __ne__(self, other):
        r"""
        Check if two Zmodn objects are not equal.

        Args:
            other: Object to compare with.

        Returns:
            bool: True if the objects are not equal, False otherwise.
        """
        return not self.__eq__(other)

    def __lt__(self, other):
        r"""
        Check if this Zmodn object is less than another.

        Args:
            other (Zmodn): The Zmodn object to compare with.

        Returns:
            bool: True if this object is less than other, False otherwise.
        """
        if not self._boolean_check_module_and_type(other):
            return False
        return all(np.array(self.representatives) < np.array(other.representatives))

    def __le__(self, other):
        r"""
        Check if this Zmodn object is less than or equal to another.

        Args:
            other (Zmodn): The Zmodn object to compare with.

        Returns:
            bool: True if this object is less than or equal to other, False otherwise.
        """
        if not self._boolean_check_module_and_type(other):
            return False
        return all(np.array(self.representatives) <= np.array(other.representatives))

    def __gt__(self, other):
        r"""
        Check if this Zmodn object is greater than another.

        Args:
            other (Zmodn): The Zmodn object to compare with.

        Returns:
            bool: True if this object is greater than other, False otherwise.
        """
        if not self._boolean_check_module_and_type(other):
            return False
        return all(np.array(self.representatives) > np.array(other.representatives))

    def __ge__(self, other):
        r"""
        Check if this Zmodn object is greater than or equal to another.

        Args:
            other (Zmodn): The Zmodn object to compare with.

        Returns:
            bool: True if this object is greater than or equal to other, False otherwise.
        """
        if not self._boolean_check_module_and_type(other):
            return False
        return all(np.array(self.representatives) >= np.array(other.representatives))

    def __hash__(self):
        r"""
        Compute a hash value for the Zmodn object.

        Returns:
            int: Hash value of the Zmodn object.
        """
        return hash(tuple(self.representatives) + (self.module,))

    def __getitem__(self, key):
        r"""
        Get an item or slice from the Zmodn object.

        Args:
            key: Index or slice to retrieve.

        Returns:
            Zmodn: A new Zmodn object containing the requested item(s).
        """
        return self.__class__(self.representatives[key].tolist(), self.module)

    def __setitem__(self, key, value):
        r"""
        Set an item or slice in the Zmodn object.

        Args:
            key: Index or slice to set.
            value (int): Value to set.

        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")
        self.representatives[key] = value % self.module

    def __delitem__(self, key):
        r"""
        Delete an item or slice from the Zmodn object.

        Args:
            key: Index or slice to delete.
        """
        self.representatives = np.delete(self.representatives, key)

    def __len__(self):
        r"""
        Get the length of the Zmodn object.

        Returns:
            int: The number of elements in the Zmodn object.
        """
        return len(self.representatives)

    def __iter__(self):
        r"""
        Create an iterator for the Zmodn object.

        Returns:
            iterator: An iterator over the elements of the Zmodn object.
        """
        return iter(self.classes)

    def __reversed__(self):
        r"""
        Create a reversed iterator for the Zmodn object.

        Returns:
            iterator: A reversed iterator over the elements of the Zmodn object.
        """
        return reversed(self.classes)

    def __contains__(self, item):
        r"""
        Check if an item is in the Zmodn object.

        Args:
            item: The item to check for.

        Returns:
            bool: True if the item is in the Zmodn object, False otherwise.
        """
        return item in self.classes

    def __bool__(self):
        r"""
        Check if the Zmodn object is True (non-zero).

        Returns:
            bool: True if any element in the Zmodn object is non-zero, False otherwise.
        """
        return bool(self.representatives.all())

    def __int__(self):
        r"""
        Convert the Zmodn object to an integer.

        Returns:
            int: The integer representation of the Zmodn object.

        Raises:
            ValueError: If the Zmodn object has more than one representative.
        """
        if self.representatives.size != 1:
            raise ValueError("Cannot convert Zmodn object with more than one representative to an integer")
        return int(self.representatives[0])
