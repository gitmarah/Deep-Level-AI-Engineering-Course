def convertToCelius(value, unit):
    unit = unit.upper()
    if unit == "C":
        return value
    if unit == "F":
        return (value - 32) * (5/9)
    if unit == "K":
        return value - 273.15
    raise ValueError(f"\nUnknown unit {unit}\n(Unit must either be C, F or K)")


def average_result(celcius, celcius2):
    return {
        "C": (celcius + celcius2) / 2,
        "F": (celcius * 9/5 + 32) + (celcius2 * 9/5 + 32) / 2,
        "K": (celcius + 273.15 + celcius2 + 273.15) / 2
    }


def main():
    print("=== The Village Temp Converter ===")
    while True:
        try:
            value = float(input("First Value: "))
            value2 = float(input("Second Value: "))
            unit = input("Enter unit (C, F or K): ").strip().upper()
            celcius = convertToCelius(value, unit)
            celcius2 = convertToCelius(value2, unit)
            result = average_result(celcius, celcius2)
            print(f"Celcius: {result["C"]:.2f}°C")
            print(f"Farenheit: {result["F"]:.2f}°F")
            print(f"Kelvin: {result["K"]:.2f}K\n")
            if result["K"] < 0:
                print("Warning, the temperature is below 0 K")
        except ValueError as e:
            print(f"Error: {e}\n") 
        again = input("Would you like continue? (y/n): ").strip().lower()
        if again != "y":
            break
    print("\nThanks for using The Village Temp Converter!")


if __name__ == "__main__":
    main()
