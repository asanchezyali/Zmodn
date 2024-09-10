The :doc:`getting-started` guide is intended to help you get started with using the :obj:`zmodn` library. If you are a developer who wants to contribute to the project or set up a development environment, please refer to the :doc:`developer-guide`.

Install the package
-------------------

First, you need to install the :obj:`zmodn` library.

The latest version of the library is available on GitHub. You can clone the repository and install the library using the
following commands:

.. code-block:: console

    git clone
    cd zmodn
    pip install -e .

Basic Usage
-----------
To start using the :obj:`zmodn` library, import it in your Python script:

.. code-block:: python

    from zmodn import Zmodn

The :obj:`zmodn` library provides a :obj:`Zmodn` class that represents a set of integers modulo a given modulus. You can
create a :obj:`Zmodn` instance by providing a list of representatives and a modulus. For example, to create a
:obj:`Zmodn` instance representing the set of integers modulo 5 with representatives 1, 2, 3, 4, and 5, you can use the
following code:

.. code-block:: python

    zmodn = Zmodn([1, 2, 3, 4, 5], 5)

You can create a :obj:`Zmodn` objects in several ways:

1. Single element:

.. code-block:: python

    a = Zmodn(1, 5)
    print(a)  # Output: [1] (mod 5)

2. List of elements:

.. code-block:: python

    b = Zmodn([1, 2, 7], 5)
    print(b)  # Output: [1 2 2] (mod 5)

3. Matrix:

.. code-block:: python

    c = Zmodn([[1, 2], [3, 4]], 5)
    print(c)  # Output: [[1 2] [3 4]] (mod 5)


Arithmetic Operations
---------------------

You can perform arithmetic operations on :obj:`Zmodn` instances using standard element-wise array arithmetic operations.

1. Addition:

.. code-block:: python

    a = Zmodn([1, 2, 7], 5)
    b = Zmodn([3, 4, 2], 5)
    print(a + b)  # Output: [4 1 4] (mod 5)

2. Subtraction:

.. code-block:: python

    print(a - b)  # Output: [3 3 0] (mod 5)

3. Multiplication:

.. code-block:: python

    print(a * b)  # Output: [3 3 4] (mod 5)

4. Division:

.. code-block:: python

    print(a / b)  # Output: [2 3 4] (mod 5)

5. Exponentiation:

.. code-block:: python

    print(a ** b)  # Output: [1 1 4] (mod 5)

Matrix Operations
-----------------

The :obj:`Zmodn` class also supports matrix operations in modular arithmetic. You can perform matrix addition,
subtraction, multiplication, exponentiation, and inversion.

1. Matrix Addition:

.. code-block:: python

    a = Zmodn([[1, 2], [3, 4]], 5)
    b = Zmodn([[2, 1], [4, 3]], 5)
    print(a + b)  # Output: [[3 3] [2 2]] (mod 5)

2. Matrix Subtraction:


.. code-block:: python

    print(a - b)  # Output: [[4 1] [4 1]] (mod 5)


3. Matrix Multiplication:

.. code-block:: python

    print(a @ b)  # Output: [[10 7] [22 15]] (mod 5)

4. Matrix Exponentiation:

.. code-block:: python

    print(a ** 2)  # Output: [[7 10] [15 22]] (mod 5)

5. Matrix Inversion:

.. code-block:: python

    print(a.inv())  # Output: [[4 3] [2 1]] (mod 5)

Modular Inverse
---------------

For non-matrix elements, you can compute the modular inverse using the :obj:`mod_inv` method.

.. code-block:: python

    a = Zmodn(3, 5)
    print(a.mod_inv())  # Output: 2 (mod 5)

Compare Elements

You can compare elements in modular arithmetic using standard comparison operators.

.. code-block:: python

    a = Zmodn(3, 5)
    b = Zmodn(4, 5)
    print(a < b)  # Output: True

Advanced Features
-----------------

Indexing and Slicing:

You can access elements of a :obj:`Zmodn` instance using indexing and slicing.

.. code-block:: python

    a = Zmodn([1, 2, 3, 4, 5], 5)
    print(a[0])  # Output: 1
    print(a[1:3])  # Output: [2 3]

You can also iterate over the elements of a :obj:`Zmodn` instance using a loop.

.. code-block:: python

    for element in a:
        print(element)


Error Handling
--------------


The :obj:`zmodn` library provides error handling for common arithmetic errors, such as division by zero and invalid
modulus.

.. code-block:: python

    a = Zmodn(3, 0)  # Raises ZeroDivisionError
    b = Zmodn(3, 1)  # Raises ValueError

Best Practices
--------------

When working with the :obj:`zmodn` library, it is recommended to follow these best practices:

1. Always ensure that Zmodn objects that you're operating on have the same modulus.
2. For matrix operations, make sure your matrices are square and invertible when necessary.
