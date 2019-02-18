"""
problem 74: Search A 2D Matrix
https://leetcode.com/search-a-2d-matrix/

solution:

""" 
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)
        if not rows:
            return False
        else:
            cols = len(matrix[0])
        if not cols:
            return False

        def search_rows(left, right):
            while left <= right:
                middle = left + (right - left) // 2
                if matrix[middle][-1] < target:
                    left = middle + 1
                else:
                    if matrix[middle][0] <= target:
                        return search_row(middle, 0, cols - 1)
                    else:
                        right = middle - 1
            return False

        def search_row(row, left, right):
            while left <= right:
                middle = left + (right - left) // 2
                if matrix[row][middle] == target:
                    return True
                elif matrix[row][middle] > target:
                    right = middle - 1
                else:
                    left = middle + 1
            return False
        return search_rows(0, rows - 1)