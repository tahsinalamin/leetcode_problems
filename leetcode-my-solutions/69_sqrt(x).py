"""
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Input: 8
Output: 2
"""
def mySqrt(x):
    sqrt = x ** (0.5)
    return int(sqrt)    


x = 8
print("output=",mySqrt(x))
