"""
problem 26: Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

solution:
    

"""  

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)

        if length <= 1:
            return length

        start = 0
        for value in nums[1:]
            if value != nums[start]:
                start += 1
                nums[start] = value
        return start + 1

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        length = len(nums)
        last_index = length - 2
        last_element = nums[-1]
        while last_index > -1 and nums[last_index] == last_element:
            last_index -= 1
        last_index += 1

        non_duplicate_index = -1
        current_index = 0
        flag = True

        while flag:
            non_duplicate_index += 1
            current_value = nums[current_index]
            nums[non_duplicate_index] = current_value
            if current_value == last_element:
                flag = False
            else:
                current_index += 1
                while current_index < last_index and nums[current_index] == current_value:
                    current_index += 1
        return non_duplicate_index + 1












