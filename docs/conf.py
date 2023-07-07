"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full list see the
documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""
# pyright: reportMissingImports=false

import dataclasses
import os
import re
import sys
from datetime import datetime
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple, Union

import sphinxcontrib.bibtex.plugin  # type: ignore[import]
from docutils import nodes
from docutils.nodes import Node as docutils_Node
from docutils.nodes import system_message
from docutils.parsers.rst.states import Inliner
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
from sphinxcontrib.bibtex.style.referencing.author_year import AuthorYearReferenceStyle

if sys.version_info < (3, 8):
    from importlib_metadata import PackageNotFoundError
    from importlib_metadata import version as get_package_version
else:
    from importlib.metadata import PackageNotFoundError
    from importlib.metadata import version as get_package_version

# -- Project information -----------------------------------------------------
project = "PWA Software Pages"
PACKAGE = "pwa_pages"
copyright = "2020, ComPWA"  # noqa: A001
author = "Common Partial Wave Analysis"


def get_branch_name() -> str:
    branch = os.environ.get("READTHEDOCS_VERSION")
    if branch == "latest":
        branch = "main"
    if branch is None:
        branch = os.environ.get("GITHUB_REF", "main")
        branch = branch.replace("refs/heads/", "")  # type: ignore[union-attr]
        branch = branch.replace("refs/pull/", "")
        branch = branch.replace("refs/tags/", "")
        if re.match(r"^\d+/[a-z]+$", branch) is not None:  # type: ignore[arg-type]
            branch = "main"  # PR preview
    print(f"  Branch name: {branch}")
    return branch


def get_repository_name() -> str:
    repo = os.environ.get("GITHUB_REPOSITORY", "ComPWA/PWA-pages")
    print(f"  Repository: {repo}")
    return repo


BRANCH = get_branch_name()
REPO_NAME = get_repository_name()

try:
    __VERSION = get_package_version(PACKAGE)
    version = ".".join(__VERSION.split(".")[:3])
except PackageNotFoundError:
    pass


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
    "sphinx_codeautolink",
    "sphinx_comments",
    "sphinx_copybutton",
    "sphinx_design",
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
codeautolink_concat_default = True
codeautolink_global_preface = """
from IPython.display import display
"""
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
    "repository_url": f"https://github.com/{REPO_NAME}",
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
pygments_style = "sphinx"
todo_include_todos = True
viewcode_follow_imported_members = True

# Cross-referencing configuration
default_role = "py:obj"
primary_domain = "py"
nitpicky = True  # warn if cross-references are missing

# Intersphinx settings
version_remapping = {
    "ipython": {
        "8.12.2": "8.13.2",
    },
    "matplotlib": {"3.5.1": "3.5.0"},
}


def get_version(package_name: str) -> str:
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
    constraints_path = f"../.constraints/py{python_version}.txt"
    package_name = package_name.lower()
    with open(constraints_path) as stream:
        constraints = stream.read()
    for line in constraints.split("\n"):
        line = line.split("#")[0]  # remove comments
        line = line.strip()
        line = line.lower()
        if not line.startswith(package_name):
            continue
        if not line:
            continue
        line_segments = tuple(line.split("=="))
        if len(line_segments) != 2:  # noqa: PLR2004
            continue
        _, installed_version, *_ = line_segments
        installed_version = installed_version.strip()
        remapped_versions = version_remapping.get(package_name)
        if remapped_versions is not None:
            existing_version = remapped_versions.get(installed_version)
            if existing_version is not None:
                return existing_version
        return installed_version
    return "stable"


def get_minor_version(package_name: str) -> str:
    installed_version = get_version(package_name)
    if installed_version == "stable":
        return installed_version
    matches = re.match(r"^([0-9]+\.[0-9]+).*$", installed_version)
    if matches is None:
        msg = f"Could not find documentation for {package_name} v{installed_version}"
        raise ValueError(msg)
    return matches[1]


intersphinx_mapping = {
    "IPython": (
        f"https://ipython.readthedocs.io/en/{get_version('IPython')}",
        None,
    ),
    "matplotlib": (
        f"https://matplotlib.org/{get_version('matplotlib')}",
        None,
    ),
    "python": ("https://docs.python.org/3", None),
    "sympy": ("https://docs.sympy.org/latest", None),
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
    "http://cgl.soic.indiana.edu/jpac/References.html",
    "https://doi.org/10.1002/andp.19955070504",  # 403 for onlinelibrary.wiley.com
    "https://doi.org/10.1093/ptep/ptaa104",
    "https://home.fnal.gov/~kutschke/Angdist/angdist.ps",
    "https://physique.cuso.ch",
    "https://suchung.web.cern.ch",
]


# Settings for myst_nb
def get_execution_mode() -> str:
    if "FORCE_EXECUTE_NB" in os.environ:
        print_once("\033[93;1mWill run ALL Jupyter notebooks!\033[0m")
        return "force"
    if "EXECUTE_NB" in os.environ:
        return "cache"
    return "off"


@lru_cache(maxsize=None)
def print_once(message: str) -> None:
    print(message)


nb_execution_mode = get_execution_mode()
nb_execution_show_tb = True
nb_execution_timeout = -1
nb_output_stderr = "remove"
nb_execution_show_tb = True

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

# Settings for sphinx_comments
comments_config = {
    "hypothesis": True,
    "utterances": {
        "repo": f"ComPWA/{REPO_NAME}",
        "issue-term": "pathname",
        "label": "📝 Docs",
    },
}

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
    def role(  # noqa: PLR0913
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
        reference_node = nodes.reference(rawtext, output_text, refuri=url, **options)
        return [reference_node], []

    return role


# Specify bibliography style
@dataclasses.dataclass
class NoCommaReferenceStyle(
    AuthorYearReferenceStyle  # pyright: ignore[reportUntypedBaseClass]
):
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
    if len(parts) == 2:  # noqa: PLR2004
        return Text(sep2).join(parts)
    if len(parts) == 3:  # noqa: PLR2004
        return Text(last_sep).join([Text(sep).join(parts[:-1]), parts[-1]])
    return Text(parts[0], Tag("em", " et al"))


@node
def names(children, context, role, **kwargs):  # type: ignore[no-untyped-def]
    """Return formatted names."""
    assert not children
    try:
        persons = context["entry"].persons[role]
    except KeyError:
        raise FieldIsMissing(role, context["entry"]) from None

    style = context["style"]
    formatted_names = [
        style.format_name(person, style.abbreviate_names) for person in persons
    ]
    return et_al(**kwargs)[formatted_names].format_data(context)


class MyStyle(UnsrtStyle):  # pyright: ignore[reportUntypedBaseClass]
    def __init__(self) -> None:
        super().__init__(abbreviate_names=True)

    def format_names(self, role, as_sentence: bool = True) -> Node:  # type: ignore[no-untyped-def]
        formatted_names = names(role, sep=", ", sep2=" and ", last_sep=", and ")
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
