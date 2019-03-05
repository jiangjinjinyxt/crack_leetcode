"""
Problem 231. Power Of Two
https://leetcode.com/problems/power-of-two/

solution:

"""
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
        	return False

        while True:
        	if n == 1:
        		return True
        	elif n % 2:
        		return False
        	n >>= 1