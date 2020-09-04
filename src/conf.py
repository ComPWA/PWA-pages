"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

import os
import shutil
import subprocess

# -- Project information -----------------------------------------------------
project = "PWA Software Pages"
copyright = "2020"
author = "Common Partial-Wave Analysis"


# -- General configuration ---------------------------------------------------

# The master toctree document
master_doc = "index"

extensions = [
    "myst_parser",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "sphinxcontrib.bibtex",
]

source_suffix = [
    ".md",
    ".rst",
]

templates_path = [
    "_templates",
]

exclude_patterns = [
    ".DS_Store",
    "README.md",
    "Thumbs.db",
    "build",
]

# Cross-referencing configuration
default_role = "py:obj"
primary_domain = "py"
nitpicky = True  # warn if cross-references are missing

# Settings for intersphinx
intersphinx_mapping = {
    "ComPWA": ("https://pwa.readthedocs.io/projects/compwa/en/latest/", None),
    "expertsystem": (
        "https://pwa.readthedocs.io/projects/expertsystem/en/latest/",
        None,
    ),
    "pycompwa": ("https://compwa.github.io/", None),
    "tensorwaves": (
        "https://pwa.readthedocs.io/projects/tensorwaves/en/latest/",
        None,
    ),
}

# Settings for autosectionlabel
autosectionlabel_prefix_document = True

# Settings for linkcheck
linkcheck_anchors = False
linkcheck_ignore = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

html_theme_options = {
    "canonical_url": "",
    "analytics_id": "",
    "logo_only": True,
    "display_version": True,
    "prev_next_buttons_location": "both",
    "style_external_links": False,
    # Toc options
    "collapse_navigation": True,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": False,
    "titles_only": False,
}
