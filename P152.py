"""
problem 152: maximum product subarray
https://leetcode.com/problems/maximum-product-subarray/description/

solution:
	dynamic programming
"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        max_product_array = [None] * length
        min_product_array = [None] * length
        max_product_array[0] = nums[0]
        min_product_array[0] = nums[0]

        for index, value in enumerate(nums[1:]):
        	index += 1
        	if value > 0:
        		# update max_product_array
        		if max_product_array[index - 1] > 0:
        			max_product_array[index] = max_product_array[index - 1] * value
        		elif max_product_array[index - 1] == 0:
        			max_product_array[index] = value
        		else:
        			max_product_array[index] = value

        		# update min_product_array
        		if min_product_array[index - 1] > 0:
        			min_product_array[index] = value
        		elif min_product_array[index - 1] == 0:
        			min_product_array[index] = 0
        		else:
        			min_product_array[index] = min_product_array[index - 1] * value
        	elif value == 0:
        		max_product_array[index] = 0
        		min_product_array[index] = 0
        	else:
        		if max_product_array[index - 1] > 0:
        			if min_product_array[index - 1] <= 0:
        				max_product_array[index] = min_product_array[index - 1] * value
        				min_product_array[index] = max_product_array[index - 1] * value
        			else:
        				max_product_array[index] = value
        				min_product_array[index] = max_product_array[index - 1] * value
        		elif max_product_array[index - 1] == 0:
        			max_product_array[index] = min_product_array[index - 1] * value
        			min_product_array[index] = value
        		else:
        			max_product_array[index] = min_product_array[index - 1] * value
        			min_product_array[index] = value
        return max(max_product_array)


