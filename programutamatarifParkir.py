import tarif_parkir

print("PILIH JENIS KENDARAAN")
print("1. Becak")
print("2. Motor")
print("3. Mobil")
print("4. Micro Bus / Box / ELF")

jenis = int(input("Masukkan jenis kendaraan: "))
tanggal = input("Masukkan tanggal parkir: ")
jam_masuk = int(input("Masukkan jam masuk (0-23): "))
jam_keluar = int(input("Masukkan jam keluar (0-23): "))

if (
    jenis in [1, 2, 3, 4]
    and 0 <= jam_masuk <= 23
    and 0 <= jam_keluar <= 23
):
    dasar, progresif, inap, total, lama = (
        tarif_parkir.hitung_parkir(
            jenis, jam_masuk, jam_keluar
        )
    )

    nama = ["Becak", "Motor", "Mobil", "Micro Bus / Box / ELF"]

    print("\n=============")
    print("Jenis kendaraan:", nama[jenis - 1])
    print("Tanggal:", tanggal)
    print("Jam masuk:", jam_masuk)
    print("Jam keluar:", jam_keluar)
    print("Lama parkir:", lama, "jam")
    print("Tarif dasar: Rp", dasar)
    print("Tarif progresif: Rp", progresif)
    print("Tarif inap: Rp", inap)
    print("Total tarif: Rp", total)
    print("=============")
else:
    print("Input tidak valid")