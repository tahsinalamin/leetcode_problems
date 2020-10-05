"""
Write a function that takes a string as input and reverse only the vowels of a string.
Input: "hello"
Output: "holle"
"""
def reverseVowels(s):
    s=list(s)
    vowel=['a','e','i','o','u','A','E','I','O','U']
    v=[]
    pos_vowel=[]
    for i in range(0,len(s)):
        if s[i] in vowel:
            v.append(s[i])
            pos_vowel.append(i)
    v=v[::-1] #reversing
    #print(v)
    for i in range(0,len(pos_vowel)):
        s[pos_vowel[i]]=v[i]
    rs=""
    for i in s:
        rs=rs+i
    return rs         
