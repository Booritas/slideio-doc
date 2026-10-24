# Opening slides

## Open a slide file

Choose **File > Open Slide...** ({kbd}`Ctrl+O`) and pick the file.

The file-type list at the bottom of the dialog decides how the file is read:

- **All Supported Slides** (the default) shows every supported file and lets
  the viewer detect the format from the file's contents.
- A **format entry**, such as "Aperio SVS" or "Carl Zeiss CZI", shows only that
  format's files and reads the chosen file with that format's driver. Use one
  only when automatic detection picks the wrong reader.
- **All Files** shows every file and detects the format automatically.

| Entry | Extensions |
|---|---|
| Aperio FluoroImage | `*.afi` |
| Carl Zeiss CZI | `*.czi` |
| DICOM | `*.dcm` |
| Generic (GDAL) | `*.tif *.tiff *.png *.jpg *.jpeg *.gif *.bmp` |
| Hamamatsu NDPI | `*.ndpi` |
| OME-TIFF | `*.ome.tif *.ome.tiff` |
| PerkinElmer QPTIFF | `*.qptiff` |
| Leica SCN | `*.scn` |
| Aperio SVS | `*.svs` |
| Olympus VSI | `*.vsi` |
| Carl Zeiss ZVI | `*.zvi` |

Philips TIFF slides have no entry of their own: open them through **All
Supported Slides**, which recognises them by their contents.

## Open a DICOM study

A DICOM whole-slide image is usually a folder of files. Choose **File > Open
DICOM Folder...** ({kbd}`Ctrl+Shift+O`) and pick the folder. A single `.dcm`
file can also be opened with **File > Open Slide...**.

## Drag and drop

Drop a slide file, or a DICOM folder, onto the window to open it. Files the
viewer cannot open show a "no entry" cursor while you drag them. If you drop
several files, the first one that can be opened is opened.

Dropping an annotation file does not import it; use
[File > Import Annotations...](annotations/import-export.md#importing-annotations).

## Recent files

**File > Recent Files** lists the last ten slides and DICOM folders you opened,
newest first. Hover over an entry to see its full path in the status bar.
**Clear Recent Files** at the bottom empties the list.

## While a slide loads

Slides open in the background. While one loads, the slide view is dimmed and
shows a spinner with "Loading" and the slide's name; the menus stay usable. To
stop a load that takes too long, choose **File > Close**.

If the viewer finds damaged tiles in a zoom level, it says "Working around
corrupted tiles" under the spinner while it adapts to them.

When the slide is open, it is shown whole (fit to the window). A Z-stack opens
on its middle slice.

If a slide cannot be opened, an error box shows the reason reported by the
reader, and the viewer is left empty.

## Scenes and associated images

Some files hold several images. A **scene** is one scanned image of the file,
for example one region of a CZI slide. **Associated images** are the small
pictures stored with the slide, such as the label, the macro photograph and
the thumbnail. The viewer opens the first scene; switch scenes and view the
associated images in the [Scenes and Associated Images panes](panes.md).

## Close a slide

**File > Close** ({kbd}`Ctrl+W`) closes the slide. Annotation changes are
saved first; nothing else needs saving.

## Several slides at once

Each SlideIO Viewer window shows one slide. To compare two slides, start the
viewer a second time. Both windows share the same preferences.

If the same slide is open in two windows, only the first one can change its
annotations; the second shows them read-only. See
[Saving annotations](annotations/saving.md#the-same-slide-in-two-windows).
