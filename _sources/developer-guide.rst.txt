This guide is intended for developers who want to contribute to the :obj:`zmodn` project or set up a development
environment for working with the library.

## Setting Up a Development Environment

1. Clone the repository from GitHub:

.. code-block:: console

    git clone https://github.com/asanchezyali/zmodn.git
    cd zmodn

2. Install the development dependencies:

.. code-block:: console

    pip install poetry
    poetry install



## Installing the Package Locally

To install the package locally so that it can be imported from anywhere in your system, you can use the command
:obj:`pip install -e .` in the root directory of your project (the directory containing the :obj:`setup.py` or
:obj:`pyproject.toml` file).

Here are the detailed steps:

1. Open a terminal.
2. Navigate to the root directory of your project.
3. Execute the command :obj:`pip install -e .`.

This command will install your library in your global Python environment (or in the active virtual environment if you
are using one). Once installed, you should be able to import your library from any Python script on your system.

Note: If you are using a virtual environment and want your library to be available globally, make sure the virtual
environment is not active when you run the :obj:`pip install -e .` command.

Additionally, if you make changes to your library and want them reflected in the installed version, you'll need to
uninstall the old version and reinstall the new one. You can do this with the commands :obj:`pip uninstall
your-library-name`
and :obj:`pip install -e .`.

## Running Tests

To run the tests for the :obj:`zmodn` library, you can use the following command:

.. code-block:: console

    pytest

This command will run all the tests in the :obj:`tests` directory and display the results in the terminal.

## Building the Documentation

The documentation for the :obj:`zmodn` library is built using Sphinx. To build the documentation:

1. Install the development dependencies (if you haven't already):
2. Navigate to the :obj:`docs` directory:

.. code-block:: console

    cd docs

3. Make your changes to the .rst files in the :obj:`source` directory.
4. Run the following command to build the HTML documentation:

.. code-block:: console

    make html

This command will generate the HTML files in the :obj:`build/html` directory. You can open the :obj:`index.html` file in
a web browser to view the documentation.

5. If you make changes to the code and want to rebuild the HTML documentation, run the following command:

.. code-block:: console

    make clean html

This command will delete the old HTML files and rebuild them with the updated content.

6. View the built documentation by opening :obj:`_build/html/index.html`` in your web browser.

Code Style
----------

The :obj:`zmodn` library uses the `Black <https://black.readthedocs.io/en/stable/ >`_ code formatter to ensure a
consistent code style. To format your code using Black, you can use the following command:

.. code-block:: console

    black .

This command will format all the Python files in the current directory and its subdirectories according to the Black
style guide.

Contributing
------------
If you would like to contribute to the :obj:`zmodn` library, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch for your changes.
3. Make your changes to the code.
4. Add tests to ensure that your changes work correctly.
5. Push your branch to your fork.
6. Create a pull request to merge your changes into the main repository.

Please ensure that your code adheres to the project's coding standards and is well-documented.

Releasing a New Version
-----------------------

To release a new version of the :obj:`zmodn` library, follow these steps:
1. Update the version number in the :obj:`pyproject.toml` file.
2. Update the version number in :obj:`zmodn/__init__.py`.
3. Update the :obj:`CHANGELOG.md` file with the changes in the new version.
4. Commit these changes with a message like "Bump version to X.Y.Z".
5. Create a new tag with the version number: :obj:`git tag vX.Y.Z`. Push the commits and the new tag: :obj:`git push
origin main --tags`.
6. Create a new release on GitHub, describing the changes.


Contact
-------

For questions or issues, please open an `issue <https://github.com/asanchezyali/zmodn/issues>`_ on GitHub or contact the maintainer directly.
You can also join our Discord community for discussions, support, and updates:
`Math & Code Discord Server <https://discord.gg/gJ3vCgSWeh>`_
Join us to connect with other users, get help, and stay updated on the latest developments!

License
-------

:obj:`zmodn` is licensed under the terms of the Creative Commons Legal Code license. See the license file for details.
