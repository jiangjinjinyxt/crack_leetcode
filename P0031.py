"""
problem 31: Next Permutation
https://leetcode.com/problems/next-permutation/

solution:

""" 

class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)

        for index in range(length - 1, 0, -1):
            if nums[index] > nums[index - 1]:
                idx = index + 1
                value = nums[index - 1]
                while idx < length and nums[idx] > value:
                    idx += 1
                nums[index - 1], nums[idx - 1] = nums[idx - 1], nums[index - 1]
                nums[index:] = nums[index:][::-1]
                break
        else:
            nums[:] = nums[::-1]

                
                