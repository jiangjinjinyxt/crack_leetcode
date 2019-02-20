"""
problem 118. Pascal's Triangle
https://leetcode.com/problems/pascals-triangle/

solution:

""" 
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        if not numRows:
            return result
        result.append([1])
        current = 1
        while current < numRows:
            previous = 0
            row = []
            for idx, value in enumerate(result[current - 1]):
                row.append(previous + value)
                previous = value
            row.append(1)
            result.append(row)
            current += 1
        return result

# dp
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for row in range(numRows):
            current = [1] * (row + 1)
            for i in range(1, row):
                current[i] = result[row - 1][i - 1] + result[row - 1][i]
            result.append(current)
        return result