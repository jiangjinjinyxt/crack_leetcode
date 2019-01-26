"""
problem 33: Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/

solution:
    firstly, use binary search to search the shift index(the value at this place 
    is greater than the previous one(if exists))

""" 


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def locate_shift_index(left, right):
            while left < right:
                if nums[left] < nums[right]:
                    return left
                else:
                    middle = left + (right - left) // 2
                    if nums[middle] > nums[right]:
                        left = middle + 1
                    else:
                        right = middle
            return left


        def binary_search(left, right):
            while left <= right:
                middle = left + (right - left) // 2
                if nums[middle] == target:
                    return middle
                elif nums[middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1
            return -1

        shift_index = locate_shift_index(0, len(nums) - 1)
        left_index = binary_search(0, shift_index - 1)
        right_index = binary_search(shift_index, len(nums) - 1)
        if left_index == -1:
            return right_index
        else:
            return left_index