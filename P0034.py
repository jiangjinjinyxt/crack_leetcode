"""
problem 34: Find First and Last Position of Element in Sorted Array
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

solution:
    use binary search
    search_left to search the left-most index of the target
    search_right to search the right_most index of the target

""" 


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def search_left(left, right):
            if left > right:
                return None
            elif nums[left] > target:
                return None
            elif nums[left] == target:
                return left
            elif nums[right] < target:
                return None
            else:
                middle = left + (right - left) // 2
                if nums[middle] > target:
                    return search_left(left, middle - 1)
                elif nums[middle] < target:
                    return search_left(middle + 1, right)
                else:
                    left_index = search_left(left, middle - 1)
                    if left_index is None:
                        return middle
                    else:
                        return left_index
        def search_right(left, right):
            if left > right:
                return None
            elif nums[left] > target:
                return None
            elif nums[right] < target:
                return None
            elif nums[right] == target:
                return right
            else:
                middle = left + (right - left) // 2
                if nums[middle] > target:
                    return search_right(left, middle - 1)
                elif nums[middle] < target:
                    return search_right(middle + 1, right)
                else:
                    right_index = search_right(middle + 1, right)
                    if right_index is None:
                        return middle
                    else:
                        return right_index

        left_index = search_left(0, len(nums) - 1)
        right_index = search_right(0, len(nums) - 1)
        if left_index is None:
            left_index = -1
        if right_index is None:
            right_index = -1
        return [left_index, right_index]
