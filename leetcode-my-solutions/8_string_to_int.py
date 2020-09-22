"""
Author: Sikder Tahsin Al-Amin
Problem: Implement atoi which converts a string to an integer.
Input: "   -42"
Output: -42
"""
def myAtoi(str):
    str = str.lstrip()
    res_string = ""
    
    #we removed all whitespace before, so we should get "-", "+" or digit directly if it is a valid number
    for char in str:
        if char.isdigit():
            res_string += char
        elif char in ['-' ,'+'] and not res_string:
            res_string += char
        else:
            break
    #in case we only got "-" or "+" without digits
    if res_string == '-' or res_string == '+':
        res_string = ""
    #when we got no valid number    
    if (not res_string):
        return 0
    else:
        return int(res_string) if pow(-2,31) <= int(res_string) <= pow(2,31)-1 else [pow(-2,31),pow(2,31)-1][int(res_string)>0]
