# RACE WORDS
print("\n==== Race Words ====")
while True:
    try:
        race = (
            input("\nEnter your race (Black, Cauca, Asian): ").strip().lower())
        if race == "black":
            print("Yo Nigger, wsp, hyd?, you're negroid!")
        elif race == "white":
            print("Good afternoon Mr. Sebastian, you are the master!")
        elif race == "asian":
            print("Yo chink, Koninchiwa!")
        else:
            print("Get outta this world, You strange motherfucker!")
    except ValueError as e:
        print(f"Error: {e}")
    again = input("\nWould you like to go again(y/n): ").strip().lower()
    if again != "y":
        break
