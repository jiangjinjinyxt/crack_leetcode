"""
problem 8: String to Integer(atoi)
https://leetcode.com/problems/string-to-integer-atoi/

solution:

"""


class Solution:
    def myAtoi(self, string):
        """
        :type string: str
        :rtype: int
        """
        MAX = 2 ** 31 - 1
        MIN = - 2 ** 31
        length = len(string)
        index = 0
        space_char = ' '
        while index < length and string[index] == space_char:
            index += 1
        
        if index == length:
            return 0

        negative_flag = False
        if string[index] == '-':
            negative_flag = True
            index += 1
            if index == length:
                return 0
        elif string[index] == '+':
            index += 1
            if index == length:
                return 0
        elif string[index].isdigit():
            pass
        else:
            return 0

        result = 0
        base = 10
        while index < length and string[index].isdigit():
            result = result * base + int(string[index])
            index += 1
        if negative_flag:
            result *= -1
            if result < MIN:
                return MIN
        else:
            if result > MAX:
                return MAX
        return result
