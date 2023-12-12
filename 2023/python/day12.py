import regex as re
from itertools import combinations

def part1(data: list[tuple[str, list[int]]]):
    # res = 0
    # for springs, groups in data:
    #     min_length = sum(groups) + len(groups) - 1
    #     broken_springs = [(idx, ch) for idx, ch in enumerate(list(springs)) if ch == "#"]
#         others = [(idx, ch) for idx, ch in enumerate(list(springs)) if ch != "#"]
#         subsets = [cmb for cmb in combinations(others, min_length-len(broken_springs))]
#         substrings = []
#         for cmb in subsets:
#             chars = list(cmb) + broken_springs
#             substrings.append(''.join(x[1] for x in sorted(chars, key=lambda x: x[0])))
#         regex = generate_regex(groups)
#         res += len([subset for subset in substrings if re.match(regex, subset)])
#     return res

# def generate_regex(groups: list[int]) -> str:
#     regex_string = ""
#     for i in range(len(groups)-1):
#         regex_string += "([#?]" + "{"+str(groups[i])+"})" + "[.?]{1}"
#     regex_string += "([#?]" + "{"+str(groups[-1])+"})"
#     return regex_string
#     # regex_string = "[.?]*"
#     # for i in range(len(groups)-1):
#     #     regex_string += "[#?]" + "{"+str(groups[i])+"}" + "[.?]+"
#     # regex_string += "[#?]" + "{"+str(groups[-1])+"}" + "[.?]*"
#     # return regex_string
    return sum([possible_arrangements(springs, groups) for springs, groups in data])

def possible_arrangements(springs: str, groups: list[int]) -> int:
    pr=False
    if springs == "" and len(groups) != 0:
        return 0
    if springs == "" and len(groups) == 0:
        raise RuntimeError("This shouldn't be reached!")
    if len(groups) == 0:
        return 0
    if len(groups) == 1:
        if pr:
            print(f"{springs}: {groups[0]}")
        broken_idx = [idx for idx, spr in enumerate(springs) if spr == "#"]
        if len(broken_idx) > 1 and max(broken_idx) - min(broken_idx) >= groups[0]:
            if pr:
                print("No possible solution bc # too far from each other!")
            return 0
        elif len(broken_idx) == 1:
            springs = springs[broken_idx[0]-groups[0]: broken_idx[0]+groups[0]]
            if pr:
                print(f"Springs reduced to {springs}")
        print(springs[-groups[0]:])
        return len(re.findall('[#?]{' + str(groups[0]) + '}[?.]{'+'1}', springs, overlapped=True)) \
                + (1 if re.match('[#?]{' + str(groups[0]) + '}', springs[-groups[0]:]) else 0)
    if len(groups) > 1:
        if pr:
            print(f"{springs}: {groups}")
        arrangements = 0
        for i in range(0, len(springs)):
            if pr:
                print(f"Trying to put {groups[0]} at index {i}")
                print(springs[i:i+groups[0]+1])
            if i == 0:
                if re.match('[#?]{' + str(groups[0]) + '}[?.]{'+'1}', springs[i:i+groups[0]+1]):
                    if pr:
                        print("Can be placed, checking possible arrangements of next numbers")
                    a = possible_arrangements(springs[i+groups[0]+1:], groups[1:])
                    if pr:
                        print(f"Possible arrangements: {a}")
                    arrangements += a
            if i > 0:
                if re.match('[?.]{'+'1}'+'[#?]{' + str(groups[0]) + '}[?.]{'+'1}', springs[i-1:i+groups[0]+1]):
                    if pr:
                        print("Can be placed, checking possible arrangements of next numbers")
                    a = possible_arrangements(springs[i+groups[0]+1:], groups[1:])
                    if pr:
                        print(f"Possible arrangements: {a}")
                    arrangements += a
        return arrangements

def part2(data):
    pass


if __name__ == "__main__":
    data = [l.strip().split(' ') for l in open("2023/python/day12_input.txt", 'r')]
    data = [(springs, [int(x) for x in groups.split(',')]) for springs, groups in data]
    # DATA FORMAT: list[tuple[str, list[int]]]
    # [('?##??....?#?', [1,3,4,1]), ...]
    # print(possible_arrangements("???#???.#??####?", [5,1,5]))
    # print(possible_arrangements(".?.????.?.", [1,2,1]))
    # print(possible_arrangements("???.###", [1,1,3]))
    # print(possible_arrangements(".??..??...?##.", [1,1,3]))
    # print(possible_arrangements("?#?#?#?#?#?#?#?", [1,3,1,6]))
    # print(possible_arrangements("????.#...#...", [4,1,1]))
    print(possible_arrangements("????.######..#####.", [1,6,5]))
    # print(possible_arrangements("?###????????", [3,2,1]))
    # print(f"Part 1: {part1(data)}")
    # print(f"Part 2: {part2(data)}")