"""
problem 200: Number Of Islands
https://leetcode.com/problems/number-of-islands/

solution:

"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        if not rows:
            return 0
        cols = len(grid[0])
        count = 0

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != '1':
                return 
            grid[row][col] = '*'
            dfs(row, col - 1)
            dfs(row, col + 1)
            dfs(row - 1, col)
            dfs(row + 1, col)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    count += 1
                    dfs(row, col)

        return count