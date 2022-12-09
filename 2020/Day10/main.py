import collections

if __name__ == '__main__':

    with open("input.txt") as f:
        raw = [0]
        for i in f.read().splitlines():
            raw.append(int(i))
        raw = sorted(raw)
        raw.append(max(raw) + 3)

    diffs = []
    for i in range(1, len(raw)):
        diffs.append(raw[i] - raw[i - 1])

    diff_counter = collections.Counter(diffs)
    print(diff_counter[1] * diff_counter[3])

    ways = [1] + [0]*raw[-1]

    for i in raw[1:]:
        ways[i] = ways[i-1] + ways[i-2] + ways[i-3]

    print(ways[-1])
