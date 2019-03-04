"""
Problem 216. Combination Sum III
https://leetcode.com/problems/combination-sum-iii/

solution:

"""
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        def helper(ans, count_left, previous, target):
        	if target < 0:
        		return
        	if not (count_left or target):
        		result.append(ans + [])
        		return
        	for i in range(previous + 1, 11 - count_left):
        		ans.append(i)
        		helper(ans, count_left - 1, i, target - i)
        		ans.pop()
        helper([], k, 0, n)
        return result
