def AOC_8_a():
    with open("src/input8.txt") as file:
        lines = file.read().splitlines()
        lines = [x.split(" | ")[1].split(' ') for x in lines]
        total = 0
        for line in lines:
            for item in line:
                if len(item) == 2 or len(item) == 3 or len(item) == 4 or len(item) == 7:
                    total += 1
        print(total)


def AOC_8_b():
    with open("input.txt") as file:
        lines = file.read().splitlines()
        lines = [x.split(" | ") for x in lines]
        total = 0
        for (lefthand, righthand) in lines:
            lefts = lefthand.split(' ')
            digits = fill_dict(lefts)
            digits["2"] = find_two(digits["1"], digits["len5"] + digits["len6"])
            digits["9"] = find_nine(digits["4"], digits["len6"])

            digits["len6"].remove(digits["9"])

            digits["5"] = find_five(digits["2"], digits["len5"])

            digits["len5"].remove(digits["2"])
            digits["len5"].remove(digits["5"])

            digits["3"] = find_three(digits["len5"])
            digits["6"] = find_six(digits["5"], digits["len6"])

            digits["len6"].remove(digits["6"])

            digits["0"] = find_zero(digits["len6"])

            del digits["len5"]
            del digits["len6"]

            number = ""
            for item in righthand.split(' '):
                item = "".join(sorted(item))
                for key, value in digits.items():
                    if (value == item):
                        number += key
            print(number)
            total += int(number)
        print(total)


def pd(dict):
    for (key, value) in dict.items():
        print(key, ": ", value)


# 0 is the last number to find, and is just the last remaining not used string
def find_zero(candidates):
    return candidates[0]


# 2 is the only digit that shares a unique single segment with 1 (5 and 6 also share
# a single segment with 1, but they're thus not unique) among unknown digits. We need both len5 and len6
# to check for this uniqueness.
def find_two(segment, candidates):
    az = {x: shares_only_one_segment(x, segment) for x in candidates if shares_only_one_segment(x, segment) is not None}
    return least_frequent(az)


# 3 will be the only len5 segment not assigned at this point
def find_three(candidates):
    return candidates[0]


# 5 is the only digit that shares three segments with 2
def find_five(segment, candidates):
    for can in candidates:
        if (shares_x_segments(segment, can, 3)):
            return can


# 6 is the only digit that shares five segments with 5
def find_six(segment, candidates):
    for can in candidates:
        if (shares_x_segments(segment, can, 5)):
            return can


# 9 is the only digit that shares four segments with 4
def find_nine(segment, candidates):
    for can in candidates:
        if (shares_x_segments(segment, can, 4)):
            return can


def least_frequent(dict):
    list = [value for (key, value) in dict.items()]
    lowest_value = min(set(list), key=list.count)

    for key, value in dict.items():
        if (lowest_value == value):
            return key


def shares_only_one_segment(segment, candidate):
    total = 0
    for a in segment:
        for b in candidate:
            if (a == b):
                total += 1
                shared = a
    return shared if total == 1 else None


def shares_x_segments(segment, candidate, x):
    total = 0
    for seg in segment:
        for can in candidate:
            if (seg == can):
                total += 1
    return total == x


def fill_dict(lefts):
    digits = {"len5": [], "len6": []}
    for num in lefts:
        num = "".join(sorted(num))
        if (len(num) == 2):
            digits["1"] = num
        if (len(num) == 4):
            digits["4"] = num
        if (len(num) == 3):
            digits["7"] = num
        if (len(num) == 7):
            digits["8"] = num
        if (len(num) == 5):
            digits["len5"].append(num)
        if (len(num) == 6):
            digits["len6"].append(num)
    return digits

if __name__ == '__main__':
    AOC_8_b()