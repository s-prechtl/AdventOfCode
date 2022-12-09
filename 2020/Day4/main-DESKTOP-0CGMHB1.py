if __name__ == '__main__':
    f = open("input", "r")
    inputs = f.read().split("\n\n")

    passports = []
    for i in inputs:
        passports.append(i.replace("\n", " ").split(" "))

    reqFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    valid = 0

    for passport in passports:
        dsplit = dict(i.split(":") for i in passport)
        if all(field in dsplit for field in reqFields):
            valid += 1

    print(valid)
