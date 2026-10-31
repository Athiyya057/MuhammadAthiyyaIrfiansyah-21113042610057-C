foods = ("Nasi Goreng", "Ayam Bakar", "Sate", "Soto", "Rendang")

print("Original menu:")

for food in foods:
    print(food)

# Mencoba mengubah salah satu elemen tuple
try:
    foods[0] = "Mie Goreng"
except TypeError:
    print("\nTuple tidak dapat diubah secara langsung.")

# Membuat ulang tuple dengan menu baru
foods = ("Mie Goreng", "Ayam Bakar", "Sate", "Bakso", "Rendang")

print("\nModified menu:")

for food in foods:
    print(food)