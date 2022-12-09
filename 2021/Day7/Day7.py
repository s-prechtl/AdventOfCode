import sys


def calcFuelCost(steps: int):
    total = 0
    for cost in range(1, steps + 1):
        total += cost

    return total


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        crabs = [int(x) for x in f.read().strip().split(",")]

    minFuel = sys.maxsize
    for i in crabs:
        totalfuelcost = 0
        for x in crabs:
            totalfuelcost += calcFuelCost(abs(x - i))

        minFuel = min(totalfuelcost, minFuel)

    print(minFuel)
