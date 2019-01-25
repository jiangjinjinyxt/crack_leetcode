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
            if left <= right:
                if nums[left] >= target:
                    return left
                elif nums[right] < target:
                    return right + 1
                else:
                    middle = left + (right - left) // 2
                    if nums[middle] == target:
                        return middle
                    elif nums[middle] > target:
                        return binary_search(left, middle - 1)
                    else:
                        return binary_search(middle + 1, right)
            else:
                return left

        def binary_search_v2(left, right):
            while left <= right:
                if nums[left] >= target:
                    return left
                elif nums[right] < target:
                    return right + 1
                else:
                    middle = left + (right - left) // 2
                    if nums[middle] == target:
                        return middle
                    elif nums[middle] > target:
                        right = middle - 1
                    else:
                        left = middle + 1
            return left
        return binary_search_v2(0, len(nums) - 1)