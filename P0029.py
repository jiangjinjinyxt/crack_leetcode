"""
problem 29: Divide Two Integers
https://leetcode.com/problems/divide-two-integers/

solution:
    bitwise operation

""" 
# kmp
class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        MAXIMUM = 2 ** 31

        sign = (dividend < 0) == (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        if dividend < divisor:
            return 0
        if divisor == 1:
            result = dividend
        else:
            result = 0
            while dividend >= divisor:
                temp = divisor
                multiple = 1
                while (dividend >= (temp << 1)):
                    temp <<= 1
                    multiple <<= 1
                dividend -= temp
                result += multiple

        if sign:
            return min(MAXIMUM - 1, result)
        else:
            return - min(MAXIMUM, result)
