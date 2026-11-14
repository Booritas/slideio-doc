# Supported formats

SlideIO reads the following formats. Every component reads all of them: the
C++ library, the Python package, the command line tools and SlideIO Viewer.
Each format is handled by an image driver, named in the last column; the
default `AUTO` driver picks the right one from the file, so naming a driver is
only needed to override that choice.

| Format | File extensions | Developer | Scanners and software | Driver |
|---|---|---|---|---|
| [Aperio SVS](https://www.leicabiosystems.com/en-de/digital-pathology/manage/aperio-imagescope/) | `*.svs` | [Leica Microsystems](https://www.leicabiosystems.com/) | [Aperio GT 450 and Aperio GT 450 DX](https://www.leicabiosystems.com/en-de/digital-pathology/scan/) | SVS |
| [Aperio AFI](https://www.pathologynews.com/fileformats/leica-afi/) (fluorescence) | `*.afi` | [Leica Microsystems](https://www.leicabiosystems.com/) | | AFI |
| [3DHISTECH MIRAX](https://openslide.org/formats/mirax/) | `*.mrxs`, `Slidedat.ini` | [3DHISTECH](https://www.3dhistech.com/) | Pannoramic scanners | MRXS |
| DICOM, including whole slide images | `*.dcm`, no extension | | | DCM |
| [Hamamatsu NDPI](https://www.hamamatsu.com/eu/en/product/life-science-and-medical-systems/digital-slide-scanner/U12388-01.html) | `*.ndpi` | [Hamamatsu](https://www.hamamatsu.com/eu/en.html) | NanoZoomer | NDPI |
| Leica SCN | `*.scn` | [Leica Microsystems](https://www.leicabiosystems.com/) | [Leica SCN400](https://www.leicabiosystems.com/en-de/news-events/leica-microsystems-launches-scn400-f-combined-fluorescence-and-brightfield-slide/) | SCN |
| Leica LIF | `*.lif` | [Leica Microsystems](https://www.leica-microsystems.com/) | Leica LAS X | LIF |
| Nikon ND2 | `*.nd2` | [Nikon](https://www.microscope.healthcare.nikon.com/) | NIS-Elements | ND2 |
| Olympus VSI | `*.vsi` | Olympus | | VSI |
| [OME-TIFF](https://docs.openmicroscopy.org/ome-model/5.6.3/ome-tiff/) | `*.ome.tif`, `*.ome.tiff`, `*.ome.tf2`, `*.ome.tf8`, `*.ome.btf` | [Open Microscopy Environment](https://www.openmicroscopy.org/) | | OMETIFF |
| PerkinElmer Vectra QPTIFF | `*.qptiff` | [Akoya Biosciences](https://www.akoyabio.com/software-data-analysis/) | [Vectra](https://www.akoyabio.com/phenoimager/instruments/vectra-3-0/) | QPTIFF |
| Philips TIFF | `*.tif`, `*.tiff` | [Philips](https://www.philips.com/) | [Philips IntelliSite Pathology Solution](https://www.usa.philips.com/healthcare/resources/landing/philips-intellisite-pathology-solution) | PHTIFF |
| [Roche Ventana BIF](https://diagnostics.roche.com/global/en/products/instruments/ventana-dp-200-ins-2575.html) | `*.bif` | [Roche Diagnostics](https://diagnostics.roche.com/) | Ventana iScan Coreo/HT, [VENTANA DP 200](https://diagnostics.roche.com/global/en/products/instruments/ventana-dp-200-ins-2575.html) | BIF |
| [Zeiss CZI](https://www.zeiss.com/microscopy/en/products/software/zeiss-zen/czi-image-file-format.html) | `*.czi` | [Zeiss Microscopy](https://www.zeiss.com/microscopy/en/home.html) | [ZEISS Axioscan 7](https://www.zeiss.com/microscopy/en/products/imaging-systems/axioscan-for-biology.html) | CZI |
| Zeiss ZVI | `*.zvi` | [Zeiss Microscopy](https://www.zeiss.com/microscopy/en/home.html) | AxioVision | ZVI |
| General images: TIFF, PNG, JPEG, BMP, GIF, JPEG 2000 | `*.tif`, `*.tiff`, `*.png`, `*.jpg`, `*.jpeg`, `*.bmp`, `*.gif`, `*.gtiff`, `*.gtif`, `*.ntif`, `*.jp2` | | | GDAL |

## Scenes, Z stacks and time frames

| Format | Multiple scenes | Z stacks | Time frames |
|---|---|---|---|
| Aperio SVS | yes | no | no |
| Aperio AFI | yes | no | no |
| 3DHISTECH MIRAX | no | no | no |
| DICOM | yes | yes | no |
| Hamamatsu NDPI | no | no | no |
| Leica SCN | yes | no | no |
| Leica LIF | yes | yes | yes |
| Nikon ND2 | yes | yes | yes |
| Olympus VSI | yes | yes | yes |
| OME-TIFF | yes | yes | yes |
| PerkinElmer QPTIFF | yes | yes | yes |
| Philips TIFF | no | no | no |
| Roche Ventana BIF | yes | no | no |
| Zeiss CZI | yes | yes | yes |
| Zeiss ZVI | no | yes | no |
| General images | no | no | no |

## Notes

- **TIFF files.** Philips TIFF, OME-TIFF and general TIFF images share the
  `*.tif` and `*.tiff` extensions. They are told apart by the content of the
  file.
- **MIRAX bundles.** A MIRAX slide is a `.mrxs` file plus a data directory of
  the same name beside it. Open the `.mrxs` file, or the `Slidedat.ini` inside
  the data directory when the `.mrxs` file is missing.
- **DICOM.** A DICOM slide can be opened as a single file, a `DICOMDIR` file or
  a directory of DICOM files.
- **Writing.** SlideIO reads all of the formats above. It writes two: the
  converter produces tiled pyramidal SVS and OME-TIFF files.

[Image drivers](../drivers.md) describes what each driver exposes: scene
naming, metadata and auxiliary images.
