def greet(first, last="", style="fiendly"):
    full = f"{first} {last}".strip()
    style = style.lower()
    if style == "friendly":
        return f"Hey, {first}! Great to see you!"
    if style == "formal":
        return f"Good afternoon, Mr./Ms. {last or first}."
    if style == "excited":
        return f"WOW {full}! So glad you are here!"
    return f"Hello {full}!"


def main():
    print("=== The Village Name Greeter ===")
    first = input("First name: ").strip()
    last = input("Last name: ").strip()
    style = input("Style (friendly, formal, excited): ").strip() or "friendly"
    print(f"\n{greet(first, last, style)}")


if __name__ == "__main__":
    main()
