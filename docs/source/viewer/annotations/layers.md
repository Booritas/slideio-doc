# Layers

Layers separate annotations made for different purposes, so you can show,
hide, protect and fade them as groups. Every annotation is on exactly one
layer.

Each scene starts with three layers: **Diagnostic**, **Teaching** and
**Research**. Diagnostic is the bottom layer and is active when a scene opens.

## The Layers pane

Open it with **View > Layers** ({kbd}`Ctrl+Shift+Y`).

% SCREENSHOT: layers-pane.png — the Layers pane with one layer hidden and
% another locked.

The top layer is listed first. Each row has:

| Column | Meaning |
|---|---|
| Show | Tick to show the layer's annotations |
| Lock | Tick to protect them from changes |
| Layer | The layer's name. The active layer is in **bold**. |
| Count | How many annotations are on the layer |
| Opacity | How strongly the layer's annotations are drawn |

## The active layer

New annotations, and imported ones, go on the **active layer**. Its name is in
bold in the pane and shown in the status bar as `Layer: ...`.

To make a layer active, click its name, count or opacity. The active layer is
not remembered: each time a scene opens, the bottom layer is active.

You cannot draw on a hidden or locked active layer; the status bar says
"Layer ... is hidden" or "Layer ... is locked".

## Hide, lock and fade layers

Show
: Untick to hide the layer. Its annotations are not drawn, cannot be selected,
  and are left out of the Annotation List. They are still saved, counted in the
  tally and included in exports.

Lock
: Tick to lock the layer. Its annotations are drawn and can be selected, but
  cannot be moved, resized, edited, deleted or moved to another layer. Their
  properties are greyed out, and the Annotation List adds "(locked)" to their
  type.

Opacity
: Drag the slider to fade the layer's annotations, from 100 % (as drawn) down
  to invisible. Clicking the slider's track or using the keyboard changes it at
  once. The annotations' own colours are not changed.

## Creating and arranging layers

| Button | Does |
|---|---|
| New | Adds "Layer 1" (or the next free number) at the top and makes it active |
| Delete | Deletes the selected layer. Only an empty layer can be deleted, and the last layer cannot. |
| Merge into… | Moves all annotations of the selected layer to the layer you pick. The emptied layer stays; delete it afterwards if you no longer need it. |
| Up / Down | Moves the selected layer one step up or down. Higher layers are drawn on top. |

To rename a layer, double-click its name, or select it and press {kbd}`F2`
(on Windows).

Merging is one undo step. Creating, deleting, renaming, reordering, showing,
locking and fading layers cannot be undone.

## Moving annotations between layers

Select an annotation and choose **Edit > Move to Layer > ...**, or right-click
its row in the Annotation List and choose **Move to Layer**. Each move is one
undo step. Neither the annotation's current layer nor the target may be
locked; moving to a hidden layer is allowed.

## Layers are saved

Layers, with their names, order, visibility, lock and opacity, are saved with
the scene's annotations. Annotations exported to GeoJSON record their layer's
name, but imported annotations always go on the active layer.
