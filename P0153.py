"""
153. Find Minimum in Rotated Sorted Array

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
solution:

"""
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] <= nums[right]:
                return nums[left]
            middle = left + (right - left) // 2
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                if nums[middle - 1] > nums[middle]:
                    return nums[middle]
                else:
                    right = middle - 1
        return nums[left]