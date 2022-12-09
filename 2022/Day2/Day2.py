if __name__ == '__main__':
    with open("input.txt", "r") as f:
        rounds = f.read()

    signsWin = {
        "A": "Y",
        "B": "Z",
        "C": "X"
    }

    signToSign = {
        "A": "X",
        "B": "Y",
        "C": "Z"
    }

    signLoose = {
        "A": "Z",
        "B": "X",
        "C": "Y"
    }

    signsToScore = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    score = rounds.count("X") + rounds.count("Y") * 2 + rounds.count("Z") * 3 + rounds.count("A Y") * 6 + rounds.count(
        "B Z") * 6 + rounds.count("C X") * 6 + rounds.count("A X") * 3 + rounds.count("B Y") * 3 + rounds.count(
        "C Z") * 3

    print(f"Solution 1: {score}")

    rounds = rounds.split("\n")
    score = 0
    for current in rounds:
        hisSymbol, result = current.split(" ")

        if result == "X":
            score += signsToScore[signLoose[hisSymbol]]
        elif result == "Y":
            score += signsToScore[signToSign[hisSymbol]]
            score += 3
        elif result == "Z":
            score += signsToScore[signsWin[hisSymbol]]
            score += 6

    print(f"Solution 2: {score}")
