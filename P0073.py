"""
problem 73: Set Matrix Zeros
https://leetcode.com/set-matrix-zeroes/

solution:

""" 
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row_index = set()
        col_index = set()
        
        rows = len(matrix)
        if rows:
            cols = len(matrix[0])
        else:
            cols = 0
        for row in range(rows):
            for col in range(cols):
                if not matrix[row][col]:
                    row_index.add(row)
                    col_index.add(col)
        for row in range(rows):
            for col in range(cols):
                if row in row_index or col in col_index:
                    matrix[row][col] = 0
                