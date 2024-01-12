.. image:: ../logo/heading.svg
   :align: center

The :obj:`zmodn` package provides a class for representing integers modulo a given positive integer. This class can be used to applications such as cryptography and computer algebra. It is designed to be easy to use, and to provide a simple interface for working with modular arithmetic.

Features
--------

- Perform arithmetic operations (addition, subtraction, multiplication, division, power) on integers modulo a given positive integer.
- Compute the modular inverse of an integer modulo a given positive integer.
- Compute the inverse of a square matrix modulo a given positive integer.
- Compare two integers modulo a given positive integer.
- Access and modify the representatives of an integer modulo a given positive integer.

Installation
------------
The :obj:`zmodn` package can be installed using `pip <https://pip.pypa.io/en/stable/>`_.

.. code-block:: bash

   $ pip install zmodn

Basic Usage
-----------

Here is a simple example of how to use Zmodn:

.. code-block:: python

   from zmodn import Zmodn

   # Create a Zmodn object with the representatives 2 and 3 modulo 5
   zmodn = Zmodn([2, 3], 5)

   # Add two Zmodn objects
   zmodn_sum = zmodn + Zmodn([1, 4], 5)

   # Subtract two Zmodn objects
   zmodn_difference = zmodn - Zmodn([1, 4], 5)

   # Multiply two Zmodn objects
   zmodn_product = zmodn * Zmodn([1, 4], 5)

   # Divide two Zmodn objects
   zmodn_quotient = zmodn / Zmodn([1, 4], 5)

   # Compute the modular inverse of a Zmodn object
   zmodn_inverse = zmodn.mod_inv()

Documentation
-------------

For more detailed information about the features and usage of :obj:`zmodn`, please refer to the documentation.

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
            title = {{Zmodn}: Efficient Modulo Arithmetic with NumPy},
            author = {Sánchez, Alejandro},
            month = {11},
            year = {2023},
            url = {https://github.com/asanchezyali/Zmodn},
         }

   .. md-tab-item:: APA

      .. code-block:: text

         Sánchez, A. (2023). Zmodn: Efficient Modulo Arithmetic with NumPy. [Computer software]. https://github.com/asanchezyali/Zmodn



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

   api.rst
