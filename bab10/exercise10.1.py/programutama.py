from pathlib import Path

path = Path("learning_python.txt")
isi = path.read_text()

print("--- Membaca seluruh isi file ---")
print(isi)

print("--- Membaca file menggunakan perulangan ---")

for baris in isi.splitlines():
    print(baris)