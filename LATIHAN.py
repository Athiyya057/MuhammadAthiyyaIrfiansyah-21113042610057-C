jenisGolongan = int(input("Masukkan jenis golongan: "))
berat = float(input("Masukkan berat barang (kg): "))
jarak = float(input("Masukkan jarak pengiriman (km): "))

def penentuanTarif(jenisGolongan, berat, jarak):
    if jenisGolongan == 1:
        tarifDasar = 2000
    elif jenisGolongan == 2:
        tarifDasar = 10000
    elif jenisGolongan== 3:
        tarifDasar = 20000
    if 0 < berat <= 5:
        tarifBerat = 2000
    elif 5 < berat <= 20:
        tarifBerat = 10000
    elif berat > 20:
        tarifBerat = 20000
    if 0 < jarak <= 10:
        tarifJarak = 2000
    elif 10 < jarak <= 30:
        tarifJarak = 10000
    elif jarak > 30:
        tarifJarak = 20000
    
    return jenisGolongan, berat, jarak, tarifDasar, tarifBerat, tarifJarak

jenisGolongan, berat, jarak, tarifDasar, tarifBerat, tarifJarak = penentuanTarif(jenisGolongan, berat, jarak)
totaltarif = tarifDasar + tarifJarak + tarifBerat
print("="*50)
print("Jenis kendaraan: ", jenisGolongan)
print("Tarif dasar: ", tarifDasar)
print("Tarif berat: ", tarifBerat)
print("Tarif jarak: ", tarifJarak)
print("Total biaya: ", totaltarif)
print("="*50)