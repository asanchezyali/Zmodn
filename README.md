
<p align="center">
  <a href="https://github.com/asanchezyali/Zmodn#readme">
    <img src="logo/logo.drawio.svg" alt="Logo" width="100%" height="140">
  </a>
</p>

<div align=center>
  <a href="https://github.com//Zmodn/actions/workflows/docs.yaml"><img src="https://github.com/mhostetter/galois/actions/workflows/docs.yaml/badge.svg"></a>
  <a href="https://github.com//Zmodn/actions/workflows/lint.yaml"><img src="https://github.com/mhostetter/galois/actions/workflows/lint.yaml/badge.svg"></a>
  <a href="https://github.comrZmodns/actions/workflows/build.yaml"><img src="https://github.com/mhostetter/galois/actions/workflows/build.yaml/badge.svg"></a>
  <a href="https://github.com//Zmodn/actions/workflows/test.yaml"><img src="https://github.com/mhostetter/galois/actions/workflows/test.yaml/badge.svg"></a>
  <a href="https://codecov.io/gh//Zmodn"><img src="https://codecov.io/gh/mhostetter/galois/branch/master/graph/badge.svg?token=3FJML79ZUK"></a>
</div>

The Zmodn package provides a class for representing integers modulo a given positive integer. This class can be used to
applications such as cryptography and computer algebra.

## Features

- Perform arithmetic operations (addition, subtraction, multiplication, division, power) on integers modulo a given
  positive integer.
- Compute the modular inverse of an integer modulo a given positive integer.
- Compute the inverse of a square matrix modulo a given positive integer.
- Compare two integers modulo a given positive integer.
- Access and modify the representatives of an integer modulo a given positive integer.

## Installation

To install Zmodn, you can use pip:

```bash
pip install zmodn
```

## Usage

Here is a simple example of how to use Zmodn:

```python
import numpy as np
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
```

## Documentation

For more detailed information about the features and usage of Zmodn, please refer to the [documentation](https://github.com/username/zmodn/docs).

## License

Zmodn is licensed under the terms of the MIT license. See the [license file](https://github.com/asanchezyali/Zmodn/blob/main/LICENSE) for details.

## Contact

If you have any questions, comments, or issues, please feel free to [contact us](https://github.com/asanchezyali).

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

## Citation

If this library was useful to you in your research, please cite us. Following the [GitHub citation standards](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files), here is the recommended citation.

### BibTeX

```bibtex
@software{Sanchez_Alejandro_2020,
    title = {{Z mod n}: Efficient Modulo Arithmetic with NumPy},
    author = {Sánchez, Alejandro},
    month = {11},
    year = {2023},
    url = {https://github.com/asanchezyali/Zmodn},
}
```

### APA

```
Sánchez, A. (2023). Z mod n: Efficient Modulo Arithmetic with NumPy.
```
