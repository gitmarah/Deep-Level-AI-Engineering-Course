def main():
    print("==== Sum Until 0 ====")
    sum = 0
    while True:
        try:
            number = int(input("\nNumber (Enter 0 to stop): "))
            if number == 0:
                break
            else:
                sum += number
        except ValueError as e:
            print(f"Error: {e}")
    print(f"Sum: {sum}")
    print("\nThanks for using our tool!")


if __name__ == "__main__":
    main()
