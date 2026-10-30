def hitung_parkir(jam):
    if jam <= 0:
        return 0
    elif jam <= 1:
        return 3000
    else:
        return 3000 + (jam - 1) * 2000


jam = int(input("Masukkan lama parkir (jam): "))

if jam >= 0:
    tarif = hitung_parkir(jam)
    print("Total tarif parkir: Rp", tarif)
else:
    print("Lama parkir tidak valid")