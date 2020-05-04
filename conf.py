# -- Project information -----------------------------------------------------

project = 'PWA Software Pages'
copyright = '2020'
author = 'Common Partial-Wave Analysis'


# -- General configuration ---------------------------------------------------

master_doc = 'README'

extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
    'sphinx_copybutton',
]

templates_path = [
    '_templates',
]

exclude_patterns = [
    'build',
    'Thumbs.db',
    '.DS_Store',
]

# Cross-referencing configuration
default_role = 'py:obj'
primary_domain = 'py'
nitpicky = True  # warn if cross-references are missing

# Settings for intersphinx
intersphinx_mapping = {
    'compwa': ('https://pwa.readthedocs.io/projects/compwa/en/latest/', None),
    'pycompwa': ('https://compwa.github.io/', None),
    'tensorwaves': ('https://pwa.readthedocs.io/projects/tensorwaves/en/latest/', None),
}

# Settings for autosectionlabel
autosectionlabel_prefix_document = True

# Settings for linkcheck
linkcheck_anchors = False
linkcheck_ignore = [
]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'canonical_url': '',
    'analytics_id': '',
    'logo_only': True,
    'display_version': True,
    'prev_next_buttons_location': 'both',
    'style_external_links': False,
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': False,
    'titles_only': False,
}
