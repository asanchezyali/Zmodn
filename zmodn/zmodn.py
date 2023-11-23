import numpy as np
from .utils.adjoint_matrix import adjoint_matrix
from .utils.validate_matrix import validate_matrix
from .utils.modular_inverse import vectorize_modular_inverse

FUNCTIONS_HANDLER = dict()


class Zmodn:
    """
    A class for representing integers modulo a given positive integer.

    This class provides methods for performing arithmetic operations on integers modulo a given positive integer.  It
    can be used for applications such as cryptography and computer algebra.

    Attributes:
        representatives: A NumPy array containing the representatives of the Zmodn object.  module: The positive integer
        modulo which the Zmodn object is defined.

    Methods:
        mod_inv(): Computes the modular inverse of the Zmodn object.  inv(): Computes the inverse of the Zmodn object,
            assuming it is a square matrix.
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
        __int__(): Returns the representative of theZmodn object.

    Examples:

    ```python import numpy as np from zmodn import Zmodn

    # Create a Zmodn object with the representatives 2 and 3 modulo 5 zmodn = Zmodn([2, 3], 5)

    # Add two Zmodn objects zmodn_sum = zmodn + Zmodn([1, 4], 5)

    # Subtract two Zmodn objects zmodn_difference = zmodn - Zmodn([1, 4], 5)

    # Multiply two Zmodn objects zmodn_product = zmodn * Zmodn([1, 4], 5)

    # Divide two Zmodn objects zmodn_quotient = zmodn / Zmodn([1, 4], 5)

    # Compute the modular inverse of a Zmodn object zmodn_inverse = zmodn.mod_inv() ```
    """

    def __init__(self, matrix_integers, module):
        """
        The function initializes an object with a matrix of integers and a module, and performs validation on the matrix
        before assigning it to the object.

        :param matrix_integers: The `matrix_integers` parameter is the input matrix that you want to perform operations
            on. It can be either a list of integers or a single integer
        :param module: The `module` parameter is an integer that represents the modulus value. It is used to perform the
            modulo operation on each element of the matrix. The modulo operation calculates the remainder when dividing
            each element by the modulus value
        """
        validated_matrix = validate_matrix(matrix_integers)
        if not validated_matrix:
            raise TypeError("Matrix must be a list of integers or a single integer")

        if not isinstance(module, (np.int64, int)) or module <= 0:
            raise ValueError("Module must be a positive integer")

        self.module = module
        self.representatives = np.array(validated_matrix) % module

    def __repr__(self):
        """
        The `__repr__` function returns a string representation of an object, including its representatives and module.
        :return: The `__repr__` method is returning a string representation of the object. If the length of the
        `representatives` list is 1, it returns a string with the first element of the list followed by " (mod
        {self.module})". Otherwise, it returns a string with the entire `representatives` list followed by " (mod
        {self.module})".
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
        :return: The code is returning the result of calling the function specified by `func` with the arguments `args`
            and `kwargs`.
        """
        if func not in FUNCTIONS_HANDLER:
            return NotImplemented
        if not all(issubclass(t, Zmodn) for t in types):
            return NotImplemented
        return FUNCTIONS_HANDLER[func](*args, **kwargs)

    def implements(numpy_function):
        """
        The `implements` function is a decorator that registers a function as the implementation for a specific numpy
        function.

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

        :param other: The `other` parameter is an object that is being compared to the current object. It is expected to
            be an instance of the same class as the current object (`self.__class__`)
        """
        if not isinstance(other, self.__class__):
            raise TypeError("Other must be a Zmodn object")
        if not self.module == other.module:
            raise ValueError("Modules must be equal")

    def _boolean_check_module_and_type(self, other):
        """
        The function checks if the given object is of the same class and has the same module as the current object.

        :param other: The "other" parameter is a variable that represents another object that we want to compare with
            the current object
        :return: a boolean value. It returns True if the other object is an instance of the same class as self and if
            the module attribute of self is equal to the module attribute of the other object. Otherwise, it returns
            False.
        """
        if not isinstance(other, self.__class__):
            return False
        if not self.module == other.module:
            return False
        return True

    def _check_square_matrix(self, matrix):
        """
        The above function checks if a matrix is square and invertible.

        :param matrix: The "matrix" parameter is a two-dimensional array or matrix
        """
        if len(matrix.shape) != 2:
            raise ValueError("Matrix is no two-dimensional")
        if matrix.shape[0] != matrix.shape[1]:
            raise ValueError("Matrix is no square")

    def _check_invertible_matrix(self, matrix):
        """
        The function checks if a matrix is invertible by calculating its determinant and raising a ValueError if the
        determinant is zero.

        :param matrix: The `matrix` parameter is a 2-dimensional array or matrix
        :return: the determinant of the matrix.
        """
        determinant = int(np.linalg.det(matrix))
        if determinant == 0:
            raise ValueError("Matrix is no invertible")
        return determinant

    @property
    def classes(self):
        """
        The function returns a list of instances of the same class, with each instance initialized with an integer
        element and a module.  :return: The method is returning a list of instances of the same class as the current
        instance. Each instance is created with an integer element from the "representatives" attribute and the "module"
        attribute of the current instance.
        """
        return [self.__class__(int(element), self.module) for element in self.representatives]

    def mod_inv(self):
        """
        The function calculates the modular inverse of an array of integers and returns a new object with the inverse
        values.  :return: an instance of the same class, with the representatives being the modular inverses of the
        original representatives, and the module being the same as the original module.
        """
        integers_array = np.array(self.representatives).astype(int)
        repr_inverse = vectorize_modular_inverse(integers_array, self.module)
        return self.__class__(repr_inverse.tolist(), self.module)

    def inv(self):
        """
        The function calculates the inverse of a matrix if it is invertible.  :return: the inverse of a matrix.
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
        """
        The above function overloads the addition operator for a class by adding the representatives of two instances
        and returning a new instance with the result.

        :param other: The `other` parameter represents another instance of the same class that you are defining. It is
            the object that you want to add to the current instance
        :return: The code is returning an instance of the class that the method belongs to.
        """
        self._check_module_and_type(other)
        repr_sum = (np.array(self.representatives) + np.array(other.representatives)) % self.module
        return self.__class__(repr_sum.tolist(), self.module)

    @implements(np.subtract)
    def __sub__(self, other):
        """
        The above function subtracts the representatives of two objects and returns a new object with the result.

        :param other: The `other` parameter is an object of the same class as the current object
        :return: The code is returning an instance of the same class with the representatives subtracted element-wise
            and then taken modulo the module value.
        """
        self._check_module_and_type(other)
        repr_sub = (np.array(self.representatives) - np.array(other.representatives)) % self.module
        return self.__class__(repr_sub.tolist(), self.module)

    @implements(np.multiply)
    def __mul__(self, other):
        """
        The above function performs element-wise multiplication of two objects, checks their module and type, and
        returns a new object with the resulting representatives modulo the module.

        :param other: The "other" parameter is an object of the same class as the current object
        :return: The code is returning an instance of the same class with the result of element-wise multiplication of
            the `representatives` attribute of `self` and `other`, modulo `self.module`.
        """
        self._check_module_and_type(other)
        repr_mul = (np.array(self.representatives) * np.array(other.representatives)) % self.module
        return self.__class__(repr_mul.tolist(), self.module)

    @implements(np.dot)
    def __matmul__(self, other):
        """
        The `__matmul__` function performs matrix multiplication on the representatives of two objects and returns a new
        object with the result.

        :param other: The `other` parameter represents another object of the same class as the current object
        :return: The code is returning an instance of the same class with the result of the matrix multiplication
            operation.
        """
        self._check_module_and_type(other)
        repr_mul = (np.array(self.representatives) @ np.array(other.representatives)) % self.module
        return self.__class__(repr_mul.tolist(), self.module)

    @implements(np.divide)
    def __truediv__(self, other):
        """
        The above function overloads the division operator for a custom class by performing element-wise division of the
        representatives of two objects and returning a new object.

        :param other: The `other` parameter represents the object that is being divided by the current object
        :return: The code is returning an instance of the same class with the result of the division operation.
        """
        self._check_module_and_type(other)
        repr_div = (np.array(self.representatives) * np.array(other.mod_inv().representatives)) % self.module
        return self.__class__(repr_div.tolist(), self.module)

    @implements(np.power)
    def __pow__(self, other):
        """
        The function raises each element in a list to a given exponent and returns a new list.

        :param other: The `other` parameter represents the exponent to which the array `self.representatives` will be
            raised. It should be an integer value
        :return: The code is returning an instance of the same class with the result of raising each element in the
            `representatives` list to the power of `other`, modulo `self.module`.
        """
        if not isinstance(other, int):
            raise TypeError("Exponent must be an integer")
        repr_pow = (np.array(self.representatives) ** other) % self.module
        return self.__class__(repr_pow.tolist(), self.module)

    @implements(np.negative)
    def __neg__(self):
        """
        The above function returns the negative of a given object by taking the modulo of its representatives with
        respect to a specified module.  :return: The `__neg__` method is returning an instance of the same class with
        the negative values of the `representatives` attribute.
        """
        repr_neg = (-np.array(self.representatives)) % self.module
        return self.__class__(repr_neg.tolist(), self.module)

    @implements(np.positive)
    def __pos__(self):
        """
        The above function returns a new instance of the class with the representatives of the current instance modified
        by taking the modulo of each element with the module attribute.  :return: The code is returning an instance of
        the class with the updated representatives.
        """
        repr_pos = (+np.array(self.representatives)) % self.module
        return self.__class__(repr_pos.tolist(), self.module)

    def __eq__(self, other):
        """
        The function checks if two objects are equal by comparing their representatives.

        :param other: The `other` parameter is the object that we are comparing to the current object. In this case, it
            is being used to check if the `representatives` attribute of the current object is equal to the
            `representatives` attribute of the `other` object
        :return: The `__eq__` method is returning a boolean value. If the `other` object is not of the same module and
            type as the current object, it returns `False`. Otherwise, it compares the `representatives` attribute of
            both objects using numpy's `array_equal` function and returns the result.
        """
        if not self._boolean_check_module_and_type(other):
            return False
        return all(np.array(self.representatives) == np.array(other.representatives))

    def __ne__(self, other):
        """
        The above function defines the "not equal" operator for a class by using the "equal" operator.

        :param other: The "other" parameter is a reference to another object that is being compared to the current
            object
        :return: The __ne__ method is returning the opposite of the result of the __eq__ method.
        """
        return not self.__eq__(other)

    def __lt__(self, other):
        """
        The function compares two objects based on their representatives and returns True if all elements of the first
        object are less than the corresponding elements of the second object.

        :param other: The `other` parameter is an object of the same class as the current object
        :return: The code is returning a boolean value. If the condition `self._boolean_check_module_and_type(other)` is
            not met, it returns `False`. Otherwise, it returns the result of the comparison
            `all(np.array(self.representatives) < np.array(other.representatives))`.
        """
        if not self._boolean_check_module_and_type(other):
            return False
        return all(np.array(self.representatives) < np.array(other.representatives))

    def __le__(self, other):
        """
        The function checks if all elements in the `representatives` attribute of `self` are less than or equal to the
        corresponding elements in the `representatives` attribute of `other`.

        :param other: The parameter "other" refers to another object that is being compared to the current object. In
            this case, it seems like both objects have a property called "representatives" which is expected to be a
            list or array-like object. The code is checking if all elements in the "representatives"
        :return: The code is returning a boolean value. If the condition `not
            self._boolean_check_module_and_type(other)` is true, then it returns False. Otherwise, it checks if all
            elements in the array `self.representatives` are less than or equal to the corresponding elements in the
            array `other.representatives`. If this condition is true for all elements, then it returns True. Otherwise,
        """
        if not self._boolean_check_module_and_type(other):
            return False
        return all(np.array(self.representatives) <= np.array(other.representatives))

    def __gt__(self, other):
        """
        The function compares the representatives of two objects and returns True if all the representatives of the
        first object are greater than the corresponding representatives of the second object.

        :param other: The `other` parameter represents another object that we are comparing to the current object
        :return: The code is returning a boolean value. If the condition `self._boolean_check_module_and_type(other)` is
            not met, it returns `False`. Otherwise, it compares each element in the `representatives` attribute of
            `self` with the corresponding element in the `representatives` attribute of `other`. If all elements in
            `self.representatives` are greater than the corresponding elements in `
        """
        if not self._boolean_check_module_and_type(other):
            return False
        return all(np.array(self.representatives) > np.array(other.representatives))

    def __ge__(self, other):
        """
        The function checks if all elements in the `representatives` attribute of the current object are greater than or
        equal to the corresponding elements in the `representatives` attribute of the `other` object.

        :param other: The parameter "other" refers to another object that you are comparing with the current object. In
            this case, it seems like both objects have a property called "representatives", which is expected to be an
            iterable (e.g., a list or a numpy array). The code is checking if all elements
        :return: The code is returning a boolean value. If the condition `not
            self._boolean_check_module_and_type(other)` is true, then it returns False. Otherwise, it returns the result
            of the comparison `all(np.array(self.representatives) >= np.array(other.representatives))`.
        """
        if not self._boolean_check_module_and_type(other):
            return False
        return all(np.array(self.representatives) >= np.array(other.representatives))

    def __hash__(self):
        """
        The `__hash__` function returns the hash value of a tuple consisting of the `representatives` attribute and the
        `module` attribute.  :return: The `__hash__` method is returning the hash value of a tuple. The tuple is created
        by concatenating the `self.representatives` list with the `self.module` attribute.
        """
        return hash(tuple(self.representatives) + (self.module,))

    def __getitem__(self, key):
        """
        The `__getitem__` function returns a new instance of the class with the representatives corresponding to the
        given key.

        :param key: The `key` parameter is the index or key used to access an element in the `representatives` attribute
        :return: The `__getitem__` method is returning an instance of the class `self.__class__`.
        """
        return self.__class__(self.representatives[key].tolist(), self.module)

    def __setitem__(self, key, value):
        """
        The function sets the value of a key in a dictionary, but raises an error if the value is not an integer.

        :param key: The key parameter is the key that will be used to access the value in the dictionary
        :param value: The `value` parameter represents the value that you want to assign to the specified key in the
            `representatives` dictionary
        """
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")
        self.representatives[key] = value % self.module

    def __delitem__(self, key):
        """
        The `__delitem__` function deletes an element from the `representatives` array at the specified key/index.

        :param key: The `key` parameter in the `__delitem__` method represents the index or indices of the elements that
            you want to delete from the `self.representatives` array
        """
        self.representatives = np.delete(self.representatives, key)

    def __len__(self):
        """
        The function returns the length of the "representatives" attribute of the object.  :return: The length of the
        "representatives" attribute.
        """
        return len(self.representatives)

    def __iter__(self):
        """
        The function returns an iterator for the "classes" attribute.  :return: The `iter()` function is being called on
        `self.classes`, which is a collection of classes. The `iter()` function returns an iterator object, which allows
        us to iterate over the elements in the collection. So, in this case, the iterator object is being returned.
        """
        return iter(self.classes)

    def __reversed__(self):
        """
        The `__reversed__` function returns a reversed iterator of the `classes` attribute.  :return: The reversed
        iterator of the "classes" attribute.
        """
        return reversed(self.classes)

    def __contains__(self, item):
        """
        The function checks if an item is in a list called "classes".

        :param item: The `item` parameter represents the object that is being checked for containment in the
            `self.classes` attribute
        :return: The code is returning whether the item is in the classes list.
        """
        return item in self.classes

    def __bool__(self):
        """
        The function returns True if there are any representatives, and False otherwise.  :return: The code is returning
        a boolean value based on whether there are any representatives associated with the object. If there are any
        representatives, the function will return True. If there are no representatives, the function will return False.
        """
        return bool(self.representatives.all())

    def __int__(self):
        """
        The function converts a Zmodn object with a single representative to an integer.  :return: The code is returning
        an integer value.
        """
        if self.representatives.size != 1:
            raise ValueError("Cannot convert Zmodn object with more than one representative to an integer")
        return int(self.representatives[0])
