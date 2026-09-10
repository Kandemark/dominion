#!/usr/bin/env python3
"""
kagua-mpangilio.py — inagundua wito wa kazi iliyofafanuliwa BAADAYE
kwenye faili moja la .swa.

Kwa nini: mkusanyaji wa Swa (stage1, hadi lugha-swa/swa#180
irekebishwe) haukagui idadi ya hoja za kazi iliyofafanuliwa baadaye
kwenye faili moja lile lile — kazi hiyo bado haijasajiliwa wakati
mwito wake unakaguliwa, na ukaguzi unaruka kimya (angalia ripoti ya
mdudu #180). Msimbo unaokusanya bila hitilafu bado unaweza kutoa
tabia isiyofafanuliwa wakati wa kukimbia.

Script hii haihitaji kubadilisha Swa — inasoma faili la .swa kwa
maandishi tu na kuripoti wito wowote unaoita kazi ambayo
imefafanuliwa CHINI ya mahali wito ulipo (isipokuwa kujiita
kwenyewe — recursion ni salama, kwa sababu kazi husajiliwa kabla
ya mwili wake kukaguliwa).

Matumizi: python3 gharama/kagua-mpangilio.py <faili1.swa> [faili2.swa ...]
Kutoka: 0 = safi, 1 = kuna wito wa mbele hatarishi.
"""

import re
import sys

# Kazi/maneno ya lugha yenyewe — si majina ya kazi za mtumiaji, kamwe
# usizichukulie kama "zilizofafanuliwa baadaye".
MANENO_MUHIMU = {
    "muundo", "rudisha", "kama", "sivyo", "wakati", "kwa", "fanya",
    "vunja", "endelea", "chagua", "hali", "husisha", "achilia",
}

# Wito maalum wa mkusanyaji (builtin) — hauhitaji usajili wa awali.
BUILTIN = {"wito_wa_mfumo"}

MSTARI_WA_KAZI = re.compile(
    r"^[A-Z]\d*\*?\s+([a-z_][a-zA-Z0-9_]*)\s*\("
)
WITO_WA_KAZI = re.compile(r"\b([a-z_][a-zA-Z0-9_]*)\s*\(")


def tafuta_kazi(mistari):
    """Rudisha {jina_la_kazi: (mstari_wa_mwanzo, mstari_wa_mwisho)}."""
    kazi = {}
    i = 0
    n = len(mistari)
    while i < n:
        m = MSTARI_WA_KAZI.match(mistari[i])
        if m and "{" in "".join(mistari[i : i + 3]):
            jina = m.group(1)
            if jina in MANENO_MUHIMU:
                i += 1
                continue
            # Tafuta { ya kwanza na } inayolingana kwa kuhesabu kina.
            kina = 0
            j = i
            imeanza = False
            while j < n:
                for ch in mistari[j]:
                    if ch == "{":
                        kina += 1
                        imeanza = True
                    elif ch == "}":
                        kina -= 1
                if imeanza and kina == 0:
                    break
                j += 1
            kazi[jina] = (i, j)
            i = j + 1
        else:
            i += 1
    return kazi


def kagua_faili(njia):
    with open(njia, encoding="utf-8") as f:
        mistari = f.readlines()

    kazi = tafuta_kazi(mistari)
    matatizo = []

    for jina, (mwanzo, mwisho) in kazi.items():
        mwili = "".join(mistari[mwanzo : mwisho + 1])
        kwa_hoja = set(WITO_WA_KAZI.findall(mwili))
        for lengwa in kwa_hoja:
            if lengwa == jina:
                continue  # kujiita — salama
            if lengwa in MANENO_MUHIMU or lengwa in BUILTIN:
                continue
            if lengwa in kazi:
                lengwa_mwanzo = kazi[lengwa][0]
                if lengwa_mwanzo > mwanzo:
                    matatizo.append(
                        (njia, mwanzo + 1, jina, lengwa, lengwa_mwanzo + 1)
                    )
    return matatizo


def main():
    if len(sys.argv) < 2:
        print("matumizi: kagua-mpangilio.py <faili1.swa> [faili2.swa ...]")
        return 2

    jumla = 0
    for njia in sys.argv[1:]:
        matatizo = kagua_faili(njia)
        for njia_f, mstari_a, kazi_a, kazi_b, mstari_b in matatizo:
            print(
                f"{njia_f}:{mstari_a}: kazi '{kazi_a}' inaita '{kazi_b}' "
                f"ambayo imefafanuliwa baadaye ({njia_f}:{mstari_b}) — "
                f"panga upya (mdudu lugha-swa/swa#180)"
            )
            jumla += 1

    if jumla:
        print(f"\nkagua-mpangilio: matatizo {jumla}")
        return 1
    print("kagua-mpangilio: safi")
    return 0


if __name__ == "__main__":
    sys.exit(main())
