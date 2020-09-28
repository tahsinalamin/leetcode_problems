"""
Author: Sikder Tahsin Al Amin
Problem:
Invert a binary tree.
"""

class Solution:
    def invertTree(self, root):
        if root == None:
            return None
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left = right
        root.right = left
        return root
