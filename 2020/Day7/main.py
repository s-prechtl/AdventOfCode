def getParent(color):
    for i in raw:
        primcolor, others = i.split(" contain ")

        others = others.split(", ")
        for j in range(0, len(others)):
            others[j] = others[j].replace(others[j][:2], "")
        if color in others:
            if primcolor not in containGold:
                containGold.append(primcolor)
                getParent(primcolor)


def getChilds(color):
    result = 0
    for i in raw:
        primcolor, others = i.split(" contain ")

        if primcolor == color:
            others = others.split(", ")
            for j in range(0, len(others)):
                times = others[j][:2]
                if times == "no":
                    result = 1
                else:
                    others[j] = others[j].replace(times, "")
                    result += int(times) * getChilds(others[j])
            break
    return result


if __name__ == '__main__':
    containGold = []
    GoldContains = 0
    with open("input.txt") as f:
        raw = f.read().split("\n")

    for i in range(0, len(raw)):
        raw[i] = raw[i].replace(" bags", "").replace(" bag", "").replace(".", "")

    getParent("shiny gold")

    print("Aufgabe 1:", len(containGold))

    GoldContains = getChilds("shiny gold")
    print("Aufgabe 2:", GoldContains+1)
