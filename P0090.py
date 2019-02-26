"""
problem 90: Subsets II
https://leetcode.com/problems/subsets-ii/

solution:

""" 
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        table = dict()
        for num in nums:
        	if num not in table:
        		table[num] = 1
        	else:
        		table[num] += 1

       	result = [[]]

       	while table:
       		num, count = table.popitem()
       		size = len(result)
       		for idx_result in range(size):
       			for idx in range(1, count + 1):
       				result.append(result[idx_result] + [num] * idx)
       	return result




