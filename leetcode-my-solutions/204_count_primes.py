""" 
Author: Sikder Tahsin Al Amin
Problem:
Count the number of prime numbers less than a non-negative number, n.
Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""

def countPrimes(n):
    i = 2
    count = 0
    if n==2:
        return 1
    while i<n:
        isPrime =True
        for num in range(2,i):
            if i%num == 0:
                isPrime = False
        if isPrime == True:
            count = count +1
        i = i+1
    return count

#Another Solution (from net)

def countPrimes2(self, n):
    if n <= 2:
        return 0
    res = [True] * n
    res[0] = res[1] = False
    for i in range(2, n):
        if res[i] == True:
            for j in range(2, (n-1)//i+1):
                res[i*j] = False
    return sum(res)
