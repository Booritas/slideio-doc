# Channels

The Channels pane ({kbd}`Ctrl+Shift+C`) controls how each channel of the
slide is displayed: whether it is shown, its colour, its brightness and the
range of values mapped from black to full colour. It is most useful for
fluorescence and multiplexed slides, but works for any slide.

% SCREENSHOT: channels-pane.png — the Channels pane for a 4-channel
% fluorescence slide with one channel expanded to show its histogram.

Changes affect only what you see; the slide file is never modified. The pane is
reset to the slide's defaults each time a slide or scene opens.

## The channel list

At the top of the pane:

- **All channels** shows or hides every channel at once. When some channels
  are visible, it shows all of them; click again to hide all; click a third
  time to return to the mix you had.
- **Reset All** returns every channel to the state it had when the slide
  opened.
- The counter on the right says how many channels are visible.

Each channel row has:

- a check box that shows or hides the channel;
- the channel's name, or "Channel 1", "Channel 2" ... when the file gives none;
- a **colour swatch**: click it to choose the colour the channel is drawn in;
- an **intensity** slider, from 0 to 4×. The default, 1×, sits about a quarter
  of the way along.

## Display range and histogram

Click the arrow at the left of a row to expand it.

The **histogram** shows how often each value occurs in the channel. The two
gold handles mark the display range: values at or below **Min** are drawn
black, values at or above **Max** in full colour, and the values between are
spread across the colour's brightness. Values outside the range are shaded in
the histogram.

To change the range:

- drag a handle; the image updates when you release the mouse;
- or type into the **Min** and **Max** boxes and press {kbd}`Enter`.

**Auto** restores the range the viewer measured when the slide opened.
**Reset** sets the full range of the data type, for example 0 to 255 for 8-bit
data or 0 to 65535 for 16-bit data.

**Log** / **Lin** switches the histogram's vertical scale between logarithmic
(the default, which makes rare values visible) and linear.

## Default colours and ranges

When a slide opens, the viewer chooses each channel's colour:

- **Brightfield** slides (one channel, or three 8-bit channels) are shown as
  they were scanned: white for a single channel, red, green and blue for three.
- **Fluorescence** channels take the colour stored in the file, or one derived
  from the channel's emission wavelength. Otherwise the colour comes from the
  dye name: DAPI blue; FITC, GFP or Alexa 488 green; Cy3, TRITC or Alexa 555
  red; Cy5 or Alexa 647 magenta. Remaining channels get blue, green, red,
  magenta, cyan, yellow and white in turn.

The display range of each channel starts at the lowest and highest values found
in the slide's overview level.
