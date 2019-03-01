"""
problem 154. Find Minimum in Rotated Sorted Array II
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

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

        while left < right:
        	if nums[left] < nums[right]:
        		return nums[left]
        	middle = left + (right - left) // 2
        	while left < middle and nums[left] == nums[middle]:
        		left += 1
        	while right > middle and nums[right] == nums[middle]:
        		right -= 1

        	if nums[left] < nums[middle]:
        		if nums[middle] <= nums[right]:
        			return nums[left]
        		else:
        			left = middle + 1
        	elif nums[left] == nums[middle]:
        		if nums[middle] <= nums[right]:
        			return nums[middle]
        		else:
        			left = middle + 1
        	else:
        		if nums[middle] < nums[middle - 1]:
        			return nums[middle]
        		else:
        			right = middle - 1
        return nums[left]
