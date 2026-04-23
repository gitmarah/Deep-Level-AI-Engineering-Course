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


def main():
    print("=== Tip Calculator ===")
    while True:
        try:
            bill = float(input("Bill (NLe): "))
            tip = float(input("Tip Percentage: "))
            split = int(input("Split Among: "))
            result = calculate_tip(bill, tip, split)
            print(f"Tip: NLe {result["tip"]:.2f}")
            print(f"Total: NLe {result["total"]:.2f}")
            print(f"Bill per person: NLe {result["per_person"]:.2f}")
        except ValueError as e:
            print(f"Error: {e}")
        again = input("Would you like continue? (y/n): ").strip().lower()
        if again != "y":
            break
    print("\nThanks for using The Village Tip Calculator!")            


if __name__ == "__main__":
    main()
