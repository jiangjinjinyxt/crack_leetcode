"""
problem 11: Container Without Most Water
https://leetcode.com/problems/container-with-most-water/

solution:
    Initially we consider the area constituting the exterior most lines. 
    Now, to maximize the area, we need to consider the area between the 
    lines of larger lengths. If we try to move the pointer at the longer 
    line inwards, we won't gain any increase in area, since it is limited 
    by the shorter line. But moving the shorter line's pointer could turn 
    out to be beneficial, as per the same argument, despite the reduction 
    in the width. This is done since a relatively longer line obtained by 
    moving the shorter line's pointer might overcome the reduction in area 
    caused by the width reduction.

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

