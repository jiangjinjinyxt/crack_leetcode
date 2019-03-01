"""
problem 169: Majority Element
https://leetcode.com/problems/majority-element/

solution:

""" 
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = None
        for num in nums:
            if not count:
                candidate = num
                count = 1
            else:
                if num == candidate:
                    count += 1
                else:
                    count -= 1
        return candidate