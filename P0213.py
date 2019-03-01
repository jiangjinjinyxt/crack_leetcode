"""
Problem 213: House Robber II

https://leetcode.com/problems/house-robber-ii/
solution:

"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        rob_first = nums[0]
        not_rob_first = 0

        rob_first_rob_current = 0
        rob_first_not_rob_current = rob_first
        not_rob_first_rob_current = nums[1]
        not_rob_first_not_rob_current = 0 

        for value in nums[2:]:
            temp1 = rob_first_rob_current
            temp2 = rob_first_not_rob_current
            temp3 = not_rob_first_rob_current
            temp4 = not_rob_first_not_rob_current
            rob_first_rob_current = temp2 + value
            rob_first_not_rob_current = max(temp1, temp2)
            not_rob_first_rob_current = temp4 + value
            not_rob_first_not_rob_current = max(temp3, temp4)
        return max(rob_first_not_rob_current, not_rob_first_rob_current, not_rob_first_not_rob_current)

