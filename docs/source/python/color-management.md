# Colour management

Some image formats embed an ICC colour profile that describes how a scene's raw
pixel values map to a real colour space. *Scene* exposes it two ways:
{py:meth}`~slideio.Scene.get_color_profile` returns the raw profile bytes, or
*None* if the scene carries none, and
{py:meth}`~slideio.Scene.get_color_profile_info` returns a parsed summary as a
{py:class}`~slideio.ColorProfileInfo` object, including where the profile came
from ({py:class}`~slideio.ColorProfileSource`: a profile embedded in the file,
one you supplied yourself, an assumed one, or none at all).

Those four values are worth keeping apart when you record what a pipeline did.
`EMBEDDED` means the slide carried the colorimetry; `SUPPLIED` means you
provided it through `source_profile_override`, so the claim about the scanner is
yours rather than the file's; `ASSUMED` means nothing was found and sRGB was
assumed, so no real correction took place.

## Converting pixels

To convert a scene's pixels into a device-independent colour space, transform
it with {py:class}`~slideio.ColorManagement`:

```python
import slideio

slide = slideio.open_slide(file_path="/data/a.svs", driver_id="SVS")
scene = slide.get_scene(0)

cm = slideio.ColorManagement()
cm.target = slideio.ColorTarget.LAB
lab_scene = slideio.transform_scene(scene, [cm])
block = lab_scene.read_block()
```

*ColorManagement* accepts three-channel scenes only, and converts to one of four
targets ({py:class}`~slideio.ColorTarget`): *SRGB*, *LINEAR_RGB*, *LAB* or
*XYZ*. When a scene carries no embedded profile it assumes sRGB by default; set
*missing_profile_policy* ({py:class}`~slideio.MissingProfilePolicy`) to change
that -- for example to *FAIL*, to reject scenes without a real embedded profile,
or to *PASS_THROUGH*, to leave the pixels untouched when the target is sRGB.

## Supplying your own profile

If you have characterised the scanner yourself, assign the profile to
*source_profile_override* as raw ICC bytes; it is used in place of whatever the
scene embeds, so even a slide with no profile converts colorimetrically and
*missing_profile_policy* never applies. Assign *None* to clear it.

```python
with open("/data/scanner.icc", "rb") as icc:
    cm.source_profile_override = icc.read()
```

The
[color-management.ipynb](https://github.com/Booritas/slideio-tutorial/blob/master/color-management.ipynb)
notebook walks through the API on real slides.
