"""
problem 114. Flatten Binary Tree to Linked List
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

solution:

""" 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        def helper(node):
            if node.left is None:
                if node.right is None:
                    return node, node
                else:
                    head, tail = helper(node.right)
                    node.right = head
                    return node, tail
            else:
                if node.right is None:
                    head, tail = helper(node.left)
                    node.right = head
                    node.left = None
                    return node, tail
                else:
                    left_head, left_tail = helper(node.left)
                    right_head, right_tail = helper(node.right)
                    node.right = left_head
                    node.left = None
                    left_tail.right= right_head
                    return node, right_tail
        if root:
            helper(root)

