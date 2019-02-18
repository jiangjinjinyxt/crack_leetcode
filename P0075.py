"""
problem 75: Sort Colors
https://leetcode.com/sort-colors/

solution:

""" 
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        zero_end_index = -1 
        two_start_index = length

        index = 0
        while index < two_start_index:
            if nums[index] == 0:
                zero_end_index += 1
                nums[zero_end_index], nums[index] = nums[index], nums[zero_end_index]
                index += 1
            elif nums[index] == 2:
                two_start_index -= 1
                nums[two_start_index], nums[index] = nums[index], nums[two_start_index]
            else:
                index += 1

