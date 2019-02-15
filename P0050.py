"""
problem 50: Pow(x, n)
https://leetcode.com/problems/powx-n/

solution:

""" 
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        elif n < 1:
            return 1 / self.myPow(x, -n)
        else:
            value = self.myPow(x, n // 2)
            value *= value
            if n % 2:
                return value * x
            else:
                return value