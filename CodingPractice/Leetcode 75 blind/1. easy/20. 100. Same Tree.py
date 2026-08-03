# 20. 100. Same Tree
# https://leetcode.com/problems/same-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        if p == None and q != None:
            return False
        if q == None and p != None:
            return False 
        if p and q and p.val == q.val:
            if p.left != None and q.left != None and p.left.val != q.left.val:
                return False
            if p.right != None and q.right != None and p.right.val != q.right.val:
                return False
            return self.isSameTree(p.left,q.left ) and self.isSameTree(p.right,q.right )
        return False

            


        