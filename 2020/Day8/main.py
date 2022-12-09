import copy as cp


def Part1():
    idx = 0
    checkedIdx = []
    acc = 0
    while True:
        operation, num = raw[idx].split()
        if idx not in checkedIdx:
            checkedIdx.append(idx)
        else:
            return acc

        if operation == "jmp":
            idx += int(num)
        elif operation == "nop":
            idx += 1
        elif operation == "acc":
            acc += int(num)
            idx += 1


def Part2():
    for i in range(len(raw)):
        newSequence = cp.deepcopy(raw)
        if newSequence[i].split()[0] == "jmp":
            newSequence[i] = newSequence[i].replace("jmp", "nop")
        elif newSequence[i].split()[0] == "nop":
            newSequence[i] = newSequence[i].replace("nop", "jmp")

        idx = 0
        checkedIdx = []
        acc = 0
        while True:
            operation, num = newSequence[idx].split()
            if idx not in checkedIdx:
                checkedIdx.append(idx)
            else:
                break

            if idx == len(newSequence)-1:
                return acc

            if operation == "jmp":
                idx += int(num)
            elif operation == "nop":
                idx += 1
            elif operation == "acc":
                acc += int(num)
                idx += 1


if __name__ == '__main__':
    with open("input.txt") as f:
        raw = f.read().splitlines()
    print(Part2())
