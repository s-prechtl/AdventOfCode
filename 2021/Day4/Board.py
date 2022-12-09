import copy


class BingoBoard:
    values = [[],
              [],
              [],
              [],
              []]
    solved : bool

    def __init__(self, values: list[str]):
        self.solved = False
        self.values = copy.deepcopy(self.values)
        for i in range(5):
            self.values[i] = [int(x) for x in values[i].split()]

    def enterValue(self, value: int):
        for row in self.values:
            for i in range(len(row)):
                if row[i] == value:
                    row[i] = 'X'
                    return

    def checkWin(self):
        for row in self.values:
            valid = ""
            for col in row:
                valid += str(col)
            if valid == 'XXXXX':
                self.solved = True
                return True

        for col in range(5):
            valid = ""
            for row in self.values:
                valid += str(row[col])
            if valid == 'XXXXX':
                self.solved = True
                return True

        return False

    def sum(self):
        sum = 0
        for row in self.values:
            for num in row:
                if num != 'X':
                    sum += int(num)

        return sum