from random import choice

kemungkinan = [
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10,
    "A", "B", "C", "D", "E"
]

my_ticket = [3, "A", 7, "D"]

jumlah_percobaan = 0

while True:
    tiket_menang = []

    while len(tiket_menang) < 4:
        item = choice(kemungkinan)

        if item not in tiket_menang:
            tiket_menang.append(item)

    jumlah_percobaan += 1

    if set(tiket_menang) == set(my_ticket):
        break

print("Tiket saya:", my_ticket)
print("Tiket pemenang:", tiket_menang)
print("Jumlah percobaan:", jumlah_percobaan)