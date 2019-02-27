"""
problem 103: Binary Tree Zigzag Level Order Traversal
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
solution:

""" 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if root:
            stack.append(root)
        left = True
        while stack:
            size = len(stack)
            level_val = []
            while size:
                size -= 1
                node = stack.pop(size)
                level_val.append(node.val)
                if left:
                    if node.right:
                        stack.append(node.right)
                    if node.left:
                        stack.append(node.left)
                else:
                    if node.left:
                        stack.append(node.left) 
                    if node.right:
                        stack.append(node.right)
            ans.append(level_val)
            left = left is False
        return ans
