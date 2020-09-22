"""
Author: Sikder Tahsin Al-Amin
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
Input: [1,3,5,6], 5
Output: 2
"""

def searchInsert(nums, target):
    if target <nums[0]:
        return 0
    for i in range(0,len(nums)):
        if nums[i]==target:
            return i
    for i in range(0,len(nums)):
        if target>nums[-1]:
            return len(nums)
        if nums[i]<target and nums[i+1]>target:
            return i+1
