#Rafi Talukder Assignment_6
"""---------------------------------------------------------------------------------"""
def convertCelsiusToKelvin(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    kelvins = celsius + 273.15
    return round(kelvins, 2)
"""---------------------------------------------------------------------------------"""
def convertCelsiusToFahrenheit(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit,2)
"""---------------------------------------------------------------------------------"""
def convertFahrenheitToCelsius(fahrenheit):
    """Takes in a float representing a Fahrenheit measurement, and returns that temperature converted into Celsius"""
    celsius = (fahrenheit - 32) * 5/9
    return round(celsius, 2)
"""---------------------------------------------------------------------------------"""
def convertFahrenheitToKelvin(fahrenheit):
    """Takes in a float representing a Fahrenheit measurement, and returns that temperature converted into Kelvins"""
    kelvins = (fahrenheit - 32) * 5/9 + 273.15
    return round(kelvins, 2)
"""---------------------------------------------------------------------------------"""
def convertKelvinToCelsius(kelvins):
    """Takes in a float representing a Kelvin measurement, and returns that temperature converted into Celsius"""
    celsius = kelvins - 273.15
    return round(celsius, 2)
"""---------------------------------------------------------------------------------"""
def convertKelvinToFahrenheit(kelvins):
    """Takes in a float representing a Kelvin measurement, and returns that temperature converted into Fahrenheit"""
    fahrenheit = (kelvins - 273.15) * 9/5 + 32
    return round(fahrenheit, 2)
"""---------------------------------------------------------------------------------"""