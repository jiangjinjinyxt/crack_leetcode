"""
problem 55: Jump Game
https://leetcode.com/problems/jump-game/

solution:

""" 
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_idx = 0

        for idx, value in enumerate(nums):
            if max_idx < idx:
                return False
            else:
                if idx + value > max_idx:
                    max_idx = idx + value
        if max_idx >= len(nums) - 1:
            return True
        else:
            return False


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        if length < 2:
            return True
        table = [0] * len(nums)
        table[-1] = 1
        for index in range(length - 2, -1, -1):
            if nums[index] + index >= length - 1:
                table[index] = 1
                continue
            for step in range(nums[index], 0, -1):
                if table[index + step]:
                    table[index] = 1
                    break
        return table[0] == 1

        
