"""
Author: Sikder Tahsin Al-Amin
Problem: Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        if n<1:
            return []
        else:
            return self.traverse(1,n)
    
    def traverse(self, left, right):
        if left > right:
            return [None]
        result = []
        for i in range(left, right+1):
            for l in self.traverse(left, i-1):
                for r in self.traverse (i+1, right):
                    node = TreeNode(i)
                    node.left = l
                    node.right = r 
                    result.append(node)
        return result
