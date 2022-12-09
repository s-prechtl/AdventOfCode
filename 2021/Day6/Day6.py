def calc(fish: {}, days):
    for i in range(256):
        toAdd = fish["0"]
        for key in "012345678":
            if key != "8":
                fish[key] = fish[str(int(key) + 1)]

        fish["6"] = int(fish["6"]) + toAdd
        fish["8"] = toAdd

    sum = 0
    for key in fish:
        sum += fish[key]

    return sum


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        raw = f.read().strip().split(",")

    fish = {"0": 0, "1": raw.count("1"), "2": raw.count("2"), "3": raw.count("3"), "4": raw.count("4"),
            "5": raw.count("5"),
            "6": raw.count("6"), "7": 0, "8": 0
            }

    print(calc(fish, 256))
