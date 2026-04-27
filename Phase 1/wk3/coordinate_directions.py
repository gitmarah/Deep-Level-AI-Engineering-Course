def get_end_coordinates(direction):
    x = 0
    y = 0
    print(direction)
    for point in direction:
        print(point)
        if point == "N":
            y += 1
        elif point == "S":
            y -= 1
        elif point == "E":
            x += 1
        elif point == "W":
            x -= 1
        else:
            raise ValueError("Invalid point!")
    print(f"({x}, {y})")


def main():
    direction = []
    while True:
        point = input("Enter Point (E,W,N,S): ").strip().upper()
        if point == "":
            break
        direction.append(point)
    if len(direction) > 0:
        get_end_coordinates(direction)
    else:
        print("Did not values for point!")


if __name__ == "__main__":
    main()
