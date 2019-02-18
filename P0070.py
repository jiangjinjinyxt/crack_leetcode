"""
problem 70: Climb Stairs
https://leetcode.com/problems/climb-stairs/

solution:

""" 
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        table = dict()
        table[1] = 1
        table[2] = 2

        def look_up(n):
            if n not in table:
                ans = look_up(n - 1) + look_up(n - 2)
                table[n] = ans
            return table[n]
        return look_up(n)
