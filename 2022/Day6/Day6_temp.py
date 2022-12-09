def findFirstUniquePackage(signal: str, numberOfUniques: int) -> int:
    for offset in range(len(signal) - numberOfUniques):
        if len(set(signal[offset:offset + numberOfUniques])) == numberOfUniques:
            return offset + numberOfUniques


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        signal = f.read()

    print(f"Solution 1: {findFirstUniquePackage(signal, 4)}")
    print(f"Solution 2: {findFirstUniquePackage(signal, 14)}")
