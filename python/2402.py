import re

def get_input_parsed():
    day = "2402"
    raw_lines = [line.strip() for line in open(f"{day}.txt", 'r')]
    pattern = r"\d+"
    parsed_data = [re.findall(pattern, entry) for entry in raw_lines]
    typed_data = [list(map(lambda x: int(x), l)) for l in parsed_data]
    return typed_data

def safe_report(report) -> bool:
    all_tuples = [(report[i-1], report[i]) for i in range(1, len(report))]
    return (all([e1 > e2 for e1, e2 in all_tuples])
        or all([e1 < e2 for e1, e2 in all_tuples])) \
        and all(1 <= abs(e1 - e2) <= 3 for e1, e2 in all_tuples)

def safe_report2(report) -> bool:
    possible_reports = {tuple(report.copy()[:i]+report.copy()[i+1:]) for i in range(len(report)-1)}
    possible_reports.add(tuple(report.copy()[:-1]))
    return sum(safe_report(r) for r in possible_reports) > 0

def part1():
    data = get_input_parsed()
    safe_reports = 0
    for report in data:
        if safe_report(report):
            safe_reports += 1
    return safe_reports


def part2():
    data = get_input_parsed()
    safe_reports = 0
    for report in data:
        if safe_report2(report):
            safe_reports += 1
    return safe_reports


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")