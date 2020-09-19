"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

# -- Project information -----------------------------------------------------
project = "PWA Software Pages"
copyright = "2020"
author = "Common Partial Wave Analysis"


# -- General configuration ---------------------------------------------------

source_suffix = [
    ".md",
    ".rst",
]

# The master toctree document.
master_doc = "index"

extensions = [
    "myst_parser",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx_copybutton",
    "sphinx_togglebutton",
    "sphinxcontrib.bibtex",
]

exclude_patterns = [
    ".DS_Store",
    "README.md",
    "Thumbs.db",
    "build",
]

# General sphinx settings
html_copy_source = True  # needed for download notebook button
html_show_copyright = False
html_show_sourcelink = False
html_show_sphinx = False
html_sourcelink_suffix = ""
html_theme = "sphinx_book_theme"
html_theme_options = {
    "repository_url": "https://github.com/ComPWA/PWA-pages",
    "repository_branch": "master",
    "path_to_docs": "src",
    "use_edit_page_button": True,
    "use_issues_button": True,
    "use_repository_button": True,
}
html_title = "Partial Wave Analysis"

# Cross-referencing configuration
default_role = "py:obj"
primary_domain = "py"
nitpicky = True  # warn if cross-references are missing
nitpick_ignore = []

# Settings for intersphinx
intersphinx_mapping = {
    "ComPWA": ("https://pwa.readthedocs.io/projects/compwa/en/latest/", None),
    "expertsystem": (
        "https://pwa.readthedocs.io/projects/expertsystem/en/latest/",
        None,
    ),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "pycompwa": ("https://compwa.github.io/", None),
    "python": ("https://docs.python.org/3", None),
    "tensorwaves": (
        "https://pwa.readthedocs.io/projects/tensorwaves/en/latest/",
        None,
    ),
    "tox": ("https://tox.readthedocs.io/en/latest/", None),
}

# Settings for autosectionlabel
autosectionlabel_prefix_document = True

# Settings for linkcheck
linkcheck_anchors = False
linkcheck_ignore = []

# Settings for myst-parser
myst_update_mathjax = False
