from pathlib import Path

path = Path("guest.txt")

nama = input("Siapa nama Anda? ")

path.write_text(nama)

print("Nama berhasil disimpan.")