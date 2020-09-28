"""
Author: Sikder Tahsin Al-Amin
Problem: Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree [1,2,2,3,4,4,3] is symmetric
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        if root == None:
            return True
        return self.helper(root.left,root.right)

    def helper(self,a,b):
        if a == None and b == None:
            return True
        if a == None or b == None:
            return False
        if a.val != b.val:
            return False
        outer_valid = self.helper(a.left,b.right)
        inner_valid = self.helper(a.right,b.left)
        return outer_valid and inner_valid


