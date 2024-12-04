import itertools
def get_input_parsed():
    return [line.strip() for line in open("2404.txt", 'r')]

def horizontal(data):
    lr_count = sum([r.count('XMAS') for r in data])
    data_reversed = [r[::-1] for r in data]
    rl_count = sum([r.count('XMAS') for r in data_reversed])
    return lr_count + rl_count

def vertical(data):
    data_transposed = [i for i in zip(*data)]
    data_transposed = ["".join(r) for r in data_transposed]
    return horizontal(data_transposed)

def diagonal(data):
    n = len(data)
    diagonals_1 = []  # lower-left-to-upper-right diagonals
    diagonals_2 = []  # upper-left-to-lower-right diagonals
    for p in range(2 * n - 1):
        diagonals_1.append([data[p - q][q] for q in range(max(0, p - n + 1), min(p, n - 1) + 1)])
        diagonals_2.append([data[n - p + q - 1][q] for q in range(max(0, p - n + 1), min(p, n - 1) + 1)])
    diagonals_1 = ["".join(r) for r in diagonals_1]
    diagonals_2 = ["".join(r) for r in diagonals_2]
    return horizontal(diagonals_1) + horizontal(diagonals_2)

def part1():
    data = get_input_parsed()
    return horizontal(data) + vertical(data) + diagonal(data)

def x_mas(data):
    xmas_count = 0
    for row in range(len(data)-2):
        for col in range(len(data)-2):
            if data[row+1][col+1] == 'A':
                if data[row][col]+data[row+2][col+2] in ['MS', 'SM']:
                    if data[row+2][col]+data[row][col+2] in ['MS', 'SM']:
                        xmas_count += 1
    return xmas_count

def part2():
    data = get_input_parsed()
    return x_mas(data)

if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")