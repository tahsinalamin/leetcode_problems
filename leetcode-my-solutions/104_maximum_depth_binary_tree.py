"""
Author: Sikder Tahsin Al-Amin
Problem: Given a binary tree, find its maximum depth.
input: [3,9,20,null,null,15,7]
output: 3
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def maxDepth(self,root):
        if root == None:
            return 0
        l_depth = self.maxDepth(root.left)
        r_depth = self.maxDepth(root.right)

        if l_depth > r_depth:
            return l_depth +1
        else:
            return r_depth +1 
