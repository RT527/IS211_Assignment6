# Rafi Talukder Assignment_6
import conversions
"""---------------------------------------------------------------------------------"""
def testCelsiusConversions():
    print("Let's test Celsius --> Fahrenheit conversions...")
    test_cases = [
        (0, 32),(90, 194),(80, 176),(-40, -40),(25, 77)
    ]
    all_passed = True
    for celsius, expected in test_cases:
        result = conversions.convertCelsiusToFahrenheit(celsius)
        if abs(result - expected) > 0.01:
            print(f"FAILED: {celsius}C -> {result}F != {expected}F")
            all_passed = False
        else:
            print(f"PASSED: {celsius}C -> {result}F (expected: {expected})")

    if all_passed:
        print("WOOHOO All Celsius -> Fahrenheit conversion tests passed!\n")
    else:
        print("OH OH, Some Celsius -> Fahrenheit tests FAILED.\n")

    print("Let's test Celsius --> Kelvin conversions...")
    test_cases = [
        (0, 273.15),(-40, 233.15),(50, 323.15),(10, 283.15),(25, 298.15)
    ]
    all_passed = True
    for celsius, expected in test_cases:
        result = conversions.convertCelsiusToKelvin(celsius)
        if abs(result - expected) > 0.01:
            print(f"FAILED: {celsius}C -> {result}K != {expected}K")
            all_passed = False
        else:
            print(f"PASSED: {celsius}C -> {result}K (expected: {expected})")
    if all_passed:
        print("WOOHOO All Celsius -> Kelvin conversion tests passed!\n")
    else:
        print("OH, OH Some Celsius -> Kelvin tests FAILED.\n")
"""---------------------------------------------------------------------------------"""
if __name__ == "__main__":
    testCelsiusConversions()
