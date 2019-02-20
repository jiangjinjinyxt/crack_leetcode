"""
problem 112. Path Sum
https://leetcode.com/problems/path-sum/

solution:

""" 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
        	return False
        if root.left is None and root.right is None:
        	return root.val == target
        if root.left:
        	if self.hasPathSum(root.left, target - root.val):
        		return True
        if root.right:
        	if self.hasPathSum(root.right, target - root.val):
        		return True
        return False

class Solution(object):
    def hasPathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def dfs_visit(node, previous_sum):
        	temp_sum = previous_sum + node.val
        	if node.left is None and node.right is None:
        		return temp_sum == target
        	else:
        		if left:
        			if dfs_visit(node.left, temp_sum):
        				return True
        		if right:
        			if dfs_visit(node.right, temp_sum):
        				return True
        		return False
        if not root:
        	return False
        else:
        	return dfs_visit(root, 0)