cities = {
    "jakarta": {
        "country": "indonesia",
        "population": 10600000,
        "fact": "The capital city of Indonesia."
    },

    "tokyo": {
        "country": "japan",
        "population": 14000000,
        "fact": "One of the world's largest metropolitan areas."
    },

    "paris": {
        "country": "france",
        "population": 2100000,
        "fact": "Famous for the Eiffel Tower."
    }
}

for city, information in cities.items():
    print(f"\nCITY: {city.title()}")
    print(f"Country: {information['country'].title()}")
    print(f"Population: {information['population']:,}")
    print(f"Fact: {information['fact']}")