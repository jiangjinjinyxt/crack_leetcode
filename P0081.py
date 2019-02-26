"""
problem 81: Search in Rotated Sorted Array II
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

solution:

""" 
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] == target:
                return True

            while left < middle and nums[left] == nums[middle]:
                left += 1

            # range [left, middle] is in ascending order
            if nums[left] <= nums[middle]:
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            # range [middle, right] is in ascending order
            else:
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
        return False

