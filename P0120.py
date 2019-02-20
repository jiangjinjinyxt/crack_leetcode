"""
problem 120. Triangle
https://leetcode.com/problems/triangle/

solution:

""" 

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        rows = len(triangle)
        for row in range(rows - 2, -1, -1):
        	for idx in range(len(triangle[row])):
        		triangle[row][idx] += min(triangle[row + 1][idx], triangle[row + 1][idx + 1])
        return triangle[0][0]