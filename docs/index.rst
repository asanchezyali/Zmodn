.. image:: ../logo/heading.svg
   :align: center

The :obj:`zmodn` package provides a class for representing and performing operations in the ring of integers modulo $n$
($\mathbb{Z}/n\mathbb{Z}$). The package is built on top of `NumPy <https://numpy.org/>`_ for efficient array operations,
making it suitable for applications in cryptography, computer algebra, and other fields requiring modular arithmetic.

Features
--------

- Perform arithmetic operations (addition, subtraction, multiplication, division, power).
- Compute the modular inverse.
- Handle matrix operations in modular arithmetic, including matrix addition, subtraction, multiplication, exponentiation, and inversion.
- Compare elements modular arithmetic.
- Seamless integration with NumPy arrays.

Installation
------------
To :obj:`zmodn` package can use pip:

.. code-block:: bash

   $ cd zmodn
   $ pip install -e .

Quick Start
-----------

Here is basic example of using the :obj:`zmodn` package:

.. code-block:: python

   from zmodn import Zmodn

   a = Zmodn([1, 2, 7], 5)
   b = Zmodn([3, 4, 2], 5)

   print(a)  # Output: [1 2 2] (mod 5)
   print(a + b)  # Output: [4 1 4] (mod 5)
   print(a * b)  # Output: [3 3 4] (mod 5)
   print(a.mod_inv())  # Output: [1 3 3] (mod 5)

License
-------
:obj:`zmodn` is licensed under the terms of the MIT license. See the license file for details.

Contact
-------

If you have any questions, comments, or issues, please feel free to contact us.

Contributing
------------

We welcome contributions to :obj:`zmodn` library! If you have an idea for a new feature or improvement, please feel free to create an issue or submit a pull request.

To contribute to the :obj:`zmodn` library, you will need to:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes to the code.
4. Add tests to ensure that your changes work correctly.
5. Push your branch to the fork.
6. Create a pull request to merge your changes into the main repository.
7. Please be sure to follow the coding style guide and add documentation for any new features or changes that you make.

We appreciate your contributions to the zmodn library!


Citation
--------

If this library was useful to you in your research, please cite us. Following the `GitHub citation standards <https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files>`_, here is the recommended citation.

.. md-tab-set::

   .. md-tab-item:: BibTeX

      .. code-block:: latex

         @software{Sanchez_Alejandro_2020,
            title = {{Zmodn}: Practical Modular Arithmetic Using NumPy},
            author = {Sánchez, Alejandro},
            month = {11},
            year = {2023},
            url = {https://github.com/asanchezyali/Zmodn},
         }

   .. md-tab-item:: APA

      .. code-block:: text

         Sánchez, A. (2023). Zmodn: Practical Modular Arithmetic Using NumPy. [Computer software]. https://github.com/asanchezyali/Zmodn



.. toctree::
   :caption: Getting Started
   :hidden:

   getting-started.rst

.. toctree::
   :caption: Developer Guide
   :hidden:

   developer-guide.rst

.. toctree::
   :caption: API Reference
   :hidden:
   :maxdepth: 2

   api.rst
