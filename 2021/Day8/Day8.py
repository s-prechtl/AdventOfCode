if __name__ == '__main__':
    with open("input.txt", "r") as f:
        data = [x.split("|")[1].strip().split() for x in f.readlines()]

    for d in range(len(data)):
        for entry in range(len(data[d])):
            data[d][entry] = "".join(sorted(data[d][entry]))

    one = "cf"
    four = "bcdf"
    seven = "acf"
    eight = "abcdefg"

    entries = 0

    for d in data:
        for entry in d:
            if len(entry) == len(one) or len(entry) == len(four) or len(seven) == len(entry) or len(eight) == len(entry):
                entries += 1

    print(entries)
