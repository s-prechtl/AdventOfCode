def getSprite(currentX: int) -> str:
    if currentX == 0:
        middle = "##."
    elif currentX == -1:
        middle = "#.."
    elif currentX < -1:
        middle = "..."
    else:
        middle = "###"

    return "." * (currentX - 1) + middle + "." * (40 - currentX - 2)


if __name__ == '__main__':
    x = 1
    cycle = 1

    savedCycleValues = {}

    toSave = [20, 60, 100, 140, 180, 220]
    output = ""
    with open("input.txt", "r") as f:
        operations = [line.replace("\n", "") for line in f.readlines()]

    for operation in operations:
        if operation == "noop":
            output += getSprite(x)[(cycle - 1) % 40]
            cycle += 1
            if cycle % 40 == 1 and cycle != 1:
                output += "\n"
        else:
            output += getSprite(x)[(cycle - 1) % 40]
            value = int(operation.split(" ")[1])
            cycle += 1
            if cycle in toSave:
                savedCycleValues[cycle] = x

            if cycle % 40 == 1 and cycle != 1:
                output += "\n"

            output += getSprite(x)[(cycle - 1) % 40]
            cycle += 1
            x += value
            if cycle in toSave:
                savedCycleValues[cycle] = x

            if cycle % 40 == 1 and cycle != 1:
                output += "\n"

    print(f"Solution 1: {sum([key * value for key, value in savedCycleValues.items()])}")
    print("Solution 2:")
    print(" " + " ".join(output))  # with join its readability is increased by a lot
