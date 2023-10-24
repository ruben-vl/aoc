def get_floor(data: str):
    return data.count('(') - data.count(')')

def enter_basement(data: str):
    '''Not efficient!'''
    for i in range(1,len(data)):
        if data[:i].count(')') > data[:i].count('('):
            return i

if __name__ == "__main__":
    path = "2015/python/day1_input.txt"
    with open(path) as f:
        data = [s.rstrip() for s in f.readlines()]
    f.close()
    part1 = get_floor(data[0])
    print(f"Part one: {part1}")

    part2 = enter_basement(data[0])
    print(f"Part two: {part2}")