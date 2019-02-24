"""
problem 54: Spiral Matrix
https://leetcode.com/problems/spiral-matrix/

solution:

""" 
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows = len(matrix)
        result = []
        if not rows:
            return result
        cols = len(matrix[0])

        start_row = -1
        end_row = rows
        start_col = -1
        end_col = cols

        while True:
            start_row += 1
            end_row -= 1
            start_col += 1
            end_col -= 1
            if start_row > end_row or start_col > end_col:
                break
            if start_row == end_row:
                for col in range(start_col, end_col + 1):
                    result.append(matrix[start_row][col])
            elif start_col == end_col:
                for row in range(start_row, end_row + 1):
                    result.append(matrix[row][start_row])
            else:
                for col in range(start_col, end_col):
                    result.append(matrix[start_row][col])
                for row in range(start_row, end_row):
                    result.append(matrix[row][end_col])
                for col in range(end_col, start_col, -1):
                    result.append(matrix[end_row][col])
                for row in range(end_row, start_row, -1):
                    result.append(matrix[row][start_col])
        return result