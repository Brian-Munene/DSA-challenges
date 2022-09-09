def add_binary(bin1: str = None, bin2: str = None)-> str:
    """
    Given two binary strings (strings containing only 1s and 0s) return their sum (also as a binary string). 
    Note: neither binary string will contain leading 0s unless the string itself is 0 

    Example: Given the following binary strings...

    "100" + "1", return "101"
    "11" + "1", return "100"
    "1" + "0", return  "1"
    """
    res = bin(int(bin1,2) + int(bin2,2))
    return res[2:]

if __name__ == '__main__':
    vals = [["100", "1"], ["11", "1"], ["1", "0"]]
    for v in vals:
        print(f'{v[0]} + {v[1]} = {add_binary(v[0], v[1])}')
