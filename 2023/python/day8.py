import math

def part1(data: dict[str, tuple[str, str]], instructions: str) -> int:
    curr = 'AAA'
    i = 0
    while curr != 'ZZZ':
        if instructions[i % 263] == 'L':
            curr = data[curr][0]
        else:
            curr = data[curr][1]
        i += 1
    return i

def part2(data: dict[str, tuple[str, str]], instructions: str) -> int:
    start_states = [node for node in data.keys() if node[-1] == 'A']
    repeat_states: dict[str, list[str]] = dict()
    for state in start_states:
        instruction_repeat_states = []
        all_states = []
        current_state = state
        while current_state not in instruction_repeat_states:
            instruction_repeat_states.append(current_state)
            for i in range(len(instructions)):
                all_states.append(current_state)
                if instructions[i] == 'L':
                    current_state = data[current_state][0]
                else:
                    current_state = data[current_state][1]
        repeat_states[state] = all_states
    zidx = {
        start: [idx for idx, s in enumerate(other) if s[-1] == 'Z']
        for start, other in repeat_states.items()
    }
    # {'FDA': [19199], 'BPA': [11309], 'BVA': [17621], 'NDA': [20777], 'AAA': [16043], 'QCA': [15517]}
    return math.lcm(19199, 11309, 17621, 20777, 16043, 15517)
    


if __name__ == "__main__":
    instructions = "LLRLRRRLRRRLRRLLRRRLLRRLLRLRLRRRLRRRLLRRRLLRRRLRRLRRLRLRRLLRRRLRRRLLRRRLRRLLLRRLRLLLRLRRRLRLRLLLRRLRRLLLRRRLLRRRLRLRLLRRLRLRRRLRLRLLRLRRLRRRLRRLRLRRRLRLRRLRRLRLRRLLRLRLRRLRLLRRLRRLRLRRLLRLRLLRRLLRLLLRRLRLRRRLRRRLRRRLRLRLRRRLLLRLRRLRLRRRLRRRLRRRLRLRRRLRRRLRRRLRRRR"
    data = [l.strip().split(' = ') for l in open("2023/python/day8_input.txt", 'r')]
    data = {loc: (tup[1:4], tup[6:9]) for loc, tup in data}
    print(f"Part 1: {part1(data, instructions)}")
    print(f"Part 2: {part2(data, instructions)}")
