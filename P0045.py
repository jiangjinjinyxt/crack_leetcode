"""
problem 45: Jump Game II
https://leetcode.com/problems/jump-game-ii/

solution:
""" 

class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last = 0
        steps = 0
        current = 0
        for idx, value in enumerate(nums):
            if idx > last:
                steps += 1
                last = current
            current = max(current, idx + value)
        return steps

