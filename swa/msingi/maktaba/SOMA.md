# maktaba/ — nakala ya maktaba ya kawaida ya Swa

Faili hizi ni nakala (vendored) kutoka lugha-swa/swa
(fda20bdbeebc68f66b9bef7e6d1fd2c1a72d8a3d, 2026-09-05), si kiungo
cha moja kwa moja kwenye hazina ya mkusanyaji. Sababu: `husisha`
inatatua `msingi/` na `msingi/maktaba/` kwa uhusiano na saraka ya
kazi ya mchakato pekee — kuweka nakala hapa inafanya ujenzi wa
Dominion kuwa huru na eneo halisi la hazina ya `swa` kwenye diski.

**Hazijaletwa `wakati.swa` na `nasibu.swa`** — hizi mbili pekee kati
ya maktaba ya kawaida bado zinategemea `husisha C::stdlib` (time()
na rand()/srand()). Kwa kuwa lengo la Dominion ni sifuri utegemezi
wa lugha nyingine, kimakusudi hazijaletwa — ukihitaji muda au namba
za nasibu, tumia syscall za moja kwa moja (`wito_wa_mfumo`) badala
yake.

Kusasisha: nakili tena kutoka `msingi/maktaba/*.swa` ya hazina ya
`swa`, ukiacha `wakati.swa`/`nasibu.swa`, na sasisha hash ya commit
hapo juu.
