"""
problem 168: Excel Sheet Column Title
https://leetcode.com/problems/excel-sheet-column-title/

solution:

""" 
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ""
        while n:
            character = n % 26
            n //= 26
            if not character:
                ans = 'Z' + ans
                n -= 1
            else:
                ans = chr(character + 64) + ans
        return ans