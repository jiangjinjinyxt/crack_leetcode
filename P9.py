"""
problem 9: Palindrome Number
https://leetcode.com/problems/palindrome-number/

solution:

"""


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        head = x
        tail = 0
        base = 10
        while x:
            tail = tail * 10 + x % 10
            x //= 10
        if head == tail:
            return True
        return False

