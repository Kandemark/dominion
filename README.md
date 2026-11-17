# Dominion

A grand strategy game written entirely in [Swa](https://github.com/lugha-swa/swa), the Swahili systems programming language. No C, no libc, no SDL, no external libraries: the game is one statically linked x86-64 binary built by the Swa compiler alone, and it talks to the Linux kernel and the Wayland compositor directly.

232 nations on a hand-built world of six continents, 1,261 provinces and about 64,000 settlements. Every nation has its own constitution: its form of government (twenty kinds, from parliamentary republics to tribal confederations and stateless communes), zero to four chambers, parties across 22 ideologies, and a full tree of offices that you can occupy, appoint and dismiss as the constitution allows.

## Requirements

- Linux on x86-64
- A Wayland compositor (tested on Hyprland)
- The Swa compiler from [lugha-swa/swa](https://github.com/lugha-swa/swa) (main branch)

## Build and run

```bash
cd swa
swa --programu moduli/programu/dominion.swa > dominion
chmod +x dominion
./dominion
```

Run it from the `swa/` directory: the game reads `rasilimali/` (world and fonts) and writes `saves/` relative to it.

Options:

| Option | Effect |
|---|---|
| `--dirishani` | start in a window instead of full screen (F11 toggles) |
| `--skrini S` | start on page S |
| `--bila-dirisha W H` | render off-screen at W×H without opening a window (with `--fremu N --dampo file` for captures) |

## Playing

- **Side navigation** opens each page: Map, Overview, Inbox, Calendar, World, Politics, Government, Military, Diplomacy, Economy, Culture, Technology, Settings.
- **Map:** drag to pan, wheel to zoom. Hover a nation for its card; click to pin it and open its dossier. Esc goes back.
- **Continue** (top right) or **Space** advances one week. The game starts on Monday 4 January 1954.
- **Government:** request meetings through your personal assistant, take any office, dismiss and appoint where the constitution gives you the power. Appointments that need confirmation go to a vote in the right chamber.
- **AI adviser:** in Settings choose Off, a local model (Ollama at 127.0.0.1:11434) or a custom chat-completions server with an API key (stored in `saves/akili`). Officials then answer in character and the Adviser weighs the consequences of what you say.

## Tests

Every `jaribio_*.swa` under `swa/moduli` is a self-checking test program:

```bash
cd swa
for f in $(find moduli -name 'jaribio_*.swa' | grep -v wayland/jaribio_dirisha); do
  swa --programu "$f" > /tmp/t && chmod +x /tmp/t && /tmp/t /tmp/t.out > /dev/null || echo "FAILED $f"
done
```

## What is not Swa yet

- `swa/rasilimali/dunia.bin`, the world, was produced from the approved map with external tooling. The generator is being ported to Swa; its random-number core already is (`moduli/dunia/nasibu_mt.swa`).
- The fonts in `swa/rasilimali/fonti` are Noto (SIL Open Font License); Swa parses and rasterises them itself.

## License

GNU Affero General Public License v3.0. See [LICENSE](LICENSE).
