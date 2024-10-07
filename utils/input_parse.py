def single_line_as_string(path: str) -> str:
    with open(path, 'r') as f:
       return f.readline()

def single_line_as_list(path: str) -> list[str]:
    with open(path, 'r') as f:
        return list(f.readline())

def many_lines_as_list(path: str) -> list[str]:
    with open(path, 'r') as f:
        return f.readlines()

if __name__ == "__main__":
    print(single_line_as_list("/home/ruben/Documents/aoc/utils/input.txt"))