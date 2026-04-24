def divisors(number: int):
    for i in range(number):
        if number % (i + 1) == 0:
            print(i + 1)


def main():
    print("==== Divisors of a Number ====")
    while True:
        try:
            number = int(input("\nEnter the number: "))
            divisors(number)
        except ValueError as e:
            print(f"Error: {e}")
        again = input("\nWould you like to try again(y/n): ").strip().lower()
        if again != "y":
            break
    print("\nThanks for using our tool!")


if __name__ == "__main__":
    main()
