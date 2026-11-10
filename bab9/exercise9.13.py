from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)


# Dadu 6 sisi
dadu6 = Die()

hasil = []

for i in range(10):
    hasil.append(dadu6.roll_die())

print("Hasil dadu 6 sisi:")
print(hasil)


# Dadu 10 sisi
dadu10 = Die(10)

hasil = []

for i in range(10):
    hasil.append(dadu10.roll_die())

print("\nHasil dadu 10 sisi:")
print(hasil)


# Dadu 20 sisi
dadu20 = Die(20)

hasil = []

for i in range(10):
    hasil.append(dadu20.roll_die())

print("\nHasil dadu 20 sisi:")
print(hasil)