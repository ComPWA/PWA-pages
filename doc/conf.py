# type: ignore

"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

from typing import Dict

from docutils import nodes
from sphinx.application import Sphinx

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
    "nbsphinx",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx_copybutton",
    "sphinx_math_dollar",
    "sphinx_togglebutton",
    "sphinxcontrib.bibtex",
]
mathjax_config = {
    "tex2jax": {
        "inlineMath": [["\\(", "\\)"]],
        "displayMath": [["\\[", "\\]"]],
    },
}

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
    "path_to_docs": "doc",
    "use_edit_page_button": True,
    "use_issues_button": True,
    "use_repository_button": True,
    "expand_sections": ["theory"],
}
html_title = "Partial Wave Analysis"
todo_include_todos = True

# Cross-referencing configuration
default_role = "py:obj"
primary_domain = "py"
nitpicky = True  # warn if cross-references are missing
nitpick_ignore = []

# Settings for intersphinx
intersphinx_mapping = {
    "ComPWA": ("https://pwa.readthedocs.io/projects/compwa/en/latest/", None),
    "expertsystem": (
        "https://pwa.readthedocs.io/projects/expertsystem/en/stable/",
        None,
    ),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "pycompwa": ("https://compwa.github.io", None),
    "python": ("https://docs.python.org/3/", None),
    "tensorwaves": (
        "https://pwa.readthedocs.io/projects/tensorwaves/en/latest/",
        None,
    ),
    "tf_pwa": ("https://pwa.readthedocs.io/projects/tf-pwa/en/latest/", None),
    "tox": ("https://tox.readthedocs.io/en/stable/", None),
}

# Settings for autosectionlabel
autosectionlabel_prefix_document = True

# Settings for linkcheck
linkcheck_anchors = False
linkcheck_ignore = []

# Settings for myst-parser
myst_update_mathjax = False

# Settings for nbsphinx
print("\033[93;1mWill run Jupyter notebooks!\033[0m")
nbsphinx_execute = "always"
nbsphinx_timeout = -1
nbsphinx_execute_arguments = [
    "--InlineBackend.figure_formats={'svg', 'pdf'}",
]

# Add roles to simplify external linnks
def setup(app: Sphinx):
    app.add_role(
        "wiki", autolink("https://en.wikipedia.org/wiki/%s", {"_": " "})
    )


def autolink(pattern: str, replace_mapping: Dict[str, str]):
    def role(
        name, rawtext, text: str, lineno, inliner, options={}, content=[]
    ):
        output_text = text
        for search, replace in replace_mapping.items():
            output_text = output_text.replace(search, replace)
        url = pattern % (text,)
        node = nodes.reference(rawtext, output_text, refuri=url, **options)
        return [node], []

    return role


# Specify bibliography style
from pybtex.plugin import register_plugin
from pybtex.richtext import Tag, Text
from pybtex.style.formatting.unsrt import Style as UnsrtStyle
from pybtex.style.template import (
    FieldIsMissing,
    _format_list,
    field,
    href,
    join,
    node,
    sentence,
    words,
)


@node
def et_al(children, data, sep="", sep2=None, last_sep=None):
    if sep2 is None:
        sep2 = sep
    if last_sep is None:
        last_sep = sep
    parts = [part for part in _format_list(children, data) if part]
    if len(parts) <= 1:
        return Text(*parts)
    elif len(parts) == 2:
        return Text(sep2).join(parts)
    elif len(parts) == 3:
        return Text(last_sep).join([Text(sep).join(parts[:-1]), parts[-1]])
    else:
        return Text(parts[0], Tag("em", " et al"))


@node
def names(children, context, role, **kwargs):
    """Return formatted names."""
    assert not children
    try:
        persons = context["entry"].persons[role]
    except KeyError:
        raise FieldIsMissing(role, context["entry"])

    style = context["style"]
    formatted_names = [
        style.format_name(person, style.abbreviate_names) for person in persons
    ]
    return et_al(**kwargs)[formatted_names].format_data(context)


class MyStyle(UnsrtStyle):
    def __init__(self):
        super().__init__(abbreviate_names=True)

    def format_names(self, role, as_sentence=True):
        formatted_names = names(
            role, sep=", ", sep2=" and ", last_sep=", and "
        )
        if as_sentence:
            return sentence[formatted_names]
        else:
            return formatted_names

    def format_url(self, e):
        return words[
            href[
                field("url", raw=True),
                field("url", raw=True, apply_func=remove_http),
            ]
        ]

    def format_isbn(self, e):
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


def remove_http(input: str) -> str:
    to_remove = ["https://", "http://"]
    for remove in to_remove:
        input = input.replace(remove, "")
    return input


register_plugin("pybtex.style.formatting", "unsrt_et_al", MyStyle)
