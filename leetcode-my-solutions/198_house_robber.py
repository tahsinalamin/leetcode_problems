"""
Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.
Input: [1,2,3,1]
Output: 4
"""
def rob(nums):
    incl =0
    excl = 0
    for i in nums:
        if excl>incl:
            new_excl = excl
        else:
            new_excl = incl 
        
        incl = excl+i
        excl = new_excl
    
    return max(excl, incl)


nums=[2,1,1,2]
print("output:",rob(nums))