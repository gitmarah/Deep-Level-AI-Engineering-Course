def calculate_tip(bill, tip, split=1):
    if bill < 0:
        raise ValueError("Bill cannot be negative!")
    if tip < 0:
        raise ValueError("Tip percent cannot be negative!")
    if split < 1:
        raise ValueError("Split cannot be negative!")
    tip_amount = (bill * tip) / 100
    total = bill + tip_amount
    per_person = total / split
    return {
        "tip": tip_amount,
        "total": total,
        "per_person": per_person
    }


def greet(first, last="", style="fiendly"):
    full = f"{first} {last}".strip()
    style = style.lower()
    if style == "friendly":
        return f"\nHey, {first}.\nWelcome to Greco!\n"
    if style == "formal":
        return f"\nWelcome to Greco.\nMr./Ms. {last or first}.\n"
    if style == "excited":
        return f"\nWOW {full}, So glad you are here.\nWelcome to Greco\n"
    return f"Hello {full}!"


def main():
    print("=== Greco Tip Calculator ===")
    while True:
        try:
            first = input("\nFirst name: ").strip()
            last = input("Last name: ").strip()
            style = (
                input("Style (friendly, formal, excited): ").strip()
                or "friendly"
            )
            print(f"{greet(first, last, style)}")
            bill = float(input("Bill (NLe): "))
            tip = float(input("Tip Percentage: "))
            split = int(input("Split Among: "))
            result = calculate_tip(bill, tip, split)
            print(f"Tip: NLe {result["tip"]:.2f}")
            print(f"Total: NLe {result["total"]:.2f}")
            print(f"Bill per person: NLe {result["per_person"]:.2f}")
        except ValueError as e:
            print(f"Error: {e}")
        again = input("\nWould you like continue? (y/n): ").strip().lower()
        if again != "y":
            break
    print("\nThanks for using The Village Tip Calculator!")


if __name__ == "__main__":
    main()
