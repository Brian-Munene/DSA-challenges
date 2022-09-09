def jewel_and_stones(jewels: str, stones: str)-> int:
    """
    Given a string representing your stones and another string representing a list of jewels, 
    return the number of stones that you have that are also jewels. 

    Example: Given the following jewels and stones...

    jewels = "abc", stones = "ac", return 2
    jewels = "Af", stones = "AaaddfFf", return 3
    jewels = "AYOPD", stones = "ayopd", return 0 
    """
    count = 0
    for s in stones:
        if s in jewels:
            count += 1
    return count

if __name__ == "__main__":
    vals = [["abc", "ac"], ["Af", "AaaddfFf"], ["AYOPD", "ayopd"]]

    for val in vals:
        print(jewel_and_stones(jewels=val[0], stones=val[1]))
