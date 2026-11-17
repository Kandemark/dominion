# Kanuni ya Majina — Dominion kwa Swa

Swa haina eneo la majina (namespace) wala faragha ya faili. Kila jina la
kazi, muundo au kigeu cha ngazi ya juu ni la programu nzima: majina mawili
yanayofanana kwenye moduli tofauti ni mgongano. Kwa hiyo kila moduli ina
kiambishi chake.

## Kanuni

1. Kila jina la ngazi ya juu huanza na kiambishi cha moduli lake, kisha
   `_` na jina kwa Kiswahili kwa mtindo wa `chini_chini`
   (`dola_unda`, `kalenda_panga`, `skrini_siasa_chora`).
2. Konstanti huandikwa kwa herufi kubwa zenye kiambishi hicho hicho
   (`DOLA_UFALME_KAMILI`, `TUKIO_BUNGE`, `SKRINI_UPAU_WA_JUU`).
3. Kazi ile ile ikihitajika na moduli mbili, huhamia kwenye msingi wa
   pamoja (`msingi/`) badala ya kunakiliwa kwa majina tofauti kidogo.
4. Maandishi anayoyaona mchezaji hupitia `ui("...")`
   (`moduli/onyesho/maneno.swa`); msimbo na maoni ni Kiswahili.
5. `hali`, `vunja` na `endelea` ni maneno muhimu ya Swa: hayatumiki kama majina.
6. Mkusanyaji una kikomo cha vigeu 1024 vya ngazi ya juu kwa programu
   nzima. Thamani za orodha ambazo msimbo hautaji kwa jina huandikwa kama
   maoni (`//   BAJETI_JESHI = 0`) badala ya vigeu.

## Viambishi kwa saraka

| Saraka / faili | Kiambishi | Wajibu |
|---|---|---|
| `msingi/msingi_civ.swa` | `civ_` | aina na matokeo ya pamoja |
| `msingi/lugha_dominion.swa` | `d_` | ujumbe wa uigaji kwa lugha tatu |
| `moduli/mchezo.swa` | `mchezo_` | kitu cha mchezo na mifumo yake 47 |
| `moduli/dunia/` | `dunia_` (`dunia_taifa_`, `dunia_atlasi_`, `dunia_eneo_`, ...) | dunia, mataifa, mikoa, makazi, mipaka |
| `moduli/dunia/nasibu_mt.swa` | `nasibu_mt_`, `crc32_` | nasibu ya kizalishaji cha dunia |
| `moduli/uchumi/` | jina la faili (`kodi_`, `bajeti_`, `benki_`, `soko_fedha_`, ...) | uchumi |
| `moduli/idadi_ya_watu/` | `idadi_ya_watu_`, `demografia_`, `jamii_`, `uhai_` | watu |
| `moduli/utamaduni/` | `utamaduni_`, `uandishi_` | utamaduni, imani, lugha |
| `moduli/teknolojia/` | `teknolojia_` | utafiti |
| `moduli/jeshi/` | `jeshi_`, `mapigano_`, `ushindi_` | majeshi |
| `moduli/diplomasia/` | `diplomasia_`, `shirika_`, `muungano_` | uhusiano kati ya mataifa |
| `moduli/mazingira/`, `moduli/matukio/` | `mazingira_`, `matukio_`, `hadithi_` | mazingira na matukio |
| `moduli/utawala/` | `utawala_<sehemu>_` (`utawala_bunge_`, `utawala_katiba_`, `utawala_uchaguzi_`, ...) | mfano wa utawala uliorithiwa |
| `moduli/siasa/dola.swa` | `dola_`, `itikadi_` | katiba ya kila taifa: aina ya utawala, mabaraza, vyama |
| `moduli/siasa/wahusika.swa` | `wahusika_`, `tawi_`, `tabia_` | mti wa vyeo na watu wake |
| `moduli/siasa/katiba.swa` | `katiba_` | mamlaka ya kuteua, kufuta, uhakiki, mikutano |
| `moduli/siasa/kalenda.swa` | `kalenda_` | shajara na matukio ya kudumu |
| `moduli/siasa/kikasha.swa` | `kikasha_` | ujumbe wa kila zamu |
| `moduli/siasa/` (kikundi, siasa, upinzani) | `siasa_` | mfumo wa siasa wa uigaji |
| `moduli/akili/mshauri.swa` | `akili_` | mteja wa HTTP wa mshauri wa AI |
| `moduli/akili/mazungumzo.swa` | `mazungumzo_`, `kumbukumbu_` | mazungumzo na kumbukumbu |
| `moduli/akili/uamuzi.swa` | `uamuzi_`, `UAMUZI_` | kichanganuzi cha DECISION na daftari la maamuzi |
| `moduli/akili/` (mbinu, mfumo, mkakati, msingi) | `akili_<sehemu>_` | AI ya mataifa ndani ya uigaji |
| `moduli/injini/` | `injini_<sehemu>_` | huduma za injini |
| `moduli/injini/tarehe.swa` | `tarehe_` | kalenda ya mchezo (zamu = wiki, mwaka wa kuanza 1700 hadi 2000) |
| `moduli/onyesho/turubai.swa` | `turubai_` | uchoraji wa 2D |
| `moduli/onyesho/maandishi.swa` | `maandishi_` | maandishi ya TrueType |
| `moduli/onyesho/sura.swa`, `vipengele.swa` | `sura_` | vipengele vya kiolesura |
| `moduli/onyesho/chati_kadi.swa` | `chati_` | vipengele vya dashibodi |
| `moduli/onyesho/bunge.swa` | `bunge_`, `BUNGE_` | michoro ya mabaraza |
| `moduli/onyesho/dunia_halisi.swa` | `dunia_halisi_`, `dh_` | kupakia na kuchora dunia |
| `moduli/onyesho/maneno.swa` | `maneno_`, `ui` | tafsiri ya kiolesura |
| `moduli/onyesho/wayland/` | `dirisha_`, `wayland_<sehemu>_` | mteja wa Wayland |
| `moduli/skrini/dunia.swa` | `skrini_dunia_`, `habari_`, `dunia_bofya_`, `DUNIA_`, `HABARI_` | ukurasa wa World na habari za dunia |
| `moduli/skrini/` | `skrini_<ukurasa>_`, na jina la ukurasa kwa kazi zake za ndani (`dashibodi_`, `mkutano_`, `kalenda_`, `kikasha_`, `mandhari_`, `kuwasha_`) | kurasa za mchezo |
| `moduli/programu/dominion.swa` | majina ya programu (`bonyeza`, `chora_fremu`, `kadi_`, `fungua_ukurasa`) | dirisha, ingizo, kurasa |

## Majaribio

Kila moduli ina `jaribio_<jina>.swa` kando yake. Jaribio huandika
`SHINDWA` (au `FAIL`) na hutoka kwa msimbo usio sifuri likishindwa.

## Historia

Viambishi vya mwanzo vilitokana na moduli za toleo la C (`src/core/`),
lililoondolewa baada ya uhamisho kukamilika. Ramani kamili ya C kwenda Swa
na kumbukumbu za uhamisho ziko kwenye historia ya git ya faili hili.
