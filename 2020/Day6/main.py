if __name__ == '__main__':
    with open("input.txt") as f:
        raw = f.read().split("\n\n")

    groups = []
    for i in raw:
        groups.append(i.split("\n"))

    counter = 0
    people = 0
    answer = 0

    for group in groups:
        curransw = []
        people = 0
        for answergroup in group:
            people += 1
            for answer in answergroup:
                curransw.append(answer)

            if curransw.count(answer) == people:
                counter += 1


    print(counter)
