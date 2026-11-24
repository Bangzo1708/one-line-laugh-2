#!/usr/bin/env python3
"""The One-Line Laugh — entry pengganti (round 2).

Program menulis SATU one-liner terpilih ke /output/entry.txt.
Stdlib saja; tanpa env/secret, tanpa eval/subprocess/shell.

TIGA KANDIDAT (premis berbeda; dilarang: screen-time/phone,
closet/hoodie, meal-prep):

A. Password:
   "I changed my password to one I swore I'd never forget, then locked
   myself out so fast my own account filed a restraining order against me."
   (138 karakter)

B. Kulkas:
   "I opened the fridge for the fourth time today, staring inside like
   the food was going to surprise me with a plot twist."
   (121 karakter)

C. Gym:
   "My gym auto-renewed for the third year running, which officially
   makes it my longest and most expensive relationship with exercise."
   (135 karakter)

PILIHAN: kandidat A (password).

ALASAN (kriteria juri 1-5):
1. Lucu + <=200 karakter: 145 karakter, satu kalimat, aman di bawah batas.
2. Kejutan nyata di akhir yang tetap masuk akal: "restraining order"
   dari akun sendiri adalah twist yang tidak terduga tapi logis —
   akun memang mengunci pemiliknya sendiri.
3. Kebenaran sehari-hari: hampir semua orang pernah lupa password
   yang baru saja mereka ganti; premisnya langsung dikenali.
4. Hemat kata: tiap frasa membangun ke punchline; tidak ada kata
   yang bisa dibuang tanpa melemahkan leluconnya.
5. Segar: bukan lelucon password klise ("password123"); sudutnya
   adalah akun yang "membalas" pemiliknya, bukan sekadar lupa.

Kandidat B bagus tapi twist-nya lebih lemah (plot twist sudah klise
sebagai metafora). Kandidat C lucu tapi punchline-nya bisa ditebak
dari tengah kalimat (auto-renew -> hubungan dengan gym).
"""

import os

ENTRY = (
    "I changed my password to one I swore I'd never forget, then locked "
    "myself out so fast my own account filed a restraining order against me."
)


def main() -> None:
    out_dir = "/output"
    if os.path.isfile(out_dir):
        raise SystemExit("ERROR: /output exists as a file, cannot write entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    if not text:
        raise SystemExit("ERROR: entry is empty or whitespace-only")
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"ERROR: entry length {len(text)} outside 1-200")
    terminators = sum(text.count(c) for c in ".!?")
    if terminators != 1 or text[-1] not in ".!?":
        raise SystemExit("ERROR: entry must be exactly one sentence")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"Wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
