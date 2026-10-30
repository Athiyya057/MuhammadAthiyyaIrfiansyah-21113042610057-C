from matematika.geometri import luasLingkaran, volTabung

jari2 = float(input("Masukkan jari-jari lingkaran: "))
tinggi = float(input("Masukkan tinggi tabung: "))
result = volTabung(jari2, tinggi)

print("volTabung: ", result)
