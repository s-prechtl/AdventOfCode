if __name__ == '__main__':
    with open("input.txt") as f:
        inputs = f.readlines()
    result = 0
    entered = 0
    for i in inputs:
        rng, let, text = i.split(" ")
        for x in range(0, len(text)):
            letequal = text[x] == let[0]
            if (letequal and x == int(rng.split("-")[0])-1) ^ (letequal and x == int(rng.split("-")[1])-1):
                entered += 1
        if entered == 1:
            result += 1
        entered = 0
    print(result)
