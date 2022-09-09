def valid_anagram(s: str, t: str)-> bool:
    return set(list(s)) == set(list(t))

if __name__ == "__main__":
    vals = [["cat","tac"], ["listen", "silent"], ["program", "function"]]

    for val in vals:
        print(valid_anagram(s=val[0], t=val[1]))