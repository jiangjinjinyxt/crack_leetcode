"""
problem 69: Sqrt(x)
https://leetcode.com/problems/sqrt(x)/

solution:

""" 
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        def helper(left, right):
            if left == right:
                return left
            middle = left + (right - left) // 2
            if middle * middle <= x:
                if (middle + 1) * (middle + 1) > x:
                    return middle
                else:
                    return helper(middle + 1, right)
            else:
                return helper(left, middle - 1)

        return helper(1, x // 2)

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x
        while left < right:
            middle = left + (right - left) // 2
            if middle * middle <= x:
                if (middle + 1) * (middle + 1) > x:
                    return middle
                else:
                    left = middle + 1
            else:
                right = middle - 1
        return left