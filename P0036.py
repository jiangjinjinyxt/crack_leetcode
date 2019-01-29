"""
problem 36: Valid Sudoku
https://leetcode.com/problems/valid-sudoku/

solution:

""" 
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [dict() for i in range(9)]
        cols = [dict() for i in range(9)]
        boxes = [dict() for i in range(9)]

        for row in range(9):
            for col in range(9):
                value = board[row][col]
                if not value.isdigit():
                    continue
                box_index = row // 3 * 3 + col // 3
                print(row, col, box_index, value)
                if value in rows[row]:
                    return False
                else:
                    rows[row][value] = True
                if value in cols[col]:
                    return False
                else:
                    cols[col][value] = True
                if value in boxes[box_index]:
                    return False
                else:
                    boxes[box_index][value] = True

        return True