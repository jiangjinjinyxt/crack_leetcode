"""
problem 162: Find Peak Element
https://leetcode.com/problems/find-peak-element/

solution:

""" 
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = left + (right - left) // 2
            if middle - 1 >= left and nums[middle - 1] > nums[middle]:
                right = middle - 1
            elif middle + 1 <= right and nums[middle + 1] > nums[middle]:
                left = middle + 1
            else:
                return middle
        return left