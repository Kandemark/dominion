# Artwork

Dominion draws everything in code, but it will show real artwork when the
files below are present. The game reads PNG itself (`moduli/onyesho/png.swa`):
8-bit RGB or RGBA, palette or greyscale, not interlaced.

| File | Used for | Size |
| --- | --- | --- |
| `kupakia.png` | Loading screen background, behind the title and progress bar | 1920 x 1080 or larger, 16:9 |

The image fills the screen without stretching (edges are cropped on other
aspect ratios) and is darkened under the title so the text stays readable.
Keep the subject in the middle two thirds and the top quarter calm.

When `kupakia.png` is missing, the game draws its own revolution scene
(crowd, flags, domed parliament) in `moduli/skrini/mandhari.swa`.
