"""
problem 7: Reverse Integer
https://leetcode.com/problems/reverse-integer/

solution:
    Math

"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        base = 10
        result = 0
        flag = False
        if x < 0:
            flag = True
            x *= -1
        while x:
            result = result * base + x % 10
            x //= 10
        if flag:
            result *= -1
        if (result < - 2 ** 31) or (result > 2 ** 31 - 1):
            result = 0
        return result