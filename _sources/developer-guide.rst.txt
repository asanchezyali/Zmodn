The latest released version of :obj:`Zmodn` can be installed from `PyPI <https://pypi.org/project/zmodn/>`_ with `pip`:

.. code-block:: console

    pip install zmodn

To install your library locally so that it can be imported from anywhere in your system, you can use the command :obj:`pip install .` in the root directory of your project (the directory containing the :obj:`setup.py` or :obj:`pyproject.toml` file).

Here are the detailed steps:

1. Open a terminal.
2. Navigate to the root directory of your project.
3. Execute the command :obj:`pip install .`.

This command will install your library in your global Python environment (or in the active virtual environment if you are using one). Once installed, you should be able to import your library from any Python script on your system.

Note: If you are using a virtual environment and want your library to be available globally, make sure the virtual environment is not active when you run the :obj:`pip install .` command.

Additionally, if you make changes to your library and want them reflected in the installed version, you'll need to uninstall the old version and reinstall the new one. You can do this with the commands :obj:`pip uninstall your-library-name` and :obj:`pip install .`.


Updated Documentation
_____________________

To generate the documentation, you need to run the following command in the root directory of docs:

.. code-block:: console

    sphinx-apidoc -o source/ ../zmodn
    make html

Now, suppose you did som changes to our code and now you want  to rebuild that HTML, go to your docs directory and run
the following command:

.. code-block:: console

    make clean html

This will delete the old HTML files and rebuild them.
