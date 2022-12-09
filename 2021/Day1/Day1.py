if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input_data = f.readlines()

    input_data = [int(x) for x in input_data]

    # Part 1
    sol = 0
    for i in range(len(input_data)):
        if i>0 and input_data[i] > input_data[i-1]:
            sol+=1

    print(sol)

    # Part 2
    windows = []
    sol = 0
    for i in range(len(input_data)):
        if i < len(input_data)-2:
            windows.append(sum(input_data[i:i+3]))

    for i in range(len(windows)):
        if i>0 and windows[i] > windows[i-1]:
            sol+=1

    print(sol)