"""
Author: Sikder Tahsin Al Amin
Problem:
Given an integer, write a function to determine if it is a power of four.
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


### Another method
def isPowerOfFour2(n):
    if n<=0:
        return False
    while(n>0):
        if n%4!=0:
            return False
        n=n/4
    return True
