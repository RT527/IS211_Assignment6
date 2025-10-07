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
def testFahrenheitConversions():
    print("Let's test Fahrenheit --> Celsius conversions...")
    test_cases = [
        (32, 0),(212, 100),(98.6, 37),(50, 10),(-40, -40)
    ]
    all_passed = True
    for fahrenheit, expected in test_cases:
        result = conversions.convertFahrenheitToCelsius(fahrenheit)
        if abs(result - expected) > 0.01:
            print(f"FAILED: {fahrenheit}F -> {result}C != {expected}C")
            all_passed = False
        else:
            print(f"PASSED: {fahrenheit}F -> {result}C (expected: {expected})")

    if all_passed:
        print("WOOHOO All Fahrenheit -> Celsius conversion tests passed!\n")
    else:
        print("OH OH, Some Fahrenheit -> Celsius tests FAILED.\n")

    print("Let's test Fahrenheit --> Kelvin conversions...")
    test_cases = [
        (32, 273.15),(212, 373.15),(98.6, 310.15),(50, 283.15),(-40, 233.15)
    ]
    all_passed = True
    for fahrenheit, expected in test_cases:
        result = conversions.convertFahrenheitToKelvin(fahrenheit)
        if abs(result - expected) > 0.01:
            print(f"FAILED: {fahrenheit}F -> {result}K != {expected}K")
            all_passed = False
        else:
            print(f"PASSED: {fahrenheit}F -> {result}K (expected: {expected})")
    if all_passed:
        print("WOOHOO All Fahrenheit -> Kelvin conversion tests passed!\n")
    else:
        print("OH OH, Some Fahrenheit -> Kelvin tests FAILED.\n")
"""---------------------------------------------------------------------------------"""
def testKelvinConversions():
    print("Let's test Kelvin --> Celsius conversions...")
    test_cases = [
        (273.15, 0),(373.15, 100),(310.15, 37),(283.15, 10),(233.15, -40)
    ]
    all_passed = True
    for kelvin, expected in test_cases:
        result = conversions.convertKelvinToCelsius(kelvin)
        if abs(result - expected) > 0.01:
            print(f"FAILED: {kelvin}K -> {result}C != {expected}C")
            all_passed = False
        else:
            print(f"PASSED: {kelvin}K -> {result}C (expected: {expected})")

    if all_passed:
        print("WOOHOO All Kelvin -> Celsius conversion tests passed!\n")
    else:
        print("OH OH, Some Kelvin -> Celsius tests FAILED.\n")

    print("Let's test Kelvin --> Fahrenheit conversions...")
    test_cases = [
        (273.15, 32),(373.15, 212),(310.15, 98.6),(283.15, 50),(233.15, -40)
    ]
    all_passed = True
    for kelvin, expected in test_cases:
        result = conversions.convertKelvinToFahrenheit(kelvin)
        if abs(result - expected) > 0.01:
            print(f"FAILED: {kelvin}K -> {result}F != {expected}F")
            all_passed = False
        else:
            print(f"PASSED: {kelvin}K -> {result}F (expected: {expected})")
    if all_passed:
        print("WOOHOO All Kelvin -> Fahrenheit conversion tests passed!\n")
    else:
        print("OH OH, Some Kelvin -> Fahrenheit tests FAILED.\n")
"""---------------------------------------------------------------------------------"""
if __name__ == "__main__":
    testCelsiusConversions()
    testFahrenheitConversions()
    testKelvinConversions()
"""---------------------------------------------------------------------------------"""
