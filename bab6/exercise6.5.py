rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "citarum": "indonesia"
}

print("RIVER AND COUNTRY")

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nRIVERS:")

for river in rivers.keys():
    print(river.title())

print("\nCOUNTRIES:")

for country in rivers.values():
    print(country.title())