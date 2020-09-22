"""
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Input: haystack = "hello", needle = "ll"
Output: 2
"""

def strStr(haystack, needle):
    pos = 0
    if len(needle)==0:
        return 0
    else:
        #pos = haystack.find(needle)   ##builtin method
        for ch in haystack:
            if needle[0] == ch:
                if haystack[pos:pos+len(needle)]==needle:
                    return pos
            pos = pos + 1
        return -1
        
        


haystack= "hello"
needle= "ll"
print("output=",strStr(haystack,needle))
