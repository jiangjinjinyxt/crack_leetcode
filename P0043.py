"""
problem 43: Multiply Strings
https://leetcode.com/problems/multiply-strings/

solution:

""" 
class Solution(object):
    def karatsuba(self, num1, num2):
        for idx, value in enumerate(num1):
            if value != '0':
                num1 = num1[idx:]
                break
        else:
            return 0
        for idx, value in enumerate(num2):
            if value != '0':
                num2 = num2[idx:]
                break
        else:
            return 0

        len1 = len(num1)
        len2 = len(num2)
        if not (len1 and len2):
            return 0
        if len1 == 1:
            result = 0
            mul = int(num1)
            for idx, value in enumerate(num2[::-1]):
                result += mul * int(value) * 10 ** idx
            return result
        if len2 == 1:
            result = 0
            mul = int(num2)
            for idx, value in enumerate(num1[::-1]):
                result += mul * int(value) * 10 ** idx
            return result
        index = max(len1, len2) // 2
        if index >= len1:
            num1_1 = ""
            num1_2 = num1
            num1_3 = num1
        else:
            num1_1 = num1[:len1-index]
            num1_2 = num1[len1-index:]
            num1_3 = str(int(num1_1) + int(num1_2))
        if index >= len2:
            num2_1 = ""
            num2_2 = num2
            num2_3 = num2
        else:
            num2_1 = num2[:len2-index]
            num2_2 = num2[len2-index:]
            num2_3 = str(int(num2_1) + int(num2_2))

        a = self.karatsuba(num1_1, num2_1)
        b = self.karatsuba(num1_2, num2_2)
        c = self.karatsuba(num1_3, num2_3)
        return a * 10 ** (index * 2) + (c - a - b) * 10 ** index + b
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(self.karatsuba(num1, num2))