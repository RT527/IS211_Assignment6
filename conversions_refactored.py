# Rafi Talukder Assignment_6
"""---------------------------------------------------------------------------------"""
class ConversionNotPossible(Exception):
    """Custom exception for incompatible unit conversions."""
    pass
"""---------------------------------------------------------------------------------"""
def convert(fromUnit, toUnit, value):
    """
        1. fromUnit - the unit we are converting from (string)
        2. toUnit - the unit we are converting to (string)
        3. value - the numeric value of fromUnit we are converting from
    """
    #Normalize the input for case-insensitivity
    fromUnit = fromUnit.lower()
    toUnit = toUnit.lower()
    temperature_units = ["celsius", "fahrenheit", "kelvin"]
    distance_units = ["miles", "yards", "meters"]

    if fromUnit == toUnit: #Check same-unit conversion
        return round(value, 2)
    #Temperature conversions
    if fromUnit in temperature_units and toUnit in temperature_units:
        if fromUnit == "celsius":
            if toUnit == "fahrenheit":
                return round((value * 9/5) + 32, 2)
            elif toUnit == "kelvin":
                return round(value + 273.15, 2)

        elif fromUnit == "fahrenheit":
            if toUnit == "celsius":
                return round((value - 32) * 5/9, 2)
            elif toUnit == "kelvin":
                return round((value - 32) * 5/9 + 273.15, 2)

        elif fromUnit == "kelvin":
            if toUnit == "celsius":
                return round(value - 273.15, 2)
            elif toUnit == "fahrenheit":
                return round((value - 273.15) * 9/5 + 32, 2)
    if fromUnit in distance_units and toUnit in distance_units: # Distance conversions
        #Convert all the distances to meters first
        to_meters = {
            "miles": value * 1609.34,
            "yards": value * 0.9144,
            "meters": value
        }
        meters_value = to_meters[fromUnit]
        #Convert from meters to target unit
        from_meters = {
            "miles": meters_value / 1609.34,
            "yards": meters_value / 0.9144,
            "meters": meters_value
        }
        return round(from_meters[toUnit], 2)
    #If units don't match any valid categories
    raise ConversionNotPossible(f"Can't convert from {fromUnit} to {toUnit} — these are incompatible units!WOMP WOMP!")
"""---------------------------------------------------------------------------------"""
