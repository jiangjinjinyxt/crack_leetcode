"""
problem 11: Container Without Most Water
https://leetcode.com/problems/container-with-most-water/

solution:
    dynamic programmingßß
"""  

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_index = 0
        right_index = len(height) - 1
        max_area = 0
        while left_index < right_index:
            if height[left_index] >= height[right_index]:
                area = height[right_index] * (right_index - left_index)
                if area > max_area:
                    max_area = area
                right_index -= 1
            else:
                area = height[left_index] * (right_index - left_index)
                if area > max_area:
                    max_area = area
                left_index += 1               
        return max_area

