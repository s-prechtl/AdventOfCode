import re


class Operation:
    amount: int
    src: int
    dest: int

    def __init__(self, amount: int, src: int, dest: int):
        self.amount = amount
        self.src = src - 1
        self.dest = dest - 1


def buildStacks(raw: [str]) -> [[str]]:
    builder = [[] for i in range(9)]
    for lineNumber in range(len(raw)):
        line = raw[lineNumber]
        for position in [x.start() for x in re.finditer('\[', line)]:
            sign = line[position + 1]
            builder[position // 4].append(sign)

    return builder


def buildOperations(raw: [str]) -> [Operation]:
    builder = []

    for currentOperation in raw:
        currentOperation = currentOperation.replace("move ", "").replace("from ", "").replace("to ", "")
        amount, src, dest = map(int, currentOperation.split(" "))
        builder.append(Operation(amount, src, dest))

    return builder


def performOperation(stacks: [[str]], op: Operation) -> [[str]]:
    for i in range(op.amount):
        stacks[op.dest].insert(0, stacks[op.src][0])
        stacks[op.src] = stacks[op.src][1:]

    return stacks


def buildSolutionString(stacks: [[str]]) -> str:
    sol = ""

    for stack in stacks:
        sol += stack[0]

    return sol


def performOperationVariant2(stacks: [[str]], op: Operation) -> [[str]]:
    for i in range(op.amount):
        stacks[op.dest].insert(i, stacks[op.src][0])
        stacks[op.src] = stacks[op.src][1:]

    return stacks


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        rawstacks, rawoperations = f.read().split("\n\n")

    stacks = buildStacks(rawstacks.split("\n"))
    operations = buildOperations(rawoperations.split("\n"))

    for operation in operations:
        stacks = performOperation(stacks, operation)

    print(f"Solution 1: {buildSolutionString(stacks)}")

    stacks = buildStacks(rawstacks.split("\n"))

    for operation in operations:
        stacks = performOperationVariant2(stacks, operation)

    print(f"Solution 2: {buildSolutionString(stacks)}")
