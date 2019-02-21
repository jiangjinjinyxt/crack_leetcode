"""
problem 36: Sudoku Solver
https://leetcode.com/problems/sudoku-solver/

solution:

""" 
class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        rows = [set()for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]
        empty_slots = []
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    empty_slots.append((row, col))
                    continue
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                boxes[row // 3 * 3 + col // 3].add(board[row][col])
        length = len(empty_slots)
        target_slots = [None] * length
        def helper(value, slot_index):
            row, col = empty_slots[slot_index]
            box = row // 3 * 3 + col // 3
            if value not in rows[row] and value not in cols[col] and value not in boxes[box]:
                rows[row].add(value)
                cols[col].add(value)
                boxes[box].add(value)
                target_slots[slot_index] = value
                if slot_index == length - 1:
                    return True
                else:
                    for i in range(1, 10):
                        if helper(str(i), slot_index + 1):
                            return True
                    else:
                        rows[row].discard(value)
                        cols[col].discard(value)
                        boxes[box].discard(value)
                        return False
            else:
                return False

        for i in range(1, 10):
            if helper(str(i), 0):
                for idx, value in enumerate(empty_slots):
                    row, col = value
                    board[row][col] = target_slots[idx]