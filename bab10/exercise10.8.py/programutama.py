from pathlib import Path

daftar_file = ["cats.txt", "dogs.txt"]

for nama_file in daftar_file:
    print(f"\nMembaca file: {nama_file}")

    path = Path(nama_file)

    try:
        isi = path.read_text()

    except FileNotFoundError:
        print("Maaf, file tidak ditemukan.")

    else:
        print(isi)