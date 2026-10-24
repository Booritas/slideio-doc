# Python module

## Overview

The Python module provides two main classes: {py:class}`~slideio.Slide` and
{py:class}`~slideio.Scene`. A *Slide* is a container object returned by the
module function {py:func}`~slideio.open_slide`. In the simplest case, a *Slide*
contains a single *Scene*. Some slides contain several scenes: for example, a
CZI file can hold several scanned regions, each represented by a *Scene*. The
*Scene* class provides methods to access pixel values and metadata.

Rasters are returned as numpy arrays, compatible with
[OpenCV](https://opencv.org).

## Installation

The module is installed from PyPI:

```
pip install slideio
```

Wheels are published for Python 3.9 through 3.14 on Windows x86-64, macOS
(Apple Silicon and Intel) and Linux x86-64. The wheel carries the SlideIO
library inside it, so no compiler, no Conan and no separate library
installation is needed. See [Downloads](downloads.md) for the release files.

### Building the module from the source

The Python module is developed in its own repository,
[Booritas/slideio-python](https://github.com/Booritas/slideio-python), where
the build instructions are kept current with the code: see
[Building from source](https://github.com/Booritas/slideio-python#building-from-source)
in its README.

## Quick start

Read a whole CZI image:

```python
import slideio
slide = slideio.open_slide(file_path="/data/a.czi", driver_id="CZI")
scene = slide.get_scene(0)
block = scene.read_block()
```

## Next steps

- [Quick tutorial](tutorial.md): short recipes for the everyday tasks.
- [Colour management](color-management.md): ICC profiles and colour conversion.
- [API reference](api/index.rst): every class and function.
- [Jupyter notebook tutorials](tutorials.md) with complete worked examples.
