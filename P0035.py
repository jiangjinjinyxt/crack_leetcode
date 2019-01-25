"""
problem 35: Search Insert Position
https://leetcode.com/problems/search-insert-position/

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
                return 0

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
        return binary_search(0, len(nums) - 1)