def get_largest_n_digit(batteries: str, n: int) -> str:
    digits = [c for c in batteries if c.isdigit()]

    to_remove = len(digits) - n
    result = digits[:]

    for _ in range(to_remove):
        for i in range(len(result) - 1):
            if result[i] < result[i + 1]:
                result.pop(i)
                break
        else:
            result.pop()

    return ''.join(result)


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        banks = f.read().split('\n')

    part1_total = 0
    part2_total = 0

    for batteries in banks:
        if not batteries:
            continue

        # part1_total += int((str(first_max)+str(second_max)))
        part1_total += int(get_largest_n_digit(batteries, 2))

        # Part 2: largest 12 digits
        part2_total += int(get_largest_n_digit(batteries, 12))

    print(f"Part 1: {part1_total}")
    print(f"Part 2: {part2_total}")
