"""
problem 42: Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/

solution:

""" 
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        if length < 3:
            return 0

        left_max_array = [0] * length
        right_max_array = [0] * length
        
        left_max_array[0] = height[0]
        for index in range(1, length):
            left_max_array[index] = max(height[index], left_max_array[index - 1])

        right_max_array[-1] = height[-1]
        for index in range(length - 2, -1, -1):
            right_max_array[index] = max(height[index], right_max_array[index + 1])

        result = 0
        for index in range(1, length - 1):
            result += min(left_max_array[index], right_max_array[index]) - height[index]
        return result

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        if length < 3:
            return 0
        result = 0
        left_max = 0
        right_max = 0
        left = 0
        right = length - 1
        while left < right:
            if height[left] <= height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    result += left_max - height[left]
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    result += right_max - height[right]
                right -= 1
        return result