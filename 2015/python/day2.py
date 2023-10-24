def wrapping_amount(l, w, h):
    area = 2*l*w + 2*w*h + 2*h*l
    extra = min([l*w, w*h, h*l])
    return area + extra

def ribbon_amount(l, w, h):
    return 2*l + 2*w + 2*h - 2*max([l,w,h])

def bow_amount(l, w, h):
    return l*w*h

if __name__ == "__main__":
    path = "2015/python/day2_input.txt"
    with open(path) as f:
        data = [s.rstrip() for s in f.readlines()]
    f.close()

    total = 0
    for dimstr in data:
        dim = [int(s) for s in dimstr.split('x')]
        total += wrapping_amount(dim[0], dim[1], dim[2])
    print(f"Part one: {total}")

    total = 0
    for dimstr in data:
        dim = [int(s) for s in dimstr.split('x')]
        total += ribbon_amount(dim[0], dim[1], dim[2])
        total += bow_amount(dim[0], dim[1], dim[2])
    print(f"Part two: {total}")
