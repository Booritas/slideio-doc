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

Three drivers accept `*.tif` and `*.tiff`: GDAL, OMETIFF and PHTIFF. They are
told apart by the content of the file, so opening a slide with the default
`AUTO` driver picks the right one. Name a driver explicitly only to override
that.

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
