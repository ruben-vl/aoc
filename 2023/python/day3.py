from functools import reduce
from operator import concat

def part1(oneline: str, symbols: set[str]):
    part_sum = 0
    i = 0
    while i < 140*140:
        if not oneline[i] in symbols | set(['.']):
            l = 1
            while not oneline[i+l] in symbols | set(['.']):
                l += 1
            surrounding = get_all_surrounding(oneline, i, l)
            if len(surrounding & symbols) > 0:
                part_sum += int(oneline[i:i+l])
            i += l
        else:
            i += 1
    return part_sum

def part2():
    possible_gears = dict()
    i = 0
    while i < 140*140:
        if not oneline[i] in symbols | set(['.']):
            l = 1
            while not oneline[i+l] in symbols | set(['.']):
                l += 1
            surrounding = get_surrounding_with_index(oneline, i, l)
            for symbol, index in surrounding:
                if symbol == "*":
                    if index in possible_gears.keys():
                        possible_gears[index].append(int(oneline[i:i+l]))
                    else:
                        possible_gears[index] = [int(oneline[i:i+l])]
            i += l
        else:
            i += 1
    gear_sum = 0
    for _, numbers in possible_gears.items():
        if len(numbers) == 2:
            gear_sum += numbers[0]*numbers[1]
    return gear_sum
            

def get_all_symbols(oneline: str):
    return set(ch for ch in oneline if not ch.isnumeric() and not ch == '.')

def get_all_surrounding(oneline: str, i: int, length: int):
    res = []
    for j in range(i-141, i-141+length+2):
        if j >= 0 and j < 140*140:
            res.append(oneline[j])
    for j in range(i+139, i+139+length+2):
        if j >= 0 and j < 140*140:
            res.append(oneline[j])
    res.append(oneline[i-1])
    res.append(oneline[i+length])
    return set(res)

def get_surrounding_with_index(oneline: str, i: int, length: int):
    res = []
    for j in range(i-141, i-141+length+2):
        if j >= 0 and j < 140*140:
            res.append((oneline[j],j))
    for j in range(i+139, i+139+length+2):
        if j >= 0 and j < 140*140:
            res.append((oneline[j],j))
    res.append((oneline[i-1],i-1))
    res.append((oneline[i+length],i+length))
    return set(res)


if __name__ == "__main__":
    data = [line.strip() for line in open("2023/python/day3_input.txt", "r")]
    oneline = reduce(concat, data)
    symbols = get_all_symbols(oneline)
    print(part1(oneline, symbols))
    print(part2())