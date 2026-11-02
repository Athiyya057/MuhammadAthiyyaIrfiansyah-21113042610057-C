def make_album(artis, judul):
    return {
        "artis": artis,
        "judul": judul
    }

while True:
    print("\nMasukkan data album (ketik q untuk berhenti).")

    artis = input("Nama artis: ")

    if artis == "q":
        break

    judul = input("Judul album: ")

    if judul == "q":
        break

    album = make_album(artis, judul)
    print(album)