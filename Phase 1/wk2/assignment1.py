def reverse(number: int):
    number_of_digits = 1
    remainder = number
    while remainder > 9:
        remainder = int(remainder / 10)
        number_of_digits += 1
    for i in range(number_of_digits):
        d = 10 ** (i + 1)
        r = number % d
        print(int(r/(d/10)))


def main():
    print("==== Reverse Number ====")
    while True:
        try:
            number = int(input("\nEnter the number: "))
            reverse(number)
        except ValueError as e:
            print(f"Error: {e}")
        again = input("\nWould you like to try again(y/n): ").strip().lower()
        if again != "y":
            break
    print("\nThanks for using our tool!")


if __name__ == "__main__":
    main()
