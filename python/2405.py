import re
from functools import cmp_to_key


def get_order_rules():
    raw_lines = [line.strip() for line in open("2405a.txt")]
    pattern = r"(\d+)\|(\d+)"
    parsed_lines = [re.match(pattern, entry).groups() for entry in raw_lines]
    return {(int(d1), int(d2)) for d1, d2 in parsed_lines}


def get_updates():
    raw_lines = [line.strip() for line in open("2405b.txt")]
    pattern = r"\d+"
    parsed_lines = [re.findall(pattern, entry) for entry in raw_lines]
    return [list(map(lambda x: int(x), entry)) for entry in parsed_lines]


def compare(i1, i2, order_rules):
    if (i1, i2) in order_rules: return -1
    if (i2, i1) in order_rules: return 1
    return 0


def part1and2():
    order_rules = get_order_rules()
    updates = get_updates()
    middle_sum_correct = 0
    middle_sum_incorrect = 0
    for update in updates:
        sorted_update = sorted(update, key=cmp_to_key(lambda x, y: compare(x, y, order_rules)))
        if update == sorted_update:
            middle_sum_correct += update[len(update) // 2]
        else:
            middle_sum_incorrect += sorted_update[len(sorted_update) // 2]
    return middle_sum_correct, middle_sum_incorrect


if __name__ == "__main__":
    print(f"Part 1 & 2: {part1and2()}")
