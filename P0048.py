"""
problem 48: Rotate Image
https://leetcode.com/problems/rotate-image/

solution:

""" 
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for row in range(length//2):
        	for col in range(row, length - row - 1):
        		total = length - 2 * row - 1
        		l = total - col
        		s = col - row
        		row_1, col_1 = row, col
        		row_2, col_2 = row + s, length - row - 1
        		row_3, col_3 = length - row - 1, col_2 - s
        		row_4, col_4 = row_3 - s, row

        		matrix[row_1][col_1], matrix[row_2][col_2], matrix[row_3][col_3], matrix[row_4][col_4] = \
        		matrix[row_4][col_4], matrix[row_1][col_1], matrix[row_2][col_2], matrix[row_3][col_3]
