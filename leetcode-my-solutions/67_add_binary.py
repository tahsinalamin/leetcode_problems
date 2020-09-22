"""
Author: Sikder Tahsin Al-Amin
Problem: Given two binary strings, return their sum (also a binary string).
Input: a = "11", b = "1"
Output: "100"
"""
def  addBinary(a,b):
    sum = int(a,2) + int (b,2)
    print(sum)
    res = []
    while sum>0:
        b = sum%2
        res.insert(0,str(b))
        sum = int(sum/2)
    s=""
    for i in res:
        s = s+i
    return s

def  addBinary2(a,b):
    sum = format(int(a,2) + int (b,2),'b')
    return sum
