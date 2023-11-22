import numpy as np


def vectorize_modular_inverse(integers, module):
    if not isinstance(integers, np.ndarray):
        raise TypeError("Integers must be a numpy array")
    if not np.issubdtype(integers.dtype, np.integer):
        raise TypeError("Integers must be an array of integers")
    if not isinstance(module, (np.int64, int)):
        raise TypeError("Module must be an integer")
    if not module > 0:
        raise ValueError("Module must be positive")
    if not np.all(np.gcd(integers, module) == 1):
        raise ValueError("All integers and module must be coprime")
    return np.vectorize(lambda integer, module: pow(integer, module - 2, module), otypes=[int])(integers, module)
