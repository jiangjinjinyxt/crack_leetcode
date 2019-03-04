"""
Problem 219. Contain Duplicate II
https://leetcode.com/problems/contains-duplicate-ii/

solution:

"""
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        table = dict()
        for idx, value in enumerate(nums):
            if value in table and idx - table[value] <= k:
                return True
            table[value] = idx
        return False