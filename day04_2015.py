import hashlib

def part1(data):
    i = 0
    while True:
        hashed = hashlib.md5(f"{data}{str(i)}".encode()).hexdigest()
        if hashed[0:5] == "00000":
            return i
        i += 1

def part2(data):
    i = 0
    while True:
        hashed = hashlib.md5(f"{data}{str(i)}".encode()).hexdigest()
        if hashed[0:6] == "000000":
            return i
        i += 1

if __name__ == "__main__":
    data = "bgvyzdsv"
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
