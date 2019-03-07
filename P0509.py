"""
Problem 509. Fibonacci Number
https://leetcode.com/problems/fibonacci-number/

solution:

"""
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        result = [0] * (N + 1)
        result[1] = 1
        for i in range(2, N + 1):
            result[i] = result[i - 1] + result[i - 2]
        return result[-1]