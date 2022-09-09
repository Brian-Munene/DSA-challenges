from collections import Counter
import cProfile, pstats, io
from pstats import SortKey

pr = cProfile.Profile()
pr.enable()

def spot_the_difference(s: str, t: str)-> str:
    s_count = Counter(s)
    t_count = Counter(t)
    diff = ''
    for char in t:
        if char in s and s_count[char] != t_count[char]:
            cnt = abs(s_count[char] - t_count[char])
            diff += 'char' * cnt
        elif char not in s:
            diff += char
    return diff

if __name__ == '__main__':
    vals = [["foobar","barfoott"], ["ide", "idea"], ["coding", "ingcod"]]

    for val in vals:
        print(f"s = {val[0]}, t = {val[1]}, difference = {spot_the_difference(s=val[0], t=val[1])}")

pr.disable()
s = io.StringIO()
sortby = SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)         
pr.print_stats()