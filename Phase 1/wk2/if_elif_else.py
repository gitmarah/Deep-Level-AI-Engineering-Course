# IF ELIF ELSE CONDITION
print("==== Voting Eligibility ====")
while True:
    try:
        age = int(input("\nEnter your age: "))
        if age < 18:
            print("You are not eligible to vote!")
        elif age > 59:
            print("You are not eligible to vote!")
        else:
            print("You are eligible to vote!")
    except ValueError as e:
        print(f"Error: {e}")
    again = input("\nWould you like to check again(y/n): ").strip().lower()
    if again != "y":
        break
