import copy


def part1():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    onesNeeded = len(lines) / 2
    gamma = ""
    eps = ""

    onesInBinaries = countOnesInBinaries(lines)

    for i in range(len(onesInBinaries)):
        if onesInBinaries[i] >= onesNeeded:
            gamma += "1"
            eps += "0"
        else:
            gamma += "0"
            eps += "1"

    return int(gamma, 2) * int(eps, 2)


def part2():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    co2 = copy.deepcopy(lines)

    onesInBinaries = countOnesInBinaries(lines)
    currpops = []

    for i in range(len(lines[0].strip())):
        for j in range(len(lines)):
            onesNeeded = len(lines) / 2
            line = lines[j].strip()
            if onesInBinaries[i] >= onesNeeded:
                if line[i] == "0":
                    currpops.append(j)
                    # lines.pop(j)
            else:
                if line[i] == "1":
                    # lines.pop(j)
                    currpops.append(j)

        if not len(currpops) is len(lines):
            currpops.reverse()
            for j in currpops:
                lines.pop(j)
            currpops = []
        else:
            lines = lines[-1]

        if len(lines) == 1:
            break

    for i in range(len(co2[0].strip())):
        for j in range(len(lines)):
            onesNeeded = len(lines) / 2
            line = co2[j].strip()
            if onesInBinaries[i] >= onesNeeded:
                if line[i] == "1":
                    currpops.append(j)
                    # co2.pop(j)
            else:
                if line[i] == "0":
                    # co2.pop(j)
                    currpops.append(j)

        if not len(currpops) is len(co2):
            currpops.reverse()
            for j in currpops:
                co2.pop(j)
            currpops = []
        else:
            co2 = co2[-1]

        if len(co2) == 1:
            break

    return int(co2[0].strip(), 2) * int(lines[0].strip(), 2)


def countOnesInBinaries(lines):
    onesInBinaries = [0 for _ in range(len(lines[0]) - 1)]

    for line in lines:
        line = line.strip()
        for i in range(len(line)):
            num = int(line[i])
            if num == 1:
                onesInBinaries[i] += 1

    return onesInBinaries


if __name__ == '__main__':
    print(part1())
    print(part2())
