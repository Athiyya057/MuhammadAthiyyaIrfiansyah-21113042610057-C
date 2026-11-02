cities = {
    "jakarta": {
        "country": "indonesia",
        "population": 10600000,
        "fact": "The capital city of Indonesia.",
        "language": "Indonesian",
        "famous_food": "Soto Betawi"
    },

    "tokyo": {
        "country": "japan",
        "population": 14000000,
        "fact": "Famous for modern technology.",
        "language": "Japanese",
        "famous_food": "Sushi"
    },

    "paris": {
        "country": "france",
        "population": 2100000,
        "fact": "Famous for the Eiffel Tower.",
        "language": "French",
        "famous_food": "Croissant"
    }
}

print("CITY INFORMATION")

for city, information in cities.items():
    print(f"\n{'=' * 30}")
    print(f"CITY: {city.title()}")
    print(f"Country: {information['country'].title()}")
    print(f"Population: {information['population']:,}")
    print(f"Fact: {information['fact']}")
    print(f"Language: {information['language']}")
    print(f"Famous Food: {information['famous_food']}")

print(f"\n{'=' * 30}")