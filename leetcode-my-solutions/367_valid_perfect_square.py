"""
Author: Sikder Tahsin Al Amin
Problem:
Given a positive integer num, write a function which returns True if num is a perfect square else False.
Input: 14
Output: false
"""

def isPerfectSquare(num):
    sqrt=num**(0.5)
    if num%sqrt ==0:
        return True
    else:
        return False
