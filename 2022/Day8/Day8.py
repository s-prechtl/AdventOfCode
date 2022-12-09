from numpy import transpose


class Tree:
    def __init__(self, height: int):
        self.height = height
        self.seen = False


def heightCheck(currentRow: [Tree]) -> int:
    visible = 0
    currentmax = -1
    for currentTree in currentRow:
        if currentTree.height > currentmax:
            if not currentTree.seen:
                visible += 1
                currentTree.seen = True
            currentmax = currentTree.height

    return visible


def checkSmaller(pos: Tree, direction: [Tree]) -> int:
    distance = 0
    for currTree in direction:
        if currTree.height < pos.height:
            distance += 1
        if currTree.height >= pos.height:
            distance += 1
            break

    return distance


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        raw = f.readlines()

    area = []
    for i, row in enumerate(raw):
        row = row.replace("\n", "")
        area.append([])
        for tree in row:
            area[i].append(Tree(int(tree)))

    verticalArea = transpose(area)
    visibleTrees = 0
    for row in area:
        visibleTrees += heightCheck(row)
        visibleTrees += heightCheck(row[::-1])

    for column in verticalArea:
        visibleTrees += heightCheck(column)
        visibleTrees += heightCheck(column[::-1])

    print(f"Solution 1: {visibleTrees}")

    bestScenic = 0
    for y, row in enumerate(area):
        for x, tree in enumerate(row):
            left = row[:x][::-1]
            right = row[x + 1:]
            up = verticalArea[x][:y][::-1]
            down = verticalArea[x][y + 1:]

            scenicCore = checkSmaller(tree, left)
            scenicCore *= checkSmaller(tree, right)
            scenicCore *= checkSmaller(tree, up)
            scenicCore *= checkSmaller(tree, down)
            if scenicCore > bestScenic:
                bestScenic = scenicCore

    print(f"Solution 2: {bestScenic}")
