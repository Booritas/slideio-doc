# Selecting and editing annotations

Editing on the slide is done with the **Navigate** tool ({kbd}`V`).

## Selecting

- **Click** an annotation to select it. Click empty slide to clear the
  selection.
- **Click a row** in the [Annotation List](list-and-properties.md) to select
  its annotation; **double-click** the row to zoom to it.

Only one annotation is selected at a time. The selected annotation is outlined
with a dashed black-and-white line; a selected point gets a ring, a selected
text a frame.

A click hits an annotation when it lands inside a closed shape or within 6
screen pixels of its outline, line or point. Where annotations overlap, the
one on top is picked: annotations on higher layers are on top, and within a
layer, newer annotations are on top of older ones. Annotations on hidden layers
cannot be selected.

Annotations on a [locked layer](layers.md#hide-lock-and-fade-layers) can be
selected, but not changed.

## Moving

Drag a selected or unselected annotation with the Navigate tool to move it. The
annotation starts moving once the pointer has travelled 6 screen pixels, so a
plain click never moves it. Press {kbd}`Esc` during the drag to put it back.

Every kind of annotation can be moved. The arrow keys pan the view; they do not
move annotations.

## Resizing rectangles and ellipses

Select a rectangle or ellipse with the Navigate tool: eight square handles
appear, on the corners and the middle of each side. Drag a handle to resize the
shape. Dragging past the opposite side flips the shape. {kbd}`Esc` during the
drag restores it.

Other shapes have no resize handles. To change the end points of an arrow,
ruler or angle, delete it and draw it again.

## Editing the points of a polygon or freehand line

**Double-click** a polygon or freehand line with the Navigate tool. A handle
appears on every point.

| To | Do |
|---|---|
| Move a point | Drag its handle |
| Add a point | Press on the outline between two points, and drag to place it |
| Remove a point | {kbd}`Ctrl`+click its handle |
| Cancel a drag | {kbd}`Esc` while dragging |
| Finish editing | {kbd}`Esc`, or click away from the shape |

A polygon keeps at least three points, and a freehand line at least two.

## Editing text

To change the words of a text annotation, do one of these:

- double-click it with the Navigate tool;
- click it with the Text tool;
- edit its **Label** in the Annotation Properties pane: the label of a text
  annotation is its text.

The words are selected when the text box opens, so you can type over them.
{kbd}`Enter` keeps the change, {kbd}`Esc` drops it. To remove a text
annotation, delete it; emptying the box keeps the old words.

## Changing colour, line width and other properties

Select the annotation and edit it in the
[Annotation Properties pane](list-and-properties.md#annotation-properties-pane):
label, classification, colour, line width, fill opacity and notes.

## Deleting

Select the annotation and press {kbd}`Delete`, with either the slide view or the
Annotation List focused. {kbd}`Backspace` does not delete annotations.

## Moving to another layer

Select the annotation and choose **Edit > Move to Layer**, or right-click its
row in the Annotation List and choose **Move to Layer**. See
[Layers](layers.md#moving-annotations-between-layers).

## Undo and redo

**Edit > Undo** ({kbd}`Ctrl+Z`) and **Edit > Redo** ({kbd}`Ctrl+Shift+Z`,
or {kbd}`Ctrl+Y` on Windows) step through the last 50 changes. On macOS use
{kbd}`Cmd` in place of {kbd}`Ctrl`. The menu names the step, such as "Undo Move Rectangle", and the status
bar confirms what was undone.

These changes can be undone:

- drawing, moving, resizing, editing points, deleting;
- editing text and properties (label, classification, colour, line width, fill
  opacity, notes);
- moving annotations to another layer and merging layers;
- renaming a category on the annotations that use it;
- importing annotations.

While you are drawing a polygon or freehand line, {kbd}`Ctrl+Z` removes the
last point instead.

These cannot be undone: creating, renaming, deleting, reordering, hiding,
locking and fading layers; changes to the category list; calibration.

The undo history belongs to the scene on screen. It is cleared when you open
another slide or scene, or change the annotation workspace.

When the cursor is in a text field, such as a properties field or the metadata
filter, {kbd}`Ctrl+Z` undoes typing in that field instead.

## Not available

These common editing features are not available yet: selecting several
annotations at once, copy and paste, duplicating, rotating, and nudging with the
arrow keys.
