from pathlib import Path
import json

angka = input("Berapa angka favorit Anda? ")

path = Path("favorite_number.json")

isi = json.dumps(angka)

path.write_text(isi)

print("Angka favorit berhasil disimpan.")