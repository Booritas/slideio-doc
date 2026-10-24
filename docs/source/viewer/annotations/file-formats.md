# File formats

This page is a reference for scripting and for exchanging annotations with
other software. You do not need it to use the viewer.

Coordinates in both formats are **full-resolution pixels of the scene**, with
the origin at the top-left corner, x to the right and y down. Timestamps are
UTC in the form `YYYY-MM-DDTHH:MM:SSZ`, in whole seconds.

## Annotation files

The viewer saves each scene's annotations in
`<workspace>/annotations/<slide id>.s<scene index>.annotations.json`: an
indented UTF-8 JSON document.

```json
{
  "schemaVersion": 2,
  "slideId": "a3f8c2e1b4d50697",
  "sceneIndex": 0,
  "slide": { "fileName": "CMU-1.svs", "path": "C:/slides/CMU-1.svs",
             "width": 46000, "height": 32914 },
  "createdAt": "2026-10-24T09:15:00Z",
  "modifiedAt": "2026-10-24T10:02:41Z",
  "layers": [
    { "id": "diagnostic", "name": "Diagnostic", "visible": true, "locked": false, "opacity": 1.0 },
    { "id": "teaching",   "name": "Teaching",   "visible": true, "locked": false, "opacity": 1.0 },
    { "id": "research",   "name": "Research",   "visible": true, "locked": false, "opacity": 1.0 }
  ],
  "annotations": [
    {
      "id": "0b9c6f1e-3a52-4d8e-9f0a-6d1c2b7e4a10",
      "type": "rectangle",
      "geometry": { "type": "rectangle",
                    "topLeft": { "x": 1200, "y": 800 },
                    "bottomRight": { "x": 2400, "y": 1650 } },
      "properties": { "label": "Region A", "classification": "Tumor",
                      "color": "#E67E22FF", "lineWidth": 2, "fillOpacity": 0.3,
                      "notes": "" },
      "metadata": { "author": "J. Smith",
                    "createdAt": "2026-10-24T09:15:00Z",
                    "modifiedAt": "2026-10-24T09:15:00Z" },
      "layerId": "research"
    }
  ]
}
```

| Key | Meaning |
|---|---|
| `schemaVersion` | `1` when the scene uses only the default layers and every annotation is on the bottom one; `2` otherwise, with `layers` and `layerId`. A viewer refuses files with a newer version than it knows. |
| `slideId`, `sceneIndex` | Which slide and scene the file belongs to |
| `slide` | Where the slide was when last saved, and its size. Informational only. |
| `layers` | Bottom layer first. `opacity` is 0 to 1. |
| `annotations[].id` | Unique within the file |
| `annotations[].type` | Written for readability; the geometry decides |
| `properties.color` | `#RRGGBBAA` |
| `properties.lineWidth` | In screen pixels |
| `properties.fillOpacity` | 0 to 1 |
| `layerId` | The layer's `id`; an unknown id puts the annotation on the bottom layer |

### Geometry

| `geometry.type` | Fields |
|---|---|
| `rectangle` | `topLeft`, `bottomRight` |
| `ellipse` | `topLeft`, `bottomRight` of its bounding box |
| `polygon` | `vertices`: at least 3 points, not repeated at the end |
| `polyline` | `vertices`: at least 2 points (a Freehand Line) |
| `point` | `position` |
| `arrow` | `tail`, `head` |
| `text` | `anchor`; the text is `properties.label` |
| `ruler` | `start`, `end` |
| `angle` | `first`, `vertex`, `second` |

Every point is an object `{ "x": ..., "y": ... }`.

### Editing files by hand

The viewer is strict when reading: a file with an invalid value, or two
annotations with the same `id`, is not loaded, and the slide's annotations
become read-only until the file is fixed. Keys the viewer does not know are
ignored and dropped the next time it saves the file. Close the slide in the
viewer before editing its file.

## GeoJSON export

**File > Export Annotations as GeoJSON...** writes a GeoJSON
`FeatureCollection` that QuPath reads, with an extra `slideio` block at the top
and on each feature for what GeoJSON has no place for.

```json
{
  "type": "FeatureCollection",
  "slideio": {
    "format": "slideio-viewer annotation export",
    "formatVersion": 1,
    "slide": "C:/slides/CMU-1.svs",
    "slideId": "a3f8c2e1b4d50697",
    "scene": 0,
    "exportedAt": "2026-10-24T10:05:00Z",
    "coordinates": "level-0 pixels of the scene; origin top-left, x right, y down",
    "pixelSizeMicrons": [0.499, 0.499],
    "calibrationSource": "metadata"
  },
  "features": [
    {
      "type": "Feature",
      "id": "0b9c6f1e-3a52-4d8e-9f0a-6d1c2b7e4a10",
      "geometry": { "type": "Polygon",
                    "coordinates": [[[1200,800],[2400,800],[2400,1650],[1200,1650],[1200,800]]] },
      "properties": {
        "objectType": "annotation",
        "name": "Region A",
        "color": [230, 126, 34],
        "classification": { "name": "Tumor", "color": [230, 126, 34] },
        "slideio": {
          "type": "rectangle", "notes": "", "author": "J. Smith",
          "createdAt": "2026-10-24T09:15:00Z", "modifiedAt": "2026-10-24T09:15:00Z",
          "color": "#E67E22FF", "lineWidth": 2, "fillOpacity": 0.3,
          "layer": "Research"
        }
      }
    }
  ]
}
```

| Annotation | GeoJSON geometry |
|---|---|
| Rectangle | `Polygon`, four corners and the closing point |
| Ellipse | `Polygon` with 512 points |
| Polygon | `Polygon` |
| Freehand Line | `LineString` |
| Point | `Point` |
| Text | `Point` at its anchor |
| Arrow | `LineString` tail, head |
| Ruler | `LineString` start, end |
| Angle | `LineString` first arm end, vertex, second arm end |

- `name` is omitted when the annotation has no label, and `classification`
  when it has no category.
- `pixelSizeMicrons` is present only when the slide is calibrated;
  `calibrationSource` is always present: `metadata`, `manual` or `none`.
- `slideio.type` lets the viewer restore ellipses, arrows, rulers, angles and
  text on import. `slideio.layer` is the layer's name; it is not used on
  import.
- Measurements are not written; QuPath computes its own.

## GeoJSON import

On import the viewer reads a `FeatureCollection`, a single `Feature`, or a list
of features. It uses each feature's `id` (other software's ids are converted to
stable identifiers, so re-importing skips them), `properties.name`,
`properties.classification` (a string, `{ "name": ... }`, or `{ "names": [...] }`),
`properties.color` or `colorRGB`, and the `slideio` block when present.
Features without an `id` get a new identifier each time, so importing such a
file twice adds them twice.

Features whose `objectType` is not `annotation` (QuPath detections, cells,
tiles) are skipped, as are polygons with holes, nested `childObjects`, and
geometry types other than `Point`, `MultiPoint`, `LineString`,
`MultiLineString`, `Polygon` and `MultiPolygon`. Each part of a `Multi*`
geometry becomes its own annotation.
