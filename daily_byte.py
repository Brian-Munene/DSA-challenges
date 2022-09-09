from collections import Counter

def daily_byte(word: str)-> bool:
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
