"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full list see the
documentation: https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

from __future__ import annotations

from datetime import datetime

from sphinx_api_relink.helpers import (
    get_branch_name,
    get_execution_mode,
    get_package_version,
    pin,
    pin_minor,
    set_intersphinx_version_remapping,
)

set_intersphinx_version_remapping({
    "ipython": {
        "8.12.2": "8.12.1",
        "8.12.3": "8.12.1",
    },
    "matplotlib": {"3.5.1": "3.5.0"},
})

BRANCH = get_branch_name()
ORGANIZATION = "ComPWA"
PACKAGE = "pwa_pages"
REPO_NAME = "PWA-pages"
REPO_TITLE = "PWA Software Pages"

add_module_names = False
api_github_repo = f"{ORGANIZATION}/{REPO_NAME}"
api_target_substitutions: dict[str, str | tuple[str, str]] = {
    "datetime": "datetime.datetime",
}
author = "Common Partial Wave Analysis"
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
    "special-members": ", ".join([
        "__call__",
        "__eq__",
    ]),
}
autosectionlabel_prefix_document = True
bibtex_bibfiles = ["bibliography.bib"]
bibtex_default_style = "unsrt_et_al"
bibtex_reference_style = "author_year"
codeautolink_concat_default = True
codeautolink_global_preface = """
from IPython.display import display
"""
comments_config = {
    "hypothesis": True,
    "utterances": {
        "repo": f"{ORGANIZATION}/{REPO_NAME}",
        "issue-term": "pathname",
        "label": "📝 Docs",
    },
}
copybutton_prompt_is_regexp = True
copybutton_prompt_text = r">>> |\.\.\. "  # doctest
copyright = f"2020, {ORGANIZATION}"
default_role = "py:obj"
exclude_patterns = [
    "**.ipynb_checkpoints",
    "*build",
]
extensions = [
    "myst_nb",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.graphviz",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx_api_relink",
    "sphinx_codeautolink",
    "sphinx_comments",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_hep_pdgref",
    "sphinx_pybtex_etal_style",
    "sphinx_thebe",
    "sphinx_togglebutton",
    "sphinxcontrib.bibtex",
]
generate_apidoc_package_path = f"../src/{PACKAGE}"
graphviz_output_format = "svg"
html_copy_source = True  # needed for download notebook button
html_css_files = ["custom.css"]
html_favicon = "_static/favicon.ico"
html_last_updated_fmt = "%-d %B %Y"
html_show_copyright = False
html_show_sourcelink = False
html_show_sphinx = False
html_sourcelink_suffix = ""
html_static_path = ["_static"]
html_theme = "sphinx_book_theme"
html_theme_options = {
    "repository_url": f"https://github.com/{ORGANIZATION}/{REPO_NAME}",
    "repository_branch": BRANCH,
    "path_to_docs": "docs",
    "use_download_button": True,
    "use_edit_page_button": True,
    "use_issues_button": True,
    "use_repository_button": True,
    "launch_buttons": {
        "binderhub_url": "https://mybinder.org",
        "colab_url": "https://colab.research.google.com",
        "notebook_interface": "jupyterlab",
        "thebe": True,
        "thebelab": True,
    },
}
html_title = "Partial Wave Analysis"
intersphinx_mapping = {
    "IPython": (f"https://ipython.readthedocs.io/en/{pin('IPython')}", None),
    "matplotlib": (f"https://matplotlib.org/{pin('matplotlib')}", None),
    "python": ("https://docs.python.org/3", None),
    "pydantic": (f"https://docs.pydantic.dev/{pin_minor('pydantic')}", None),
    "sympy": ("https://docs.sympy.org/latest", None),
}
linkcheck_anchors = False
linkcheck_ignore = [
    "http://127.0.0.1:8000",
    "http://cgl.soic.indiana.edu/jpac/References.html",
    "https://doi.org/10.1002/andp.19955070504",  # 403 for onlinelibrary.wiley.com
    "https://doi.org/10.1093/ptep/ptaa104",
    "https://home.fnal.gov/~kutschke/Angdist/angdist.ps",
    "https://physique.cuso.ch",
    "https://suchung.web.cern.ch",
    "https://www.bookfinder.com",
]
master_doc = "index"
modindex_common_prefix = [f"{PACKAGE}."]
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "dollarmath",
    "smartquotes",
    "substitution",
]
myst_substitutions = {
    "branch": BRANCH,
    "build_date": datetime.today().strftime("%d %B %Y"),
    "repo": REPO_NAME,
}
myst_update_mathjax = False
nb_execution_mode = get_execution_mode()
nb_execution_show_tb = True
nb_execution_timeout = -1
nb_output_stderr = "remove"
nitpick_ignore_regex = [
    (r"py:(class|obj)", "ConfigDict"),
    (r"py:(class|obj)", "FieldInfo"),
    (r"py:(class|obj)", "Model.__fields__"),
    (r"py:(class|obj)", "pydantic.main.BaseModel"),
]
nitpicky = True
primary_domain = "py"
project = REPO_TITLE
pygments_style = "sphinx"
release = get_package_version(PACKAGE)
source_suffix = {
    ".ipynb": "myst-nb",
    ".md": "myst-nb",
    ".rst": "restructuredtext",
}
thebe_config = {
    "repository_url": html_theme_options["repository_url"],
    "repository_branch": html_theme_options["repository_branch"],
}
todo_include_todos = True
version = get_package_version(PACKAGE)
