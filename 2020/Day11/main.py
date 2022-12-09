import collections
import copy


def getNeighbors():
    count = [temp[x][y + 1], temp[x][y - 1], temp[x + 1][y + 1], temp[x - 1][y + 1], temp[x + 1][y], temp[x - 1][y],
             temp[x - 1][y - 1], temp[x + 1][y + 1]]

    count = collections.Counter(count)
    return count


if __name__ == '__main__':
    with open("input.txt") as f:
        raw = list(f.read().splitlines())

    while True:
        temp = copy.deepcopy(raw)
        for x in range(len(temp)):
            for y in range(len(temp[x])):
                line = list(temp[x])
                symbol = line[y]
                if symbol != '.':
                    neigh = getNeighbors()
                    if symbol == "L" and neigh["#"] == 0:
                        line[y] = '#'
                    if symbol == "#" and neigh["#"] >= 4:
                        line[y] = 'L'
                temp[x] = line
        if temp != raw:
            break

        raw = copy.deepcopy(temp)

    print(getNeighbors()["#"])
