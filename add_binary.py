def add_binary(bin1: str = None, bin2: str = None)-> str:
    res = bin(int(bin1,2) + int(bin2,2))
    return res[2:]

if __name__ == '__main__':
    vals = [["100", "1"], ["11", "1"], ["1", "0"]]
    for v in vals:
        print(f'{v[0]} + {v[1]} = {add_binary(v[0], v[1])}')
