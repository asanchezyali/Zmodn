import numpy as np
from .utils.modular_inverse import vectorize_modular_inverse

FUNCTIONS_HANDLER = dict()


class Zmodn:
    def __init__(self, integers, module):
        if isinstance(integers, int):
            integers = [integers]
        elif isinstance(integers, list):
            for i in integers:
                if not isinstance(i, int):
                    raise TypeError("All elements of the list must be integers")
        else:
            raise TypeError("Integers must be an integer or a list of integers")
        self.representatives = np.array(integers) % module
        self.module = module

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

    @implements(np.add)
    def __add__(self, other):
        if not self.module == other.module and not isinstance(other, self.__class__):
            raise ValueError("Modules must be equal")
        repr_sum = (np.array(self.representatives) + np.array(other.representatives)) % self.module
        return self.__class__(repr_sum.tolist(), self.module)

    @implements(np.subtract)
    def __sub__(self, other):
        if not self.module == other.module and not isinstance(other, self.__class__):
            raise ValueError("Modules must be equal")
        repr_sub = (np.array(self.representatives) - np.array(other.representatives)) % self.module
        return self.__class__(repr_sub.tolist(), self.module)

    @implements(np.multiply)
    def __mul__(self, other):
        if not self.module == other.module and not isinstance(other, self.__class__):
            raise ValueError("Modules must be equal")
        repr_mul = (np.array(self.representatives) * np.array(other.representatives)) % self.module
        return self.__class__(repr_mul.tolist(), self.module)

    def modular_inverse(self):
        integers_array = np.array(self.representatives).astype(int)
        repr_inverse = vectorize_modular_inverse(integers_array, self.module)
        return self.__class__(repr_inverse.tolist(), self.module)
