"""
problem 53: Maximum Subarray
https://leetcode.com/problems/maximum-subarray/

solution:

""" 
# divide and conquer
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        def helper(left, right):
            if left == right:
                return nums[left], nums[left], nums[left], nums[left]
            else:
                middle = left + (right - left) // 2
                left_first_half, left_max, left_second_half, left_total = helper(left, middle)
                right_first_half, right_max, right_second_half, right_total = helper(middle + 1, right)
                
                total = left_total + right_total
                first_half = max(left_first_half, left_total + right_first_half)
                second_half = max(right_second_half, right_total + left_second_half)
                max_sub = max(left_max, right_max, first_half, second_half, left_second_half + right_first_half)
                return first_half, max_sub, second_half, total

        return helper(0, len(nums) - 1)[1]

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum_sum = nums[0]
        previous_sum = nums[0]
        for value in nums[1:]:
            if previous_sum > 0:
                previous_sum += value
            else:
                previous_sum = value
            if previous_sum > maximum_sum:
                maximum_sum = previous_sum
        return maximum_sum