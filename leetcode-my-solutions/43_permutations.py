"""
Author: Sikder Tahsin Al-Amin
Problem: Given a collection of distinct integers, return all possible permutations.

Input: [1,2,3]
Output:
[
  [1,2,3],  [1,3,2],  [2,1,3],  [2,3,1],  [3,1,2],  [3,2,1]
]
"""

def permute(nums):
    if len(nums) == 0:
        return []
    if len(nums)==1:
        return [nums]
    
    l=[]
    for i in range(0,len(nums)):
        m=nums[i]
        l_rem = nums[:i]+nums[i+1:]
        #print(l_rem)
        for j in permute(l_rem):
            l.append([m]+j)
            print(l)

    return l
