def get_visited(data: str):
    visited = set()
    visited.add((0,0))
    current_x = 0
    current_y = 0
    for char in data:
        match char:
            case '^':
                current_y += 1
            case 'v':
                current_y -= 1
            case '<':
                current_x -= 1
            case '>':
                current_x += 1
        visited.add((current_x, current_y))
    return visited

if __name__ == "__main__":
    path = "2015/python/day3_input.txt"
    with open(path) as f:
        data = [s.rstrip() for s in f.readlines()]
    f.close()
    data = data[0]

    print(f"Part one: {len(get_visited(data))}")

    santa_string = ""
    robo_string = ""

    for i in range(len(data)):
        if i % 2 == 0:
            santa_string += data[i]
        else:
            robo_string += data[i]
    
    santa_visited = get_visited(santa_string)
    robo_visited = get_visited(robo_string)
    all_visited = santa_visited | robo_visited
    print(f"Part two: {len(all_visited)}")