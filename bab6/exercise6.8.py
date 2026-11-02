pet_1 = {
    "animal": "Bird",
    "owner": "Athiyya"
}

pet_2 = {
    "animal": "Cat",
    "owner": "Naufal"
}

pet_3 = {
    "animal": "Elephant",
    "owner": "Abi"
}

pet_4 = {
    "animal": "Cow",
    "owner": "Akbar"
}

pets = [pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print(f"\nAnimal: {pet['animal'].title()}")
    print(f"Owner: {pet['owner']}")