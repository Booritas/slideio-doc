# Annotations

Annotations are shapes, markers, text and measurements you draw on a slide:
outline a tumour region, count cells with point markers, label a structure,
measure a distance or an angle.

% SCREENSHOT: annotations-overview.png — a slide with a few annotation types,
% the Annotation List and the Layers pane open.

## Before you start

The drawing tools need your name: every annotation records who created it.
Enter it once in **Tools > Preferences...**; see
[First-time setup](../install.md#first-time-setup).

## Key ideas

Annotations belong to a scene
: Each scene of a slide has its own annotations. Associated images cannot be
  annotated.

Shapes live in slide coordinates
: An annotation is stored in full-resolution slide pixels, so it stays on the
  same tissue at every zoom. Line widths, markers and labels keep the same
  size on screen whatever the zoom.

One annotation is selected at a time
: Click an annotation to select it; its outline is drawn with a dashed
  black-and-white line. Edit its properties in the
  [Annotation Properties pane](list-and-properties.md#annotation-properties-pane).

Annotations are saved automatically
: There is no Save command. Changes are written to the annotation workspace
  within two seconds. See [Saving annotations](saving.md).

Layers organise annotations
: Every annotation is on a layer, which can be hidden, locked or faded. New
  annotations go on the active layer. See [Layers](layers.md).

Categories classify annotations
: A classification such as "Tumor" can be given to any annotation. Point
  markers are counted per category. See [Categories and counting](categories.md).

Everything can be undone
: Drawing, moving, editing, deleting, importing and moving between layers can
  be undone with {kbd}`Ctrl+Z`, up to 50 steps. See
  [Undo and redo](editing.md#undo-and-redo).

## In this section

```{toctree}
:maxdepth: 2

tools
editing
measurements
list-and-properties
categories
layers
saving
import-export
file-formats
```
