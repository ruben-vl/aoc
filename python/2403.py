import re

def get_input_parsed():
    day = "2403"
    raw_lines = [line.strip() for line in open(f"{day}.txt", 'r')]
    pattern = r"mul\(\d+,\d+\)"
    parsed_data = [re.findall(pattern, entry) for entry in raw_lines]
    pattern2 = r"(\d+,\d+)"
    muls = re.findall(pattern2, str(parsed_data))
    return muls

def part1():
    data = get_input_parsed()
    sum = 0
    for i in data:
        splitted = i.split(',')
        sum += int(splitted[0])*int(splitted[1])
    return sum


def part2():
    raw_lines = [line.strip() for line in open("2403.txt", "r")]
    one_line = "".join(raw_lines)
    one_line = one_line.replace('do()', 'dothis')
    one_line = one_line.replace("don't()", "dontdodisabled")
    splitted = re.split(r"dothis|dontdo", one_line)
    filtered = [x for x in splitted if not x.startswith('disabled')]
    res = "".join(filtered)
    pattern = r"mul\(\d+,\d+\)"
    parsed_data = list(re.findall(pattern, res))
    pattern2 = r"(\d+,\d+)"
    muls = re.findall(pattern2, str(parsed_data))
    sum = 0
    for i in muls:
        spl = i.split(',')
        sum += int(spl[0]) * int(spl[1])
    return sum


    # for i in splitted:
    #     print(i)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")