"""
Author: Sikder Tahsin Al-Amin
Problem: Given a string, find the length of the longest substring without repeating characters.
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
"""

def lengthOfLongestSubstring(s):
    length = 0
    max_length = 0
    s=list(s)
    prev= []
    for i in s:
        if i in prev:
            if max_length < length:
                max_length = length
            #length =1
            prev =prev[prev.index(i)+1:]
            prev.append(i)
            length = len(prev)
        else:
            prev.append(i)
            length = length + 1 
        print(i, max_length, prev, length)
    if length> max_length:
        return length
    return max_length
