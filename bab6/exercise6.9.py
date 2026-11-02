favorite_places = {
    "Athiyya": ["Ponorogo", "Tangerang", "Bali"],
    "Abi": ["Kediri", "Malang"],
    "Akbar": ["Surakarta", "Semarang", "Lombok"]
}

for name, places in favorite_places.items():
    print(f"\n{name}'s favorite places:")

    for place in places:
        print(f"- {place}")