"""
Author: Sikder Tahsin Al-Amin
Problem: Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
Input: [1,2,3]
Output: [1,2,4]
"""

def plusOne(digits):
    s=""
    for i in digits:
        s= s+str(i)
    number = int(s)
    number = number +1 
    list_number=[]
    for i in str(number):
        list_number.append(int(i))

    return list_number
