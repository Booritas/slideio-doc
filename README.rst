SlideIO documentation
=====================

Sources of the documentation site for the SlideIO projects:

- the SlideIO C++ library (`Booritas/slideio <https://github.com/Booritas/slideio>`_),
- the SlideIO Python module (`Booritas/slideio-python <https://github.com/Booritas/slideio-python>`_),
- SlideIO Viewer (`Booritas/slideio-view <https://github.com/Booritas/slideio-view>`_).

The site is built with Sphinx, using MyST Markdown for the pages, and is
published on Read the Docs (see ``.readthedocs.yaml``).

Building locally
----------------

Requires Python, git and `Doxygen <https://www.doxygen.nl>`_ on ``PATH``. The
SlideIO library is a git submodule, so clone with it:

.. code-block:: shell

   git clone --recurse-submodules https://github.com/Booritas/slideio-doc.git
   # or, in an existing clone:
   git submodule update --init extern/slideio

Its own submodules are not needed. Then:

.. code-block:: shell

   python -m venv .venv
   .venv/bin/pip install -r docs/requirements.txt     # .venv\Scripts\pip on Windows
   .venv/bin/sphinx-build -b html docs/source docs/build/html

The documented version and the two API references come from these sources:

- **Version**: read from ``extern/slideio/CMakeLists.txt``.
- **C++**: ``conf.py`` runs Doxygen on the public headers listed in each
  module's ``public-headers.cmake`` in ``extern/slideio``, and Breathe renders
  the XML. A public header that no page under ``docs/source/cpp/reference``
  documents is reported as a warning.
- **Python**: autodoc reads the installed ``slideio`` package, pinned in
  ``docs/requirements.txt``. The build warns if it differs from the version of
  ``extern/slideio``.

To preview the reference for unreleased headers, check out another commit in
the submodule (``git -C extern/slideio checkout master``) and build; switch it
back before committing.

Documenting a new release
-------------------------

.. code-block:: shell

   git -C extern/slideio fetch --tags
   git -C extern/slideio checkout v<version>
   # set slideio==<version> in docs/requirements.txt
   git add extern/slideio docs/requirements.txt

Layout
------

::

   docs/source/
     index.md            home page
     python/             Python module: install, tutorials, colour management, API reference, downloads
     cpp/                C++ library: install, API overview, reference, third-party libraries, downloads
     viewer/             SlideIO Viewer: user guide, release notes, downloads
     tools/              slideio-converter and slideio-tiffinspector, downloads
     drivers.md          image drivers and the formats they read
     news/               library release notes
     _static/            images and favicon
