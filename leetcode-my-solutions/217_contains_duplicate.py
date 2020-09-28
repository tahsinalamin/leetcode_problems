"""
Author: Sikder Tahsin Al Amin
Problem:
Given an array of integers, find if the array contains any duplicates.
Input: [1,2,3,1]
Output: true
"""
def containsDuplicate(nums):
    if len(nums)!=len(set(nums)):
        return True
    return False
