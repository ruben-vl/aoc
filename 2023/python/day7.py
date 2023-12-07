from functools import cmp_to_key, reduce
from operator import add

def part1(data: list[tuple[str, int]]):
    data.sort(key=cmp_to_key(lambda i1, i2: compare_hands(i1[0], i2[0])))
    return reduce(add, [(rank+1)*bid for rank, (_, bid) in enumerate(data)])

def compare_hands(hand1, hand2):
    if hand_type(hand1) == hand_type(hand2):
        return secondary_order(hand1, hand2)
    return hand_type(hand1) - hand_type(hand2)

def hand_type(hand: str) -> int:
    char_counts = {c: hand.count(c) for c in set(hand)}
    match len(char_counts.keys()):
        case 1: return 7
        case 2: return 6 if 4 in char_counts.values() else 5
        case 3: return 4 if 3 in char_counts.values() else 3
        case 4: return 2
        case _: return 1

def secondary_order(hand1, hand2):
    strength = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8,
                '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
    for i in range(len(hand1)):
        if strength[hand1[i]] > strength[hand2[i]]:
            return 1
        elif strength[hand1[i]] < strength[hand2[i]]:
            return -1
    return 0

def part2(data: list[tuple[str, int]]):
    data.sort(key=cmp_to_key(lambda i1, i2: compare_hands2(i1[0], i2[0])))
    return reduce(add, [(rank+1)*bid for rank, (_, bid) in enumerate(data)])

def compare_hands2(hand1: str, hand2: str):
    type1 = max([hand_type(hand1.replace('J',c)) for c in hand1])
    type2 = max([hand_type(hand2.replace('J',c)) for c in hand2])
    if type1 == type2:
        return secondary_order2(hand1, hand2)
    return type1 - type2

def secondary_order2(hand1: str, hand2: str):
    strength = {'A': 14, 'K': 13, 'Q': 12, 'T': 10, '9': 9, '8': 8,
                '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'J': 1}
    for i in range(len(hand1)):
        if strength[hand1[i]] > strength[hand2[i]]:
            return 1
        elif strength[hand1[i]] < strength[hand2[i]]:
            return -1
    return 0


if __name__ == "__main__":
    data = [l.strip().split(' ') for l in open("2023/python/day7_input.txt", 'r')]
    data = [(hand, int(bid)) for hand, bid in data]
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
