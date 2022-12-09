import re


def checkDate(min, max, val):
    return min <= int(val) <= max and len(val) == 4


def checkHeight(height):
    unit = height[-2:]
    rv = False
    if unit == "cm" or unit == "in":
        num = height.strip(unit)

        if unit == "cm" and 150 <= int(num) <= 193:
            rv = True
        elif unit == "in" and 59 <= int(num) <= 76:
            rv = True
    return rv


def checkHair(color):
    return re.match(r'#[a-f0-9]{6}', color)


def checkAll():
    rv = 0
    for val in keys:
        for j in range(0, len(keyval)):
            if val == keyval[j][0]:
                rv += 1
                break
    return rv == 7


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        raw = f.read().split("\n\n")

    keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    eclValids = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    pp = []

    for i in raw:
        pp.append(i.replace("\n", " ").split(" "))

    valid = 0

    for passport in pp:
        keyval = []
        counter = 0
        for i in passport:
            keyval.append(i.split(":"))

        if checkAll():
            for i in keyval:
                key = i[0]
                val = i[1]
                if key == "byr" and checkDate(1920, 2002, val):
                    counter += 1
                elif key == "iyr" and checkDate(2010, 2020, val):
                    counter += 1
                elif key == "eyr" and checkDate(2020, 2030, val):
                    counter += 1
                elif key == "hgt" and checkHeight(val):
                    counter += 1
                elif key == "hcl" and checkHair(val):
                    counter += 1
                elif key == "ecl" and val in eclValids:
                    counter += 1
                elif key == "pid" and len(val) == 9 and val.isdigit():
                    counter += 1

            if counter == 7:
                valid += 1

    print(valid)
