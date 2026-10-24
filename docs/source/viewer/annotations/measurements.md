# Measurements

## What is measured

| Annotation | Measurement | Where it is shown |
|---|---|---|
| Ruler | Length | On the slide, and in the Annotation Properties pane |
| Angle | Angle in degrees | On the slide, and in the Annotation Properties pane |
| Rectangle, Ellipse, Polygon | Area and perimeter | Annotation Properties pane |
| Freehand Line, Arrow | Length | Annotation Properties pane |

All measurements are also written by
[File > Export Measurements...](import-export.md#measurements-csv).

## On the slide

Rulers and angles carry a label with their value, drawn in the annotation's
colour on a white plate. The ruler's label sits beside the middle of the line;
the angle's label sits outside the angle, at its vertex. Labels keep the same
size at every zoom, and are shown live while you draw.

## Units and precision

When the slide is [calibrated](#calibration):

- lengths are given to three significant figures in micrometres (`123 µm`),
  switching to millimetres from 1000 µm (`1.25 mm`);
- areas in µm², switching to mm² from 1,000,000 µm².

When it is not, lengths and areas are whole pixels (`542 px`, `px²`), and the
ruler and angle labels show a warning icon.

Angles are given in degrees with one decimal (`37.5°`), from 0 to 180°. On a
slide whose pixels are not square, the angle is computed in real distances, so
it can differ slightly from the angle as it appears on screen.

The area of a polygon whose outline crosses itself cannot be computed; it is
shown as "unavailable (self-intersecting)".

## Calibration

Converting pixels to micrometres needs the size of a pixel. Most scanners
record it in the slide, and the viewer uses it automatically. When a slide does
not record it, or records it wrongly, enter it yourself.

When you open a slide without a pixel size, the status bar says: "This slide
has no calibration — measurements are in pixels."

### Set the pixel size

Choose **View > Calibration...**. The dialog shows the size recorded in the
slide ("From the slide's metadata"), or "none".

```{figure} ../../_static/calibration-dialog.webp
:alt: The Calibration dialog

The Calibration dialog for a slide that records its pixel size.
```

1. Enter the **Pixel width** in µm per pixel.
2. Leave **Square pixels** ticked if the pixel is as tall as it is wide;
   untick it to enter a different **Pixel height**.
3. Click **OK**.

The value must be between 0.01 and 100 µm per pixel. The new calibration
applies at once to every measurement, label, the scale bar and exports.

**Reset to metadata** removes your value and goes back to the one recorded in
the slide.

The calibration is stored for this scene of this slide on this computer. It is
not saved in the annotation files, and it cannot be undone with Edit > Undo.

### Seeing where the calibration comes from

| Where | Slide's own value | Your value | No value |
|---|---|---|---|
| Properties pane, Calibration row | `metadata, x × y µm/px` | `manual, x × y µm/px` | `none` |
| Scale bar | the length | the length + "(manual)" | Uncalibrated |
| Ruler and angle labels | the value | the value + "(manual)" | value in pixels with a warning icon |
| Annotation Properties pane | — | "manual calibration" | "uncalibrated" |
| Exports | `metadata` | `manual` | `none` |
