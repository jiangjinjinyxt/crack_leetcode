"""
problem 63: Unique Paths II
https://leetcode.com/problems/unique-paths-ii/

solution:

""" 
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        row = len(obstacleGrid) - 1
        col = len(obstacleGrid[0]) - 1        
        if obstacleGrid[0][0] or obstacleGrid[row][col]:
            return 0
        table = dict()
        table[(row, col)] = 1
        
        def look_up(i, j):
            if (i, j) not in table:
                if i == row:
                    j += 1
                    if obstacleGrid[i][j]:
                        ans = 0
                    else:
                        ans = look_up(i, j)
                elif j == col:
                    i += 1
                    if obstacleGrid[i][j]:
                        ans = 0
                    else:
                        ans = look_up(i, j)
                else:
                    ans = 0
                    if not obstacleGrid[i + 1][j]:
                        ans += look_up(i + 1, j)
                    if not obstacleGrid[i][j + 1]:
                        ans += look_up(i, j + 1)
                table[(i, j)] = ans
            return table[(i, j)]
        return look_up(0, 0)
                    
