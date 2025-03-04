# SPDX-FileCopyrightText: 2021 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "Python for Data Science"
copyright = "2019–2023, Veit Schiele"
author = "Veit Schiele"

# The full version, including alpha/beta/rc tags
release = "1.0.0"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "nbsphinx",
    "IPython.sphinxext.ipython_console_highlighting",
    # 'jupyter_sphinx.execute',
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.graphviz",
    "sphinx.ext.todo",
    "sphinxcontrib.cairosvgconverter",
    "sphinxext.opengraph",
    "sphinx_copybutton",
    "sphinx_inline_tabs",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# Fix for Sphinx < 2.0
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "**/.ipynb_checkpoints",
    "**/.*.ipynb",
    "**/input.ipynb",
    "**/output*.ipynb",
]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "furo"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# Change default HTML title
html_title = "Python for Data Science 1.0.0"
#
# html_theme_options = {}
# html_sidebars = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_logo = "_static/images/logo/logo.png"
html_favicon = "_static/images/logo/favicon.ico"

html_css_files = [
    "css/alerts.css",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'a4paper',
    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '9pt',
    # Additional stuff for the LaTeX preamble.
    "preamble": r"\usepackage{pmboxdraw}",
    # Latex figure (float) alignment
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "Python4DataScience.tex",
        "Python for Data Science",
        "Veit Schiele",
        "manual",
    ),
]

# -- nbsphinx configuration --------------------------------------------------

nbsphinx_allow_errors = True
# nbsphinx_execute = 'always'

# -- intersphinx configuration -----------------------------------------------

intersphinx_mapping = {
    "jupyter-tutorial": (
        "https://jupyter-tutorial.readthedocs.io/en/latest/",
        None,
    ),
    "python": ("https://docs.python.org/3", None),
    "ipython": ("https://ipython.readthedocs.io/en/latest/", None),
    "pytest": ("https://docs.pytest.org/en/latest/", None),
    "jupyter-notebook": (
        "https://jupyter-notebook.readthedocs.io/en/stable/",
        None,
    ),
    "jupyterhub": ("https://jupyterhub.readthedocs.io/en/stable/", None),
    "nbconvert": ("https://nbconvert.readthedocs.io/en/latest/", None),
    "jupyter-contrib-nbextensions": (
        "https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/",
        None,
    ),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
    "nbsphinx": ("https://nbsphinx.readthedocs.io/en/0.4.2/", None),
    "pipenv": ("https://pipenv.pypa.io/en/latest/", None),
    "spack": ("https://spack-tutorial.readthedocs.io/en/latest/", None),
    "ipyparallel": ("https://ipyparallel.readthedocs.io/en/latest/", None),
    "bokeh": ("https://docs.bokeh.org/en/latest/", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable/", None),
    "pyviz": ("https://pyviz-tutorial.readthedocs.io/de/latest/", None),
    "python-basics": (
        "https://python-basics-tutorial.readthedocs.io/en/latest/",
        None,
    ),
}


def setup(app):
    # from sphinx.ext.autodoc import cut_lines
    # app.connect('autodoc-process-docstring', cut_lines(4, what=['module']))
    app.add_object_type(
        "label",
        "label",
        objname="label value",
        indextemplate="pair: %s; label value",
    )


# -- graphviz configuration --------------------------------------------------

graphviz_output_format = "svg"
