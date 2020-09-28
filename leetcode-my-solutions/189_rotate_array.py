"""
Given an array, rotate the array to the right by k steps, where k is non-negative.
Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
"""
def rotate(nums,k):
    for rotation in range(0,k):
        temp=nums[len(nums)-1]
        for i in range(len(nums)-1,0,-1):
            nums[i]=nums[i-1]
            print(i, nums[i])
        nums[0]=temp
        print(nums)
    print(nums)

def rotate2(nums, k):
    k %= len(nums)
    for i in range(k):
        nums.insert(0, nums.pop(-1))
    print(nums)

nums=[1,2,3,4,5,6,7]
k=3
print("output:",rotate2(nums,k))
