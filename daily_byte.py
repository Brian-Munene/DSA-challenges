from collections import Counter

def daily_byte(word: str)-> bool:
    """
    Given a string representing the sequence of moves a robot vacuum makes, return whether or not it will return to its original position. The string will only contain L, R, U, and D characters, representing left, right, up, and down respectively.

    Example: Given the following strings...

    "LR", return true
    "URURD", return false
    "RUULLDRD", return true
    """
    
    horizontal = 0
    vertical = 0

    for i in word:
        if i == 'U':
            vertical += 1
        elif i == 'D':
            vertical -= 1
        elif i == 'L':
            horizontal += 1
        elif i == 'R':
            horizontal -= 1
    print(vertical, horizontal)

    if horizontal == 0 and vertical == 0:
        print(True)
        return True
    else:
        print(False)
        return False


daily_byte('LR')
daily_byte('URURD')
daily_byte("RUULLDRD")
