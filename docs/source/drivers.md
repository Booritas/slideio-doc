# Image drivers

SlideIO uses a *driver* pattern to read specific image formats. Each driver
implements the functionality needed to access one or more image formats, and
each driver has a unique ID. The following drivers are available:

| Driver ID | File format | File extensions |
|---|---|---|
| SVS | [Aperio SVS](https://www.leicabiosystems.com/en-de/digital-pathology/manage/aperio-imagescope/) | *.svs |
| AFI | [Aperio AFI - Fluorescent images](https://www.pathologynews.com/fileformats/leica-afi/) | *.afi |
| SCN | [Leica](https://www.leica-microsystems.com/) SCN images | *.scn |
| CZI | [Zeiss CZI](https://www.zeiss.com/microscopy/en/products/software/zeiss-zen/czi-image-file-format.html) images | *.czi |
| ZVI | Zeiss ZVI image format | *.zvi |
| DCM | DICOM images | *.dcm, no extension |
| NDPI | [Hamamatsu NDPI image format](https://www.hamamatsu.com/eu/en/product/life-science-and-medical-systems/digital-slide-scanner/U12388-01.html) | *.ndpi |
| GDAL | General image formats | *.png, *.jpeg, *.jpg, *.tif, *.tiff, *.bmp, *.gif, *.gtiff, *.gtif, *.ntif, *.jp2 |
| VSI | Olympus VSI image format | *.vsi |
| QPTIFF | PerkinElmer Vectra QPTIFF | *.qptiff |
| OMETIFF | [OME-TIFF](https://docs.openmicroscopy.org/ome-model/5.6.3/ome-tiff/) image format | *.ome.tif, *.ome.tiff, *.ome.tf2, *.ome.tf8, *.ome.btf |
| PHTIFF | [Philips](https://www.usa.philips.com/healthcare/resources/landing/philips-intellisite-pathology-solution) TIFF whole slide images | *.tif, *.tiff |
| MRXS | [3DHISTECH](https://www.3dhistech.com/) MIRAX whole slide images | *.mrxs, Slidedat.ini |
| BIF | [Roche Ventana](https://diagnostics.roche.com/) BIF whole slide images | *.bif |
| LIF | [Leica](https://www.leica-microsystems.com/) LIF images | *.lif |
| ND2 | [Nikon](https://www.microscope.healthcare.nikon.com/) NIS-Elements ND2 images | *.nd2 |

Three drivers accept `*.tif` and `*.tiff`: GDAL, OMETIFF and PHTIFF. They are
told apart by the content of the file, so opening a slide with the default
`AUTO` driver picks the right one. Name a driver explicitly only to override
that.

## Open options

Some drivers take options that change how they open a file. Options are passed
when the slide is opened, as a map of keys to values: the `options` argument of
`open_slide` in Python, the third argument of `slideio::openSlide()` in C++,
and `-o key=value` of `slideio-converter`.

Every key is written `<driver-id>.<name>`. The driver ID is matched in any
letter case, the name exactly. Keys addressed to a driver other than the one
that opens the file are ignored, so one set of options can serve slides of
several formats. A key without a driver prefix, or with a driver ID that does
not exist, is rejected before the file is opened; an option name the driver
does not know is rejected when the driver opens the file. Boolean values are
written `true`, `false`, `1` or `0`; Python also accepts `True` and `False`.

Converting a scene re-opens it with the options its slide was opened with.

| Option | Default | Description |
|---|---|---|
| `mrxs.crop_to_content` | `true` | Crop an MRXS scene to the bounding box of the scanned area; `false` gives the full canvas. See [Cropping to the scanned area](#cropping-to-the-scanned-area). |

## Driver capabilities

| Driver | Multiple scenes | Z stacks | Time frames |
|---|---|---|---|
| CZI | yes | yes | yes |
| SVS | yes | no | no |
| AFI | yes | no | no |
| SCN | yes | no | no |
| GDAL | no | no | no |
| ZVI | no | yes | no |
| DCM | yes | yes | no |
| NDPI | no | no | no |
| VSI | yes | yes | yes |
| QPTIFF | yes | yes | yes |
| OMETIFF | yes | yes | yes |
| PHTIFF | no | no | no |
| MRXS | no | no | no |
| BIF | yes | no | no |
| LIF | yes | yes | yes |
| ND2 | yes | yes | yes |

## CZI driver

### Overview

A CZI image is a collection of multi-dimensional pixel regions (sub-blocks)
that are acquired with different parameters. The following parameters
(dimensions) are supported:

- Channel (C) - index of a channel in a multi-channel data set.
- Slice index (Z) - index of a slice in Z direction.
- Time point (T) - index of a time frame in a sequentially acquired series of data.
- Rotation (R) - used in acquisition modes where the data is recorded from various angles.
- Region (S) - for clustering items in X/Y direction (data belonging to contiguous regions of interests in a mosaic image).
- Illumination (I) - illumination direction index (e.g. from left=0, from right=1).
- Acquisition (B) - block index in segmented experiments.
- Mosaic tile index (M) - this index uniquely identifies all tiles in a specific plane.
- Phase index (H) - for specific acquisition methods.
- View index (V) - for multi-view images, e.g. SPIM.

SlideIO combines the sub-blocks into 2D-4D continuous scenes (depending on
whether Z slices and time frames are present). Each scene corresponds to a
different combination of the dimensions:

- Rotation (R).
- Region (S).
- Illumination (I).
- Acquisition (B).
- Mosaic tile index (M).
- Phase index (H).
- View index (V).

### Scene naming

The actual values of the dimension parameters are coded in the scene name. For
example, a scene named `s:1 i:0 v:2 h:1 r:0 b:1` corresponds to a region with
index 1, illumination index 0, view index 2, phase index 1, rotation angle index
0 and block index 1.

### Metadata

The *Slide* property *raw_metadata* returns a textual representation of the XML
metadata document embedded in the slide.

### Auxiliary images

The driver supports auxiliary images for *Slide* and *Scene* objects. Images are
extracted from the corresponding "attachment" sections of the file.

## SVS driver

The SVS driver exposes images extracted from Aperio SVS slides. Each *Slide*
object contains at least one *Scene* object, the image itself. Other *Scene*
objects represent the thumbnail, label and macro.

### Scene naming

The following scene names are used:

- Image: main image;
- Macro: macro image;
- Thumbnail: thumbnail image;
- Label: label image.

The main image is always the first in the scene collection.

### Metadata

The *Slide* property *raw_metadata* returns the string extracted from the
"Image Description" TIFF tag of the main image directory.

### Auxiliary images

The driver supports auxiliary images for *Slide* objects.

## AFI driver

An AFI image is a collection of SVS images bundled together by an XML file with
the extension `afi`. Each SVS image is represented by a separate *Scene* object.
The *Slide* property *raw_metadata* always returns an empty string.

## SCN driver

The SCN driver reads images produced by the
[Leica SCN400 scanner](https://www.leicabiosystems.com/en-de/news-events/leica-microsystems-launches-scn400-f-combined-fluorescence-and-brightfield-slide/).
Files produced by the scanner have the extension `.scn` and normally contain
multiple images, such as high resolution scans of different regions of tissue,
thumbnails, labels and barcodes. Each of these internal images is exposed as a
separate scene object. The scene property *rect* describes the size of the image
and the offset of the region.

### Scene naming

Scene names are taken from the XML metadata document located in the "Image
Description" TIFF tag.

### Metadata

The *Slide* property *raw_metadata* returns the string extracted from the
"Image Description" TIFF tag of the main image directory.

### Auxiliary images

The driver supports auxiliary images for *Slide* objects.

## GDAL driver

The GDAL driver opens generic formats such as JPEG, PNG and TIFF. A *Slide*
object always contains a single *Scene* object.

### Metadata

The *Slide* property *raw_metadata* always returns an empty string.

## ZVI driver

The ZVI driver opens images produced by the Carl Zeiss AxioVision microscope.
The files can contain 2D or 3D images. A *Slide* object always contains a single
*Scene* object.

### Metadata

The *raw_metadata* property of a *Slide* object always returns an empty string.

## DCM driver

The DCM driver opens DICOM images and directories. The path passed when opening
a slide can be one of the following:

- a path to a DICOM image;
- a path to a DICOMDIR file;
- a path to a directory with DICOM files.

Each *Scene* object of a slide corresponds to a single series of a study and a
patient. If the path references a DICOMDIR file or a directory with DICOM files,
all images are sorted by series, study and patient, and a collection of scene
objects is created.

### Metadata

The *raw_metadata* property of a *Slide* object always returns an empty string.
The *raw_metadata* property of a *Scene* object returns a JSON representation
of the DICOM tags of the first image of the scene.

### Auxiliary images

Auxiliary images are not supported by the driver.

## NDPI driver

The NDPI driver opens NDPI pathology images created by Hamamatsu slide scanners,
such as the Hamamatsu NanoZoomer.

### Metadata

The *raw_metadata* property of *Slide* and *Scene* objects always returns an
empty string.

### Auxiliary images

The driver supports auxiliary images for *Slide* objects. A slide may contain
the following auxiliary images:

- map
- macro

## VSI driver

The VSI driver opens Olympus VSI slides.

### Metadata

The *raw_metadata* property of a *Slide* returns a JSON representation of the
metadata extracted from the images.

### Auxiliary images

The driver supports auxiliary images for *Slide* objects. A slide may contain
auxiliary images such as:

- overview
- map

## QPTIFF driver

The QPTIFF driver opens PerkinElmer Vectra slides.

### Metadata

The *raw_metadata* property of a *Slide* returns an XML representation of the
metadata extracted from the images.

### Auxiliary images

The driver supports auxiliary images for *Slide* objects.

## OMETIFF driver

The driver opens OME-TIFF slides.

### Metadata

The *raw_metadata* property of a *Scene* returns a JSON representation of the
metadata extracted from the images.

### Auxiliary images

The driver does not support auxiliary images.

## PHTIFF driver

The driver opens Philips TIFF whole slide images produced by Philips IntelliSite
scanners. Philips files use the generic `.tif` and `.tiff` extensions, so the
driver identifies them by the metadata in the description of the first TIFF
directory. A Philips file is therefore recognised by automatic driver selection:
opening a slide with the default driver ID `AUTO` picks PHTIFF, while a plain
TIFF file is still opened by GDAL and an OME-TIFF file by the OMETIFF driver.

A *Slide* object contains a single *Scene* object with the whole slide image.
The zoom levels of the image are matched to TIFF directories by the level number
that each directory declares, and the tile padding that Philips writes at the
right and bottom edge of a level is cropped, so the level sizes are consistent
across the pyramid. The objective magnification of the scene is reported in the
*magnification* property.

### Scene naming

The main image scene is named "Image". Auxiliary images are named after the kind
of image they contain: Thumbnail, Macro or Label.

### Metadata

The *raw_metadata* property of a *Slide* object returns the XML document
extracted from the "Image Description" TIFF tag of the first directory. The
*raw_metadata* property of a *Scene* object returns a JSON representation of the
TIFF tags of the level directory. The *metadata* property of both objects
returns the metadata as a navigable tree.

### Auxiliary images

The driver supports auxiliary images for *Slide* objects. A slide may contain
the following auxiliary images:

- Thumbnail
- Macro
- Label

## MRXS driver

The driver opens 3DHISTECH MIRAX slides scanned by Pannoramic scanners. A MIRAX
slide is a bundle rather than a single file: an entry file `<name>.mrxs` and,
beside it, a directory `<name>` holding `Slidedat.ini`, an index file and the
data files. Open the slide through the `.mrxs` file, or through `Slidedat.ini`
itself, which also opens a bundle whose `.mrxs` file is missing. The extension
is matched in any letter case.

A *Slide* object contains a single *Scene* object: the slide's 8-bit RGB image,
with every zoom level the bundle stores. MIRAX stores the image as overlapping
camera photos; the driver places each photo at its recorded position and
combines the overlaps the way OpenSlide does, so a region read from the scene
closely matches what OpenSlide shows (JPEG tiles can differ slightly in colour,
because the two libraries use different JPEG decoders). Areas without image data take the slide's
background colour. Fluorescence slides are read as their RGB rendering; slides
whose filters are stored in more than one image group, such as five-channel
multiplex scans, are not supported and are reported as such when opened.

### Cropping to the scanned area

A MIRAX slide's nominal canvas is much larger than the area the scanner actually
photographed, and most of it is background. By default the scene is cropped to the
bounding box of the scanned area. That is the same rectangle OpenSlide publishes as
`openslide.bounds-*` and QuPath displays. The scene's coordinates start at the
corner of that box, and every zoom level shrinks to match. The box surrounds every
photographed field, so it is not a tissue outline: two tissue pieces far apart
give one box with background between them.

For the full canvas, with the coordinates and level sizes OpenSlide reports,
open the slide with the `mrxs.crop_to_content` option set to false:

```python
slide = slideio.open_slide("slide.mrxs", "MRXS", {"mrxs.crop_to_content": False})
```

```cpp
auto slide = slideio::openSlide("slide.mrxs", "MRXS", {{"mrxs.crop_to_content", "false"}});
```

The `crop` entry of the `mrxs` metadata branch gives the box's offset and size on
the full canvas, for translating coordinates between the two.

### Scene naming

The scene is named after the slide's data directory, which is the name of the
`.mrxs` file without its extension.

### Metadata

The *raw_metadata* property of the *Slide* and *Scene* objects returns the
`Slidedat.ini` file exactly as written. The *metadata* property returns a tree
with two branches: `ini`, every group and key of `Slidedat.ini`, and `mrxs`,
what the driver derived from them -- zoom levels with their sizes and image
formats, the source of the camera positions, the bounds of the scanned area,
the crop box when the scene is cropped (`crop`), and the layers of the bundle
that are not rendered.

### Auxiliary images

The driver supports auxiliary images for *Slide* objects. A slide may contain
the following auxiliary images:

- Macro
- Label
- Thumbnail

## BIF driver

The driver opens Roche Ventana BIF whole slide images produced by Ventana iScan
(Coreo/HT) and VENTANA DP 200 scanners. A BIF file is a TIFF file whose first
directory carries `iScan` XML metadata; a file without it is refused. The
extension is matched in any letter case.

Each scanned area of interest (AOI) of the slide is a separate *Scene* object,
an 8-bit RGB image with every zoom level the file stores. The scanner records
each AOI as overlapping tiles together with the geometry of every boundary
between them; the driver stitches the tiles with that geometry, as QuPath does.
A file whose image carries no stitching information opens as a single
unstitched scene. The objective magnification of a scene is reported in the
*magnification* property, and the ICC profile embedded by DP 200 scanners is
reported by the scene.

BIF files with more than one focal layer (Z stacks) are not supported yet and
are refused when opened.

### Scene naming

Scenes are named `AOI` followed by the index of the area, `AOI0`, `AOI1` and
so on, in the order the file lists them. Areas that were not scanned are left
out, so the indices are not necessarily consecutive. A scene without stitching
information is named `Image`.

### Metadata

The *raw_metadata* property of a *Slide* object returns the `iScan` XML
document of the first TIFF directory. The *raw_metadata* property of a *Scene*
object returns the XML description of its area of interest. The *metadata*
property of both objects returns the XML as a navigable tree.

### Auxiliary images

The driver supports auxiliary images for *Slide* objects. A slide may contain
the following auxiliary images:

- Label
- Thumbnail
- Probability (DP 200 probability map)

## LIF driver

The driver opens Leica LIF projects written by Leica LAS X. A LIF
file holds a tree of images; each image is exposed as a separate *Scene*
object, and a tile scan gives one scene per field. Tiles are not stitched; a
"Merged" image written by LAS X opens as an ordinary scene. The extension is
matched in any letter case. `.lifext`, LOF and XLIF files are not read.

Scenes hold 8- and 16-bit integer and 16-, 32- and 64-bit floating point
channels, with Z slices and time frames where the image has them. Each scene
has a single level; reads far below native size are downscaled from it in
bounded memory. The resolution, Z and time intervals and the objective
magnification are read from the image description, the number of significant
bits of each channel is reported (for example 12 bits stored in 16-bit
samples), and per-plane timestamps are available when the file records one
for every plane.

An image the driver cannot read, such as a lambda scan or an image with 32- or
64-bit integer samples, is left out of the scene list with a warning instead of
failing the whole project. Scene indices then no longer match the order of the
images in the file; select scenes by name where it matters.

### Scene naming

A scene is named by the path of its image inside the project, with folder
names joined by `/`, for example `TileScan 1/Merged`. The fields of a tile scan
are named `<path>/Field 1`, `<path>/Field 2` and so on.

### Channel attributes

Every attribute of the channel description in the file (`LUTName`,
`ChannelTag`, `Min`, `Max` and others) is reported as a channel attribute. A
channel whose lookup table is red, green, blue, cyan, magenta, yellow or gray
also has a `Color` attribute.

### Metadata

The *raw_metadata* property of a *Slide* object returns the XML document of the
project. The *raw_metadata* property of a *Scene* object returns the XML
element of its image, without the elements of other images. The *metadata*
property of both objects returns the XML as a navigable tree.

### Auxiliary images

The driver does not support auxiliary images.

## ND2 driver

The driver opens Nikon ND2 files written by NIS-Elements: chunked files
(versions 2 and 3) and legacy JPEG 2000 files, including legacy files with 9- to
15-bit codestreams. The extension is matched in any letter case.

Each XY position of the experiment is a separate *Scene* object, with the Z
slices and time frames taken from the experiment loops. Scenes hold 8- and
16-bit integer and 32-bit floating point channels; every component is a
channel of its own, so an RGB acquisition gives three channels. Each scene has
a single level; reads far below native size are downscaled from it in bounded
memory. The pixel size, the Z and time intervals and the objective
magnification are reported, the magnification being parsed from the objective
name (`60x`) where the file states no number. Per-plane timestamps are
available when every frame records one. The number of time frames matches the
frames actually present in the file, and missing frames read as background.

A file whose chunk map is missing or out of date, as left by an interrupted
acquisition, is recovered by scanning the file, with a warning. Files with
lossy compression, tiled frames or more than one time loop are refused.

### Scene naming

A scene is named after its XY position as named in the file, or `Position 1`,
`Position 2` and so on for unnamed positions; a duplicated name gets the
position number appended. A file without an XY loop has a single scene named
after the file.

### Channel attributes

Each channel is named after its description in the file; the components of an
RGB channel are named `<name> R`, `<name> G` and `<name> B`. The channel
attributes are `Color` (`#RRGGBB`), `ND2Channel`, `Component` and
`FluorescentProbe`.

### Metadata

The *raw_metadata* property of a *Slide* object returns a JSON document with
the image attributes, metadata, text information and calibration records of the
file. The *raw_metadata* property of a *Scene* object returns the JSON record of
its XY position. The *metadata* property of both objects returns the JSON as a
navigable tree.

### Auxiliary images

The driver does not support auxiliary images.
