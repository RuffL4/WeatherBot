from project import kelvin_to_celcius, kelvin_to_fahrenheit, get_weather_type


def test_kelvin_to_celcius():
    assert round(kelvin_to_celcius(273.15), 2) == 0.00
    assert round(kelvin_to_celcius(263.15), 2) == -10.00


def test_kelvin_to_fahrenheit():
    assert round(kelvin_to_fahrenheit(273.15), 2) == 32.00
    assert round(kelvin_to_fahrenheit(0), 2) == -459.67


def test_get_weather_type():
    sample_data = {"weather":[{"description": "rain"}]}
    assert get_weather_type(sample_data) == "rain"
