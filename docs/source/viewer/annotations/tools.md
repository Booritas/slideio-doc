# Drawing tools

Choose a tool from the **Tools** menu or press its key while the slide view has
focus. The checked item in the Tools menu is the active tool.

| Tool | Key | Draws |
|---|---|---|
| Navigate | {kbd}`V` | Nothing: pans, selects and edits |
| Rectangle | {kbd}`R` | A rectangle or square |
| Ellipse | {kbd}`E` | An ellipse or circle |
| Polygon | {kbd}`P` | A closed outline, clicked or traced |
| Freehand Line | {kbd}`F` | An open line, clicked or traced |
| Point Marker | {kbd}`M` | A point, for counting |
| Arrow | {kbd}`A` | An arrow from tail to head |
| Text | {kbd}`T` | A line of text on the slide |
| Ruler | {kbd}`L` | A distance measurement |
| Angle | {kbd}`G` | An angle measurement |

The tool keys work only while the slide view has keyboard focus, so typing in a
pane's text field never switches tools. If a key seems to do nothing, click the
slide first.

## What all tools have in common

- **The tool stays active.** After you draw a shape you can draw the next one
  straight away. Press {kbd}`V` to go back to Navigate.
- **The new annotation is selected**, so you can set its label, classification
  and colour in the [Annotation Properties pane](list-and-properties.md#annotation-properties-pane).
- **It goes on the active layer**, shown in the status bar as `Layer: ...`. If
  that layer is hidden or locked, nothing is drawn and the status bar says so;
  choose another layer in the [Layers pane](layers.md).
- **New annotations look the same:** orange (#E67E22), a 2-pixel line and 30 %
  fill. Change the look afterwards in the properties pane.
- **While you draw**, a dashed orange preview shows the shape.
- **{kbd}`Esc` cancels** the shape being drawn.
- **You can pan without switching tools:** drag with the middle mouse button,
  or hold {kbd}`Space` and drag. The mouse wheel zooms as usual.
- **A click without dragging selects.** With the Rectangle, Ellipse, Arrow or
  Ruler tool, a press and release that moves less than 6 screen pixels draws
  nothing: it selects the annotation under the pointer, or clears the
  selection on empty slide. A real drag always draws a new shape, even when it
  starts on an existing annotation.

The drawing tools are unavailable, and greyed out in the menu, when no slide is
open, when an associated image is shown, and when the slide's annotations are
[read-only](saving.md#read-only-annotations).

## Rectangle and Ellipse

Press where the shape should start, drag, and release.

| Hold | Effect |
|---|---|
| {kbd}`Shift` | A square or circle, sized by the larger side of the drag |
| {kbd}`Alt` | Draw from the centre: the press point is the centre |
| {kbd}`Shift+Alt` | A square or circle centred on the press point |

The modifiers are read while the mouse moves, so what the preview shows is what
you get.

## Polygon

A polygon is a closed outline. Build it from clicks, from traced strokes, or a
mix of both:

- **Click** to add a corner.
- **Press and drag** to trace: the outline follows the pointer. Releasing the
  button does not finish the polygon, so you can continue with clicks or
  another stroke.

While you draw, a line follows the pointer from the last point, and a dotted
line shows how the outline will close.

Finish the polygon, once it has at least three points, in any of these ways:

- **double-click** (the first click of the double-click adds the last point);
- press {kbd}`Enter`;
- click the **first point** again; an orange dot appears on it when the
  pointer is close enough.

While drawing:

- {kbd}`Backspace` removes the last point, as does {kbd}`Ctrl+Z`;
- {kbd}`Esc` discards the whole polygon, and so does switching tools.

The status bar reminds you: "Click to add points, double-click or Enter to
finish, Esc to cancel".

## Freehand Line

A freehand line is an open line: it is never closed or filled. It is drawn
exactly like a polygon, and needs at least two points. Clicking the first point
does not close it; finish with a double-click or {kbd}`Enter`.

## Point Marker

Click to place a point. The tool stays active for the next one, so you can
click cell after cell.

Each new marker is given the **counting category** chosen in the Annotation
List, so the markers are counted per category as you place them. See
[Counting with point markers](categories.md#counting-with-point-markers).

## Arrow

Press at the tail, drag, and release at the head. The arrowhead is drawn at the
end where you released.

## Text

Click where the text should go. A text box opens; type a line of text and press
{kbd}`Enter`. The text is drawn next to a small anchor dot at the point you
clicked.

- {kbd}`Enter`, or clicking elsewhere, keeps the text.
- {kbd}`Esc` discards it.
- An empty text box creates nothing.

Clicking an existing text with the Text tool opens it for editing instead of
placing a new one. Clicking another shape places a new text there, which is a
quick way to label a region.

Text is a single line, in a fixed size on screen.

## Ruler

Press at one end, drag, and release at the other end. The length is shown next
to the ruler while you drag and stays on the slide afterwards. See
[Measurements](measurements.md).

## Angle

An angle is drawn in two steps:

1. Press at the **vertex** (the corner of the angle), drag along the first
   arm, and release.
2. Move the pointer to place the second arm; the angle in degrees follows the
   pointer. **Click** to fix it.

{kbd}`Esc`, {kbd}`Ctrl+Z` or switching tools discards a half-drawn angle.

## Minimum sizes

To avoid creating shapes by accident, a drag must be at least 6 screen pixels
long for a rectangle, ellipse, arrow, ruler or the first arm of an angle.
Zoom in to draw very small shapes.
