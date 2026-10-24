# Installation and setup

## System requirements

- Windows 10 or 11 (x86-64), macOS (Apple Silicon or Intel), or Linux x86-64.
- A graphics card with **OpenGL 3.3** support. Any GPU of the last decade
  qualifies, including integrated graphics.

No Python, compiler or separate SlideIO installation is needed: everything the
viewer depends on, Qt included, ships inside the package.

## Download

Get the package for your platform from the
[latest release](https://github.com/Booritas/slideio-view/releases/latest).

| Platform | Package |
|---|---|
| Windows 10/11 (x86-64) | Installer (`.exe`) or portable archive (`.zip`) |
| macOS | Disk image (`.dmg`): `macos-arm64` for Apple Silicon, `macos-x86_64` for Intel |
| Debian 12+ / Ubuntu 22.04+ | Package (`.deb`) |
| Other Linux (x86-64) | Archive (`.tar.gz`) |

### Windows

Run the installer, or unpack the `.zip` anywhere and start
`slideio-viewer.exe`. The installer registers the viewer as an "Open with"
choice for `.svs`, `.ndpi` and `.czi` files.

### macOS

Open the disk image and drag the application to Applications. The application is
not signed by a registered developer, so macOS may refuse to open it the first
time; clear the quarantine flag with:

```
xattr -d com.apple.quarantine /Applications/slideio-viewer.app
```

### Linux

On Debian and Ubuntu install the package with `apt`; the leading `./` makes it
install the downloaded file rather than search the repositories:

```
sudo apt install ./slideio-viewer_<version>_amd64.deb
```

On other distributions unpack the `.tar.gz` and run `slideio-viewer` from it.

## Starting the viewer

Start SlideIO Viewer from the Start menu, Applications or your desktop's
launcher, or from a terminal. A slide path on the command line is opened at
start-up:

```
slideio-viewer                      # start with no slide
slideio-viewer path/to/slide.svs    # open a slide
slideio-viewer path/to/dicom-study  # open a folder as a DICOM study
```

Only the first argument is used.

## First-time setup

Viewing slides needs no setup. Before you draw your first annotation, open
**Tools > Preferences...** (on macOS: **SlideIO Viewer > Preferences...**) and
fill in:

Your name
: Every annotation records who created it. The drawing tools stay unavailable
  until a name is entered; choosing one without a name opens Preferences for
  you.

Annotation workspace
: The folder annotations are saved in. The default is a `SlideIO Viewer`
  folder in your Documents folder. See [Saving annotations](annotations/saving.md).

Annotation categories
: The classifications offered for counting and classifying annotations, one
  per line. The default list is Tumor, Stroma, Necrosis, Normal and Artifact.
  See [Categories and counting](annotations/categories.md).

These three are the only preferences. Click **OK** to apply them.

% SCREENSHOT: preferences.png — the Preferences dialog with the three fields.

## Where the viewer keeps its data

| What | Windows | macOS | Linux |
|---|---|---|---|
| Settings | Registry, `HKEY_CURRENT_USER\Software\SlideIO\SlideIO Viewer` | `~/Library/Preferences/com.slideio.SlideIO Viewer.plist` | `~/.config/SlideIO/SlideIO Viewer.conf` |
| Log file | `%LOCALAPPDATA%\SlideIO\SlideIO Viewer\logs\slideio-viewer.log` | `~/Library/Application Support/SlideIO/SlideIO Viewer/logs/slideio-viewer.log` | `~/.local/share/SlideIO/SlideIO Viewer/logs/slideio-viewer.log` |
| Annotations | `Documents\SlideIO Viewer\annotations` | `~/Documents/SlideIO Viewer/annotations` | `~/Documents/SlideIO Viewer/annotations` |

The settings hold the preferences, the recent-files list, the window layout,
colour profiles and calibration overrides. The annotation folder follows the
workspace you choose in Preferences.

The log file is the first thing to look at when something goes wrong. Open it
with **File > Open Log File**; **Help > About SlideIO Viewer...** shows its exact
path on the **System** tab. The log rotates at 10 MB and keeps three old copies.

## About the viewer

**Help > About SlideIO Viewer...** shows the version and build, your system and
graphics card, the third-party components and the license. **Copy to
Clipboard** copies all of it as text, which is useful in a bug report.
