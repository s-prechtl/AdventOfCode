def part1():
    answer = 0
    horizontal =  0
    depth = 0

    with open("input.txt", "r") as f:
        input = f.readlines()

        for line in input:
            line = line.strip()
            line = line.split(" ")
            val = int(line[1])

            if line[0] == "forward":
                horizontal += val
            if line[0] == "up":
                depth -= val
            if line[0] == "down":
                depth += val
    answer = horizontal*depth
    return answer


def part2():
    answer = 0
    horizontal = 0
    aim = 0
    depth = 0

    with open("input.txt", "r") as f:
        input = f.readlines()

        for line in input:
            line = line.strip()
            line = line.split(" ")
            val = int(line[1])

            if line[0] == "forward":
                horizontal += val
                depth += val*aim
            if line[0] == "up":
                aim -= val
            if line[0] == "down":
                aim += val
    answer = horizontal*depth
    return answer


if __name__ == '__main__':
    print(part1())
    print(part2())
