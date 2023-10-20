import math
import numpy as np


def modular_inverse(integer, module):
    if not isinstance(integer, (np.int64, int)):
        raise TypeError("Integer must be an integer")
    if not isinstance(module, (np.int64, int)):
        raise TypeError("Module must be an integer")
    if not module > 0:
        raise ValueError("Module must be positive")
    if not math.gcd(integer, module) == 1:
        raise ValueError("Integer and module must be coprime")

    # Extended Euclidean algorithm
    # https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
    aux1 = 0
    aux2 = 1
    y = integer
    x = module
    while y != 0:
        q, r = divmod(x, y)
        x, y = y, r
        aux1, aux2 = aux2, aux1 - q * aux2
    return aux1 % module


vectorize_modular_inverse = np.vectorize(modular_inverse)
