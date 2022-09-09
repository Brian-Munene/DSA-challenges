def valid_anagram(s: str, t: str)-> bool:
    """
    Given two strings s and t return whether or not s is an anagram of t. 
    Note: An anagram is a word formed by reordering the letters of another word. 

    Example: Given the following strings...

    s = "cat", t = "tac", return true
    s = "listen", t = "silent", return true
    s = "program", t = "function", return false
    """
    return set(list(s)) == set(list(t))

if __name__ == "__main__":
    vals = [["cat","tac"], ["listen", "silent"], ["program", "function"]]

    for val in vals:
        print(valid_anagram(s=val[0], t=val[1]))