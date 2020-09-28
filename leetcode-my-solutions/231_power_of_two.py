"""
Author: Sikder Tahsin Al Amin
Problem:
Given an integer, write a function to determine if it is a power of two.
Input: 16
Output: true
"""
def isPowerOfTwo(n):
    if n<=0:
        return False
    while(n%2 ==0):
        n=n/2
    if n==1:
        return True
    return False
