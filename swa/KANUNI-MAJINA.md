# Kanuni ya Majina — Uandishi wa Swa wa Dominion

Swa haina eneo la majina (namespace) wala neno muhimu la faragha ya
faili (`static`). Kila jina la kazi la ngazi ya juu ni la ulimwengu
mzima wa programu — kazi mbili zenye jina moja kwenye moduli tofauti
ni mgongano, hata kama hazihusiani. Kwa hiyo kila moduli ya Dominion
ina kiambishi chake cha lazima, tangu kazi ya kwanza.

## Ramani ya viambishi (moduli za C → kiambishi cha Swa)

| Moduli ya C (`src/core/`) | Kiambishi cha Swa |
|---|---|
| `politics/`     | `siasa_`        |
| `technology/`   | `teknolojia_`   |
| `diplomacy/`    | `diplomasia_`   |
| `economy/`      | `uchumi_`       |
| `governance/`   | `utawala_`      |
| `culture/`      | `utamaduni_`    |
| `military/`     | `jeshi_`        |
| `population/`   | `idadi_ya_watu_`|
| `ai/`           | `akili_bandia_` |
| `events/`       | `matukio_`      |
| `environment/`  | `mazingira_`    |
| `world/`        | `dunia_`        |
| `simulation_engine/` | `injini_`  |

Msingi wa pamoja (`include/common.h`) hauna kiambishi cha moduli —
unatumia `civ_` (kutoka jina la asili la mradi, "Civilization
simulation") kwa sababu kila faili litahusisha hili, na hakuna hatari
ya mgongano na moduli mahususi.

## Kanuni

1. Kila jina la kazi/muundo/kigezo cha ulimwengu LAZIMA lianze na
   kiambishi cha moduli lake. Hakuna ubaguzi, hata kwa kazi ndogo za
   ndani zinazoonekana salama.
2. Kiambishi kinafuatwa na `_` kisha jina la kazi kwa Kiswahili,
   kwa mtindo wa `chini_chini` (snake_case), sawa na maktaba za Swa
   zilizopo (`orodha_ongeza`, `ramani_weka`).
3. Migogoro ya majina kati ya moduli mbili (mfano: `siasa_` na
   `utawala_` zote zikihitaji kazi ya "chagua_kiongozi") ni ishara
   kuwa kazi hiyo inapaswa kuhamishwa kwenye msingi wa pamoja
   (`swa/msingi/`), si kuachwa kwenye moduli zote mbili kwa majina
   tofauti kidogo.
