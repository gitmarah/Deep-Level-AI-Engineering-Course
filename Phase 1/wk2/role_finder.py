# ROLE FINDER
print("\n==== Role Finder ====")
while True:
    try:
        yoe = float(input("\nEnter your year of experience: "))
        if yoe < 0:
            raise ValueError("Negative year not allowed!")
        elif yoe <= 2:
            print("Junior Engineer!")
        elif yoe <= 4:
            print("Intermediate Engineer!")
        elif yoe <= 6:
            print("Senior Engineer!")
        elif yoe <= 39:
            print("Project Manager!")
        else:
            print("You are too old for this job!")
    except ValueError as e:
        print(f"Error: {e}")
    again = input("\nWould you like to check again(y/n): ").strip().lower()
    if again != "y":
        break
