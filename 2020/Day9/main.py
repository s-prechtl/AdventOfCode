def Part1():
    for i in range(len(raw)):
        isSum = False
        if i >= 25:
            last = []
            for roUnUdL in range(1, 26):
                last.append(int(raw[i - roUnUdL]))

            for j in last:
                for k in last:
                    if j + k == int(raw[i]):
                        isSum = True

            if not isSum:
                return int(raw[i])


if __name__ == '__main__':
    raw = []
    with open("input.txt") as f:
        for i in f.read().splitlines():
            raw.append(int(i))

    invalid = Part1()
    beg = 0
    end = 0
    while end <= len(raw):
        nums = raw[beg:end]
        sumNums = sum(nums)
        if sumNums == invalid:
            print(max(nums) + min(nums))
            exit()
        elif sumNums > invalid:
            beg += 1
        elif sumNums < invalid:
            end += 1
