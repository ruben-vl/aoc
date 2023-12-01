day1_input = [l.strip() for l in open('2023/python/day1_input.txt', 'r')]

no_alpha = map(lambda x: ''.join(ch for ch in x if ch.isnumeric()), day1_input)
print(f"first: {sum(int(i[0] + i[-1]) for i in no_alpha)}")

convert = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
    'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

def convert_forwards(x: str):
    res = ''
    for i in range(len(x)):
        res += x[i]
        for k, v in convert.items():
            res = res.replace(k, v)
    return res

def convert_backwards(x: str):
    res = ''
    for i in range(len(x)-1,-1,-1):
        res = x[i] + res
        for k, v in convert.items():
            res = res.replace(k, v)
    return res

c = map(lambda x: (convert_forwards(x), convert_backwards(x)), day1_input)
na = map(lambda x: (
    ''.join(ch for ch in x[0] if ch.isnumeric()),
    ''.join(ch for ch in x[1] if ch.isnumeric())
), c)

print(f"second: {sum(int(i1[0] + i2[-1]) for i1, i2 in na)}")
