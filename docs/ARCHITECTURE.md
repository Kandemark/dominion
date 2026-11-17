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

**Continue** and Space call `songa_kipindi`, which runs `zamu_inayofuata` once or repeatedly: one week, until the month changes, thirteen weeks, or until a turn produces a request, a warning or a diary meeting (at most 26 weeks). Each turn advances the simulation, applies the active decisions, generates the inbox and the world press, and marks the page for redrawing.

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

## Houses of power

`moduli/siasa/nguvu.swa` turns every seat of every chamber, and a bench of nine justices, into a person (`Mbunge`): name, party (seats are allocated by the constitution's seat counts), two traits, age, attitude to the player, party loyalty, venality and influence, with the Speaker, Deputy Speaker, Majority Leader, Chief Whip and Leader of the Opposition picked from the right parties. Traits change the numbers: loyal members follow the whip, corrupt ones are cheap, idealists refuse money.

The player spends **political capital** (regenerates each week with legitimacy):

| Action | Capital | Effect |
|---|---|---|
| Payment of 5M, 20M or 50M | 3 + treasury | attitude up by venality, loyalty down, corruption and scandal risk up; idealists refuse and resent it |
| Lobby | 4 | the assistant raises a member's attitude next week |
| Summon | 2 | the assistant books an official into your diary, if they agree |
| Table a motion | 10 | the member tables it next week if their attitude, party and payments allow |
| Whip the party | 8 | government members in that chamber gain loyalty |
| Veto | 15 | stops a passed bill unless the chamber has two thirds |

A motion is voted two weeks after it is tabled. Each member votes yes when party line × loyalty + attitude × 0.6 (sign depending on the side of the motion) plus a fixed per-member noise is positive; the same computation run before the vote gives the forecast and the odds shown on the page. Impeaching the Speaker needs two thirds and makes the sponsor Speaker; no confidence swaps government and opposition; finance bills move treasury and legitimacy; bills wait two weeks for assent or veto. Each week the opposition may table its own motion (more likely when legitimacy is low and its seats many; an allied Speaker halves the chance), and accumulated scandal risk can be exposed by the press, costing legitimacy. Results arrive in the inbox.

## Currencies and markets

`moduli/soko/masoko.swa`. Simulation values are in gold units; each nation's currency has a rate in its units per gold (×10000). The eight largest economies are on the gold standard; about 60% of the rest peg to one of them (a land neighbour if possible) with reserves that move with treasury and stability and, when exhausted under low stability, break the peg and devalue it by 20–45%; the rest float with stability, treasury and growth.

Each exchange lists companies whose sectors exist in the start year (railways from 1830, oil from 1870, motor vehicles from 1905...). Prices move each week by a long-run drift, the nation's growth and stability, a world shock per sector and company noise; a year of history is generated before turn one. Tycoons own most companies (the state owns them in one-party states); their net worth is their stake. The player's wallet holds home cash, gold and shares bought in any currency, receives the office salary and dividends, and pays a hired adviser.

The same weekly pass moves every nation's state: stability and legitimacy drift with the economy, and strikes, protests, coups (likelier under military rule and dictatorship), elections on the constitutional term, devaluations and sell-offs are logged as events.

## The constitution

`moduli/siasa/hati.swa` is a clause engine, not a text. A generator walks the state and emits clauses by rule: every appointed office (appointment, confirming chamber, days to confirm), every senior office (age and citizenship requirements), every ministry, every chamber (composition, term, eligibility, quorum, removal of the Speaker, sittings, immunity, vacancies), every standing committee, every province on the map (establishment, governor, council), a catalogue of 36 rights admitted by the form of government and the start year (the right to strike only after 1880, social rights after 1900), the division of legislative power over 22 policy areas, lower court tiers, independent institutions of the era, public finance, elections, emergency, amendment, and transitional provisions. Each clause has a kind, a subject and up to four numeric parameters; the text is assembled from them with grammar pieces that vary per clause. Clauses are numbered into parts, articles and sections and laid out as a paginated book.

The engine reads the parameters: vote thresholds for every kind of motion, weeks before a vote, weeks for assent, the veto and its override threshold, the term of the head of state, and the amendment procedure (decree under emergency or absolute rule, the legislature with a referendum where the amendment clause requires one, the party congress, a referendum, or the council of chiefs and governors). Any parameter of any clause can be amended, or a clause repealed, through that procedure; entrenched rights cannot be curtailed. Every amendment is recorded.

Constitutions evolve: each nation has a version that rises when it amends its own constitution or suffers a coup, and each version mutates a share of the parameters of the one before.

## Dashboard panels

`moduli/skrini/jopo.swa` holds the panels shared by the nation pages, each reading one metric (GDP, per capita, population, the four indices, stability, legitimacy, growth, treasury) for all 232 nations: world ranking, distribution histogram, scatter of two metrics (GDP and population on a log scale), land neighbours, averages by form of government, and the offices of a branch. The page's nation is highlighted everywhere, and clicking a nation opens it. Clicks on these panels, the World page and the Government page go through `moduli/onyesho/bofya.swa`, where every clickable element registers its rectangle while it is drawn.

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

### Decisions

Conversations can be about anything, but the engine alone decides what an agreement does. When an exchange concludes something, the reply carries one more line of short tokens (`moduli/akili/uamuzi.swa`):

```
DECISION: kind=trade with=Baical volume=120 friendliness=5 corruption=0 fund=-20 tax=0 support=0 weeks=52
```

| Key | Meaning | Range |
|---|---|---|
| `kind` | trade, aid, loan, sanction, treaty, alliance, war, peace, tax, budget, law, election, project, reform, crackdown, amnesty | |
| `with` | the other nation (spaces written as `_`); required for the first eight kinds | |
| `volume` | trade in millions per week | 0 to 1000 |
| `friendliness` | change in relations with that nation | −20 to 20 |
| `corruption` | change in the national corruption level | −10 to 10 |
| `fund` | one-off amount in millions (negative is spending) | −100 to 100 |
| `tax` | change in tax, percentage points | −10 to 10 |
| `support` | change in public approval | −10 to 10 |
| `weeks` | how long the decision lasts (0 is one-off) | 0 to 520 |

Missing keys are 0, keys are matched whole (`supporttax=` is not `tax=`), every number is clamped, and an unknown kind or nation is rejected with a reason the meeting page shows. An accepted decision is appended to `saves/nafasi_N/maamuzi` as ten integers per line, applied once (relations, corruption, treasury, legitimacy), and then applied every week while it is active: trade adds its volume and treasury income, aid and loans move the treasury, sanctions erode relations and stop trade, war drains stability, public works build it. On start-up the ledger is read back and replayed, so relations and corruption are rebuilt from the recorded decisions alone.

## Time

`moduli/injini/tarehe.swa`: the start year is chosen at launch (`--mwaka`, 1700 to 2000, default 1900). Day 0 is 1 January of that year and turn *n* starts on day 7(*n* − 1). Weekdays come from the Gregorian calendar, so 1 January 1820 is a Saturday and 1 January 1900 a Monday. Dates are computed from the day number, so the start year is the only clock state. `kalenda.swa` derives the recurring events of any day from the constitution and adds the meetings booked in the diary.

The borders on the map are still the approved world's; a start year changes the calendar and the history, not the map. Borders that move with the start year come with the world generator port.

## Tests

Each `jaribio_*.swa` is a program that checks its module against known values, or renders a screen to a raw frame and checks it. On failure they print `SHINDWA` or `FAIL` and exit non-zero.
