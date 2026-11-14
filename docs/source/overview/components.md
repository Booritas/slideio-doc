# Components

SlideIO is a family of four components built on one image-reading core. They
share the same image drivers, so they all read the same
[formats](formats.md) and see a slide the same way.

```{list-table}
:header-rows: 1
:widths: 22 38 40

* - Component
  - What it is
  - Who it is for
* - [C++ library](../cpp/index.md)
  - The core: image drivers, the `Slide` and `Scene` API, transformations and
    conversion.
  - Developers building SlideIO into their own application.
* - [Command line tools](../tools/index.md)
  - `slideio-converter` and `slideio-tiffinspector`, shipped with the library.
  - Anyone who needs to convert or inspect a slide without writing code.
* - [Python package](../python/index.md)
  - The library as a Python module, with rasters returned as numpy arrays.
  - Data scientists and image analysis pipelines.
* - [SlideIO Viewer](../viewer/index.md)
  - A desktop application for viewing and annotating slides.
  - Pathologists, researchers and anyone who wants to look at a slide.
```

## SlideIO C++ library

The C++ library is where the formats are read. It is reached through two
global functions, `slideio::openSlide()` and `slideio::getDriverIDs()`, and two
classes: `slideio::Slide`, a container for one image file, and
`slideio::Scene`, a single raster within it, such as a scanned region, a label
or a macro image.

A scene is read as a whole or as any region of it, resized to the size you ask
for. A region read at reduced size comes from the closest level of the zoom
pyramid stored in the slide rather than from full resolution, so even a
gigapixel slide is scaled down quickly. Scenes can hold several channels, Z slices and time
frames, and report their resolution, magnification, metadata and colour
profile. Reads of one scene from several threads run concurrently for most
formats.

Beyond reading, the library applies transformations to a scene, such as
filters and colour management, and converts a scene into a tiled pyramidal
SVS or OME-TIFF file.

Prebuilt packages are published for Windows, macOS and Linux and are consumed
with CMake `find_package`. See [C++ library](../cpp/index.md).

## Command line tools

Every library package carries two command line tools, which need neither
Python nor a line of code:

- **`slideio-converter`** converts a slide, or a region of one, into a tiled
  pyramidal SVS or OME-TIFF file, choosing the scene, channels, Z slices, time
  frames and compression.
- **`slideio-tiffinspector`** prints every directory of a TIFF file: geometry,
  tiling, channels, compression and the ICC profile. It shows how many pyramid
  levels a slide really has and which directory holds the label.

See [Command line tools](../tools/index.md).

## SlideIO Python package

The `slideio` Python package exposes the library to Python. It is installed
with `pip install slideio`, and the wheel carries the library inside it, so no
compiler or separate installation is needed. Wheels are published for
Windows, macOS and Linux.

```python
import slideio

slide = slideio.open_slide("image.svs")
scene = slide.get_scene(0)
# a 10000 x 10000 region, scaled down to 500 x 500 pixels
image = scene.read_block((0, 0, 10000, 10000), (500, 500))
```

Rasters are returned as numpy arrays, compatible with
[OpenCV](https://opencv.org). The package also covers transformations,
colour management and conversion. See [Python module](../python/index.md).

## SlideIO Viewer

SlideIO Viewer is a free desktop application for Windows, macOS and Linux. It
opens a slide in a window and pans and zooms through it at interactive speed,
with GPU-accelerated rendering from the slide's zoom pyramid. It shows the
scenes, channels, Z slices, time frames, associated images and metadata of a
slide, and lets you annotate, count and measure, then export the results for
QuPath or a spreadsheet.

The viewer is built on the C++ library and reads every format it supports. See
[SlideIO Viewer](../viewer/index.md).
