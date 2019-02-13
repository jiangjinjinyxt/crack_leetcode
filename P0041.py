"""
problem 41: First Missing Positive
https://leetcode.com/problems/first-missing-positive/

solution:
    for every number which is in the range [0, length], try to
    put it in the right place(at index: number-1)
    works like this
        loop through the list
            at the current index, if the current value is not in 
            the range, continue
        step1   if the currnet value is in the range:
                if the current value is euql to the current index + 1,
                in the right place, continue
                else:
                    we need to try to put the value into the right 
                    place
                    we have to args now, current_value, current_index,
                    and current_value != current_index + 1
                    check the index = current_value - 1, this index is
                    the right place where current_value should be.
                    if the value at the index(current_value - 1) is not
                    equal to current_value(so, the value does not match
                    the index), we swap the two values, goto step1
            loop through the list again, return index + 1, if the value
            at the index is not equal to index + 1.
""" 
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        for idx in range(length):
            # print(nums, idx)
            while 0 < nums[idx] <= length and nums[idx] != idx + 1 and nums[nums[idx] - 1] != nums[idx]:
                idx_temp = nums[idx] - 1
                nums[idx], nums[idx_temp] = nums[idx_temp], nums[idx]
        idx = -1
        for idx, value in enumerate(nums):
            if value != idx + 1:
                return idx + 1
        else:
            return idx + 2
