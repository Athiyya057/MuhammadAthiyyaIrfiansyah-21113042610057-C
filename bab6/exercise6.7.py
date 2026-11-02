person_1 = {
    "first_name": "Muhammad",
    "last_name": "Athiyya",
    "age": 18,
    "city": "Ponorogo"
}

person_2 = {
    "first_name": "Naufal",
    "last_name": "Rizky",
    "age": 18,
    "city": "Cilacap"
}

person_3 = {
    "first_name": "Fayaz",
    "last_name": "Rasyid",
    "age": 18,
    "city": "Magelang"
}

people = [person_1, person_2, person_3]

for person in people:
    print("\nPERSON INFORMATION")
    print(f"First Name: {person['first_name']}")
    print(f"Last Name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")