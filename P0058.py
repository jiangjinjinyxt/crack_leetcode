"""
problem 58: Length of Last Word
https://leetcode.com/problems/length-of-last-word/

solution:

""" 
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        length = len(s)
        index = length - 1
        while index > -1 and s[index].isspace():
            index -= 1
        for idx in range(index, -1, -1):
            if s[idx].isspace():
                return total
            else:
                total += 1
        return total
