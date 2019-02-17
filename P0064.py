"""
problem 64: Minimum Path Sum
https://leetcode.com/problems/minimum-path-sum/

solution:

""" 
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid) - 1
        col = len(grid[0]) - 1
        
        table = dict()
        table[(row, col)] = grid[row][col]
        
        def look_up(i, j):
            if (i, j) not in table:
                if i == row:
                    ans = look_up(i, j + 1) + grid[i][j]
                elif j == col:
                    ans = look_up(i + 1, j) + grid[i][j]
                else:
                    ans = grid[i][j] + min(look_up(i + 1, j), look_up(i, j + 1))
                table[(i, j)] = ans
            return table[(i, j)]
        return look_up(0, 0)
                    
