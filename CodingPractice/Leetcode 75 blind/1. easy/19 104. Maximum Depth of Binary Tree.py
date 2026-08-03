# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# 19 104. Maximum Depth of Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right 
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            return 1 + self.getMax(root)
        return 0

    def getMax(self, root):
        h1, h2 = 0, 0
        if root.left != None:
            h1 = 1 + self.getMax(root.left )
        if root.right != None:
            h2 = 1 + self.getMax(root.right)
        return max(h1, h2)
            