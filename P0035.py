"""
problem 35: Search Insert Position
https://leetcode.com/problems/search-insert-position/

solution:
    bitwise operation

""" 


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binary_search(left, right):
            while left < right:
                if nums[left] >= target:
                    return left
                elif nums[right - 1] <= target:
                    return right
                else:
                    middle = left + (right - left) // 2
                    if nums[middle] == target:
                        return middle
                    elif nums[middle] > target:
                        return binary_search(left, middle)
                    else:
                        return binary_search(middle, right)
            return 0

        return binary_search(0, len(nums))