def hitung_gaji(jam_kerja, upah_per_jam):
    if jam_kerja <= 40:
        gaji = jam_kerja * upah_per_jam
    else:
        gaji_normal = 40 * upah_per_jam
        jam_lembur = jam_kerja - 40
        gaji_lembur = jam_lembur * upah_per_jam * 1.5
        gaji = gaji_normal + gaji_lembur

    return gaji, gaji_normal, gaji_lembur


jam = float(input("Masukkan jumlah jam kerja: "))
upah = float(input("Masukkan upah per jam: "))

if jam >= 0 and upah >= 0:
    total_gaji = hitung_gaji(jam, upah)
    print("Gaji normal: ", ga)
    print("Total gaji: Rp", total_gaji)
else:
    print("Input tidak valid")