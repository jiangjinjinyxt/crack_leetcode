"""
problem 102: Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/
solution:

""" 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if not root:
            return ans

        stack = [root]

        while stack:
            size = len(stack)
            level_val = []
            for i in range(size):
                node = stack.pop(0)
                level_val.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            ans.append(level_val)
        return ans