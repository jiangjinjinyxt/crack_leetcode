"""
Problem 152. Maximum Product Subarray
https://leetcode.com/problems/maximum-product-subarray/
solution:

"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        product = nums[0]
        imax = nums[0]
        imin = nums[0]
        for value in nums[1:]:
            if value < 0:
                imax, imin = imin, imax
            imax = max(value, imax * value)
            imin = min(value, imin * value)
            if imax > product:
                product = imax
        return product