"""
problem 59: Spiral Matrix II
https://leetcode.com/problems/spiral-matrix-ii/

solution:

""" 
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = [[0] * n for i in range(n)]
        start = -1
        end = n
        value = 1
        while True:
            start += 1
            end -= 1
            if start > end:
                break
            if start == end:
                result[start][start] = value
                break
            else:
                for col in range(start, end):
                    result[start][col] = value
                    value += 1
                for row in range(start, end):
                    result[row][end] = value
                    value += 1
                for col in range(end, start, -1):
                    result[end][col] = value
                    value += 1
                for row in range(end, start, -1):
                    result[row][start] = value
                    value += 1
        return result
        
