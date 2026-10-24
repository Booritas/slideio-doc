# Importing and exporting

| Command (File menu) | Reads or writes | Format |
|---|---|---|
| Import Annotations... | Annotations from QuPath, ASAP or SlideIO Viewer | GeoJSON, ASAP XML |
| Export Annotations as GeoJSON... | All annotations of the scene | GeoJSON |
| Export Counts... | The tally of categories | CSV |
| Export Measurements... | One row of measurements per annotation | CSV |

All four work on the scene on screen. Exports include every annotation of the
scene, on every layer, hidden ones too, regardless of the list filter. They are
available for read-only annotations as well, but not when the annotations
could not be loaded.

## Importing annotations

1. Make the layer the annotations should go on active in the
   [Layers pane](layers.md#the-active-layer). It must be visible and unlocked.
2. Choose **File > Import Annotations...** and pick the file.
3. Read the summary and click **Import**.

The format is recognised from the file's contents, whatever its extension.

% SCREENSHOT: import-summary.png — the import confirmation with a few
% skipped items and a warning.

The summary says how many annotations will be added and what is skipped and
why. It warns when the file was exported from a different slide or scene, and
when annotations lie entirely outside the scene; usually a sign that the file
belongs to another slide.

An import only adds annotations. Annotations already in the scene, recognised
by their identifier, are skipped, so importing the same file twice, or
re-importing your own export, adds nothing the second time. The import is one
undo step: **Edit > Undo Import ... annotations** removes everything it added.

Coordinates are read as full-resolution pixels of the scene, as QuPath, ASAP
and SlideIO Viewer write them.

### From QuPath (GeoJSON)

In QuPath, export the annotations with **File > Export objects as GeoJSON**,
then import the file here.

| QuPath | SlideIO Viewer |
|---|---|
| Rectangle | Rectangle |
| Ellipse | Polygon (outline of the ellipse) |
| Polygon, brush and wand areas | Polygon; an axis-aligned four-corner box becomes a Rectangle |
| Line, polyline | Freehand Line |
| Points | One point marker per point |
| Name | Label |
| Classification | Classification |
| Colour | Colour (the object's colour, else its classification's) |

Not imported: detections, cells, tiles and other non-annotation objects,
polygons with holes, nested child objects, measurements and locks. The summary
counts each.

### From ASAP (XML)

| ASAP | SlideIO Viewer |
|---|---|
| Dot | Point marker |
| PointSet | One point marker per point |
| Polygon | Polygon |
| Spline | Polygon through the spline's control points |
| Rectangle | Rectangle, or Polygon when rotated |
| Measurement with two points | Ruler |
| Measurement with more points | Freehand Line |
| Name | Label (ASAP's automatic names such as "Annotation 3" are dropped) |
| Group (PartOfGroup) | Classification ("None" means no classification) |
| Colour | Colour, else the group's colour |

### From SlideIO Viewer

A GeoJSON file exported by SlideIO Viewer comes back with its shapes, label,
classification, colour, line width, fill, notes, author and dates. The layer is
not restored: everything goes on the active layer.

## Exporting annotations to GeoJSON

**File > Export Annotations as GeoJSON...** writes every annotation of the scene
to a `.geojson` file, suggested as `<slide name>.s<scene>.geojson`.

In QuPath, drag the file onto the open slide, or use **File > Import objects
from file**:

- rectangles and polygons arrive as rectangles and polygons;
- ellipses arrive as polygons;
- freehand lines, arrows, rulers and angles arrive as lines;
- points and text arrive as points;
- the label becomes the name, and the classification and colour carry over.

The file also keeps everything SlideIO Viewer needs to restore the annotations
exactly. See [File formats](file-formats.md#geojson-export).

## Counts CSV

**File > Export Counts...** writes the [tally](categories.md#the-tally) to a
CSV file, suggested as `<slide name>.s<scene>.counts.csv`:

| Column | Content |
|---|---|
| `category` | Category name, or `Unclassified` |
| `count` | Number of annotations with the category (text, rulers and angles are not counted) |
| `in_list` | `true` if the category is in the category list |
| `slide`, `scene`, `slide_id`, `exported_at` | Which slide and scene, and when (UTC) |

## Measurements CSV

**File > Export Measurements...** writes one row per annotation, suggested as
`<slide name>.s<scene>.measurements.csv`:

| Column | Content |
|---|---|
| `id` | The annotation's identifier |
| `type` | `rectangle`, `ellipse`, `polygon`, `polyline` (Freehand Line), `point`, `arrow`, `text`, `ruler` or `angle` |
| `label`, `classification` | As in the Properties pane |
| `center_x_px`, `center_y_px` | Centre of the annotation's bounding box, in slide pixels |
| `area_px2`, `perimeter_px` | For rectangles, ellipses and polygons |
| `length_px` | For freehand lines, arrows and rulers |
| `area_um2`, `perimeter_um`, `length_um` | The same in µm² and µm, when the slide is calibrated |
| `angle_deg` | For angles |
| `area_note` | `self-intersecting` when the area could not be computed |
| `pixel_width_um`, `pixel_height_um` | The pixel size used |
| `calibration_source` | `metadata`, `manual` or `none`. See [Calibration](measurements.md#calibration). |
| `slide`, `scene`, `slide_id`, `exported_at` | Which slide and scene, and when (UTC) |

Values are not rounded, and micrometre columns are always in µm, never mm.
Cells that do not apply to an annotation are empty.

### CSV format

Both CSV files open directly in Excel and other spreadsheets: they are UTF-8
with a byte-order mark, comma-separated, with a dot as the decimal separator.
Text that a spreadsheet could mistake for a formula, such as a label starting
with `=`, is prefixed with an apostrophe.
