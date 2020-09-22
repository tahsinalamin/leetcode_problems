"""
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
Input: "III"
Output: 3
"""

def romanToInt(s):
    s=list(s)
    dict_roman = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
    print(s)
    num = 0
    for i in range(0,len(s)):
        print(i,"------------",s[i],s[i-1])
        if i<1:
            num = num + dict_roman.get(s[i])
        elif s[i-1]=="I" and s[i]=="X":
            num = num - dict_roman.get(s[i-1])+ dict_roman.get(s[i]) - dict_roman.get(s[i-1])
            print("A")
        elif s[i-1]=="I" and s[i]=="V":
            num = num - dict_roman.get(s[i-1])+ dict_roman.get(s[i]) - dict_roman.get(s[i-1])
            print("B")
        elif s[i-1]=="X" and s[i]=="L":
            num = num - dict_roman.get(s[i-1])+ dict_roman.get(s[i])- dict_roman.get(s[i-1])
            print("C")
        elif s[i-1]=="X" and s[i]=="C":
            num = num - dict_roman.get(s[i-1])+ dict_roman.get(s[i])  - dict_roman.get(s[i-1])
            print("D")
        elif s[i-1]=="C" and s[i]=="D":
            num = num - dict_roman.get(s[i-1])+ dict_roman.get(s[i]) - dict_roman.get(s[i-1])
            print("E")
        elif s[i-1]=="C" and s[i]=="M":
            num = num - dict_roman.get(s[i-1])+ dict_roman.get(s[i]) - dict_roman.get(s[i-1])
            print("F")
        else:
            num = num + dict_roman.get(s[i])
            print("G")
        print(s[i],num)
    return num


s="MMMCDXC"
print("output:",romanToInt(s))