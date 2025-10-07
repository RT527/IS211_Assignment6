# Rafi Talukder Assignment_6
import conversions_refactored
"""---------------------------------------------------------------------------------"""
def testTemperatureConversions():
    print("Let's test ALL the Temperature Conversions =) (Celsius, Fahrenheit, Kelvin)...")
    all_passed = True
    test_cases = [
        ("celsius", "fahrenheit", 0, 32),
        ("celsius", "kelvin", 100, 373.15),
        ("fahrenheit", "celsius", 212, 100),
        ("fahrenheit", "kelvin", 32, 273.15),
        ("kelvin", "celsius", 273.15, 0),
        ("kelvin", "fahrenheit", 373.15, 212)
    ]

    for fromU, toU, val, expected in test_cases:
        try:
            result = conversions_refactored.convert(fromU, toU, val)
            if abs(result - expected) > 0.01:
                print(f"FAILED: {val} {fromU} -> {result} {toU} != {expected} {toU}")
                all_passed = False
            else:
                print(f"PASSED: {val} {fromU} -> {result} {toU} (expected: {expected})")
        except Exception as e:
            print(f"FAILED with Exception: {e}")
            all_passed = False

    if all_passed:
        print("WOOHOO All Temperature conversion tests passed!\n")
    else:
        print("OH OH, Some Temperature conversion tests FAILED.\n")
"""---------------------------------------------------------------------------------"""
def testDistanceConversions():
    print("Let's test ALL the Distance Conversions (Miles, Yards, Meters)...")
    all_passed = True

    test_cases = [
        ("miles", "yards", 1, 1760),
        ("yards", "miles", 1760, 1),
        ("meters", "yards", 100, 109.36),
        ("yards", "meters", 100, 91.44),
        ("miles", "meters", 1, 1609.34)
    ]

    for fromU, toU, val, expected in test_cases:
        try:
            result = conversions_refactored.convert(fromU, toU, val)
            if abs(result - expected) > 0.5:  # larger margin for distance rounding
                print(f"FAILED: {val} {fromU} -> {result} {toU} != {expected} {toU}")
                all_passed = False
            else:
                print(f"PASSED: {val} {fromU} -> {result} {toU} (expected: {expected})")
        except Exception as e:
            print(f"FAILED with Exception: {e}")
            all_passed = False

    if all_passed:
        print("WOOHOO All Distance conversion tests passed!\n")
    else:
        print("OH OH, Some Distance conversion tests FAILED.\n")
"""---------------------------------------------------------------------------------"""
def testSameUnitConversions():
    print("Let's test ALL Same Unit Conversions...")
    all_passed = True

    test_cases = [
        ("celsius", "celsius", 100, 100),
        ("kelvin", "kelvin", 300, 300),
        ("fahrenheit", "fahrenheit", -40, -40),
        ("miles", "miles", 2.5, 2.5),
        ("yards", "yards", 10, 10)
    ]

    for fromU, toU, val, expected in test_cases:
        try:
            result = conversions_refactored.convert(fromU, toU, val)
            if abs(result - expected) > 0.01:
                print(f"FAILED: {val} {fromU} -> {result} {toU} != {expected} {toU}")
                all_passed = False
            else:
                print(f"PASSED: {val} {fromU} -> {result} {toU} (expected: {expected})")
        except Exception as e:
            print(f"FAILED with Exception: {e}")
            all_passed = False

    if all_passed:
        print("WOOHOO All Same Unit conversion tests passed!\n")
    else:
        print("OH OH, Some Same Unit conversion tests FAILED.\n")
"""---------------------------------------------------------------------------------"""
def testIncompatibleConversions():
    print("Let's test ALL Incompatible Conversions (should raise ConversionNotPossible)...")
    incompatible_tests = [
        ("celsius", "yards", 100),
        ("kelvin", "miles", 300),
        ("meters", "fahrenheit", 10)
    ]
    all_passed = True
    for fromU, toU, val in incompatible_tests:
        try:
            conversions_refactored.convert(fromU, toU, val)
            print(f"FAILED: {fromU} -> {toU} did NOT raise ConversionNotPossible!")
            all_passed = False
        except conversions_refactored.ConversionNotPossible:
            print(f"PASSED: Properly raised ConversionNotPossible for {fromU} -> {toU}")
        except Exception as e:
            print(f"FAILED: Wrong exception for {fromU} -> {toU}: {e}")
            all_passed = False

    if all_passed:
        print("WOOHOO All Incompatible Conversion tests passed!\n")
    else:
        print("OH OH, Some Incompatible Conversion tests FAILED.\n")
"""---------------------------------------------------------------------------------"""
if __name__ == "__main__":
    testTemperatureConversions()
    testDistanceConversions()
    testSameUnitConversions()
    testIncompatibleConversions()
"""---------------------------------------------------------------------------------"""
