def convertToCelius(value, unit):
    unit = unit.upper()
    if unit == "C":
        return value
    if unit == "F":
        return (value - 32) * (5/9)
    if unit == "K":
        return value - 273.15
    raise ValueError(f"\nUnknown unit {unit}\n(Unit must either be C, F or K)")


def convertFromCelius(celcius):
    return {
        "C": celcius,
        "F": celcius * 9/5 + 32,
        "K": celcius + 273.15
    }


def main():
    print("=== The Village Temp Converter ===")
    while True:
        try:
            value = float(input("Enter Value: "))
            unit = input("Enter unit (C, F or K): ").strip().upper()
            celcius = convertToCelius(value, unit)
            result = convertFromCelius(celcius)
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
