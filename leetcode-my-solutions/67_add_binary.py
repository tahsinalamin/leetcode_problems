"""
Given two binary strings, return their sum (also a binary string).
Input: a = "11", b = "1"
Output: "100"
"""
def  addBinary(a,b):
    sum = int(a,2) + int (b,2)
    print(sum)
    res = []
    while sum>0:
        b = sum%2
        res.insert(0,str(b))
        sum = int(sum/2)
    s=""
    for i in res:
        s = s+i
    return s

def  addBinary2(a,b):
    sum = format(int(a,2) + int (b,2),'b')
    return sum

    
a="10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101"
b="110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011"
print("output:",addBinary2(a,b))