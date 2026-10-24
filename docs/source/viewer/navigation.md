# Navigating a slide

## Zoom

| To | Do |
|---|---|
| Zoom in or out at the mouse pointer | Turn the mouse wheel. Each notch zooms by 10 %. |
| Zoom in or out at the centre of the view | {kbd}`Ctrl++` / {kbd}`Ctrl+-`, or {kbd}`+` / {kbd}`-` when the slide view has focus |
| Show the whole slide | **View > Fit to Window**, {kbd}`Ctrl+0` |
| Show one screen pixel per slide pixel | **View > Actual Pixels**, {kbd}`Ctrl+1`. The view is centred on the slide. |
| Jump to any zoom | Drag the zoom slider in the bottom-left corner |

Zoom ranges from 0.1 % to 10,000 % of the slide's full resolution. Beyond
100 % the viewer enlarges the full-resolution pixels.

## Pan

| To | Do |
|---|---|
| Pan | Drag with the left mouse button on an empty part of the slide, with the **Navigate** tool ({kbd}`V`) |
| Pan with any tool | Drag with the middle mouse button, or hold {kbd}`Space` and drag with the left button |
| Pan in steps | Arrow keys, 20 screen pixels per press |
| Jump to a region | Click or drag in the minimap |

When a drawing tool is active, the left button draws; use {kbd}`Space` or the
middle button to pan without switching tools.

The slide view takes keyboard focus whenever a slide opens. If the arrow keys
or the single-letter tool shortcuts do nothing, click the slide first.

If you lose the slide off the edge of the view, press {kbd}`Ctrl+0` to bring it
back.

## Full screen

**View > Full Screen** ({kbd}`F11`) fills the screen with the viewer window.
Press {kbd}`F11` again to leave full screen.

## Minimap

The minimap in the top-right corner shows the whole slide with the visible area
outlined in red. Click a point in it, or drag in it, to centre the view there.
Toggle it with **View > Minimap** ({kbd}`Ctrl+M`); it is shown each time the
viewer starts.

Slides without a downsampled zoom level have no overview picture, and the
minimap says "Overview unavailable".

## Magnification and zoom

The zoom indicator in the bottom-left corner shows two numbers:

- the **magnification**, such as `20.0x`: the zoom multiplied by the
  objective magnification recorded in the slide, so that `40.0x` on a 40×
  scan is full resolution;
- the **zoom**, such as `50.0%`: the size of a slide pixel on the screen, where
  100 % is one screen pixel per slide pixel.

Slides that do not record an objective magnification show only the
percentage. The same values appear in the status bar.

## Scale bar

Under the magnification, the scale bar shows a length on the slide at the
current zoom. Its length is picked from the series 1, 2, 5, 10, 20, 50 ... µm so
that it fits the indicator; the value is always given in micrometres.

The scale bar needs to know the size of a pixel. If the slide does not record
it, the indicator shows a warning icon and **Uncalibrated** instead of a bar.
You can enter the pixel size yourself with **View > Calibration...**; the bar
then shows "(manual)" after its length. See
[Calibration](annotations/measurements.md#calibration).

## Mouse position

The status bar shows the position under the mouse pointer as `X` and `Y` in
full-resolution slide pixels, counted from the top-left corner of the scene.

## Z-stacks and time series

Slides with more than one Z slice or time frame show the **Z/T navigator** in
the top-left corner of the slide view, with a slider for each dimension that
has more than one plane:

- **Z** selects the focal plane. A Z-stack opens on its middle slice.
- **T** selects the time frame. A time series opens on the first frame.

The number on the right of each slider is the current plane, counted from 1.
The previous image stays on screen while the new plane loads.
