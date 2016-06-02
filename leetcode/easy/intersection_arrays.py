'''
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.'''

def get_intersection(array1,array2):
    intersection = []
    for num in array1:
        if num in array2:
            if num not in intersection:
                intersection.append(num)
    return intersection

def main():
    array1 = [1,2,3]
    array2 = [2,3,4]
    print get_intersection(array1,array2)

if __name__ == "__main__": main()