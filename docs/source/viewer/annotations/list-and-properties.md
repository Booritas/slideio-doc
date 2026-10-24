# Annotation List and Properties

Two panes show the annotations of the scene on screen: the **Annotation List**
({kbd}`Ctrl+Shift+L`) and **Annotation Properties** ({kbd}`Ctrl+Shift+E`).
Open them from the **View** menu.

## Annotation List pane

% SCREENSHOT: annotation-list.png — the Annotation List with the counting
% combo, the tally, the filter and a few rows.

The pane title shows how many annotations the scene has, for example
"Annotations (12)", or "Annotations (8 of 12)" when some are hidden by a filter
or on hidden layers.

From top to bottom, the pane contains:

1. **Counting:** the category given to new point markers. See
   [Counting with point markers](categories.md#counting-with-point-markers).
2. **The tally:** how many annotations carry each category. See
   [The tally](categories.md#the-tally).
3. **Filter** box and **sort** order.
4. **The list** of annotations, one row each.

### The list

| Column | Shows |
|---|---|
| Label | The annotation's label. Annotations without one are called by their type and number, such as "Rectangle 3". For text annotations the label is the text. |
| Type | Rectangle, Ellipse, Polygon, Freehand Line, Point, Arrow, Text, Ruler or Angle. "(locked)" is added for annotations on a locked layer. |
| Classification | The annotation's category, or empty. |

Annotations on hidden layers are not listed.

- **Click** a row to select the annotation on the slide.
- **Double-click** a row to zoom to the annotation.
- Press {kbd}`Delete` to delete the selected annotation.
- **Right-click** a row for **Move to Layer**.

Selecting an annotation on the slide highlights its row and scrolls it into
view.

### Filter and sort

Type in **Filter by label or classification** to list only the annotations
whose label or classification contains the text, ignoring case. The tally is
not affected by the filter.

The sort box orders the list by **Creation order**, **Label**,
**Classification**, **Type** or **Last modified** (newest first). Clicking a
column header does not sort.

## Annotation Properties pane

% SCREENSHOT: annotation-properties.png — the Annotation Properties pane for
% a polygon on a calibrated slide.

The Properties pane shows the selected annotation.

### Fields you can edit

| Field | Description | Applied when |
|---|---|---|
| Label | A name for the annotation. For text annotations, the text itself. | You press {kbd}`Enter` or leave the field |
| Classification | Pick a category from the list or type one. Typing "Unclassified" clears it. | You pick an item, or press {kbd}`Enter` / leave the field |
| Colour | Click the swatch to choose a colour | You close the colour dialog with OK |
| Line width | 1 to 5 screen pixels | Immediately |
| Fill opacity | How strongly closed shapes are filled, from transparent to solid | You release the slider |
| Notes | Free text, several lines | You leave the field |

Each change is one undo step, such as "Undo Recolour annotation".

The fields are greyed out when nothing is selected, when the annotation is on a
locked layer, and when the slide's annotations are read-only.

Typing a new classification here does not add it to the category list; it
appears in the tally as an extra row. Add categories in
[Preferences](categories.md#managing-the-category-list).

### Information shown

| Row | Shows |
|---|---|
| Type | The kind of annotation |
| Author | Who drew it (the name in Preferences) |
| Created, Modified | Date and time in UTC, for example `2026-10-24T09:15:00Z` |
| Area, Perimeter | For rectangles, ellipses and polygons |
| Length | For lines, arrows and rulers |
| Angle | For angles |

Under the measurements, an amber note says **manual calibration** when you
entered the pixel size yourself, or **uncalibrated** when no pixel size is
known. Hover over it for details. See [Measurements](measurements.md).
