# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = "SlideIO"
copyright = "2020-2026, Stanislav Melnikov"
author = "Stanislav Melnikov"

# The short X.Y version.
version = "2.10"
# The full version, including alpha/beta/rc tags.
release = "2.10.0"

# -- General configuration ---------------------------------------------------

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

myst_enable_extensions = [
    "colon_fence",
    "deflist",
]
myst_heading_anchors = 3

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = "furo"
html_title = "SlideIO"
html_logo = "_static/slideio-small.png"
html_favicon = "_static/favicon.ico"
html_static_path = ["_static"]
html_theme_options = {
    "source_repository": "https://github.com/Booritas/slideio-doc",
    "source_branch": "main",
    "source_directory": "docs/source/",
}

# -- Options for EPUB output -------------------------------------------------

epub_show_urls = "footnote"
