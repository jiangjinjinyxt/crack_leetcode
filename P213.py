class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # two types
        # 1. with first house robbed
        # 2. with first house unrobbed
        if not nums:
        	return 0
        if len(nums) == 0:
        	return nums[1]

        # type 1
        index_2, index_1 = nums[0], nums[0]
        for value in nums[2:-1]:
        	temp = max(index_2 + value, index_1)
        	index_2, index_1 = index_1, temp
        maximum = index_1
        index_2, index_1 = 0, 0
        for value in nums[1:]:
        	temp = max(index_2 + value, index_1)
        	index_2, index_1 = index_1, temp
        if index_1 > maximum:
        	return index_1
        else:
        	return maximum
