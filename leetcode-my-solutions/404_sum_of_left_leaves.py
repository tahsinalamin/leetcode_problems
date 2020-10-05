"""
Author: Sikder Tahsin Al Amin
Problem:
Find the sum of all left leaves in a given binary tree.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.sum = 0
        return self.helper(root,0)


    def helper(self,root,flag):
        if root== None:
            return 0
        if root.left == None and root.right == None and flag==1:
            self.sum = self.sum + root.val
            return self.sum 
        left = self.helper(root.left,1)
        right = self.helper(root.right,0)
        return self.sum
