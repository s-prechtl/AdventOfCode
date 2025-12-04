def count_neighbours(x: int, y: int, grid: [str]) -> int:
    count = 0
    for y_i in range(max(y-1, 0), min(y+2, len(grid))):
        for x_i in range(max(x-1, 0), min(x+2, len(grid[y_i]))):
            if x_i == x and y_i == y:
                continue
            if grid[y_i][x_i] == '@':
                count += 1
    return count


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        grid = f.read().split("\n")

    total = 0
    for y, row in enumerate(grid):
        for x, symbol in enumerate(row):
            if symbol != '@':
                continue
            if count_neighbours(x, y, grid) < 4:
                total += 1

    print(total)
