def two_sum_with_sorting(lst: list, k):
    lst.sort()
    l, r = 0, len(lst) - 1

    while l < r:
        sum_v = lst[l] + lst[r]
        if sum_v == k:
            return f"{True} ({lst[l]} + {lst[r]})"
        elif sum_v > k:
            r -= 1
        elif sum_v < k:
            l += 1
    return False

def two_sum_with_dict(nums:list, k):
    record = dict()
    for i, n in enumerate(nums):
        if n not in record:
            record[k-n] = i
        else:
            return f"{True} ({nums[i]} + {k-n})"
    return False

if __name__ == "__main__":
    vals = [[[1, 3, 8, 2],10], [[3, 9, 13, 7], 8], [[4, 2, 6, 5, 2], 4]]

    print('\n Two sum with sorting.\n')
    print('--------------------')
    for val in vals:
        print(two_sum_with_sorting(lst=val[0], k=val[1]))

    print("\n Two sum using compliments method \n")
    print('--------------------------------')
    for val in vals:
        print(two_sum_with_dict(nums=val[0], k=val[1]))