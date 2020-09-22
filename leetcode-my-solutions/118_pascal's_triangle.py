"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
Input: 5
Output:
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
"""
def generate(numRows):
    pascal=[]
    for i in range(1,numRows+1):
        temp=[]
        for j in range(1,i+1):
            if i>2 and j>1 and j<i:
                temp.append(pascal[i-2][j-1]+pascal[i-2][j-2])
                #print(pascal[i-2])
            else:
                temp.append(1)
        pascal.append(temp)
    return pascal


numRows = 5
print("output:",generate(numRows))