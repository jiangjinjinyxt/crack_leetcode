"""
Problem 217. Contain Duplicate
https://leetcode.com/problems/contains-duplicate/

solution:

"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        table = set()
        for i in nums:
            if i in table:
                return True
            table.add(i)
        return False