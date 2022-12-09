if __name__ == '__main__':
    elvePairs = []
    notNeeded = 0
    intersections = 0

    with open("input.txt", "r") as f:
        for line in f.readlines():
            line = line.replace("/n", "")
            elveSections = [boundries.split("-") for boundries in line.split(",")]
            elvePairs.append([[number for number in range(int(elveSections[0][0]), int(elveSections[0][1]) + 1)],
                              [number for number in range(int(elveSections[1][0]), int(elveSections[1][1]) + 1)]])

        for elvePair in elvePairs:
            if set(elvePair[0]).issubset(elvePair[1]) or set(elvePair[1]).issubset(elvePair[0]):
                notNeeded += 1
            if len(set(elvePair[0]) & set(elvePair[1])) > 0:
                intersections += 1

    print(f"Solution 1: {notNeeded}")
    print(f"Solution 2: {intersections}")
