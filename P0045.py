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

,
                in the right place, continue
                else:
                    we need to try to put the value into the right 
                    place
                    we have to args now, current_value, current_index,
                    and current_value != current_index + 1
                    check the index = current_value - 1, this index is
                    the right place where current_value should be.
                    if the value at the index(current_value - 1) is not
                    equal to current_value(so, the value does not match
                    the index), we swap the two values, goto step1
            loop through the list again, return index + 1, if the value
            at the index is not equal to index + 1.
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

