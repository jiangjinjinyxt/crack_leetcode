"""
Problem 230. Kth Smallest Element in a BST
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

solution:

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        count = 0
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            count += 1
            if count == k:
                return root.val
            root = root.right
