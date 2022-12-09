import copy

from Board import BingoBoard

if __name__ == '__main__':
    boards = []
    with open("input.txt", "r") as f:
        toPop = []
        inp = f.readlines()
        nums = [int(x) for x in inp[0].split(",")]
        inp.pop(0)
        for i in range(len(inp)):
            inp[i] = inp[i].strip()
            if inp[i] == "":
                toPop.append(i)

        toPop.reverse()
        for i in toPop:
            inp.pop(i)

        for board in range(len(inp) // 5):
            boards.append(BingoBoard(inp[board * 5:board * 5 + 5]))

    # part1
    # for num in nums:
    #     for board in boards:
    #         board.enterValue(num)
    #         if board.checkWin():
    #             print(board.sum() * num)
    #             exit()

    # part2
    won = 0
    for num in nums:
        for board in boards:
            if not board.solved:
                board.enterValue(num)
                if board.checkWin():
                    won += 1
                    if won == len(boards):
                        print(board.sum()*num)
                        exit()
