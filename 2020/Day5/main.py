if __name__ == '__main__':
    highest = 0
    with open("input.txt", "r") as f:
        raw = f.read().split("\n")

    seatIDs = []

    for less in raw:
        row = int(less[:7].replace("F", "0").replace("B", "1"), 2)
        seatnum = int(less[-3:].replace("L", "0").replace("R", "1"), 2)
        seatID = row*8+seatnum
        seatIDs.append(seatID)

    seatIDs = sorted(seatIDs)

    mySeat = set(range(seatIDs[0], seatIDs[-1])) - set(seatIDs)
    print(mySeat)
