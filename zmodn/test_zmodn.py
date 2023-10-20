import numpy as np
from zmodn import Zmodn


def test_zmodn():
    # Test initialization with a single integer
    zmodn = Zmodn(2, 5)
    assert np.array_equal(zmodn.representatives, np.array([2]))
    assert zmodn.module == 5

    # Test initialization with a list of integers
    zmodn = Zmodn([2, 3], 5)
    assert np.array_equal(zmodn.representatives, np.array([2, 3]))
    assert zmodn.module == 5

    # Test initialization with a non-integer argument
    try:
        zmodn = Zmodn("2", 5)
    except TypeError:
        pass
    else:
        assert False, "Expected TypeError"

    # Test addition
    zmodn_sum = zmodn + Zmodn([1, 4], 5)
    assert np.array_equal(zmodn_sum.representatives, np.array([3, 2]))

    # Test subtraction
    zmodn_sub = zmodn - Zmodn([1, 4], 5)
    assert np.array_equal(zmodn_sub.representatives, np.array([1, 4]))

    # Test multiplication
    zmodn_product = zmodn * Zmodn([1, 4], 5)
    assert np.array_equal(zmodn_product.representatives, np.array([2, 2]))

    # Test modular inverse
    zmodn_inverse = zmodn.mod_inv()
    assert np.array_equal(zmodn_inverse.representatives, np.array([3, 2]))

    # Test inverse of a square matrix
    zmodn_matrix = Zmodn([[1, 2], [3, 4]], 5)
    zmodn_matrix_inv = zmodn_matrix.inv()
    assert np.array_equal(zmodn_matrix_inv.representatives, np.array([[4, 1], [2, 3]]))

    # Test division
    zmodn_div = zmodn / Zmodn([2, 3], 5)
    assert np.array_equal(zmodn_div.representatives, np.array([1, 4]))

    # Test exponentiation
    zmodn_pow = zmodn**2
    assert np.array_equal(zmodn_pow.representatives, np.array([4, 4]))

    # Test negative
    zmodn_neg = -zmodn
    assert np.array_equal(zmodn_neg.representatives, np.array([3, 2]))
