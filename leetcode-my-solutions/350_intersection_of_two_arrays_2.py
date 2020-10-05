"""
Author: Sikder Tahsin Al Amin
Problem:
Given two arrays, write a function to compute their intersection.
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
"""

def intersect(nums1, nums2):
    intersect = []
    nums1 = sorted(nums1)
    nums2 = sorted(nums2)
    if len(nums1)==0 or len(nums2)==0:
        intersect=[]
        return None
    i = j= 0
    while i<len(nums1) and j<len(nums2):
        if nums1[i] == nums2[j]:
            intersect.append(nums1[i])
            i = i+1
            j = j+1
        elif nums1[i]>nums2[j]:
           j = j+1
        else:
            i = i+1
    return intersect


##Alternate solution - easy but higher complexity
def intersect2(nums1, nums2):
    intersect = []
    for i in nums1:
        if i in nums2:
            intersect.append(i)
            nums2.remove(i)                
    return intersect
