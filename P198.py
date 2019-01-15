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
        nums[1] = max(nums[0], nums[1])
        for idx, value in enumerate(nums[2:]):
        	idx += 2
        	nums[idx] = max(nums[idx - 1], nums[idx - 2] + value)
        return max(nums)