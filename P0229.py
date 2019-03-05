"""
Problem 229. Majority Element II
https://leetcode.com/problems/majority-element-ii/

solution:

"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        if not length:
            return []
        if length == 1:
            return nums 
        candidate1, candidate2, count1, count2 = None, None, 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
                continue
            if num == candidate2:
                count2 += 1
                continue
            if not count1:
                candidate1 = num
                count1 = 1
                continue
            if not count2:
                candidate2 = num
                count2 = 1
                continue
            count1 -= 1
            count2 -= 1
        return [i for i in [candidate1, candidate2] if nums.count(i) > length // 3]
                