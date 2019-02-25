"""
problem 79: Word Search
https://leetcode.com/problems/word-search/

solution:

""" 
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        rows = len(board)
        if not rows:
            return False
        cols = len(board[0])
        len_word = len(word)
        if rows * cols < len_word:
            return False

        table = set()

        def match(row, col, sequence):
            if not sequence:
                return True
            if -1 < row < rows and -1 < col < cols and (row, col) not in table and board[row][col] == sequence[0]:
                table.add((row, col))
                for row_temp in [row - 1, row + 1]:
                    for col_temp in [col - 1, col + 1]:
                        if match(row_temp, col_temp, sequence[1:]):
                            return True
                else:
                    table.discard((row, col))
                return False
            else:
                return False

        for row in range(rows):
            for col in range(cols):
                if match(row, col, word):
                    return True
        else:
            return False


