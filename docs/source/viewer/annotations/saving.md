# Saving annotations

## Annotations are saved automatically

There is no Save command. The viewer writes the annotations of the scene on
screen to disk:

- two seconds after your last change;
- at least every 30 seconds while you keep editing;
- when you close the slide, open another slide or scene, change the
  annotation workspace, or quit.

Each save replaces the file in one step, so an interrupted save leaves the
previous version intact. If the computer crashes or the viewer is killed, at
most the last few seconds of work are lost.

## The annotation workspace

Annotations are saved in the **annotation workspace**, a folder you choose in
**Tools > Preferences...**. The default is the `SlideIO Viewer` folder in your
Documents folder. The files go in its `annotations` subfolder.

**File > Open Annotations Folder** opens that folder in your file manager.

Use a shared or synchronised folder as the workspace to share annotations
between computers or colleagues.

### How a slide finds its annotations

Each scene of each slide has its own file, named after an identifier the viewer
computes from the slide's contents (its size in bytes and the size and channels
of each scene), for example `a3f8c2e1b4d50697.s0.annotations.json`. The `s0` is
the scene index.

Because the identifier does not depend on the file's name or location:

- you can **move or rename** a slide, and its annotations still appear;
- the same slide opened from **another computer** finds its annotations, as
  long as both use the same workspace;
- a slide that has been **modified**, for example re-compressed or
  anonymised, counts as a different slide and starts without annotations. The
  old annotations stay in their file.

For a DICOM study opened as a folder, adding or removing files in the folder
also changes the identifier.

### Changing the workspace

Changing the folder in Preferences does not move or delete any files: existing
annotation files stay where they are, and the viewer reads and writes the new
folder from then on.

If a slide is open when you change the folder, the viewer saves to the old
folder first and then asks what to do with the annotations on screen:

When the new folder already has annotations for this scene
: - **Merge**: combine both sets and save the result in the new folder. For
    an annotation that exists in both, the most recently modified version is
    kept.
  - **Keep what's on screen**: save the annotations on screen to the new
    folder, replacing what is there.
  - **Use the new folder's**: show the new folder's annotations; nothing is
    written.

When it has none
: - **Copy to the new folder**: save the annotations on screen there.
  - **Switch without copying**: start with an empty scene in the new folder.

**Cancel** keeps the old folder. Only the scene on screen is carried over;
other scenes and slides stay in the folder they were saved in. The undo history
is cleared.

## Read-only annotations

Sometimes a slide's annotations are shown but cannot be changed. The drawing
tools are greyed out, and the status bar shows **Annotations disabled** in
amber; hover over it to see the reason.

### The same slide in two windows

When a slide is open in one SlideIO Viewer window, or on another computer
using the same shared workspace, another window that opens it shows its
annotations read-only: "Another window has this slide's annotations open, so
they are read-only here." Close the slide in the first window and reopen it in
the second to edit there.

### A file that cannot be read

If the annotation file is damaged, or was written by a newer version of the
viewer, the viewer says "Annotations could not be opened", leaves the file
untouched, and disables annotations for the slide so the file is not
overwritten.

### A file that belongs to another slide

If an annotation file names a different slide than the one open, usually
because the file was copied or renamed by hand, the viewer asks:

- **Open Read-Only**: show the annotations without allowing changes;
- **Use for This Slide**: adopt them for this slide and save them for it;
- **Ignore Them**: show nothing and leave the file alone.

### Slides without annotations

Associated images, and slides whose identifier cannot be computed, cannot be
annotated: "This slide could not be identified, so annotations cannot be
saved."

## When saving fails

If the workspace cannot be written, for example a network drive is
disconnected, the viewer warns once, keeps the annotations open and retries
every two seconds. Choose a writable folder in Preferences if the problem
persists.

If saving fails when you close the slide or quit, the viewer asks before
anything is lost:

- **Retry**: try the same folder again;
- **Choose Another Folder...**: save to a folder you pick, which becomes the
  workspace;
- **Discard and Close**: close without saving.

After five failed retries the annotations of that slide are discarded.
