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

.. code-block:: shell

   python -m venv .venv
   .venv/bin/pip install -r docs/requirements.txt     # .venv\Scripts\pip on Windows
   .venv/bin/sphinx-build -b html docs/source docs/build/html

The Python API reference is generated with autodoc from the installed
``slideio`` package, so the version pinned in ``docs/requirements.txt`` is the
one documented.

Layout
------

::

   docs/source/
     index.md            home page
     python/             Python module: install, tutorial, colour management, API reference
     cpp/                C++ library: install, API overview, third-party libraries
     viewer/             SlideIO Viewer
     drivers.md          image drivers and the formats they read
     tools.md            slideio-converter and slideio-tiffinspector
     tutorials.md        Jupyter notebook tutorials
     downloads.md        packages for all three projects
     news/               release notes
     _static/            images and favicon
