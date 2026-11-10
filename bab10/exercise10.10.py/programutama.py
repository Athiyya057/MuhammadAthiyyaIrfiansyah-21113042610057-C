from pathlib import Path

path = Path("teks.txt")

try:
    isi = path.read_text()

except FileNotFoundError:
    print("File tidak ditemukan.")

else:
    jumlah = isi.lower().count("the")
    jumlah_spasi = isi.lower().count("the ")

    print(f"Kata 'the' muncul sebanyak {jumlah} kali.")
    print(f"Kata 'the ' muncul sebanyak {jumlah_spasi} kali.")