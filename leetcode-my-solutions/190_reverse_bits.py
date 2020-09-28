"""
Reverse bits of a given 32 bits unsigned integer.
Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
"""
def reverseBits(n):
    n = list(str(n))
    for i in range(0, (len(n)//2)):
        temp = n[i]
        n[i] = n[len(n)-i-1]
        n[len(n)-i-1] = temp
    s=""
    for i in n:
        s=s+i
    return s
