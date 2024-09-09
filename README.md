# Zmodn: Practical Modular Arithmetic Using NumPy

<div align="center">
  <a href="https://github.com/asanchezyali/zmodn#readme">
    <img src="logo/heading.svg" alt="Logo" width="100%" height="180px">
  </a>
</div>

Zmodn provides a Python class for representing and performing operations in the ring of integers modulo n (ℤ/nℤ). It's built on NumPy for efficient array operations, making it suitable for applications in cryptography, computer algebra, and other fields requiring modular arithmetic.

## Features

- Perform modular arithmetic operations (addition, subtraction, multiplication, division, exponentiation)
- Compute modular inverses
- Handle matrix operations in modular arithmetic, including multiplication and inversion
- Compare elements in modular arithmetic
- Seamless integration with NumPy functions

## Installation

Install Zmodn using pip:

```bash
pip install -e .
```

## Quick Start

Here's a basic example of using the Zmodn class:

```python
from zmodn import Zmodn

# Create Zmodn objects
a = Zmodn([1, 2, 7], 5)
b = Zmodn([3, 4, 2], 5)

print(a)  # Output: [1 2 2] (mod 5)
print(a + b)  # Output: [4 1 4] (mod 5)
print(a * b)  # Output: [3 3 4] (mod 5)
print(a.mod_inv())  # Output: [1 3 3] (mod 5)
```

## Detailed Usage

### Creating Zmodn Objects

```python
# Single element
x = Zmodn(3, 7)  # 3 (mod 7)

# List of elements
y = Zmodn([1, 2, 3], 5)  # [1 2 3] (mod 5)

# Matrix
z = Zmodn([[1, 2], [3, 4]], 6)  # [[1 2] [3 4]] (mod 6)
```

### Arithmetic Operations

```python
a = Zmodn([1, 2], 7)
b = Zmodn([3, 4], 7)

print(a + b)  # Addition: [4 6] (mod 7)
print(a - b)  # Subtraction: [5 5] (mod 7)
print(a * b)  # Multiplication: [3 1] (mod 7)
print(a / b)  # Division: [5 4] (mod 7)
print(a ** 2)  # Exponentiation: [1 4] (mod 7)
print(-a)  # Negation: [6 5] (mod 7)
```

### Matrix Operations

```python
m1 = Zmodn([[1, 2], [3, 4]], 5)
m2 = Zmodn([[2, 3], [1, 4]], 5)

print(m1 @ m2)  # Matrix multiplication: [[4 1] [0 0]] (mod 5)
print(m1.inv())  # Matrix inversion: [[4 3] [2 4]] (mod 5)
```

### Modular Inverse

```python
x = Zmodn([2, 3], 5)
print(x.mod_inv())  # Modular inverse: [3 2] (mod 5)
```

### Comparison Operations

```python
a = Zmodn([1, 2], 7)
b = Zmodn([1, 3], 7)

print(a == b)  # False
print(a < b)   # True
print(a >= b)  # False
```

## Notes and Limitations

- The `mod_inv()` method works for individual elements and vectors, but not for matrices. Use `inv()` for matrix inversion.
- All operations assume that Zmodn objects have the same modulus.
- The class includes type checking and error handling for invalid inputs.

## Documentation

For more detailed information, please refer to the [full documentation](https://asanchezyali.github.io/zmodn/).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the Creative Commons Zero v1.0 Universal license. See the [LICENSE](LICENSE) file for details.

## Citation

If you use Zmodn in your research, please cite it as follows:

```bibtex
@software{Sanchez_Alejandro_2020,
    title = {{Zmodn}: Practical Modular Arithmetic Using NumPy},
    author = {Sánchez, Alejandro},
    month = {11},
    year = {2023},
    url = {https://github.com/asanchezyali/Zmodn},
}
```

## Contact

For questions or issues, please open an issue on GitHub or contact the maintainer directly.
You can also join our Discord community for discussions, support, and updates:
[Math & Code](https://discord.gg/gJ3vCgSWeh) Discord Server
Join us to connect with other users, get help, and stay updated on the latest developments!
