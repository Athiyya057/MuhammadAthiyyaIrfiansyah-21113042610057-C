from unittest import result


def luasPersegi(panjang, lebar):
    luas = panjang * lebar
    return luas

def luasLingkaran(jari_jari):
    luas = 3.14 * jari_jari * jari_jari
    return luas

def volTabung(jari_jari, tinggi):
    volume = 3.14 * jari_jari * jari_jari * tinggi
    return volume

def main():
    jari2 = float(input("Masukkan jari-jari lingkaran: "))
    tinggi = float(input("Masukkan tinggi tabung: "))
    volTab = volTabung(jari2, tinggi)
    print("volTabung: ", volTab)

if __name__ == "__main__":
    main()