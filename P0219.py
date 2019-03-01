"""
Problem 219: Contain Duplicate II

https://leetcode.com/problems/contain-duplicate-ii/
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
        for idx, num in enumerate(nums):
            if num in table and idx - table[num] <= k:
                return True
            table[num] = idx
        return False
                