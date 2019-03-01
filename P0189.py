"""
problem 189. Rotate Array
https://leetcode.com/problems/rotate-array/

solution:

"""
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        ans = [0] * length
        k %= length
        for idx, value in enumerate(nums):
            ans[(idx + k) % length] = value
        for idx in range(length):
            nums[idx] = ans[idx]

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        length = len(nums)
        k %= length
        reverse(0, length - 1)
        reverse(0, k - 1)
        reverse(k, length - 1)