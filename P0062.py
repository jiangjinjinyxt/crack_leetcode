"""
problem 62: Unique Path
https://leetcode.com/problems/unique-paths/

solution:

""" 
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        table = dict()
        table[(1, 1)] = 1
        table[(1, 2)] = 1
        table[(2, 1)] = 1

        def look_up(i, j):
            if (i, j) not in table:
                if i == 1:
                    ans = 1
                elif j == 1:
                    ans = 1
                else:
                    ans = look_up(i - 1, j) + look_up(i, j - 1)
                table[(i, j)] = ans
            return table[(i, j)]
        return look_up(m, n)