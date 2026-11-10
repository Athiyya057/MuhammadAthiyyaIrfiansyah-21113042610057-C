from pathlib import Path
import json

path = Path("favorite_number.json")

isi = path.read_text()

angka = json.loads(isi)

print(f"Saya tahu angka favorit Anda! Angkanya adalah {angka}.")