"""
problem 198: House Robber
https://leetcode.com/problems/house-robber/

solution:

"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob = 0
        not_rob = 0
        for value in nums:
            temp_rob = not_rob + value
            not_rob = max(not_rob, rob)
            rob = temp_rob
        return max(not_rob, rob)