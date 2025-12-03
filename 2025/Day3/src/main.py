def get_max_joltage(batteries: [str], last_index: int = -1) -> (int, int):
    max = 0
    max_index = -1
    last_is_last = last_index == (len(batteries)-1)
    for i, battery in enumerate(batteries):
        battery_value = int(battery)
        if battery_value > max and ((last_is_last and i != last_index) or i > last_index):
            max = battery_value
            max_index = i

    return max_index, max


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        banks = f.read().split('\n')

    total_joltage = 0
    for batteries in banks:
        f_i, first_max = get_max_joltage(batteries)
        s_i, second_max = get_max_joltage(batteries, f_i)

        if f_i == len(batteries)-1:
            first_max, second_max = second_max, first_max

        total_joltage += int((str(first_max)+str(second_max)))

    print(total_joltage)
