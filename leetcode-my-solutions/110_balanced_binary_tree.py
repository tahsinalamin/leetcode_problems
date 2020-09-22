"""
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self,root):
        return self.helper(root) != -1
    
    def helper(self,root):
        if root == None:
            return 0
        else:
            left = self.helper(root.left)
            right = self.helper(root.right)
            if left == -1 or right == -1 or abs(left-right)>1:
                return -1
            return 1+max(left,right)

