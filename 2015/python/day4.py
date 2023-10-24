import hashlib

def find_lowest_nat(data: str, start):
    i = 0
    hash: str = ""
    while not hash.startswith(start):
        i += 1
        hash = hashlib.md5((data+str(i)).encode()).hexdigest()
    return i

if __name__ == "__main__":

    data = "bgvyzdsv"

    print(f"Part one: {find_lowest_nat(data, '00000')}")
    print(f"Part two: {find_lowest_nat(data, '000000')}")
