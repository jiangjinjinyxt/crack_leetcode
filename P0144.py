"""
problem 144: Binary Tree Preorder Traversal
https://leetcode.com/problems/binary-tree-preorder-traversal/

solution:

""" 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# recursive
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        if not root:
            return ans

        def helper(node):
            ans.append(node)
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
        helper(root)
        return ans

# iterative
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        ans = []
        if root:
            stack.append(root)
        while stack:
            node = stack.pop()
            while node:
                ans.append(node.val)
                if node.right:
                    stack.append(node.right)
                node = node.left
        return ans
        