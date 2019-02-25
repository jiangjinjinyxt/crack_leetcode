"""
problem 78: Subsets
https://leetcode.com/problems/subsets/

solution:

""" 
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        while nums:
            value = nums.pop()
            length = len(result)
            for idx in range(length):
                result.append(result[idx] + [value])
        return result



