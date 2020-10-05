"""
Author: Sikder Tahsin Al Amin
Problem:
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
Input: "abab"
Output: True
Explanation: It's the substring "ab" twice
"""
def repeatedSubstringPattern(s):
    c = s[0]
    pos = 0
    flag =1
    substr=""
    for ch in s:
        if ch == c and flag ==1 and pos!=0:
            substr=s[0:pos]
            flag=0
        pos = pos+1
        
    #print("substr=",substr)
    #print("-----")
    i = 0
    while i <len(s):
        if s[i:i+len(substr)] != substr:
            return False
        else:
            i = i+len(substr)
    return True


## from net
def repeatedSubstringPattern2(s: str) -> bool:
        N = len(s)
        for i in range(1, N):
            if N % i == 0:
                sub_s = s[:i]
                if sub_s * (N // i) == s:
                    return True
        return False
