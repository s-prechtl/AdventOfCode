from Line import Line


def getHighestIndixes(lines: [Line]):
    currMaxX = 0
    currMaxY = 0
    for line in lines:
        currMaxX = max(currMaxX, max(line.start.x, line.end.x) + 1)
        currMaxY = max(currMaxX, max(line.start.y, line.end.y) + 1)
    return currMaxX, currMaxY


def part1(lines: [Line], arraySize: []):
    area = []
    for x in range(arraySize[0]):
        area.append([])
        area[x] = []
        for y in range(arraySize[1]):
            area[x].append(0)

    for line in lines:
        if line.axis == "X":
            for y in range(min(line.start.y, line.end.y), max(line.start.y, line.end.y) + 1):
                area[line.start.x][y] += 1
        elif line.axis == "Y":
            for x in range(min(line.start.x, line.end.x), max(line.start.x, line.end.x) + 1):
                area[x][line.start.y] += 1
        elif line.axis == "DIAG":
            if line.start.x > line.end.x:
                y = line.end.y
            else:
                y = line.start.y

            if y < max(line.start.y, line.end.y):
                op = 1
            else:
                op = -1

            for x in range(min(line.start.x, line.end.x), max(line.start.x, line.end.x) + 1):

                area[x][y] += 1

                y += op

    danger = 0

    for row in area:
        for val in row:
            if val > 1:
                danger += 1
    return danger


if __name__ == '__main__':
    lines = []
    with open("input.txt", "r") as f:
        raw = [x.strip() for x in f.readlines()]

    for i in raw:
        inp = i.replace(" -> ", ", ")
        vals = [int(x) for x in inp.split(",")]
        lines.append(Line(vals[0], vals[1], vals[2], vals[3]))
        if lines[-1].axis == "INVALID":
            lines.pop(-1)

    print(part1(lines, getHighestIndixes(lines)))
