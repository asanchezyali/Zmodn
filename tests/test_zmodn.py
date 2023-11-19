import numpy as np
from zmodn import Zmodn


def test_init():
    # Test initialization with a single integer
    zmodn = Zmodn(2, 5)
    assert np.array_equal(zmodn.representatives, np.array([2]) % 5)
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


def test_repr():
    # Test __repr__ with a single representative
    zmodn = Zmodn(2, 5)
    assert zmodn.__repr__() == "2 (mod 5)"

    # Test __repr__ with multiple representatives
    zmodn = Zmodn([2, 3], 5)
    assert zmodn.__repr__() == "[2 3] (mod 5)"


def test_mod_inv():
    # Test modular inverse
    zmodn = Zmodn(2, 5)
    zmodn_inverse = zmodn.mod_inv()
    assert np.array_equal(zmodn_inverse.representatives, np.array([3]))


def test_inv():
    # Test inverse of a square matrix
    zmodn_matrix = Zmodn([[1, 2], [3, 4]], 5)
    zmodn_matrix_inv = zmodn_matrix.inv()
    assert np.array_equal(zmodn_matrix_inv.representatives, np.array([[3, 1], [4, 2]]))

    # Test inverse of a non-square matrix
    zmodn_matrix = Zmodn([[1, 2, 3], [4, 5, 6]], 7)
    try:
        zmodn_matrix_inv = zmodn_matrix.inv()
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError"

    # Test inverse of a matrix with a non-invertible determinant
    zmodn_matrix = Zmodn([[1, 2], [2, 4]], 5)
    try:
        zmodn_matrix_inv = zmodn_matrix.inv()
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError"

    # Test inverse of a matrix with a non-integer determinant
    zmodn_matrix = Zmodn([[1, 2], [3, 4]], 6)
    try:
        zmodn_matrix_inv = zmodn_matrix.inv()
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError"

    # Test inverse of a matrix with a zero determinant
    zmodn_matrix = Zmodn([[1, 2], [3, 6]], 6)
    try:
        zmodn_matrix_inv = zmodn_matrix.inv()
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError"


def test_add():
    # Test addition
    zmodn = Zmodn(2, 5)
    zmodn_sum = zmodn + Zmodn([1, 4], 5)
    assert np.array_equal(zmodn_sum.representatives, np.array([3, 1]))

    # Test addition with a different module
    zmodn = Zmodn(2, 5)
    try:
        zmodn_sum = zmodn + Zmodn([1, 4], 6)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError"

    # Test addition with a non-Zmodn object
    zmodn = Zmodn(2, 5)
    try:
        zmodn_sum = zmodn + 2
    except TypeError:
        pass
    else:
        assert False, "Expected TypeError"

    # Test addition with a non-integer
    zmodn = Zmodn(2, 5)
    try:
        zmodn_sum = zmodn + Zmodn([1.0, 4.0], 5)
    except TypeError:
        pass
    else:
        assert False, "Expected TypeError"


def test_sub():
    # Test subtraction
    zmodn = Zmodn(2, 5)
    zmodn_sub = zmodn - Zmodn([1, 4], 5)
    assert np.array_equal(zmodn_sub.representatives, np.array([1, 3]))

    # Test subtraction with a different module
    zmodn = Zmodn(2, 5)
    try:
        zmodn_sub = zmodn - Zmodn([1, 4], 6)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError"

    # Test subtraction with a non-Zmodn object
    zmodn = Zmodn(2, 5)
    try:
        zmodn_sub = zmodn - 2
    except TypeError:
        pass
    else:
        assert False, "Expected TypeError"

    # Test subtraction with a non-integer
    zmodn = Zmodn(2, 5)
    try:
        zmodn_sub = zmodn - Zmodn([1.0, 4.0], 5)
    except TypeError:
        pass
    else:
        assert False, "Expected TypeError"


def test_mul():
    # Test multiplication
    zmodn = Zmodn(2, 5)
    zmodn_product = zmodn * Zmodn([1, 4], 5)
    assert np.array_equal(zmodn_product.representatives, np.array([2, 3]))

    # Test multiplication with a different module
    zmodn = Zmodn(2, 5)
    try:
        zmodn_product = zmodn * Zmodn([1, 4], 6)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError"

    # Test multiplication with a non-Zmodn object
    zmodn = Zmodn(2, 5)
    try:
        zmodn_product = zmodn * 2
    except TypeError:
        pass
    else:
        assert False, "Expected TypeError"

    # Test multiplication with a non-integer
    zmodn = Zmodn(2, 5)
    try:
        zmodn_product = zmodn * Zmodn([1.0, 4.0], 5)
    except TypeError:
        pass
    else:
        assert False, "Expected TypeError"


def test_matmul():
    # Test matrix multiplication
    zmodn_matrix = Zmodn([[1, 2], [3, 4]], 5)
    zmodn_matrix_product = zmodn_matrix @ Zmodn([[1, 2], [3, 4]], 5)
    assert np.array_equal(zmodn_matrix_product.representatives, np.array([[2, 0], [0, 2]]))

    # Test matrix multiplication with a different module
    zmodn_matrix = Zmodn([[1, 2], [3, 4]], 5)
    try:
        zmodn_matrix_product = zmodn_matrix @ Zmodn([[1, 2], [3, 4]], 6)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError"

    # Test matrix multiplication with a non-Zmodn object
    zmodn_matrix = Zmodn([[1, 2], [3, 4]], 5)
    try:
        zmodn_matrix_product = zmodn_matrix @ 2
    except TypeError:
        pass
    else:
        assert False, "Expected TypeError"

    # Test matrix multiplication with a non-integer
    zmodn_matrix = Zmodn([[1, 2], [3, 4]], 5)
    try:
        zmodn_matrix_product = zmodn_matrix @ Zmodn([[1.0, 2.0], [3.0, 4.0]], 5)
    except TypeError:
        pass
    else:
        assert False, "Expected TypeError"


def test_truediv():
    # Test division
    zmodn = Zmodn(2, 5)
    zmodn_div = zmodn / Zmodn([2, 3], 5)
    assert np.array_equal(zmodn_div.representatives, np.array([1, 4]))

    # Test division with a different module
    zmodn = Zmodn(2, 5)
    try:
        zmodn_div = zmodn / Zmodn([2, 3], 6)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError"

    # Test division with a non-Zmodn object
    zmodn = Zmodn(2, 5)
    try:
        zmodn_div = zmodn / 2
    except TypeError:
        pass
    else:
        assert False, "Expected TypeError"

    # Test division with a non-integer
    zmodn = Zmodn(2, 5)
    try:
        zmodn_div = zmodn / Zmodn([2.0, 3.0], 5)
    except TypeError:
        pass
    else:
        assert False, "Expected TypeError"


def test_pow():
    # Test exponentiation
    zmodn = Zmodn(2, 5)
    zmodn_pow = zmodn**2
    assert np.array_equal(zmodn_pow.representatives, np.array([4]))

    # Test exponentiation with a non-integer
    zmodn = Zmodn(2, 5)
    try:
        zmodn_pow = zmodn**2.0
    except TypeError:
        pass
    else:
        assert False, "Expected TypeError"


def test_neg():
    # Test negative
    zmodn = Zmodn(2, 5)
    zmodn_neg = -zmodn
    assert np.array_equal(zmodn_neg.representatives, np.array([3]))


def test_pos():
    # Test positive
    zmodn = Zmodn(2, 5)
    zmodn_pos = +zmodn
    assert np.array_equal(zmodn_pos.representatives, np.array([2]))


def test_eq():
    # Test equality
    zmodn = Zmodn(2, 5)
    assert zmodn == Zmodn(2, 5)

    # Test equality with a different module
    zmodn = Zmodn(2, 5)
    assert not zmodn == Zmodn(2, 6)

    # Test equality with a non-Zmodn object
    zmodn = Zmodn(2, 5)
    assert not zmodn == 2


def test_ne():
    # Test inequality
    zmodn = Zmodn(2, 5)
    assert zmodn != Zmodn(3, 5)

    # Test inequality with a different module
    zmodn = Zmodn(2, 5)
    assert zmodn != Zmodn(2, 6)

    # Test inequality with a non-Zmodn object
    zmodn = Zmodn(2, 5)
    assert zmodn != 2


def test_lt():
    # Test less than
    zmodn = Zmodn(2, 5)
    assert zmodn < Zmodn(3, 5)

    # Test less than with a different module
    zmodn = Zmodn(2, 5)
    assert not zmodn < Zmodn(2, 6)

    # Test less than with a non-Zmodn object
    zmodn = Zmodn(2, 5)
    assert not zmodn < 2


def test_le():
    # Test less than or equal to
    zmodn = Zmodn(2, 5)
    assert zmodn <= Zmodn(2, 5)

    # Test less than or equal to with a different module
    zmodn = Zmodn(2, 5)
    assert not zmodn <= Zmodn(2, 6)

    # Test less than or equal to with a non-Zmodn object
    zmodn = Zmodn(2, 5)
    assert not zmodn <= 2


def test_gt():
    # Test greater than
    zmodn = Zmodn(2, 5)
    assert zmodn > Zmodn(1, 5)

    # Test greater than with a different module
    zmodn = Zmodn(2, 5)
    assert not zmodn > Zmodn(2, 6)

    # Test greater than with a non-Zmodn object
    zmodn = Zmodn(2, 5)
    assert not zmodn > 2


def test_ge():
    # Test greater than or equal to
    zmodn = Zmodn(2, 5)
    assert zmodn >= Zmodn(2, 5)

    # Test greater than or equal to with a different module
    zmodn = Zmodn(2, 5)
    assert not zmodn >= Zmodn(2, 6)

    # Test greater than or equal to with a non-Zmodn object
    zmodn = Zmodn(2, 5)
    assert not zmodn >= 2


def test_hash():
    # Test hash
    zmodn = Zmodn(2, 5)
    assert hash(zmodn) == hash(Zmodn(2, 5))


def test_getitem():
    # Test __getitem__
    zmodn = Zmodn([2, 3], 5)
    assert zmodn[0] == Zmodn(2, 5)
    assert zmodn[1] == Zmodn(3, 5)

    # Test __getitem__ with a negative index
    zmodn = Zmodn([2, 3], 5)
    assert zmodn[-1] == Zmodn(3, 5)

    # Test __getitem__ with an out of bounds index
    zmodn = Zmodn([2, 3], 5)
    try:
        zmodn[2]
    except IndexError:
        pass
    else:
        assert False, "Expected IndexError"

    # Test __getitem__ with slice notation
    zmodn = Zmodn([2, 3, 4], 5)
    assert np.array_equal(zmodn[1:].representatives, np.array([3, 4]))
