from city_functions import city_country


def test_city_country():
    hasil = city_country("santiago", "chile")

    assert hasil == "Santiago, Chile"


def test_city_country_population():
    hasil = city_country(
        "santiago",
        "chile",
        population=5000000
    )

    assert hasil == "Santiago, Chile - population 5000000"