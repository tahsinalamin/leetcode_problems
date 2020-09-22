"""
Given a binary tree, return the inorder traversal of its nodes' values.
Input: [1,null,2,3]
Output: [1,3,2]
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def printInorder(self,root):
        res = []
        if root != None:
            if root.left != None:
                res = self.printInorder(root.left) 
            res.append(root.val)
            if root.right!=None:
                res = res + self.printInorder(root.right)
        return res


root = TreeNode(1)
#root.left  = TreeNode(None)
root.right = TreeNode(2)
root.right.left  = TreeNode(3)
obj = TreeNode(root)
print("output:",obj.printInorder(root))