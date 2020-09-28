"""
Author: Sikder Tahsin Al Amin
Problem:
Given an array of integers and an integer k,
find out whether there are two distinct indices i and j in the array
such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
Input: nums = [1,2,3,1], k = 3
Output: true
"""

def containsNearbyDuplicate(nums,k): ##from net
    seen = dict()
    for indx, val in enumerate(nums):
        if indx - k <= seen.get(val,-k-1):
            return True
        seen[val] = indx
    return False
