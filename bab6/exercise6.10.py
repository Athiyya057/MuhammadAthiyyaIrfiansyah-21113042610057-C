favorite_numbers = {
    "Athiyya": [11, 22, 8],
    "Abi": [3, 7],
    "Naufal": [5, 12, 20],
    "Fayaz": [4, 9],
    "Akbar": [2, 6, 69]
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name}'s favorite numbers:")

    for number in numbers:
        print(number)