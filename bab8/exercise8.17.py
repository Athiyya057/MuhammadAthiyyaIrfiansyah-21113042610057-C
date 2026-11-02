def hitung_luas(panjang, lebar):
    """Menghitung luas persegi panjang."""
    luas = panjang * lebar
    return luas


def tampilkan_hasil(luas):
    """Menampilkan hasil perhitungan luas."""
    print(f"Luas persegi panjang: {luas}")


hasil = hitung_luas(10, 5)
tampilkan_hasil(hasil)