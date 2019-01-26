"""
problem 34: Find First and Last Position of Element in Sorted Array
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

solution:
    use binary search
    left represents the index of the first element
    right represents the index of the last element
    
    if left > right:
        empty array, return 0
    if the left-most element is greater than or equal to the target element:
        return the left index
    if the right-most element is smaller than the target element:
        retunr the right + 1 index
    else:
        if the middle element is equal to the target:
            return the middle index (as the numbers in the array are unique)
        if the middle element is greater than the target:
            search the range [left, middle - 1]
                this range must be non-empty, because if middle - 1 < left
                => middle <= left => middle == left, as left-most element is
                smaller than the target, but the middle element is greater than
                the target, contradiction.
        if middle element is smaller than the target:
            search the range [middle + 1, right]
                this range must be non-empty...


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
