The :doc:`getting-started` guide is intended to help you get started with installing and using the library in your own
projects. See ":doc:`Basic Usage`" for more detailed information on how to use the library.

Install the package
-------------------

The last stable release is available on PyPI and can be installed with pip:

.. code-block:: console

    pip install zmodn
    zmodn.__version__

Create a :obj:`Zmodn` instance
------------------------------

The :obj:`Zmodn` class is the main interface to the library. It represents a set of integers modulo a given modulus. The
modulus must be a positive integer. The representatives of the set are given as a list of integers or a single integer.
In this example, we create a :obj:`Zmodn` instance representing the set of integers modulo 5 with representatives 1, 2,
3, 4, and 5 (which are equivalent to 1, 2, 3, 4, and 0 modulo 5, respectively):

.. code-block:: python

    from zmodn import Zmodn
    zmodn = Zmodn([1, 2, 3, 4, 5], 5)

The :obj:`Zmodn` class is a subclass of :obj:`numpy.ndarray`, so it can be used in the same way as a NumPy array:

.. code-block:: python

    zmodn[0]
    zmodn[1:3]
    zmodn[0] = 6
    zmodn[1:3] = [7, 8]
    zmodn[0] = 1
    zmodn[1:3] = [2, 3]

The :obj:`Zmodn` class also supports the :obj:`len` function, which returns the number of representatives:

.. code-block:: python

    len(zmodn)

The :obj:`Zmodn` class supports the :obj:`in` operator, which checks if a given representative is in the set:

.. code-block:: python

    1 in zmodn
    2 in zmodn
    3 in zmodn
    4 in zmodn
    5 in zmodn
    6 in zmodn
    7 in zmodn
    8 in zmodn

The :obj:`Zmodn` class supports the :obj:`bool` function, which returns :obj:`True` if the set is not empty and

:obj:`False` otherwise:

.. code-block:: python

    bool(zmodn)

Perform arithmetic operations
-----------------------------

Once you have two :obj:`Zmodn` instances, you can perform arithmetic can be performed using normal NumPy arithmetic.

standard element-wise array arithmetic operations -- addition, subtraction, multiplication, division and exponentiation
are easily performed on :obj:`Zmodn` instances. For example, to add two :obj:`Zmodn` instances, you can use the :obj:`+`
operator:

.. code-block:: python

    zmodn1 = Zmodn([1, 2, 3, 4, 5], 5)
    zmodn2 = Zmodn([1, 2, 3, 4, 5], 5)
    zmodn1 + zmodn2

The :obj:`Zmodn` class also supports the :obj:`-`, :obj:`*`, :obj:`/`, and :obj:`**` operators:

.. code-block:: python

    zmodn1 - zmodn2
    zmodn1 * zmodn2
    zmodn1 / zmodn2
    zmodn1 ** zmodn2

The :obj:`Zmodn` class supports the :obj:`==` and :obj:`!=` operators, which check if two :obj:`Zmodn` instances are equal or not equal, respectively:

.. code-block:: python

    zmodn1 == zmodn2
    zmodn1 != zmodn2

See :doc:`/basic-usage/operations` for more information on the arithmetic operations.
