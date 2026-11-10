try:
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))

except ValueError:
    print("Maaf, Anda harus memasukkan angka.")

else:
    hasil = angka1 + angka2

    print(f"Hasil penjumlahan {angka1} dan {angka2} adalah {hasil}.")