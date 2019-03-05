"""
Problem 240. Search a 2D Matrix II
https://leetcode.com/problems/search-a-2d-matrix-ii/

solution:

"""
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)
        if not rows:
            return False
        cols = len(matrix[0])
        def helper(min_row, min_col, max_row, max_col):
            if max_row < min_row or max_col < min_col:
                return False
            middle_row = min_row + (max_row - min_row) // 2
            middle_col = min_col + (max_col - min_col) // 2
            if matrix[middle_row][middle_col] == target:
                return True
            elif matrix[middle_row][middle_col] < target:
                return helper(min_row, middle_col + 1, max_row, max_col) or helper(middle_row + 1, min_col, max_row, middle_col)
            else:
                return helper(min_row, min_col, middle_row - 1, max_col) or helper(middle_row, min_col, max_row, middle_col - 1)

        return helper(0, 0, rows - 1, cols - 1)

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)
        if not rows:
            return False
        cols = len(matrix[0])

        row = 0
        col = cols - 1
        while row < rows and col > -1:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False