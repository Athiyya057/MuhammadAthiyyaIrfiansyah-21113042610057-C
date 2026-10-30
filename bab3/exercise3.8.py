places = ["Jepang", "Swiss", "Paris", "Korea Selatan", "Italia"]

print("Urutan asli:")
print(places)

print("\nUrutan alfabetis:")
print(sorted(places))

print("\nUrutan alfabetis terbalik:")
print(sorted(places, reverse=True))

print("\nUrutan asli dibalik:")
places.reverse()
print(places)

print("\nKembali ke urutan asli:")
places.reverse()
print(places)

print("\nUrutan alfabetis permanen:")
places.sort()
print(places)

print("\nUrutan alfabetis terbalik permanen:")
places.sort(reverse=True)
print(places)