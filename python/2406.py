def turn_right(direction):
    match direction:
        case 0, -1: return -1, 0
        case 1, 0: return 0, -1
        case 0, 1: return 1, 0
        case -1, 0: return 0, 1

def part1(data):
    # data = [line.strip() for line in open("2406.txt", 'r')]
    guard_pos = None
    for r in range(len(data)):
        for c in range(len(data[0])):
            if data[r][c] == '^':
                guard_pos = r,c
                break
        if guard_pos:
            break
    # print(guard_pos)
    guard_dir = -1, 0
    iteration = 0
    visited = set()
    visited.add(guard_pos)
    new_pos = guard_pos[0]+guard_dir[0], guard_pos[1]+guard_dir[1]
    # print(f"new pos: {new_pos}")
    while 0 <= new_pos[0] < len(data) and 0 <= new_pos[1] < len(data[0]):
        iteration += 1
        if iteration == 9999:
            return 9999
        if data[new_pos[0]][new_pos[1]] == '#':
            guard_dir = turn_right(guard_dir)
        else:
            guard_pos = new_pos
            visited.add(guard_pos)
        new_pos = guard_pos[0]+guard_dir[0], guard_pos[1]+guard_dir[1]
        # print(f"new pos: {new_pos}")
    return len(visited)





def part2():
    data = [line.strip() for line in open("2406.txt", 'r')]
    obstruction_count = 0
    for r in range(len(data)):
        for c in range(len(data[0])):
            if data[r][c] not in ['^', '#']:
                original = data[r][c]
                if c == len(data[0]) -1:
                    data[r] = data[r][:c] + '#'
                else:
                    data[r] = data[r][:c] + '#' + data[r][c+1:]

                if part1(data) == 9999:
                    obstruction_count += 1

                if c == len(data[0]) -1:
                    data[r] = data[r][:c] + original
                else:
                    data[r] = data[r][:c] + original + data[r][c+1:]

    return obstruction_count



if __name__ == "__main__":
    # print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")