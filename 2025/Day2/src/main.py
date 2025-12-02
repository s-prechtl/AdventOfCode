def is_repeated(id: str) -> bool:
    if id[:len(id)//2] == id[len(id)//2:]:
        return True
    return False


def is_repeated_n(id: str) -> bool:
    max_bundle_size = len(id) // 2
    for bundle_size in range(1, max_bundle_size + 1):
        if len(id) % bundle_size != 0:
            continue

        for pos in range(bundle_size, len(id) - bundle_size + 1, bundle_size):
            prev_pos = pos - bundle_size

            if id[prev_pos:pos] != id[pos:pos+bundle_size]:
                break

            if pos+bundle_size == len(id):
                return True

    return False


if __name__ == '__main__':
    count = 0

    with open("input.txt", "r") as f:
        ids = [(int(lower), int(upper)) for element in f.read().split(",")
               for lower, upper in [element.split("-")]]

    for (lower, upper) in ids:
        for id in range(lower, upper+1):
            if str(id)[0] == '0':
                continue

            if is_repeated_n(str(id)):
                count += id

    print(count)
