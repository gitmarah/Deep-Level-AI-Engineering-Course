from datetime import date


def convert_age(dob: date):
    today = date.today()
    if dob > today:
        raise ValueError("Invaid date of birth!")
    years = today.year - dob.year
    months = today.month - dob.month
    days = today.day - dob.day
    if days < 0:
        months -= 1
        prev_month_end = (
            today.replace(day=1) - __import__("datetime").timedelta(days=1))
        days += prev_month_end.day
    if months < 0:
        years -= 1
        months += 12
    total_days = (today - dob).days
    total_weeks = total_days // 7
    total_months = years * 12 + months
    return {
        "years": years,
        "months": months,
        "days": days,
        "total_days": total_days,
        "total_weeks": total_weeks,
        "total_months": total_months,
    }


def main():
    print("=== Age Converter ===")
    while True:
        try:
            raw = input("Date of Birth (YYYY-MM-DD): ").strip()
            dob = date.fromisoformat(raw)
            result = convert_age(dob)
            print(
                f"\nAge: {result["years"]} years, {result["months"]} months, {result["days"]} days"
            )
            print(f"Total days: {result["total_days"]}")
            print(f"Total months: {result["total_months"]}")
            print(f"Total weeks: {result["total_weeks"]}")
        except ValueError as e:
            print(f"Error: {e}")
        again = input("Convert another age(y/n): ").strip().lower()
        if again != "y":
            break
    print("Thanks for using The Age Converter")


if __name__ == "__main__":
    main()
