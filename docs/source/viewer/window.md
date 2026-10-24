# The main window

```{figure} ../_static/window-overview.webp
:alt: The main window

The main window with a slide open: the minimap at the top right, the zoom
indicator at the bottom left, and the Scenes and Annotations panes on the
right.
```

The window has five parts:

Slide view
: The large area in the middle, where the slide is drawn. Three overlays sit
  on top of it:
  - the **minimap** in the top-right corner;
  - the **zoom indicator** with the scale bar and zoom slider in the
    bottom-left corner;
  - the **Z/T navigator** in the top-left corner, only for slides with several
    Z slices or time frames.

Panes
: Dockable panels for scenes, associated images, properties, metadata,
  channels and annotations. All of them start hidden; open them from the
  **View** menu. See [Panes](panes.md).

Menu bar
: **File**, **Edit**, **View**, **Tools** and **Help**. There is no toolbar:
  every command is in a menu, and most have a keyboard shortcut. See
  [Keyboard shortcuts](shortcuts.md).

Status bar
: At the bottom. Described below.

Title bar
: Shows "SlideIO Viewer - " followed by the full path of the open slide.

## Panes and layout

Every pane is a dockable panel. Drag a pane's title bar to move it to another
edge of the window, drop it onto another pane to stack them as tabs, or
double-click the title bar to float it as a separate window. The Properties and
Metadata panes dock only on the left or right.

The viewer remembers the window's size and position and which panes are open,
and restores them the next time it starts. Opening or closing a slide never
opens or closes panes.

## Status bar

The left part of the status bar shows short messages, which disappear after
four seconds, and a description of the menu item under the mouse. The right
part holds these fields:

| Field | Shows |
|---|---|
| `X: 1234  Y: 5678` | The position under the mouse, in full-resolution slide pixels. |
| `20.0x (50.0%)` | The current magnification and zoom. See [Magnification and zoom](navigation.md#magnification-and-zoom). |
| **Annotations disabled** | Shown in amber when annotations cannot be edited on this slide. Hover over it to see why. See [Read-only annotations](annotations/saving.md#read-only-annotations). |
| `Layer: Diagnostic` | The layer new annotations are drawn on. See [Layers](annotations/layers.md). |
| `sRGB` | Shown while [colour management](color-management.md) is on. |

## Theme

The menus, the status bar and most panes use a dark theme. Dialogs and file
pickers follow your operating system's theme.
