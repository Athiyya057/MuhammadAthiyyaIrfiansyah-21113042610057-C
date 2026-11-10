print("Ketik q kapan saja untuk berhenti.")

while True:
    try:
        angka1 = input("\nMasukkan angka pertama: ")

        if angka1 == "q":
            break

        angka1 = int(angka1)

        angka2 = input("Masukkan angka kedua: ")

        if angka2 == "q":
            break

        angka2 = int(angka2)

    except ValueError:
        print("Maaf, Anda harus memasukkan angka.")

    else:
        hasil = angka1 + angka2

        print(f"Hasil penjumlahan adalah {hasil}.")