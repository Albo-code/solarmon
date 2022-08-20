# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('./../../'))


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'solarmon'
copyright = '2022, Albo-code'
author = 'Albo-code'
release = '0.1'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.autodoc',
    'sphinx.ext.linkcode'
]

#templates_path = ['_templates']

exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'

# If this is not None, a ‘Last updated on:’ timestamp is inserted at every page
# bottom, using the given strftime() format. The empty string is equivalent to
# '%b %d, %Y' (or a locale-dependent equivalent).
html_last_updated_fmt = '%A %d %b %Y at %H:%M:%S'

#html_static_path = ['_static']


# -- Options autodoc

# This value contains a list of modules to be mocked up. This is useful when
# some external dependencies are not met at build time and break the building
# process. You may only specify the root package of the dependencies themselves
# and omit the sub-modules:
autodoc_mock_imports = ['plac', 'yaml']

# -- sphinx.ext.linkcode
# See https://www.sphinx-doc.org/en/master/usage/extensions/linkcode.html

LINKCODE_REPO_URL = 'https://github.com/Albo-code/solarmon/tree'
# Update following to point to branch containing source that is to be linked to
LINKCODE_REPO_BRANCH = 'main'

def linkcode_resolve(domain, info):
    if domain != 'py':
        return None
    if not info['module']:
        return None
    filename = info['module'].replace('.', '/')
    return f"{LINKCODE_REPO_URL}/{LINKCODE_REPO_BRANCH}/{filename}.py"
