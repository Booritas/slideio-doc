# SlideIO

```{image} _static/slideio.webp
:alt: SlideIO reads a whole slide and its zoom pyramid, from Python or C++
```

**SlideIO** is an open-source library for reading medical images, with a C++ API
and a Python module, and a free desktop viewer built on it.

It reads whole slides as well as any region of a slide. Large slides can be
scaled to a smaller size efficiently, because the library reads from the zoom
pyramid stored in the image. SlideIO supports 2D slides as well as 3D data sets
and time series. The Python module delivers a raster as a numpy array, compatible
with [OpenCV](https://opencv.org).

## Components

[SlideIO for Python](python/index.md)
: `pip install slideio`. The module most users want: open a slide, read regions
  as numpy arrays, inspect metadata.

[SlideIO C++ library](cpp/index.md)
: Build SlideIO into your own application. Prebuilt packages for Windows, macOS
  and Linux, consumed with CMake `find_package`.

[SlideIO Viewer](viewer/index.md)
: A desktop application for Windows, macOS and Linux that renders a whole slide
  with GPU-accelerated panning and zooming. No code to write.

[Command line tools](tools/index.md)
: `slideio-converter` and `slideio-tiffinspector`, shipped with every library
  package.

[Components](overview/components.md) describes each one and how they fit
together.

## Supported formats

SlideIO reads 16 formats, among them Aperio SVS, Zeiss CZI, Hamamatsu NDPI,
3DHISTECH MIRAX, Roche Ventana BIF, Philips TIFF, Leica SCN and LIF, Nikon ND2,
Olympus VSI, OME-TIFF and DICOM whole slide images. See
[Supported formats](overview/formats.md) for the full list.

## SlideIO Viewer

Slides can also be opened without writing any code. SlideIO Viewer renders a
whole slide with GPU-accelerated panning and zooming, and shows its scenes,
channels, associated images and metadata.

```{image} _static/viewer.webp
:alt: SlideIO Viewer
:target: viewer/index.html
```

[Read more about SlideIO Viewer](viewer/index.md) or
[download it](https://github.com/Booritas/slideio-view/releases/latest).

## Latest news

- [Version 2.11.0 – MRXS, BIF, LIF and ND2 Drivers and Computed Scenes](news/2026-11-14-version-2-11-0.md)
- {ref}`SlideIO Viewer 0.3.0 – MIRAX, BIF, LIF and ND2 Slides <viewer-0-3-0>`
- [Library release notes](news/index.md)
- [Viewer release notes](viewer/release-notes.md)

```{toctree}
:hidden:
:caption: Overview

overview/components
overview/formats
```

```{toctree}
:hidden:
:caption: Python

python/index
python/tutorial
python/tutorials
python/color-management
python/api/index
python/downloads
```

```{toctree}
:hidden:
:caption: C++

cpp/index
cpp/api
cpp/reference/index
cpp/third-party
cpp/downloads
```

```{toctree}
:hidden:
:caption: Viewer

viewer/index
viewer/release-notes
viewer/downloads
```

```{toctree}
:hidden:
:caption: Command line tools

tools/index
tools/downloads
```

```{toctree}
:hidden:
:caption: Reference

drivers
```

```{toctree}
:hidden:
:caption: Project

news/index
about
license
```
