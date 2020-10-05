"""
Author: Sikder Tahsin Al Amin
Problem:
Given two arrays, write a function to compute their intersection.
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
"""
def intersection(num1,num2):
    intersect = []
    #intersect = num1

    for i in num1:
        if i in num2:
            intersect.append(i)
    intersect = list(set(intersect))
    return intersect
