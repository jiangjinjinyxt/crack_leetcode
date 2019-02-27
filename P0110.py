"""
problem 110. Balanced Binary Tree
https://leetcode.com/problems/balanced-binary-tree/

solution:

""" 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def helper(node):
            if node is None:
                return 0
            left_height = helper(node.left)
            right_height = helper(node.right)
            if left_height == -1 or right_height == -1:
                return -1
            if abs(left_height - right_height) < 2:
                return max(left_height, right_height) + 1
            else:
                return -1
        return helper(root) != -1
