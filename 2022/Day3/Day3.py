def itemToPriority(item: str) -> int:
    if item >= 'a':
        return ord(item) - (ord('a')-1)
    elif item >= 'A':
        return ord(item) - (ord('A')-27)


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        rucksacks = [line.replace("\n", "") for line in f.readlines()]

    actualItems = []

    for rucksack in rucksacks:
        compartmentLength = len(rucksack) // 2
        compartments = [rucksack[:compartmentLength], rucksack[compartmentLength:]]
        for item in compartments[0]:
            if item in compartments[1]:
                actualItems.append(item)
                break

    print(f"Solution 1: {sum([itemToPriority(item) for item in actualItems])}")

    groupIdentifiers = []
    for i in range(0, len(rucksacks), 3):
        currentSacks = rucksacks[i:i + 3]
        for item in currentSacks[0]:
            if item in currentSacks[1] and item in currentSacks[2]:
                groupIdentifiers.append(item)
                break

    print(f"Solution 2: {sum([itemToPriority(item) for item in groupIdentifiers])}")
