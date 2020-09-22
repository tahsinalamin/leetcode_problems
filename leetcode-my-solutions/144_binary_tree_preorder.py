"""
Given a binary tree, return the preorder traversal of its nodes' values.
Input: [1,null,2,3]
Output: [1,2,3
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def preorderTraversal(self,root):
        res = []
        if root != None:
            res.append(root.val)
            if root.left != None:
                res = res + self.preorderTraversal(root.left) 
            
            if root.right!=None:
                res = res + self.preorderTraversal(root.right)
        return res


root = TreeNode(1)
#root.left  = TreeNode(None)
root.right = TreeNode(2)
root.right.left  = TreeNode(3)
obj = TreeNode(root)
print("output:",obj.preorderTraversal(root))