def part1():
    data: list[int|str] = sum([int(char) * [idx//2] if idx % 2 == 0 else int(char) * ['.']
                               for idx, char in enumerate(open("2409test.txt").readline().strip())], [])
    data_reversed_filtered: list[int] = [e for e in data[::-1] if e != '.']
    whitespace_replaced = [e if e != '.' else data_reversed_filtered[data[:i+1].count('.') - 1]
                           for i, e in enumerate(data)]
    return sum([idx * elem for idx, elem in enumerate(whitespace_replaced[:len(data_reversed_filtered)])])

def part2():
    data = [int(char) * [str(idx//2)] if idx % 2 == 0 else int(char) * '.'
            for idx, char in enumerate(open("2409.txt").readline().strip())]
    data = [e for e in data if e != '']
    i = 1
    while i < len(data):
        if '.' not in data[-i]:
            for j in range(len(data)-i):
                if '.' in data[j] and len(data[j]) >= len(data[-i]):
                    moved_elem = data[-i]
                    data[i] = len(data[-i]) * '.'
                    if len(data[j]) == len(data[-i]):
                        data = data[:j] + [moved_elem] + data[j+1:]
                        i += 1
                    else:
                        data = data[:j] + [moved_elem] + [(len(data[j])-len(moved_elem))*'.'] + data[j+1:]
            data = [e for e in data if e != '']
    temp = []
    for e in data:
        if type(e) == str:
            temp += list(e)
        else:
            for i in e:
                temp.append(i)
    return sum([idx * int(elem) for idx, elem in enumerate(temp) if elem != '.'])



if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")