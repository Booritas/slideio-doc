# Colour management

Scanners record colour in their own colour space. Many slides embed an **ICC
profile** that describes that colour space. With colour management on, the
viewer converts the slide's colours to **sRGB** through the profile, so the
slide looks as the scanner's manufacturer intended on a standard monitor.

## Turn colour management on

Choose **View > Color Management** ({kbd}`Ctrl+Shift+I`). While it is on, the
status bar shows `sRGB`.

The setting is remembered, and is applied to every slide that supports it.
Slides that do not support it open unmanaged, without changing the setting.

Colour management works only for **RGB brightfield slides** (three channels of
8- or 16-bit data, not fluorescence) that have a profile: one embedded in the
slide, a default profile, or a profile you set for the slide. When it is not
available, the menu item is greyed out; hover over it to see why:

- "Color management applies to RGB brightfield slides only"
- "This slide embeds no ICC profile, and no default profile is set"
- "This slide's color profile could not be used"

## A default profile for slides without one

If your scanner writes slides without an embedded profile, give the viewer its
profile once with **View > Set Default ICC Profile...** and pick the `.icc` or
`.icm` file. The default profile is used only for slides that embed no profile
of their own, and only for slides opened afterwards; reopen the current slide
to apply it.

**View > Clear Default ICC Profile** removes it.

The profile must be a valid ICC profile for RGB data; otherwise the viewer
says why it cannot be used.

## A profile for one slide

**View > Set ICC Profile for This Slide...** assigns a profile to the open
slide. It replaces any profile the slide embeds; the viewer asks for
confirmation first, because the slide will then be displayed through a profile
the scanner did not produce. The slide is reopened and colour management is
turned on.

**View > Clear ICC Profile for This Slide** removes the assignment and reopens
the slide.

The viewer recognises a slide by its contents, not its file name, so the
assignment still applies after you move or rename the file.

## Manage per-slide profiles

**View > Manage Slide ICC Profiles...** lists every slide that has a profile
assigned, with the slide's file name, the profile's path and its status:

| Status | Meaning |
|---|---|
| OK | The profile can be used. |
| File missing | The profile file is no longer there. |
| Not a profile | The file is not a valid ICC profile. |
| Not RGB | The profile is not for RGB data. |

"displaces embedded" marks assignments that override a profile embedded in the
slide. Select a row and click **Remove** to delete that assignment, or **Remove
All** to delete them all.

## What the Properties pane shows

The **Color profile** row of the [Properties pane](panes.md#properties) shows
which profile applies and where it comes from:

| Row | Meaning |
|---|---|
| Source | Embedded (in the slide), Supplied (by you), Assumed, or None |
| Origin | Slide, Default setting, or Per-slide override. Reads "Origin when managed" while colour management is off. |
| Embedded | "displaced: ..." when your assignment replaces the slide's own profile |
| Description, Manufacturer, Model, Version | Taken from the profile |
| Data space, Connection space, Intent, Size | Technical details of the profile |

A slide without any profile shows "None (not color-managed)".
