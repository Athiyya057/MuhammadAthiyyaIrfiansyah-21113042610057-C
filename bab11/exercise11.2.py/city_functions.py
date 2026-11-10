def city_country(city, country, population=0):
    

    hasil = f"{city.title()}, {country.title()}"

    if population:
        hasil += f" - population {population}"

    return hasil