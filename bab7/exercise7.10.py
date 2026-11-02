jawaban = {}

aktif = True

while aktif:
    nama = input("Siapa nama Anda? ")

    tempat = input("Jika bisa berlibur ke mana saja, Anda ingin ke mana? ")

    jawaban[nama] = tempat

    ulang = input("Apakah orang lain ingin menjawab? (yes/no): ")

    if ulang == "no":
        aktif = False

print("\n--- Hasil Polling ---")

for nama, tempat in jawaban.items():
    print(f"{nama} ingin berlibur ke {tempat}.")