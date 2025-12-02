def is_repeated(id: str) -> bool:
    #print(id[:len(id)//2], id[len(id)//2:])
    if id[:len(id)//2] == id[len(id)//2:]:
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

            if is_repeated(str(id)):
                count += id

    print(count)
