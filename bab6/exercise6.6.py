favorite_languages = {
    "Athiyya": "python",
    "Abi": "c",
    "Naufal": "rust",
    "Akbar": "python"
}

people = [
    "Athiyya",
    "Abi",
    "fayaz",
    "nafis",
    "khairul",
    "samuel"
]

for person in people:
    if person in favorite_languages.keys():
        print(f"Thank you, {person.title()}, for taking the poll.")
    else:
        print(f"{person.title()}, please take our poll!")