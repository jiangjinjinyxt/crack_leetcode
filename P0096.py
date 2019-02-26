"""
problem 96. Unique Binary Search Trees
https://leetcode.com/problems/unique-binary-search-trees/

solution:

""" 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 1

        table = dict()
        table[1] = 1

        def helper(num):
            if num not in table:
                if num <= 1:
                    ans = 1
                else:
                    ans = 0
                    for index in range(1, num + 1):
                        ans += helper(index - 1) * helper(num - index)
                table[num] = ans
            return table[num]
        return helper(n)