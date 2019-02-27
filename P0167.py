"""
problem 167. Two Sum II - Input array is sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

solution:

""" 
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = dict()
        for idx, value in enumerate(numbers):
            if target - value in table:
                return [table[target - value], idx + 1]
            else:
                table[value] = idx + 1
                
                