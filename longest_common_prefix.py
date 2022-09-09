def longest_common_prefix(strs: list = None)-> str:
    if len(strs) == 0:
            return ""
    current = strs[0]
    for i in range(1,len(strs)):
        temp = ""
        if len(current) == 0:
            break
        for j in range(len(strs[i])):
            if j<len(current) and current[j] == strs[i][j]:
                temp+=current[j]
            else:
                break
        current = temp
    return current


if __name__ == "__main__":
    words = [["colorado", "color", "cold"], ["a", "b", "c"], ["spot", "spotty", "spotted"]]

    for word in words:
        print(f"Words are {word} longest prefix is:{longest_common_prefix(word)}")