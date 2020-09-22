"""
Author: Sikder Tahsin Al-Amin
Problem: Given two binary trees, write a function to check if they are the same or not.
input: [1,2,3] [1,2,3]
output: True
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def preorderTraversal(self,root):
        res = []
        #if root != None:
        if root == None:
            res.append(root)
            return res
        res.append(root.val)
        #if root.left != None:
        res = res + self.preorderTraversal(root.left) 
            
        #if root.right!=None:
        res = res + self.preorderTraversal(root.right)
        return res
    
    def isSameTree(self, p, q):
        list_p=[]
        if p!= None:
            list_p = self.preorderTraversal(p)
        #print(list_p)

        list_q=[]
        if q!= None:
            list_q = self.preorderTraversal(q)
        #print(list_q)

        if list_p == list_q:
            return True
        else:
            return False


p = TreeNode(1)
p.left  = TreeNode(None)
p.right = TreeNode(2)
p.right.left  = TreeNode(3)

q = TreeNode(1)
#root.left  = TreeNode(None)
q.right = TreeNode(2)
q.right.left  = TreeNode(4)

#obj = TreeNode(root)
print("output:",p.isSameTree(p,q))
