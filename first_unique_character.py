import cProfile, pstats, io
from pstats import SortKey

pr = cProfile.Profile()
pr.enable()
def first_unique_character(s: str)-> int:
    """
    Given a string, return the index of its first unique character. If a unique character does not exist, return -1. 

    Example: Given the following strings...

    "abcabd", return 2
    "thedailybyte", return 1
    "developer", return 0
    """
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            return i
    
    return -1

if __name__ == "__main__":
    vals = ["abcabd", "thedailybyte", "developer"]
    
    print("\n The first unique character is at index: \n")

    for val in vals:
        print(f"{val}, returns {first_unique_character(val)}\n")


pr.disable()
s = io.StringIO()
sortby = SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)         
pr.print_stats()