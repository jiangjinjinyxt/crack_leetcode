"""
problem 129: Sum Root to Leaf Numbers
https://leetcode.com/problems/sum-root-to-leaf-numbers/

solution:

""" 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = 0
        if not root:
            return ans

        def helper(num, node):
            nonlocal ans
            num = num * 10 + node.val
            if not (node.left or node.right):
                ans += num
            if node.left:
                helper(num, node.left)
            if node.right:
                helper(num, node.right)
        helper(0, root)
        return ans

