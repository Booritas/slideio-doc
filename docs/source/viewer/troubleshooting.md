# Troubleshooting

## The viewer does not start, or the slide view stays black

The viewer needs a graphics card with OpenGL 3.3. Update the graphics driver.
On a virtual machine or remote desktop, enable 3D acceleration. The **System**
tab of **Help > About SlideIO Viewer...** shows the OpenGL version the viewer
found.

## A slide does not open

The error box shows the reason given by the reader. Try:

- choosing the format explicitly in the file-type list of **File > Open
  Slide...**;
- for a DICOM study, **File > Open DICOM Folder...** on the study folder;
- checking the slide with the Python module or `slideio-tiffinspector`
  ([Command line tools](../tools/index.md)).

Details are in the log: **File > Open Log File**.

## Keyboard shortcuts do nothing

The tool keys, the arrow keys and {kbd}`+` / {kbd}`-` act only while the slide
view has keyboard focus. Click the slide, then try again.

## The drawing tools are greyed out

- No slide is open, or an associated image is shown.
- The annotations are read-only: the status bar shows **Annotations
  disabled**; hover over it for the reason. See
  [Read-only annotations](annotations/saving.md#read-only-annotations).

If the tools are available but nothing is drawn, the active layer is hidden or
locked; the status bar says which. Choose another layer in the
[Layers pane](annotations/layers.md).

## "Your name is needed"

Annotations record who created them. Enter your name in **Tools >
Preferences...**.

## My annotations are gone

- **Another workspace.** Check the annotation workspace in Preferences. Files
  are never moved when you change it; switch back to the old folder to see
  them.
- **The slide was modified.** A re-compressed, anonymised or re-saved slide is
  a different slide to the viewer. Its old annotations are still in the
  workspace's `annotations` folder.
- **Another scene.** Each scene has its own annotations; check the
  [Scenes pane](panes.md#scenes).
- **A hidden layer.** Hidden layers' annotations are not drawn or listed; check
  the [Layers pane](annotations/layers.md).

## Measurements are in pixels

The slide does not record its pixel size. Enter it with **View >
Calibration...**; see [Calibration](annotations/measurements.md#calibration).

## Colour management is greyed out

It applies only to RGB brightfield slides that have an ICC profile. Hover over
the menu item for the reason; see [Colour management](color-management.md).

## The slide disappeared off the screen

Press {kbd}`Ctrl+0` to fit it back into the window.

## Reporting a problem

Report bugs on the
[issue tracker](https://github.com/Booritas/slideio-view/issues). Include the
text from **Help > About SlideIO Viewer... > Copy to Clipboard** and the
relevant part of the log file (**File > Open Log File**).
