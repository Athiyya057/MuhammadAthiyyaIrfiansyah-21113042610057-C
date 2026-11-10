from city_functions import city_country


def test_city_country():
    hasil = city_country("santiago", "chile")

    assert hasil == "Santiago, Chile"