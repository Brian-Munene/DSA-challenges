def intersection_of_numbers(nums1: list, nums2: list)-> list:
    """
    Given two integer arrays, return their intersection. 
    Note: the intersection is the set of elements that are common to both arrays.

    Ex: Given the following arrays...

    nums1 = [2, 4, 4, 2], nums2 = [2, 4], return [2, 4]
    nums1 = [1, 2, 3, 3], nums2 = [3, 3], return [3]
    nums1 = [2, 4, 6, 8], nums2 = [1, 3, 5, 7], return []
    """
    res = []
    
    for i in nums1:
        if i in nums2 and i not in res:
            res.append(i)
    return res

if __name__ == "__main__":
    vals = [[[2, 4, 4, 2], [2, 4]], [[1, 2, 3, 3], [3, 3]], [[2, 4, 6, 8], [1, 3, 5, 7]]]

    for val in vals:
        print(intersection_of_numbers(nums1=val[0], nums2=val[1]))

