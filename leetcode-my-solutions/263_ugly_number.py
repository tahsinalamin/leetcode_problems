"""
Author: Sikder Tahsin Al Amin
Problem:
Write a program to check whether a given number is an ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
Input: 6
Output: true
Explanation: 6 = 2 × 3
"""
import math
def isUgly(num):
    prime_factors=[]
    if num<1:
        return False
    while num%2 ==0:
        prime_factors.append(2)
        num=int(num/2)
    i=3
    for j in range(3,int(math.sqrt(num))+1,2):
        while num%i == 0:
            prime_factors.append(i)
            num = int(num/i)
    if num>2:
        prime_factors.append(num)
    print(prime_factors)

    for i in prime_factors:
        if i not in [2,3,5]:
            return False
    return True

def isUgly2(num): ##from net + me
    for p in 2, 3, 5:
        while num%p ==0:
            num=num/p
    if num==1:
        return True
    else:
        return False
        
def isUgly3(num): ##from net
    if num == 0:
        return False
    while num % 2 == 0:
        num = num/2
    while num % 3 == 0:
        num = num/3
    while num % 5 == 0:
        num = num/5
    if num == 1:
        return True
    return False
