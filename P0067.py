"""
problem 67: Add Binary
https://leetcode.com/problems/add-binary/

solution:

""" 
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        len_a = len(a)
        len_b = len(b)
        previous = 0
        result = ""
        while len_a and len_b:
            len_a -= 1
            len_b -= 1
            char_a = a[len_a]
            char_b = b[len_b]
            if char_a == '1':
                previous += 1
            if char_b == '1':
                previous += 1
            if previous == 3:
                previous = 1
                result += '1'
            elif previous == 2:
                previous = 1
                result += '0'
            elif previous == 1:
                previous = 0
                result += '1'
            else:
                result += '0'
        while len_a:
            len_a -= 1
            char_a = a[len_a]
            if char_a == '1':
                previous += 1
            if previous == 2:
                previous = 1
                result += '0'
            elif previous == 1:
                previous = 0
                result += '1'
            else:
                result += '0'
        while len_b:
            len_b -= 1
            char_b = b[len_b]
            if char_b == '1':
                previous += 1
            if previous == 2:
                previous = 1
                result += '0'
            elif previous == 1:
                previous = 0
                result += '1'
            else:
                result += '0'
        if previous:
            result += '1'
        return result[::-1]

