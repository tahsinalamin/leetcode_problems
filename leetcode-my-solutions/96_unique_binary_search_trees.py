"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
Input: 3
Output: 5
"""

def numTrees(n):
    if n<=1:
        return 1
    else:
        return int(factorial(2*n)/(factorial (n+1) * factorial(n))) ## 2n! / (n+1)!n!

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1) 


n = 3
print("output:",numTrees(n))