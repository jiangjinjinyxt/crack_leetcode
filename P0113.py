"""
problem 113. Path Sum II
https://leetcode.com/problems/path-sum-ii/

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
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        parent_table = dict()
        result = []

        def path(node):
            temp = []
            while node in parent_table:
                temp.append(node.val)
                node = parent_table[node]
            result.append(temp)
        def dfs(node, previous_sum):
            if node.left is None and node.right is None:
                if node.val + previous_sum == target:
                    path(node)
            else:
                if node.left:
                    dfs(node.left, previous_sum + node.val)
                if node.right:
                    dfs(node.right, previous_sum + node.val)
        if root is None:
            return result
        else:
            dfs(root, 0)
            return result

# iterative
class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []

        def dfs(previous_nodes, node, target_sum):
            previous_nodes = previous_nodes + [node.val]
            if node.left is None and node.right is None and node.val == target_sum:
                result.append(previous_nodes)
            if node.left:
                dfs(previous_nodes, node.left, target_sum - node.val)
            if node.right:
                dfs(previous_nodes, node.right, target_sum - node.val)

        if not root:
            return result
        else:
            dfs([], root, target)
            return result