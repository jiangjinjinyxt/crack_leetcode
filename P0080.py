"""
problem 80. Remove Duplicates from Sorted Array II
https://leetcode.com/remove-duplicates-from-sorted-array-ii/

solution:

""" 
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        previous_value = None
        previous_index = -1
        previous_count = 1
        for value in nums:
            if value == previous_value:
                previous_count += 1
                if previous_count < 3:
                    previous_index += 1
                    nums[previous_index] = value
            else:
                previous_count = 1
                previous_value = value
                previous_index += 1
                nums[previous_index] = value
        return previous_index + 1
                
                    

