"""
problem 136: Single Number
https://leetcode.com/problems/single-number/

solution:

""" 
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in nums:
            ans ^= i
        return ans

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dictionary = dict()
        for i in nums:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
        for i in dictionary:
            if dictionary[i] == 1:
                return i