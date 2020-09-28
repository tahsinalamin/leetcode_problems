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




n = '00000010100101000001111010011100'
print("output:",reverseBits(n))

###cracking coding interview 5.1
def insertion(N,M,i,j):
    N = list(str(N))
    N.reverse()
    M = list(str(M))
    M.reverse()
    m_index = 0
    for index in range(0,len(N)):
        if index <= j-1 and index >=i-1:
            N[index] = M[m_index]
            m_index = m_index - 1
        print(index, N[index])
    s=""
    for index in N:
        s =  index + s
    return s


N = 1000000000
M = 10011
i = 2
j = 6
print("output:",insertion(N,M,i,j))
