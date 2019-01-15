"""
problem 1: two sum
https://leetcode.com/problems/two-sum/

solution:
	dictionary
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        look_up = dict()
        for idx, value in enumerate(nums):
        	value_to_find = target - value
        	if value_to_find in look_up:
        		return [look_up[value_to_find], idx]
        	else:
        		look_up[value] = idx
        		
