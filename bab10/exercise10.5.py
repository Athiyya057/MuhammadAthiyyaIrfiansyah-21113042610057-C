from pathlib import Path

path = Path("guest_book.txt")

daftar_nama = []

while True:
    nama = input("Masukkan nama (ketik quit untuk berhenti): ")

    if nama == "quit":
        break

    print(f"Terima kasih, {nama}. Nama Anda sudah dicatat.")

    daftar_nama.append(nama)

isi_file = ""

for nama in daftar_nama:
    isi_file += f"{nama}\n"

path.write_text(isi_file)

print("Buku tamu berhasil disimpan.")