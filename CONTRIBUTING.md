# Contributing to Dominion

Dominion is a grand strategy game written entirely in Swa. Contributions are welcome under the AGPLv3 license.

## Rules

1. **Swa only.** No code in any other language, no foreign-function imports (`nje`), no libc. The game must stay a single statically linked binary built by the Swa compiler.
2. **Swahili code, English play.** Identifiers and comments are Swahili. Text the player sees goes through `ui("English text")` (`moduli/onyesho/maneno.swa`) with Swahili and French translations; names inside the world come from its own languages.
3. **Real data only.** Every number on a screen comes from the simulation.
4. **Every module has a test.** Add or update a `jaribio_*.swa` beside the code you change, and make sure all tests pass.

## Building

```bash
cd swa
swa --programu moduli/programu/dominion.swa > dominion && chmod +x dominion && ./dominion
```

`--bila-dirisha 1920 1080 --fremu 2 --dampo frame.bgra` renders a frame off-screen, which is how screens are checked in review.

## Pull requests

1. Branch from `main`.
2. Keep each change focused, with a commit message in Swahili: `<aina>: <maelezo>`.
3. All `jaribio_*.swa` programs compile and pass.
4. Attach a captured frame for any change to what the player sees.
