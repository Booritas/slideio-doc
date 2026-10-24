# SlideIO

```{image} _static/slideio.png
:alt: SlideIO
:width: 320px
```

**SlideIO** is an open-source library for reading medical images, with a C++ API
and a Python module, and a free desktop viewer built on it.

It reads whole slides as well as any region of a slide. Large slides can be
scaled to a smaller size efficiently, because the library reads from the zoom
pyramid stored in the image. SlideIO supports 2D slides as well as 3D data sets
and time series. The Python module delivers a raster as a numpy array, compatible
with [OpenCV](https://opencv.org).

## Products

[SlideIO for Python](python/index.md)
: `pip install slideio`. The module most users want: open a slide, read regions
  as numpy arrays, inspect metadata.

[SlideIO C++ library](cpp/index.md)
: Build SlideIO into your own application. Prebuilt packages for Windows, macOS
  and Linux, consumed with CMake `find_package`.

[SlideIO Viewer](viewer/index.md)
: A desktop application for Windows, macOS and Linux that renders a whole slide
  with GPU-accelerated panning and zooming. No code to write.

[Command line tools](tools.md)
: `slideio-converter` and `slideio-tiffinspector`, shipped with every library
  package.

## Supported formats

SlideIO accesses images through a system of image drivers, each implementing
the specifics of one or more formats:

| **Driver** | **File format** | **File extensions** | **Format developer** | **Scanners** |
|---|---|---|---|---|
| **SVS** | [Aperio SVS](https://www.leicabiosystems.com/en-de/digital-pathology/manage/aperio-imagescope/) | *.svs | [Leica Microsystems](https://www.leicabiosystems.com/) | [Aperio GT 450 and Aperio GT 450 DX](https://www.leicabiosystems.com/en-de/digital-pathology/scan/) |
| **AFI** | [Aperio AFI - Fluorescent images](https://www.pathologynews.com/fileformats/leica-afi/) | *.afi | [Leica Microsystems](https://www.leicabiosystems.com/) |  |
| **SCN** | [Leica](https://www.leica-microsystems.com/) SCN images | *.scn | [Leica Microsystems](https://www.leicabiosystems.com/) | [Leica SCN400](https://www.leicabiosystems.com/en-de/news-events/leica-microsystems-launches-scn400-f-combined-fluorescence-and-brightfield-slide/) |
| **CZI** | [Zeiss CZI](https://www.zeiss.com/microscopy/en/products/software/zeiss-zen/czi-image-file-format.html) images | *.czi | [Zeiss Microscopy](https://www.zeiss.com/microscopy/en/home.html) | [ZEISS Axioscan 7](https://www.zeiss.com/microscopy/en/products/imaging-systems/axioscan-for-biology.html) |
| **ZVI** | Zeiss ZVI image format | *.zvi | [Zeiss Microscopy](https://www.zeiss.com/microscopy/en/home.html) |  |
| **DCM** | DICOM images, including whole slide images | *.dcm, no extension |  |  |
| **NDPI** | [Hamamatsu NDPI image format](https://www.hamamatsu.com/eu/en/product/life-science-and-medical-systems/digital-slide-scanner/U12388-01.html) | *.ndpi | [Hamamatsu](https://www.hamamatsu.com/eu/en.html) |  |
| **VSI** | Olympus VSI image format | *.vsi |  |  |
| **QPTIFF** | PerkinElmer Vectra QPTIFF | *.qptiff | [Akoya Biosciences](https://www.akoyabio.com/software-data-analysis/) | [Perkin Elmer Vectra scanner](https://www.akoyabio.com/phenoimager/instruments/vectra-3-0/) |
| **GDAL** | General image formats | *.png, *.jpeg, *.jpg, *.tif, *.tiff, *.bmp, *.gif, *.gtiff, *.gtif, *.ntif, *.jp2 | - | - |
| **OMETIFF** | OME-TIFF image format | *.ome.tiff, *.ome.tif | [OME-TIFF](https://docs.openmicroscopy.org/ome-model/5.6.3/ome-tiff/) |  |
| **PHTIFF** | Philips TIFF whole slide images | *.tif, *.tiff | [Philips](https://www.philips.com/) | [Philips IntelliSite Pathology Solution](https://www.usa.philips.com/healthcare/resources/landing/philips-intellisite-pathology-solution) |

See [Image drivers](drivers.md) for what each driver exposes.

## SlideIO Viewer

Slides can also be opened without writing any code. SlideIO Viewer renders a
whole slide with GPU-accelerated panning and zooming, and shows its scenes,
channels, associated images and metadata.

```{image} _static/viewer.png
:alt: SlideIO Viewer
:target: viewer/index.html
```

[Read more about SlideIO Viewer](viewer/index.md) or
[download it](https://github.com/Booritas/slideio-view/releases/latest).

## Latest news

- [Version 2.10.0 – Parallel Reads, Colour Management and Binary Distributions](news/2026-09-29-version-2-10-0.md)
- [SlideIO Viewer 0.1.0 – A Desktop Application for Whole-Slide Images](news/2026-10-04-slideio-viewer-0-1-0.md)
- [All release notes](news/index.md)

```{toctree}
:hidden:
:caption: Python

python/index
python/tutorial
python/color-management
python/api/index
```

```{toctree}
:hidden:
:caption: C++

cpp/index
cpp/api
cpp/third-party
```

```{toctree}
:hidden:
:caption: Viewer

viewer/index
```

```{toctree}
:hidden:
:caption: Reference

drivers
tools
tutorials
downloads
```

```{toctree}
:hidden:
:caption: Project

news/index
about
license
```
