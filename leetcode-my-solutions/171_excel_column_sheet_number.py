"""
Author: Sikder Tahsin Al Amin
Problem: Given a column title as appear in an Excel sheet, return its corresponding column number.
Input: "AB"
Output: 28
"""
def titleToNumber(s):
    column = dict({'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,
    'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26})
    value = 0
    if len(s) == 0:
        return 0
    for i in range(0,len(s)):
        if i == len(s)-1:
            value = value + column.get(s[i])
        else:
            value = value + (column.get(s[i])*26**(len(s)-i-1))
            print("else:",value)
    return value
