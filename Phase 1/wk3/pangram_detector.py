EACH_LETTER = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]


def is_pangram(sentence: str):
    if len(sentence) < 26:
        print("This sentence is not a Pangram")
        exit()
    for (index, letter) in enumerate(EACH_LETTER):
        if letter not in sentence:
            print("This sentence is not a Pangram!")
            exit()
        if letter in sentence and index != 25:
            continue
        else:
            print("This sentence is a Pangram!")
            exit()


sentence = input("Enter sentence: ").strip().upper()
is_pangram(sentence)
