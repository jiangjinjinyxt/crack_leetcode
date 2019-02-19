"""
108. Convert Sorted Array to Binary Search Tree
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

solution:

""" 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def helper(left, right):
            if left <= right:
                middle = left + (right - left) // 2
                node = TreeNode(nums[middle])
                node.left = helper(left, middle - 1)
                node.right = helper(middle + 1, right)
            else:
                node = None
            return node
        return helper(0, len(nums) - 1)
