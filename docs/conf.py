# pylint: disable=invalid-name,no-value-for-parameter
"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

import dataclasses
import os
import re
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple, Union

import sphinxcontrib.bibtex.plugin  # type: ignore[import]
from docutils import nodes
from docutils.nodes import Node as docutils_Node
from docutils.nodes import system_message
from docutils.parsers.rst.states import Inliner
from pkg_resources import get_distribution
from pybtex.database import Entry
from pybtex.plugin import register_plugin
from pybtex.richtext import BaseText, Tag, Text
from pybtex.style.formatting.unsrt import Style as UnsrtStyle
from pybtex.style.template import (
    FieldIsMissing,
    Node,
    _format_list,
    field,
    href,
    join,
    node,
    sentence,
    words,
)
from sphinx.application import Sphinx
from sphinx.util.typing import RoleFunction
from sphinxcontrib.bibtex.style.referencing.author_year import (
    AuthorYearReferenceStyle,
)

# -- Project information -----------------------------------------------------
project = "PWA Software Pages"
PACKAGE = "pwa_pages"
REPO_NAME = "ComPWA/PWA-pages"
copyright = "2020, ComPWA"  # noqa: A001
author = "Common Partial Wave Analysis"

# https://docs.readthedocs.io/en/stable/builds.html
BRANCH = os.environ.get("READTHEDOCS_VERSION", default="main")
if BRANCH == "latest":
    BRANCH = "main"
if re.match(r"^\d+$", BRANCH):  # PR preview
    BRANCH = "main"
REPO_NAME = os.environ.get("REPO", REPO_NAME)

if os.path.exists(f"../src/{PACKAGE}/version.py"):
    __release = get_distribution(PACKAGE).version
    version = ".".join(__release.split(".")[:3])


# -- General configuration ---------------------------------------------------
master_doc = "index.md"
source_suffix = {
    ".ipynb": "myst-nb",
    ".md": "myst-nb",
    ".rst": "restructuredtext",
}

# The master toctree document.
master_doc = "index"
modindex_common_prefix = [
    f"{PACKAGE}.",
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
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
    "sphinx_math_dollar",
    "sphinx_panels",
    "sphinx_thebe",
    "sphinx_togglebutton",
    "sphinxcontrib.bibtex",
    "sphinxcontrib.hep.pdgref",
]
exclude_patterns = [
    "**.ipynb_checkpoints",
    "*build",
]

# General sphinx settings
add_module_names = False
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
    "special-members": ", ".join(
        [
            "__call__",
            "__eq__",
        ]
    ),
}
graphviz_output_format = "svg"
html_copy_source = True  # needed for download notebook button
html_css_files = ["custom.css"]
html_favicon = "_static/favicon.ico"
html_show_copyright = False
html_show_sourcelink = False
html_show_sphinx = False
html_sourcelink_suffix = ""
html_static_path = ["_static"]
html_theme = "sphinx_book_theme"
html_theme_options = {
    "repository_url": f"https://github.com/{REPO_NAME}",
    "repository_branch": "main",
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
    "theme_dev_mode": True,
}
html_title = "Partial Wave Analysis"
panels_add_bootstrap_css = False  # wider pages
pygments_style = "sphinx"
todo_include_todos = True
viewcode_follow_imported_members = True

# Cross-referencing configuration
default_role = "py:obj"
primary_domain = "py"
nitpicky = True  # warn if cross-references are missing

# Intersphinx settings
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

# Settings for autosectionlabel
autosectionlabel_prefix_document = True

# Settings for bibtex
bibtex_bibfiles = [
    "bibliography.bib",
]
bibtex_reference_style = "author_year_no_comma"

# Settings for copybutton
copybutton_prompt_is_regexp = True
copybutton_prompt_text = r">>> |\.\.\. "  # doctest

# Settings for linkcheck
linkcheck_anchors = False
linkcheck_ignore = [
    "http://127.0.0.1:8000",
    "https://doi.org/10.1093/ptep/ptaa104",
]

# Settings for myst_nb
execution_timeout = -1
nb_output_stderr = "remove"
nb_render_priority = {
    "html": (
        "application/vnd.jupyter.widget-view+json",
        "application/javascript",
        "text/html",
        "image/svg+xml",
        "image/png",
        "image/jpeg",
        "text/markdown",
        "text/latex",
        "text/plain",
    )
}

jupyter_execute_notebooks = "off"
if "EXECUTE_NB" in os.environ:
    print("\033[93;1mWill run Jupyter notebooks!\033[0m")
    jupyter_execute_notebooks = "force"

# Settings for myst-parser
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

# Settings for Thebe cell output
thebe_config = {
    "repository_url": html_theme_options["repository_url"],
    "repository_branch": html_theme_options["repository_branch"],
}


# Add roles to simplify external links
def setup(app: Sphinx) -> Dict[str, Any]:
    app.add_role(
        "wiki",
        wikilink("https://en.wikipedia.org/wiki/%s"),
    )
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


def wikilink(pattern: str) -> RoleFunction:
    def role(
        # pylint: disable=too-many-arguments,unused-argument
        name: str,
        rawtext: str,
        text: str,
        lineno: int,
        inliner: Inliner,
        options: Optional[Dict] = None,
        content: Optional[List[str]] = None,
    ) -> Tuple[List[docutils_Node], List[system_message]]:
        output_text = text
        output_text = output_text.replace("_", " ")
        url = pattern % (text,)
        if options is None:
            options = {}
        reference_node = nodes.reference(
            rawtext, output_text, refuri=url, **options
        )
        return [reference_node], []

    return role


# Specify bibliography style
@dataclasses.dataclass
class NoCommaReferenceStyle(AuthorYearReferenceStyle):
    author_year_sep: Union["BaseText", str] = " "


sphinxcontrib.bibtex.plugin.register_plugin(
    "sphinxcontrib.bibtex.style.referencing",
    "author_year_no_comma",
    NoCommaReferenceStyle,
)


@node
def et_al(children, data, sep="", sep2=None, last_sep=None):  # type: ignore[no-untyped-def]
    if sep2 is None:
        sep2 = sep
    if last_sep is None:
        last_sep = sep
    parts = [part for part in _format_list(children, data) if part]
    if len(parts) <= 1:
        return Text(*parts)
    if len(parts) == 2:
        return Text(sep2).join(parts)
    if len(parts) == 3:
        return Text(last_sep).join([Text(sep).join(parts[:-1]), parts[-1]])
    return Text(parts[0], Tag("em", " et al"))


@node
def names(children, context, role, **kwargs):  # type: ignore[no-untyped-def]
    """Return formatted names."""
    assert not children
    try:
        persons = context["entry"].persons[role]
    except KeyError:
        # pylint: disable=raise-missing-from
        raise FieldIsMissing(role, context["entry"])

    style = context["style"]
    formatted_names = [
        style.format_name(person, style.abbreviate_names) for person in persons
    ]
    return et_al(**kwargs)[formatted_names].format_data(context)


class MyStyle(UnsrtStyle):
    def __init__(self) -> None:
        super().__init__(abbreviate_names=True)

    def format_names(self, role, as_sentence: bool = True) -> Node:  # type: ignore[no-untyped-def]
        formatted_names = names(
            role, sep=", ", sep2=" and ", last_sep=", and "
        )
        if as_sentence:
            return sentence[formatted_names]
        return formatted_names

    def format_eprint(self, e: Entry) -> Node:
        if "doi" in e.fields:
            return ""
        return super().format_eprint(e)

    def format_url(self, e: Entry) -> Node:
        if "doi" in e.fields or "eprint" in e.fields:
            return ""
        return words[
            href[
                field("url", raw=True),
                field("url", raw=True, apply_func=remove_http),
            ]
        ]

    def format_isbn(self, e: Entry) -> Node:
        return href[
            join[
                "https://isbnsearch.org/isbn/",
                field("isbn", raw=True, apply_func=remove_dashes_and_spaces),
            ],
            join[
                "ISBN:",
                field("isbn", raw=True),
            ],
        ]


def remove_dashes_and_spaces(isbn: str) -> str:
    to_remove = ["-", " "]
    for remove in to_remove:
        isbn = isbn.replace(remove, "")
    return isbn


def remove_http(url: str) -> str:
    to_remove = ["https://", "http://"]
    for remove in to_remove:
        url = url.replace(remove, "")
    return url


register_plugin("pybtex.style.formatting", "unsrt_et_al", MyStyle)
