"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
Input: "Hello World"
Output: 5
"""
def lengthofLastWord(s):
    substr = s.split()
    if len(substr)==0:
        return 0
    else:
        return len(substr[-1])



s="hello world"
print("output:", lengthofLastWord(s))
