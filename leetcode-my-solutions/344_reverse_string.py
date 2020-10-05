"""
Write a function that reverses a string. The input string is given as an array of characters char[].
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""
def reverseString(s):
    for i in range(0,(len(s)//2)):
        temp = s[i]
        s[i]=s[len(s)-1-i]
        s[len(s)-1-i]=temp
    return s
