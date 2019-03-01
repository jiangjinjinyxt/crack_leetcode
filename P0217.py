"""
Problem 217: Contain Duplicate

https://leetcode.com/problems/contain-duplicate/
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
            else:
                table.add(i)
        return False