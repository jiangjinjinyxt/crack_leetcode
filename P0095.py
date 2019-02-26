"""
problem 95. Unique Binary Search Trees II
https://leetcode.com/problems/unique-binary-search-trees-ii/

solution:

""" 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        table = dict()
        def helper(left, right):
            if (left, right) not in table:
                if left > right:
                    return [None]
                elif left == right:
                    return [TreeNode(left)]
                trees = []
                for index in range(left, right + 1):
                    for left_tree in helper(left, index - 1):
                        for right_tree in helper(index + 1, right):
                            tree = TreeNode(index)
                            tree.left = left_tree
                            tree.right = right_tree
                            trees.append(tree)
                table[(left, right)] = trees
            return table[(left, right)]
        if n < 1:
            return []
        return helper(1, n)





