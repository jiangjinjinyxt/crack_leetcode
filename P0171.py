"""
problem 171. Excel Sheet Column Number
https://leetcode.com/problems/excel-sheet-column-number/

solution:

""" 
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        for i in s:
            total = total * 26 + ord(i) - 64
        return total

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        for idx, value in enumerate(s[::-1]):
            total += (ord(value) - 64) * 26 ** idx
        return total