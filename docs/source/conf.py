# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import importlib.metadata
import logging as pylogging
import re
import shutil
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path

from sphinx.util import logging

logger = logging.getLogger(__name__)

# -- SlideIO sources ---------------------------------------------------------
#
# The SlideIO library is the git submodule extern/slideio, checked out at the
# release being documented. The documented version and the C++ reference both
# come from it, so moving the submodule to a new tag updates them together.

REPO_ROOT = Path(__file__).resolve().parents[2]
SLIDEIO_SOURCE_DIR = REPO_ROOT / "extern" / "slideio"
DOCS_BUILD_DIR = REPO_ROOT / "docs" / "build"

# Modules whose headers are installed with the library, as listed in the
# top-level CMakeLists.txt of SlideIO (SLIDEIO_PUBLIC_HEADER_MODULES).
SLIDEIO_PUBLIC_MODULES = ["core", "slideio", "imagetools", "converter", "transformer"]


def slideio_version(source_dir):
    cmake_lists = source_dir / "CMakeLists.txt"
    if not cmake_lists.exists():
        raise RuntimeError(
            f"SlideIO sources not found in {source_dir}. "
            "Run: git submodule update --init extern/slideio"
        )
    match = re.search(r"set\(projectVersion\s+([0-9.]+)\)", cmake_lists.read_text(encoding="utf-8"))
    return match.group(1)


# -- Project information -----------------------------------------------------

project = "SlideIO"
copyright = "2020-2026, Stanislav Melnikov"
author = "Stanislav Melnikov"

# The full version, including alpha/beta/rc tags.
release = slideio_version(SLIDEIO_SOURCE_DIR)
# The short X.Y version.
version = ".".join(release.split(".")[:2])

# -- C++ API reference -------------------------------------------------------


def public_headers(source_dir):
    """Map each public module to its headers, read from public-headers.cmake."""
    headers = {}
    for module in SLIDEIO_PUBLIC_MODULES:
        module_dir = source_dir / "src" / "slideio" / module
        listing = (module_dir / "public-headers.cmake").read_text(encoding="utf-8")
        listing = re.sub(r"#.*", "", listing)
        names = re.search(r"set\(\s*\S+(.*?)\)", listing, re.S).group(1).split()
        # The *_def.hpp headers only hold export macros.
        headers[module] = [module_dir / name for name in names if not name.endswith("_def.hpp")]
    return headers


def run_doxygen(source_dir, headers, output_dir):
    # Start clean, so no XML of a header from an earlier source is left behind.
    shutil.rmtree(output_dir, ignore_errors=True)
    output_dir.mkdir(parents=True)
    inputs = " ".join(f'"{h.as_posix()}"' for module in headers.values() for h in module)
    export_macros = " ".join(
        f"SLIDEIO_{m.upper()}_EXPORTS=" for m in ["core", "imagetools", "converter", "transformer"]
    )
    doxyfile = f"""
PROJECT_NAME           = SlideIO
PROJECT_NUMBER         = {release}
INPUT                  = {inputs}
OUTPUT_DIRECTORY       = "{output_dir.as_posix()}"
STRIP_FROM_PATH        = "{(source_dir / 'src').as_posix()}"
STRIP_FROM_INC_PATH    = "{(source_dir / 'src').as_posix()}"
GENERATE_XML           = YES
GENERATE_HTML          = NO
GENERATE_LATEX         = NO
EXTRACT_ALL            = YES
EXTRACT_PRIVATE        = NO
EXTRACT_STATIC         = YES
ENABLE_PREPROCESSING   = YES
MACRO_EXPANSION        = YES
EXPAND_ONLY_PREDEF     = YES
PREDEFINED             = SLIDEIO_EXPORTS= {export_macros}
# rect.hpp and size.hpp forward-declare OpenCV types for conversions.
EXCLUDE_SYMBOLS        = cv cv::*
QUIET                  = YES
WARNINGS               = NO
WARN_IF_INCOMPLETE_DOC = NO
"""
    subprocess.run(["doxygen", "-"], input=doxyfile, text=True, check=True)


def check_reference_coverage(headers):
    """Warn about public headers that no page of the C++ reference documents."""
    reference_dir = Path(__file__).parent / "cpp" / "reference"
    pages = " ".join(p.read_text(encoding="utf-8") for p in reference_dir.glob("*.md"))
    for module in headers.values():
        for header in module:
            if "{doxygenfile} " + header.name not in pages:
                logger.warning("C++ reference: public header %s is not documented", header.name)


def check_python_module_version():
    """Warn if the slideio module autodoc reads is not the documented release."""
    installed = importlib.metadata.version("slideio")
    if installed != release:
        logger.warning(
            "Python reference: installed slideio is %s, the documented release is %s; "
            "update the pin in docs/requirements.txt",
            installed,
            release,
        )


check_python_module_version()
_public_headers = public_headers(SLIDEIO_SOURCE_DIR)
_doxygen_dir = DOCS_BUILD_DIR / "doxygen"
run_doxygen(SLIDEIO_SOURCE_DIR, _public_headers, _doxygen_dir)
check_reference_coverage(_public_headers)

breathe_projects = {"slideio": str(_doxygen_dir / "xml")}
breathe_default_project = "slideio"
breathe_default_members = ("members",)



def doxygen_namespaces(xml_dir):
    index = ET.parse(xml_dir / "index.xml").getroot()
    return {
        c.findtext("name").split("::")[-1]
        for c in index.iter("compound")
        if c.get("kind") == "namespace"
    }


_namespaces = doxygen_namespaces(_doxygen_dir / "xml")


def _drop_namespace_duplicates(record):
    """Filter out duplicate-declaration warnings for namespaces.

    doxygenfile renders the enclosing namespace of the header, and all headers
    share the slideio namespace, so each one declares it again. Duplicates of
    anything else are still reported.
    """
    if getattr(record, "type", None) == "duplicate_declaration" and getattr(
        record, "subtype", None
    ) == "cpp":
        # Read the formatted message: records from parallel build workers
        # arrive with their arguments already merged into it.
        match = re.search(r"Declaration is '\.\. cpp:\w+:: (.+?)'", record.getMessage())
        return not (match and match.group(1) in _namespaces)
    return True


def setup(app):
    for handler in pylogging.getLogger("sphinx").handlers:
        if isinstance(handler, logging.WarningStreamHandler):
            # Ahead of the filter that turns warnings into errors under -W.
            handler.filters.insert(0, _drop_namespace_duplicates)

# -- General configuration ---------------------------------------------------

extensions = [
    "myst_parser",
    "breathe",
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
