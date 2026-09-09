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

## Kiambishi maalum kwa faili za `src/core/` (ngazi ya juu, si saraka ndogo)

Baadhi ya faili za `src/core/` ziko ngazi ya juu (si ndani ya saraka
ndogo ya moduli) na zinahitaji viambishi vyao maalum, tofauti na
ramani ya juu (ambayo ni kwa saraka ndogo pekee):

| Faili ya C (`src/core/*.c`) | Kiambishi cha Swa | Muhimu |
|---|---|---|
| `role.c` | `jukumu_` | |
| `character.c` | `mhusika_` | |
| `knowledge_system.c` | `maarifa_` | |
| `constitution.c` | `taifa_katiba_` | TOFAUTI na `utawala_katiba_` (governance/legal/constitution.c) -- majina mawili ya faili ya C yanayofanana lakini mifumo tofauti kabisa (ruhusa za vitendo vya mchezaji dhidi ya matawi/taasisi za serikali) |
| `faction.c` | `taifa_kianzio_` | TOFAUTI na `siasa_kikundi_` (politics/faction_system.c, imezuiwa na #182(b)) -- hii ni aina za awali za taifa (archetypes), si miungano ya kisiasa |
| `npc_engine.c` | `wakala_` | |
| `time_engine.c` | `injini_saa_` | Sehemu YA SAA KUU pekee imetafsiriwa (mwaka/siku/zamu) -- mfumo wa kalenda nyingi/enzi umeachwa, angalia maelezo kwenye `swa/moduli/injini/saa_kuu.swa` |

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
