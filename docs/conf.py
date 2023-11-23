# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath(".."))


# -- Project information -----------------------------------------------------

project = "Zmodn"
copyright = "2023, Alejandro Sánchez Yalí"
author = "Alejandro Sánchez Yalí"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.mathjax",
    "sphinx.ext.intersphinx",
    "sphinx_last_updated_by_git",
    "sphinx_immaterial",
    "sphinx_immaterial.apidoc.python.apigen",
    "sphinx_math_dollar",
    "myst_parser",
    "sphinx_design",
    "IPython.sphinxext.ipython_console_highlighting",
    "IPython.sphinxext.ipython_directive",
    "ipython_with_reprs",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_immaterial"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


html_css_files = [
    "extra.css",
]

# Define a custom inline Python syntax highlighting literal
rst_prolog = """
.. role:: python(code)
   :language: python
   :class: highlight
"""
# Sets the default role of `content` to :python:`content`, which uses the custom Python syntax highlighting inline literal
default_role = "python"

html_title = "Zmodn"
html_favicon = "../logo/favicon.png"
html_logo = "../logo/favicon.png"

# Sphinx Immaterial theme options
html_theme_options = {
    "icon": {
        "repo": "fontawesome/brands/github",
    },
    "repo_url": "https://github.com/asanchezyali/Zmodn",
    "repo_name": "asanchezyali/Zmodn",
    "social": [
        {
            "icon": "fontawesome/brands/github",
            "link": "https://github.com/asanchezyali/Zmodn",
        },
        {
            "icon": "fontawesome/brands/twitter",
            "link": "https://twitter.com/asanchezyali",
        },
    ],
    "edit_uri": "",
    "globaltoc_collapse": False,
    "features": [
        # "navigation.expand",
        "navigation.tabs",
        # "toc.integrate",
        # "navigation.sections",
        # "navigation.instant",
        # "header.autohide",
        "navigation.top",
        "navigation.tracking",
        "toc.follow",
        "toc.sticky",
        "content.tabs.link",
        "announce.dismiss",
    ],
    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "toggle": {
                "icon": "material/weather-night",
                "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "toggle": {
                "icon": "material/weather-sunny",
                "name": "Switch to light mode",
            },
        },
    ],
    "analytics": {
        "provider": "google",
        "property": "G-4FW9NCNFZH",
    },
    "version_dropdown": True,
    "version_json": "../versions.json",
}

html_last_updated_fmt = ""
html_use_index = True
html_domain_indices = True
