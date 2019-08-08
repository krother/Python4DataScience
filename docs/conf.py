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

project = 'Jupyter Tutorial'
copyright = '2019, Veit Schiele'
author = 'Veit Schiele'

# The full version, including alpha/beta/rc tags
release = '0.1.9'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'nbsphinx',
    'sphinx.ext.intersphinx',
    'sphinx.ext.graphviz',
    'sphinx.ext.todo',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'de'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    '**/.ipynb_checkpoints',
]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'description': 'Aufbau und Nutzung einer Forschungsinfrastruktur auf Basis von Jupyter Notebooks.',
    'fixed_sidebar': False,
    'show_powered_by': False,
    'github_user': 'veit',
    'github_repo': 'jupyter-tutorial',
    'github_banner': False,
    'github_button': False,
    'show_related': True,
    'show_relbar_bottom': False,
    'sidebar_includehidden': True,
}

html_sidebars = {
    '**':    ['about.html', 'searchbox.html', 'navigation.html']
}

# Change default HTML title
html_title = 'Jupyter Tutorial v0.1.9'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- intersphinx configuration -----------------------------------------------

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'ipython': ('https://ipython.readthedocs.io/en/latest/', None),
    'pytest': ('https://docs.pytest.org/en/latest/', None),
    'jupyter-notebook':  ('https://jupyter-notebook.readthedocs.io/en/stable/', None),
    'jupyterhub':  ('https://jupyterhub.readthedocs.io/en/stable/', None),
    'nbconvert':  ('https://nbconvert.readthedocs.io/en/latest/', None),
    'jupyter-contrib-nbextensions':  ('https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/', None),
    'sphinx':  ('http://www.sphinx-doc.org/en/master/', None),
    'nbsphinx':  ('https://nbsphinx.readthedocs.io/en/0.4.2/', None),
    'pipenv': ('https://docs.pipenv.org/en/latest/', None),
    'spack':  ('https://spack.readthedocs.io/en/latest/', None),
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

graphviz_output_format = 'svg'

# Fix for Sphinx < 2.0
master_doc = 'index'

