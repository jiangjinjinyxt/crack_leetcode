"""
problem 12: Integer to Roman
https://leetcode.com/problems/integer-to-roman/


solution:
    Use a dictionary to store integer conversion to roman

"""  

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ""
        table = {0: ['I', 'V'],
                 1: ['X', 'L'],
                 2: ['C', 'D'],
                 3: ['M', 'N']}
        result = ""
        key = -1
        while num:
            key += 1
            digit = num % 10
            num //= 10
            roman_1 = table[key][0]
            roman_5 = table[key][1]
            if digit <= 3:
                result = digit * roman_1 + result
            elif digit == 4:
                result = roman_1 + roman_5 + result
            elif digit == 5:
                result = roman_5 + result
            elif digit <= 8:
                result = roman_5 + (digit - 5) * roman_1 + result
            else:
                result = roman_1 + table[key + 1][0] + result
        return result
