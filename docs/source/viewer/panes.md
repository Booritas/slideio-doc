# Slide panes

Open and close the panes from the **View** menu. Each pane remembers where you
docked it.

| Pane | View menu | Shortcut |
|---|---|---|
| [Channels](channels.md) | Channels | {kbd}`Ctrl+Shift+C` |
| [Scenes](#scenes) | Scenes | {kbd}`Ctrl+Shift+T` |
| [Associated Images](#associated-images) | Associated Images | {kbd}`Ctrl+Shift+A` |
| [Properties](#properties) | Properties | {kbd}`Ctrl+Shift+P` |
| [Metadata](#metadata) | Metadata | {kbd}`Ctrl+Shift+D` |
| [Annotation List](annotations/list-and-properties.md) | Annotation List | {kbd}`Ctrl+Shift+L` |
| [Annotation Properties](annotations/list-and-properties.md#annotation-properties-pane) | Annotation Properties | {kbd}`Ctrl+Shift+E` |
| [Layers](annotations/layers.md) | Layers | {kbd}`Ctrl+Shift+Y` |

## Scenes

```{figure} ../_static/scenes-pane.webp
:alt: The Scenes pane

The Scenes pane for a Leica SCN file with several scenes. The scene on
screen has a blue border.
```

The Scenes pane shows a thumbnail of every scene in the file, with its name, or
"Scene 1", "Scene 2" ... when the file gives none. The scene on screen has a
blue border. Click another thumbnail to open that scene; it is shown whole.

Thumbnails load in the background. A scene without a downsampled zoom level
keeps a grey placeholder.

Each scene has its own annotations, and switching scenes clears the undo
history.

## Associated images

The Associated Images pane shows the extra pictures stored in the slide, such
as the label, the macro photograph and the thumbnail, under the names the file
gives them. Click one to open it at full size in a separate window. You can
open several, and close them one by one; the slide stays as it was.

Associated images are for viewing only: they cannot be annotated.

## Properties

The Properties pane summarises the open scene:

| Property | Meaning |
|---|---|
| File name, File path | The slide file |
| Driver | The SlideIO driver that reads the file, such as `SVS` |
| Pixel type | Data type of a sample, such as `uint8` or `uint16` |
| Magnification | Objective magnification recorded by the scanner |
| Width (pixels), Height (pixels) | Size of the scene at full resolution |
| Width (µm), Height (µm) | Physical size, when the pixel size is known |
| Pixel width (µm), Pixel height (µm) | Size of one pixel as recorded in the slide |
| Channels, Z-slices, Time frames | Dimensions of the scene |
| Compression | How the image data is compressed, such as JPEG or JPEG 2000 |
| Uncompressed size | Width × height × channels × slices × frames × bytes per sample |
| Pyramid levels | Number of zoom levels stored in the file |
| Levels | One row per zoom level: size, scale, tile size and tile count. Expand it to see them. |
| Color profile | The ICC profile in use. See [Colour management](color-management.md#what-the-properties-pane-shows). |
| Calibration | The pixel size measurements use and where it comes from: `metadata`, `manual`, or `none`. See [Calibration](annotations/measurements.md#calibration). |

Right-click the pane and choose **Copy properties as text** to copy everything
to the clipboard.

## Metadata

The Metadata pane shows everything the file records about the slide, in three
groups: **Slide**, **Scene** and **Channels**. Expand an entry to see what it
contains.

Type in the **Filter...** box to show only entries whose name or value contains
the text, ignoring case. The tree expands to show every match; clear the box to
collapse it again.

Right-click the pane to copy the whole tree, either as indented text (**Copy
metadata as text**) or as JSON (**Copy metadata as JSON**).

In the Channels group, channels are numbered from 0.
