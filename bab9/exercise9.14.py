from random import choice

kemungkinan = [
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10,
    "A", "B", "C", "D", "E"
]

tiket_menang = []

print("Mengundi tiket pemenang...")

while len(tiket_menang) < 4:
    item = choice(kemungkinan)

    if item not in tiket_menang:
        tiket_menang.append(item)

print("\nKombinasi tiket pemenang:")
print(tiket_menang)

print("Tiket dengan kombinasi tersebut memenangkan hadiah!")