"""
Given an integer, write a function to determine if it is a power of two.
Input: 16
Output: true
"""
def isPowerOfFour(n):
    if n<=0:
        return False
    while(n%4 ==0):
        n=n/4
    if n==1:
        return True
    return False


n =168
print("output:",isPowerOfFour(n))
