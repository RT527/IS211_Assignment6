#Rafi Talukder Assignment_6
import conversions
"""---------------------------------------------------------------------------------"""
def testCelsiusConversions():
    print("Let's test Celsius --> Fahrenheit conversions...")
    test_cases = [
        (0, 32),(90, 194),(80, 176),(-40, -40),(25, 77)
    ]
    for celsius, expected in test_cases:
        result = conversions.convertCelsiusToFahrenheit(celsius)
        print(f"Celsius: {celsius} -> Fahrenheit: {result} (expected: {expected})")
        assert abs(result - expected) < 0.01, f"FAILED: {celsius}C -> {result}F != {expected}F"
    print("All Celsius -> Fahrenheit conversion tests passed!WOOHOO!\n")

    print("Let's test Celsius --> Kelvin conversions...")
    test_cases = [
        (0, 273.15),(-40, 233.15),(50, 323.15),(10,283.15),(25, 298.15)
    ]
    for celsius, expected in test_cases:
        result = conversions.convertCelsiusToKelvin(celsius)
        print(f"Celsius: {celsius} -> Kelvin: {result} (expected: {expected})")
        assert abs(result - expected) < 0.01, f"FAILED: {celsius}C -> {result}K != {expected}K"
    print("All Celsius -> Kelvin conversion tests passed!WOOHOO!\n")
"""---------------------------------------------------------------------------------"""
if __name__ == "__main__":
    testCelsiusConversions()
