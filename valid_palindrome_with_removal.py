def validPalindromeWithRemoval(word: str=None):
    """
    Given a string and the ability to delete at most one character, 
    return whether or not it can form a palindrome. 
    """
    if word == "": return True

    removed = []
    chars = list(word)
    l,r = 0, len(chars)-1
    while l < r:
        if chars[l] == chars[r]:
            l += 1
            r -= 1
        else:
            chars.pop(r)
            r -=1
            removed.append(chars[r])
    print(removed)
    if len(removed) == 1:
        return f"{True} (remove {removed[0]})"
    if len(removed) > 1:
        return False
    if len(removed) == 0:
        return True

if __name__ == "__main__":
    vals = ['abcba', 'foobof', 'abccab']
    for val in vals:
        print(validPalindromeWithRemoval(val))