"""
Author: Sikder Tahsin Al Amin
Problem: Given a positive integer, return its corresponding column title as appear in an Excel sheet.
Input: 28
Output: "AB"
"""
def convertToTitle(n):
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    d= {}
    for i in range(0,len(alphabet)):
        d[i+1]=alphabet[i]
    #print(d)

    s = ""
    #if (n<=26):
        #return d.get(n)
    while n>0:
        m = int(n%26)
        n = int(n/26)
        if m==0:
            s="Z"+s
            n = n-1
        else:
            s=str(d.get(m))+s
    return s
