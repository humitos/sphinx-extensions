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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'sphinx-extensions'
copyright = '2021, Manuel Kaufmann'
author = 'Manuel Kaufmann'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinxemoji.sphinxemoji',
    'sphinx-prompt',
    'sphinx_copybutton',
    'notfound.extension',
    'myst_parser',
    'sphinxcontrib.httpdomain',
    'autoapi.extension',
    'nbsphinx',
    'sphinx_last_updated_by_git',
    'sphinx_design',
    'sphinx_favicon',
]


favicons = [
   {
      "rel": "icon",
      "href": "favicon.svg",
   },
]
autosectionlabel_prefix_document = True

nbsphinx_execute = 'auto'
nbsphinx_execute_arguments = [
    "--InlineBackend.figure_formats={'svg', 'pdf'}",
]

autoapi_dirs = [
    'sphinx-notfound-page/notfound',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'sphinx-notfound-page', '.ipynb_checkpoints/*']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_material'
html_logo = '_static/logo.svg'

# Material theme options (see theme.conf for more information)
html_theme_options = {
    'nav_title': 'sphinx-extensions',
    'color_primary': 'blue',
    'color_accent': 'light-blue',
    'version_dropwdown': False,

    'master_doc': None,
    'nav_links': [],

    'heroes': {},

    # Set the repo location to get a badge with stats
    'repo_url': 'https://github.com/humitos/sphinx-extensions/',
    'repo_name': 'sphinx-extensions',
}

# globaltoc seems it's not added by default
html_sidebars = {
    '**': ['globaltoc.html', 'localtoc.html', 'searchbox.html']
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
