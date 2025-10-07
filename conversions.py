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
