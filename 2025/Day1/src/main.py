TOTAL_CLICKS = 100

if __name__ == '__main__':
    current = 50
    count = 0
    with open("input.txt", "r") as f:
        rotations = [{'direction': line[0], 'count': int(
            line[1:])} for line in f.readlines()]

    for rotation in rotations:
        print(rotation)
        # Convert left to right to avoid negatives
        if rotation["direction"] == 'L':
            rotation["count"] = TOTAL_CLICKS - rotation["count"]

        current = (current + rotation["count"]) % TOTAL_CLICKS

        if current == 0:
            count += 1

    print(count)
