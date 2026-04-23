def calculator(a, op, b):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            raise ValueError("Division by zero is inadmissible!")
        return a / b
    raise ValueError(f"Unknown operator: {op}")


def main():
    print("=== The Village Calculator ===")
    while True:
        try:
            a = float(input("First number: "))
            op = input("Operator (+, -, *, /): ").strip()
            b = float(input("Second number: "))
            result = calculator(a, op, b)
            print(f"{a} {op} {b} = {result}")
        except ValueError as e:
            print(f"Error {e}\n")
        again = input("Do you want to calculate? (y/n): ").strip().lower()
        if again != "y":
            break
    print("Thanks for using The Village Calculator!\n")


if __name__ == "__main__":
    main()
