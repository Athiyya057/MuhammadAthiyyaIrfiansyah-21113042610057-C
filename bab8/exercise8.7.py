def make_album(artis, judul, jumlah_lagu=None):
    album = {
        "artis": artis,
        "judul": judul
    }

    if jumlah_lagu is not None:
        album["jumlah_lagu"] = jumlah_lagu

    return album

print(make_album("Tulus", "Manusia"))
print(make_album("Hindia", "Menari dengan Bayangan"))
print(make_album("NIKI", "Nicole", 12))