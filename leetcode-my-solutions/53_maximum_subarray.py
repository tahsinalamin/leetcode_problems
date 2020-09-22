"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""
def maxSubArray(nums):
    max_so_far = max(nums)
    max_ending_here = 0
    if len(nums)==1:
        return nums[0]
    for i in range(0,len(nums)):
        max_ending_here = max_ending_here + nums[i]
        if max_ending_here<0:
            max_ending_here =0
        else:
            if max_so_far <max_ending_here:
                max_so_far = max_ending_here
    return max_so_far


def maxSubArray2(nums):
    n=len(nums)
    maxsofar=max(nums)
    temp=0
    for i in range(n):
        temp+=nums[i]
        if temp>=0:
            maxsofar=max(maxsofar, temp)
        else: temp=0
            
    return maxsofar



nums = [-2,-1]
print("output:",maxSubArray(nums))