import random


def main():
    print("==== Guess Number ====")
    number = random.randint(0, 100)
    while True:
        try:
            guess = int(input("\nGuess the number (0 - 100): "))
            if number > guess:
                print("Guess higher!")
            elif number < guess:
                print("Guess lower!")
            else:
                print("You guessed correct!")
                break
        except ValueError as e:
            print(f"Error: {e}")

    print("\nThanks for using our tool!")


if __name__ == "__main__":
    main()
