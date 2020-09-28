"""
Author: Sikder Tahsin Al Amin
Problem: 
Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).
Input: 00000000000000000000000000001011
Output: 3

"""


def hammingWeight(n):
        """
        :type n: int
        :rtype: int
        """
        count =0
        for i in str(n):
            if i=='1':
                count = count +1
        return count
