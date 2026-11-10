from pathlib import Path
import json

path = Path("favorite_number.json")

try:
    isi = path.read_text()

except FileNotFoundError:
    angka = input("Berapa angka favorit Anda? ")

    isi = json.dumps(angka)

    path.write_text(isi)

    print("Angka favorit berhasil disimpan.")

else:
    angka = json.loads(isi)

    print(f"Saya ingat angka favorit Anda! Angkanya adalah {angka}.")