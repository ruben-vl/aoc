def part1(data: list[list[int]]):
    return sum(extrapolate_forwards(l) for l in data)

def diff_seqs(seq: list[int]) -> list[list[int]]:
    seqs = [seq]
    while not all(map(lambda x: x == 0, seqs[-1])):
        seqs.append([seqs[-1][i+1]-n for i, n in enumerate(seqs[-1][:-1])])
    return seqs

def extrapolate_forwards(seq: list[int]) -> int:
    seqs = diff_seqs(seq)[::-1]
    for idx, seq in enumerate(seqs):
        seq.append(seq[-1] + seqs[max(0, idx-1)][-1])
    return seqs[-1][-1]

def part2(data: list[list[int]]):
    return sum(extrapolate_backwards(l) for l in data)

def extrapolate_backwards(seq: list[int]) -> int:
    seqs = diff_seqs(seq)[::-1]
    for idx, seq in enumerate(seqs):
        seqs[idx] = [seq[0] - seqs[max(0, idx-1)][0]] + seq
    return seqs[-1][0]


if __name__ == "__main__":
    data = [list(map(lambda x: int(x), l.strip().split(' '))) for l in open("2023/python/day9_input.txt", 'r')]
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
