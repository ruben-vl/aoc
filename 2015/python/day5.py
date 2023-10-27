def contains_three_vowels(data: str):
    vowel_count = 0
    for ch in data:
        if ch in ['a', 'e', 'i', 'o', 'u']:
            vowel_count += 1
    return vowel_count >= 3

def contains_letter_twice_in_row(data: str):
    for i in range(1,len(data)):
        if data[i-1] == data[i]:
            return True
    return False

def contains_not_ab_cd_pq_xy(data: str):
    return not 'ab' in data and not 'cd' in data \
            and not 'pq' in data and not 'xy' in data

def is_nice_string_old(data: str):
    return contains_three_vowels(data) \
        and contains_letter_twice_in_row(data) \
        and contains_not_ab_cd_pq_xy(data)

def contains_double_pair(data: str):
    pair_indices: dict[str, list[int]] = dict()
    for i in range(1, len(data)):
        if not data[i-1:i+1] in pair_indices.keys():
            pair_indices[data[i-1:i+1]] = [i-1]
        else:
            pair_indices[data[i-1:i+1]].append(i-1)
    for k, v in pair_indices.items():
        if len(v) > 2 or len(v) == 2 and abs(v[0] - v[1]) > 1:
            return True
    return False

def contains_one_gapper(data: str):
    for i in range(2, len(data)):
        if data[i-2] == data[i]:
            return True
    return False

def is_nice_string_new(data: str):
    return contains_one_gapper(data) and contains_double_pair(data)


if __name__ == "__main__":
    path = "2015/python/day5_input.txt"
    with open(path) as f:
        data = [s.rstrip() for s in f.readlines()]

    nice_count = 0
    for s in data:
        if is_nice_string_old(s):
            nice_count += 1
    
    print(f"Part one: {nice_count}")

    nice_count = 0
    for s in data:
        if is_nice_string_new(s):
            nice_count += 1

    print(f"Part two: {nice_count}")