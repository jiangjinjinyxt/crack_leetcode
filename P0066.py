"""
problem 66: Plus One
https://leetcode.com/problems/plus-one/

solution:

""" 
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits) - 1
        for idx, value in enumerate(digits[::-1]):
            idx = length - idx
            if value < 9:
                digits[idx] += 1
                return digits
            else:
                digits[idx] = 0
        else:
            digits.insert(0, 1)
            return digits
                    
