# Architecture

Dominion is a single Swa program. `swa/moduli/programu/dominion.swa` is the entry point; it pulls in everything else with `husisha { ... }`, and the compiler produces one static binary. All paths below are relative to `swa/`.

Identifiers and comments are in Swahili. This document gives the English meaning of the main names.

## Layout

| Directory | Contents |
|---|---|
| `msingi/` | Shared foundation: `msingi_civ.swa` (common types), `lugha_dominion.swa` (simulation messages in three languages), and `maktaba/`, a vendored copy of the Swa standard library (memory, strings, files, maths) |
| `moduli/mchezo.swa` | The game object (`Mchezo`): creates, updates and destroys all 47 simulation systems, keeps per-nation GDP history, saves and loads |
| `moduli/dunia/` | The world: nations (`taifa.swa`), the approved world loaded into the simulation (`dunia_atlasi.swa`), provinces, settlements, borders, resources, and the Mersenne Twister used by the world generator port (`nasibu_mt.swa`) |
| `moduli/uchumi/` | Economy: agriculture, industry, energy, labour, taxes, budget, banks, markets, trade, currency |
| `moduli/idadi_ya_watu/`, `utamaduni/`, `teknolojia/`, `jeshi/`, `diplomasia/`, `mazingira/`, `matukio/` | Population, culture, technology, military, diplomacy, environment and events |
| `moduli/utawala/` | The inherited governance model: branches, institutions, legal system, elections, corruption |
| `moduli/siasa/` | The playable state: constitutions (`dola.swa`), the office tree (`wahusika.swa`), constitutional powers (`katiba.swa`), the diary (`kalenda.swa`) and the inbox (`kikasha.swa`) |
| `moduli/akili/` | Simulation AI for nations, plus the AI adviser client (`mshauri.swa`) and conversations (`mazungumzo.swa`) |
| `moduli/injini/` | Engine services: orchestration, timing, saving, and the game calendar (`tarehe.swa`) |
| `moduli/onyesho/` | Drawing: the canvas (`turubai.swa`), TrueType text (`maandishi.swa`), the UI toolkit (`sura.swa`, `vipengele.swa`), data components (`chati_kadi.swa`), assembly charts (`bunge.swa`), the world renderer (`dunia_halisi.swa`), interface translations (`maneno.swa`), and the Wayland client (`wayland/`) |
| `moduli/skrini/` | One file per page: map, overview dashboard, world, politics, government, economy, military, diplomacy, culture, technology, calendar, inbox, settings, and the boot screens |
| `moduli/programu/` | The program: window, input, pages, frame loop |
| `rasilimali/` | Data: `dunia.bin` (the world) and the Noto fonts |

## The frame loop

`anza` in `dominion.swa`:

1. Reads the saved interface language, opens the Wayland window (full screen unless `--dirishani`), and shows the Kajara splash and the loading screen.
2. Creates the game (`mchezo_unda`, `mchezo_anzisha`) while the loading screen fills its assembly.
3. Loops: read window events, handle them, and draw a frame only when something changed.

The state of the program is a `Hali`: the current page, the map's centre and zoom, the selected nation, hover and pin state, and the cached map image.

- **Map page:** the map (with the top bar and side navigation) is drawn once per view into `h->msingi` and copied each frame. Only the summary cards and the nation card under the pointer are drawn on top, so hovering is cheap.
- **Other pages:** `chora_skrini_ya_taifa` draws the whole page. Pages share the frame drawn by `skrini_upau_wa_juu` (top bar) and `skrini_urambazaji` (side navigation).

**Continue** and Space call `zamu_inayofuata`: the simulation advances one week, the inbox receives the week's messages, and the page is redrawn.

## The world file

`rasilimali/dunia.bin` starts with `DUNIA001`, the width and height of the world grid (4096 × 2048), and a table of sections `[id, offset, length]`:

| Id | Section | Encoding |
|---|---|---|
| 1 | Land: sea, land, lake, ice | run-length per row |
| 2 | Hill shading | raw, half resolution |
| 3 | Nation of each pixel | run-length per row, 16-bit |
| 4 | Province of each pixel | run-length per row |
| 5 | Nation table: names, colour, capital | records |
| 6 | Rivers with flow | point chains |
| 7 | Roads in three tiers | point chains |
| 8 | Railways | point chains |
| 9 | Settlements: position, population, rank, port, airport | records |
| 10 | Labels: seas, mountains, rivers, regions | records |
| 11 | Disputed territories | bounding box and run-length mask |
| 12 | Elevation | raw, half resolution |

`moduli/onyesho/dunia_halisi.swa` loads and renders it at any zoom; `moduli/dunia/dunia_atlasi.swa` builds the simulation's 232 nations from it.

## Rendering

- **Canvas:** `turubai.swa` draws anti-aliased shapes with alpha and clipping into a 32-bit buffer.
- **Text:** `maandishi.swa` parses TrueType outlines and rasterises glyphs at any size.
- **Toolkit:** `sura.swa` holds the palette and basic pieces (labels, panels, bars, tables); `vipengele.swa` adds buttons, segmented controls, gauges, sparklines, donuts and Sankey flows; `chati_kadi.swa` holds the dashboard components (stat tiles, target bar chart, segmented gauge, funnel, heatmap, attention list, task cards).
- **Window:** `wayland/` speaks the Wayland wire protocol over a Unix socket, with shared-memory buffers, pointer, keyboard, resize and full screen.

`dirisha_bila_compositor` is a window with no compositor behind it: `--bila-dirisha W H --fremu N --dampo file` renders frames into memory and writes them out, which is how screens are checked without touching the desktop.

## Localisation

Everything the player reads goes through `ui("English text")` in `moduli/onyesho/maneno.swa`. The English text is the key; the table holds Swahili and French. A word with two meanings gets a lowercase context before a bar (`ui("tab|GDP")`), which English strips. Untranslated text falls back to English. Names inside the world (nations, cities, rivers, people) are never translated.

## Constitutions and the office tree

`dola_unda` in `moduli/siasa/dola.swa` builds a nation's state from its title on the map ("Kingdom of X", "People's Republic of X", "Tribes of X") and its seed: form of government, chambers (size from the cube root of the population), parties, seats, the governing party or coalition, titles, term, franchise, and the ages of the state and its constitution.

`wahusika_unda` turns that constitution into the office tree. Every office records its branch, rank, superior, how it is filled, who appoints it, and which chamber must confirm the appointment. `katiba.swa` applies the rules: only the appointing office can dismiss, confirmation votes count the parties' real seats, and meeting requests depend on rank, attitude and party.

## AI conversations

`moduli/akili/mshauri.swa` is a plain HTTP/1.1 client written over raw socket system calls. It sends OpenAI-style `/v1/chat/completions` requests with an optional bearer key, a token limit and, for local models, reasoning switched off.

`moduli/akili/mazungumzo.swa` builds the prompt:

- **Officials:** the setting (nation, form of government, date, the three indicators), then the official's name, office, age, party, ideology, two temperament traits and attitude to the player, with the instruction to stay in character.
- **The Adviser:** the same setting, playing the player's private counsel who weighs consequences.
- **Memory:** the last lines of the save's memory file (`saves/nafasi_N/kumbukumbu`) are included in every prompt.

Every reply must end with one line:

```
EFFECT: attitude=N stability=N legitimacy=N treasury=N
```

The game removes the line from the displayed text, clamps the numbers (attitude ±10, the rest ±5), applies them, and appends the exchange to the memory file.

## Time

`moduli/injini/tarehe.swa`: day 0 is Monday 4 January 1954 and turn *n* starts on day 7(*n* − 1). Dates are computed from the day number, so there is no clock state to save. `kalenda.swa` derives the recurring events of any day from the constitution and adds the meetings booked in the diary.

## Tests

Each `jaribio_*.swa` is a program that checks its module against known values, or renders a screen to a raw frame and checks it. On failure they print `SHINDWA` or `FAIL` and exit non-zero.
