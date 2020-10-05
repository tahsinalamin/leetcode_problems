"""
Given an integer, write a function to determine if it is a power of three.
Input: 27
Output: true
"""
def isPowerOfThree(n):
    if n<=0:
        return False
    while(n!=1):
        if n%3 !=0:
            return False
        n=n/3
    return True



n =9
print("output:",isPowerOfThree(n))
