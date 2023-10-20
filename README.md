# Zmodn

The Zmodn package provides a class for representing integers modulo a given prime number. This class can be used to
applications such as cryptography and computer algebra.

## Setup
To install the `zmodn`` library, run the following command:

```bash
pip install zmodn
```

## Usage
To use the `zmodn` library, simply import the `Zmodn` class and create a new instance of it. The constructor takes
two arguments: the value of the integer and the prime number to use as the modulus. For example, to create the integer
`5` modulo `7`, you would run the following code:

```python
from zmodn import Zmodn

x = Zmodn(5, 7)
```

The `Zmodn` class supports all of the standard arithmetic operations, including addition, subtraction, multiplication,
and division. For example, to add two integers modulo `7`, you would run the following code:

```python
from zmodn import Zmodn

x = Zmodn(5, 7)
y = Zmodn(3, 7)

z = x + y
```

The `Zmodn` class also supports the comparison operators, including equality, inequality, less than, less than or equal
to, greater than, and greater than or equal to. For example, to check if two integers modulo `7` are equal, you would
run the following code:

```python
from zmodn import Zmodn

x = Zmodn(5, 7)
y = Zmodn(3, 7)

z = x == y
```

## Contributing

We welcome contributions to the `zmodn` library! If you have an idea for a new feature or improvement, please feel free to create an issue or submit a pull request.

To contribute to the `zmodn` library, you will need to:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes to the code.
4. Add tests to ensure that your changes work correctly.
5. Push your branch to the fork.
6. Create a pull request to merge your changes into the main repository.
   
Please be sure to follow the coding style guide and add documentation for any new features or changes that you make.

We appreciate your contributions to the zmodn library!