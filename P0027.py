"""
problem 27: Remove Element
https://leetcode.com/problems/remove-element/

solution:
    

"""  

class Solution:
    def removeElement(self, nums, val):
        start = 0
        for value in nums:
            if value != val:
                nums[start] = value
                start += 1
        return start

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for idx, value in enumerate(nums):
            if value == val:
                start_index = idx
                break
        else:
            return len(nums)

        for value in nums[idx + 1:]:
            if value != val:
                nums[start_index] = value
                start_index += 1
        return start_index














